x,k=input().split()
polynomial=input()
print(eval(polynomial.replace('x',x))==int(k))