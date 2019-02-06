def print_and_return(a):
  for i in range(len(a)):
    # print(a[i])
    return a[i+1]

b = print_and_return([1,2])
print(b)