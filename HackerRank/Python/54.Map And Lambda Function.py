cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    l=[]
    a,b=-1,1
    for i in range(n):
        a,b=b,a+b
        l.append(b)
    return l
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))