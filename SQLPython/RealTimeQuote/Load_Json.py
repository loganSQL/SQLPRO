# https://blogs.msdn.microsoft.com/cdndevs/2015/03/11/python-and-data-sql-server-as-a-data-source-for-python-applications/
import shutil
import pypyodbc


def load_json(symbol,svr,drv,db):

    # copy to sql server local drive first
    source_path=r"./data"
    dest_path=f"//{svr}/{drv}$/temp"
    filename=f"/data_{symbol}.json"
    shutil.copyfile(source_path + filename, dest_path + filename)

    # load into sql server by exec a T-SQL store procedure
    connstr='Driver=SQL Server;Server='+svr+';Database='+db+'; Trusted_Connection=Yes;'
    conn = pypyodbc.connect(connstr)
    cursor = conn.cursor()
    #SQLCommand="exec Load_Parse_Json '"+symbol+"','"+dest_path + filename"'"
    SQLCommand="exec Load_Parse_Json '"+symbol+"','"+dest_path + filename+"'"
    cursor.execute(SQLCommand)
    cursor.commit()
    conn.close()


if __name__ == '__main__':
 #   load_json('Symbol','MyServer','MyDiskDrive','MyDB')
    load_json('ROKU','LoganSQL','E','DBA')
    load_json('MSFT','LoganSQL','E','DBA')