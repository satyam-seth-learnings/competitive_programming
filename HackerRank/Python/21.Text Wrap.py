import textwrap

# Logic-1
# def wrap(string, max_width):
#     return "\n".join(textwrap.wrap(string,max_width))

# Logic-2
# def wrap(string, max_width):
#     return (textwrap.fill(string,max_width))

# Logic-3 (without textwrap module)

# print(string[max_width*0:max_width*1])
# print(string[max_width*1:max_width*2])
# print(string[max_width*2:max_width*3])

# Logic-4
def wrap(string, max_width):
    s=''
    for i in range(len(string)//max_width+1):
        s+=string[max_width*i:max_width*(i+1)]+'\n'
    return s
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

