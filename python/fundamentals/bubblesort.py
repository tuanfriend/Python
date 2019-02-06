def bubblesort(a):
    for j in range(len(a)-1):
        for i in range(len(a)-1-j):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
    return a

b = [1,4,5,2,3,8,6,7]
print(bubblesort(b))
