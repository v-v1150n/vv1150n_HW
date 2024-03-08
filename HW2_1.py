num1 = int(input("請輸入數字一: "))
num2 = int(input("請輸入數字二: "))
num3 = int(input("請輸入數字三: "))

if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
    print("第二大的數字是:",num1)
elif (num2 > num1 and num2 < num3) or (num2 > num3 and num2 < num1):
    print("第二大的數字是:",num2)
else:
    print("第二大的數字是:",num3)
