def print_rangoli(size):
    # your code goes here
    l=[]
    for i in range(n):
        l.append(chr(i+97))
    n1=(2*n-1)
    n2=n1+(n1-1)
    l2=[]
    for i in range(n):
        l2.append(("-".join(l[-1:i:-1]+l[i::])).center(n2,"-"))
    print(*(l2[:0:-1]+l2),sep='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)