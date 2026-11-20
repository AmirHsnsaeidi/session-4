n=int(input("please enter a number :")) 
numbers=[]
for i in range (5):
    n=int(input("please enter a number :"))
    numbers.append(n)
    print("koochak:",min(numbers))
    print("bozorg:",max(numbers))
