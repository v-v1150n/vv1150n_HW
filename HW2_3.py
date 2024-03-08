import random
name = input("請輸入您的名字: ")
print("請輸入簡稱: 剪刀(S), 石頭(R), 布(P)")
trans = {'S':1,'R':2,'P':3}
com_trans = {'S':'剪刀','R':'石頭','P':'布'}
ply = (input(name+" 您要出的👊: "))
print(name,"您出的👊:",com_trans.get(ply))
cmp = random.choice('SRP')
print("電腦出的👊:",com_trans.get(cmp))

if(ply == 'S' and cmp == 'P') or (ply == 'R' and cmp == 'S') or (ply == 'P' and cmp == 'R'):
    print(name,"你贏了！")
elif(ply == 'S' and cmp == 'S') or (ply == 'R' and cmp == 'R') or (ply == 'P' and cmp == 'P'):
    print(name,"你跟電腦平手~")
else:
    print(name,"你輸了QQ")




