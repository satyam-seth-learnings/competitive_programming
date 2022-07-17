from collections import OrderedDict
d=OrderedDict()
for _ in range(int(input())):
    word=input()
    if word not in d:
        d[word]=1
    else:
        d[word]+=1
print(len(d))
# for frq in d.values():
#     print(frq,end=' ')
print(*d.values())