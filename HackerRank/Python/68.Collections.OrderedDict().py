# Logic-1
from collections import OrderedDict
on=OrderedDict()
for _ in range(int(input())):
    l=input().split()
    item_name=' '.join(l[:-1])
    net_price=int(l[-1])
    if item_name in on:
        temp=on[item_name]+net_price
        on[item_name]=temp
    else:
        on[item_name]=net_price
for k,v in on.items():
    print(k,v)

# Logic-2
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)