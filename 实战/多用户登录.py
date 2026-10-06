# 模拟用户登录，输入账号及密码，验证包括账号是否存在，账号密码是否匹配等情况。
user={
    'aaa':123456,
    'bbb':345678,
    'ccc':345894
}
account=input()
key=int(input())
if account in user:
    if key==user[account]:
        print("Success")
    else:
        print("Fail")
else:
    print("error user")