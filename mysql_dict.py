"""
    pymysql创建字典库
"""
import pymysql

#连接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')
#创建游标对象（操作数据库语句，获取查询结果）
cur=db.cursor()

#数据库操作
with open('dict.txt') as f:
    sql="insert into words (word,mean) values(%s, %s)"
    for line in f :
        w=line[0:17].rstrip()
        m=line[17:].rstrip()
        tup=[w,m]
        try:
            cur.execute(sql,tup)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()



#关闭游标和数据库
cur.close()
db.close()