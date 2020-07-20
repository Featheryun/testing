import MySQLdb

def exdbsql(sql):
    # 连接数据库
    db = MySQLdb.connect('localhost', 'root', '123456', 'dbname')
    # 创建一个游标对象
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # 得到查询结果
    datas = cursor.fetchall()
    # 关闭连接
    db.close()
    return datas

if __name__ == '__main__':
    datas = exdbsql('select * from student')