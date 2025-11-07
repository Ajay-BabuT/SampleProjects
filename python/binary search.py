def search(a,n,key):
    start=0
    end=n-1
    while start <= end:
        mid=int((start+end)/2)
        if key==a[mid]:
            print("Key is present")
            return -1
        elif key < a[mid]:
            end=mid-1
        elif key > a[mid]:
            start=mid+1
    print("Key Not Found...!")
a=[]
size=int(input("Enter the size of list : "))
print("Enter the elements : ")
for i in range(size):
    x=int(input())
    a.append(x)
a.sort()
k=int(input("Enter the nnumber to search : "))
search(a,size,k)