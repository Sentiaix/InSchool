a = int(input("1번째 숫자 "))
b = int(input("2번째 숫자 "))
c = int(input("3번째 숫자 "))
d = int(input("4번째 숫자 "))

sum=a+b+c+d

print("합계==> %d" %sum)

aa=[0,0,0,0]
i = 0

aa[0]=int(input("1번째 숫자: "))
aa[1]=int(input("2번째 숫자: "))
aa[2]=int(input("3번째 숫자: "))
aa[3]=int(input("4번째 숫자: "))

for i in range(4):
    aa[i]=int(input("%d번째 숫자: "%(1+i)))

sum=aa[0]+aa[1]+aa[2]+aa[3]

print("sum is : %d" %sum)