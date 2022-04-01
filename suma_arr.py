def sum(arr):
    sum=0

    for i in arr:
        sum=sum+i
    return (sum)
arreglo=[]

arreglo=[30,29,4,68]

n=len(arreglo)

ans=sum(arreglo)

print("La suma del arreglo es: ", ans)