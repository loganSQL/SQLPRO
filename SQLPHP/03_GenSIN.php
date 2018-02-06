<?php
/*
	Generate Dummy Social Insurance Numbers into a sql table in PHP
	 
		$howMany =100 :		number of SINs you want (by default is 1000)
		$separator='-':		the default separator is ' ', but I changed to '-'

	Interesting Reading for SIN :	http://www.hackcanada.com/canadian/other/sin.html
	Credit							https://github.com/corbanworks/fng-sin-tools
*/

class fngsin{
	// Validates using the Luhn Algorithm (MOD10)
	// See: http://en.wikipedia.org/wiki/Luhn_algorithm
	function luhn($str){
		$odd = !strlen($str)%2;
		$sum = 0;
		for($i=0;$i<strlen($str);++$i){
			$n=0+$str[$i];
			$odd=!$odd;
			if($odd){
				$sum+=$n;
			}else{
				$x=2*$n;
				$sum+=$x>9?$x-9:$x;
			}
		}
		return(($sum%10)==0);
	}
	function validateSIN($sin){
		$sin = preg_replace('/[^0-9]/','',$sin);
		if(strlen($sin) == 9){
			if($sin[0] == '0' || $sin[0] == '8'){
				return false;
			}else{
				return $this->luhn($sin);
			}
		}else{
			return false;
		}
	}
	function generateSIN($separator = ' '){
		$validPrefix = array(1,2,3,4,5,6,7,9);
		$sin = array_rand($validPrefix,1);
		$length = 9;
		while(strlen($sin) < ($length - 1)){
			$sin .= rand(0,9);
		}
		$sum = 0;
		$pos = 0;
		$reversedSIN = strrev( $sin );
		while($pos < $length - 1){
			$odd = $reversedSIN[ $pos ] * 2;
			if($odd > 9){
				$odd -= 9;
			}
			$sum += $odd;
			if($pos != ($length - 2)){
				$sum += $reversedSIN[ $pos +1 ];
			}
			$pos += 2;
		}
		$checkdigit = (( floor($sum/10) + 1) * 10 - $sum) % 10;
		$sin .= $checkdigit;
		$sin1 = substr($sin,0,3);
		$sin2 = substr($sin,3,3);
		$sin3 = substr($sin,6,3);
		// I like to change $separator to '-'
		$separator='-';
		return $sin1.$separator.$sin2.$separator.$sin3;
	}
	
}

/*
-- SQL script for a table 

USE [TestDB]
GO

CREATE TABLE [dbo].[DummySIN](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[SIN] [varchar](12) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
*/

/* Specify the server and connection string attributes. */  
$serverName = "1.1.1.111";  
$connectionInfo = array( "Database"=>"testdb", "UID"=>"sa", "PWD"=>"luckypwd");  

$conn = sqlsrv_connect( $serverName, $connectionInfo);  
if( $conn === false )  
{  
     echo ("Unable to connect." . PHP_EOL);  
     die( print_r( sqlsrv_errors(), true));  
}  

//Insert a dummy SIN into the table
// Instantiate the class
$newSINObj = new fngsin();
$howMany = 1000;
for ($i = 0; $i < $howMany; $i++) {
	$newSIN = $newSINObj->generateSIN();
	echo ("generate a new SIN " . $newSIN . PHP_EOL);
	$tsql= "INSERT INTO DummySIN (SIN) VALUES (?);";
	$params = array($newSIN);
	$getResults= sqlsrv_query($conn, $tsql, $params);
	$rowsAffected = sqlsrv_rows_affected($getResults);
	if ($getResults == FALSE or $rowsAffected == FALSE)
		die(FormatErrors(sqlsrv_errors()));
	echo ($rowsAffected. " row(s) inserted: " . PHP_EOL);
	sqlsrv_free_stmt($getResults);
}


/* Free statement and connection resources. */  
sqlsrv_free_stmt( $stmt);  
sqlsrv_close( $conn);  


?>