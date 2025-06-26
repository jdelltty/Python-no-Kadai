# 1.hello world
print("hello world")

# 2.greet関数
def greet():
    print("こんにちは")
    return

greet()

# 3.print_name関数
def print_name(nama):
    print("私の名前は" + name + "です。")
    return

name = input("名前を入力してください: ")
print_name(name)

# 4.get_greet関数
def get_greet():
    return "おはようございます"

message = get_greet()
print(message)

# 5.add関数
def add(a,b):
    return a+b

a = input("1つ目の数字を入力してください: ")
a = int(a)
b = input("2つ目の数字を入力してください: ")
b = int(b)
sum = add(a,b)
print("合計は " + str(sum) + " です。")