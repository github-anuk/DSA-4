list=[1,2,3,4,5,6,7,8,9]
item=int(input("enter the number you want to search "))
start = 0 
end= len(list)-1
flag = False
while start <= end:
    midpoint=(start+end)//2
    if list[midpoint]== item:
        print("key found")
        flag=True
        break
    elif list[midpoint] > item:
        end=midpoint-1
    else:
        start=midpoint+1

if flag == False:
    print("never heard of it")

