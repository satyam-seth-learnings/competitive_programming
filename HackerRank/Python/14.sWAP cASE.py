def swap_case(s):
# Logic-1    
    # l=list(s)
    # for i in range(len(l)):
    #     if l[i].isupper():
    #         l[i]=l[i].lower()
    #     else:
    #         l[i]=l[i].upper()
    # return ''.join(l)
# Logic-2
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)