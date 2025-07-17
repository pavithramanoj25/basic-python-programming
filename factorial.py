def fact(n):
  if n==0 or n==1:
    return 1
  return n*fact(n-1)
s=int(input())
factorial=fact(s)
print(factorial)
