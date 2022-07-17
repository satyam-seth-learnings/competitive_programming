if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Logic-1
    # l=list(set(arr))
    # l.sort()
    # print(l[-2])

    # Logic-2
    print(sorted(list(set(arr)))[-2])