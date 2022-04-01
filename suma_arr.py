def sum(arr):
    sum=0

    for i in arr:
        sum=sum+i
    return (sum)
arr=[]

arr=[30,29,4,68]

n=len(arr)

ans=sum(arr)

print("La suma del arreglo es: ", ans)