def split_and_join(line):
    # write your code here
# Logic-1 
    # return "-".join(line.split())
# Logic-2
    return line.replace(" ","-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)