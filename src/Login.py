usr="admin"
pwd=123456
username=input("请输入用户名:")
password=int(input("请输入密码:"))
if username==usr and password==pwd:
    print("Welcome！")
else:
    print("Error username or password...")