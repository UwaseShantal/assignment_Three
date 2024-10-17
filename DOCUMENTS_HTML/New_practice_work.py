list=[1,3,4,7,89,5]

#add the list
sum=1
for i in list:
    sum=sum+i
print(f"Sum of list {sum}")

#multiplication of the list
mult=1
for i in list:
    mult=mult*i
print(f"Result is {mult}")    

#reverse the list
rev=list[::-1]
print(f"{rev}")

#max
mx=0
for i in list:
    mx=mx>i
print(f"{mx}")