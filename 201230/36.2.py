def check_name(name):
    if len(name) >= 6:
        return True
    else:
        return False

name = input("6文字以上の名前を登録")
result = check_name(name)
if result:
    print("登録完了")
else:
    print("名前が短過ぎます")