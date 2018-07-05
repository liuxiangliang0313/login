import pymysql
from hashlib import sha1

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='Python3',charset='utf8')
# 接收用户输入
name = input("请输入用户名:")
pwd = input("请输入密码:")
res = [name]
# 对密码加密
# m = sha1()
# s = m.update(pwd.encode("utf-8"))
# print(s)
pwd2=sha1(pwd.encode('utf-8')).hexdigest()
# 根据用户名查询密码

sql = 'select passwd from userinfo where name=%s'
cus1 = conn.cursor()
cus1.execute(sql,res)
psw = cus1.fetchall()
if psw == ():
    print("用户名错误")
elif psw[0][0] == pwd2:
    print("登陆成功")
else:
    print("密码错误")
conn.commit()
cus1.close()
conn.close()