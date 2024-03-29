"""
    pymysql数据库查询（读）操作流程演示
"""
import pymysql

#连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
#创建游标对象（操作数据库语句，获取查询结果）
cur=db.cursor()

#数据库操作
sql="select name,age from class_1"
cur.execute(sql)
    #获取查询结果
one_row=cur.fetchone()
print(one_row)

many_row=cur.fetchmany(3)
print(many_row)

all_row=cur.fetchall()
print(all_row)

#关闭游标和数据库
cur.close()
db.close()