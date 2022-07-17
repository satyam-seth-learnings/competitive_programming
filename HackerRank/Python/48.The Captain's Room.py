from collections import Counter
k=int(input())
room_no=list(map(int,input().split()))
counts=Counter(room_no)
for i in counts.items():
    if i[1]==1:
        print(i[0])











# Time Error


# k=int(input())
# room_no=list(map(int,input().split()))
# for i in set(room_no):
#     if room_no.count(i)!=k:
#             print(i)


# Time Error


# k=int(input())
# room_no=list(map(int,input().split()))
# d=dict()
# for i in room_no:
#     d[i]=room_no.count(i)
# for i in d.items():
#     if i[1]==1:
#         print(i[0])