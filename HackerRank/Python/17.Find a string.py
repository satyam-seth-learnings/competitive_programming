def count_substring(string, sub_string):
    count=0
    for i in range(len(string)-(len(sub_string)-1)):
        tempstr=''
        for j in range(len(sub_string)):
            tempstr+=string[i+j]
        if(tempstr)==sub_string:
            count+=1
    return  count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)