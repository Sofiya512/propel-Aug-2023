'''A=[0,0,0,0,0,0,0]
found=0
n=int(input("Enter a number:"))
print("enter n numbers")
for i in range(0,n):
    A[i]=int(input())
key=(int(input("Enter a key to be searched:")))
for i in range(0,n):
    if key==A[i]:
        print("key found")
        found+=1
    else:
        continue
    if found==0:
        print("key not found")'''


'''def binarySearch(A,item):
    first=0
    last=len(A)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if A[midpoint]==item:
            found=True
        else:
            if item<a[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    if found==True:
        print("key found")
    else:
        print("key not found")
X=[0,0,0,0,0,0,0]
n=int(input("Enter a number:"))
print("enter n numbers")
for i in range(0,n):
    X[i]=int(input())
key=(int(input("Enter a key to be searched:")))
print(binarySearch(X,key))'''


def selectionsort(A,x):
    
    for i in range(len(A)-1,0,-1):
        max=0
        for j in range(1,i+1):
            if A[j]>A[max]:
                max=j
        temp=A[i]
        A[i]=A[max]
        A[max]=temp
x=[0,0,0,0,0,0]
n=int(input("Enter a number:"))
print("enter n numbers")
for i in range(0,n):
    x[i]=int(input())
selectionsort(x)
print(x)