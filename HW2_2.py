YY = int(input("請輸入一個西元年份: "))

if (YY %4 == 0 and YY % 100 != 0) or YY % 400 == 0:
    print("西元",YY,"年是閏年")
else:
   print("西元",YY,"年不是閏年！")
