#List operation

#1. + operator: concatenate a list

#a=[1,2,3]
#b=[4,5,6]
#c=a+b
#print(c)

#2. * operator
a=[0,1,2,3,4]
a =a*4
print(a)


#3. 
b=[1,2,3,4,5,6,7,8,9]
print(len(b))

#4.max(): return the item with the highest value in list
c=[11,22323,44566,12,144,155]
print(max(c))

print(min(c))

#5 sum(): return the sum of all items in the list
d=[222,222,222]
print(sum(d))
print(sum(d) / len(d))

total=0
count=0
while(True):
    inp=input("Enter a number")
    if inp== 'done' :break
    value=float(inp)
    total=total+value
    count = count+1
    avg= total / count
print(f'Average {avg}')    


mylist=[]
while(True):
    inp=input("Enter a number")
    if inp == 'done':break
    value=float(inp)
    mylist.append(value)
    average=sum(mylist) / len(mylist)