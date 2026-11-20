num=int(input("please enter a number: "))
k=0
for i in range(1,num):
    if num %i ==0:
        k=k+i

if k==num:
     print( "kamel")
else:
     print(" not kamel")
