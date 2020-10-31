import pymysql
def get_databasedata(sql):
    myconnect = pymysql.connect(host='127.0.0.1',
                                user = 'root',
                                password = '123456',
                                port = 3306,
                                database= 'ranzhi')
    datasql = myconnect.cursor()
    datasql.execute(sql)
    accountdata = datasql.fetchall()
    datasql.close()
    myconnect.close()
    return (accountdata[-1][0])

if __name__ == '__main__':
    print(get_databasedata())