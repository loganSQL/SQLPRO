/* 
 The T-SQL Snippet to load JSON data file to tempdb and parse the content
*/
CREATE PROCEDURE Load_Parse_Json @Symbol nvarchar(100), @fileName nvarchar(100)
AS
/* Make sure the Json data file exists on E:\temp\data.json */
/* The table to store */
/*

CREATE TABLE Quotes (
    [symbol] [nvarchar](max) NULL,
    [key] [nvarchar](max) NULL,
	[value] [nvarchar](max) NULL
)

truncate table  Quotes
*/
Declare @sql nvarchar(max)

/*
INSERT INTO Quotes ([symbol],[key],[value])
SELECT @Symbol,[key],[value]
FROM OPENROWSET (BULK 'E:\temp\data_ROKU.json', SINGLE_CLOB) as j
CROSS APPLY OPENJSON(BulkColumn)
*/
Set @sql='INSERT INTO Quotes ([symbol],[key],[value])
SELECT '''+@Symbol+''',[key],[value]
FROM OPENROWSET (BULK '''+ @fileName+''', SINGLE_CLOB) as j
CROSS APPLY OPENJSON(BulkColumn)'

 --Print @sql
 Exec(@sql)

/*
-- analysis
select Quotes.symbol,Quotes.[Key] as 'date', Stockquote.* from Quotes 
CROSS APPLY OPENJSON(value)
WITH ( "1. open" float
, "2. high" float
, "3. low" float
, "4. close" float
, "5. adjusted close" float
, "6. volume" bigint
, "7. dividend amount" float
, "8. split coefficient" float
) as Stockquote
*/
GO