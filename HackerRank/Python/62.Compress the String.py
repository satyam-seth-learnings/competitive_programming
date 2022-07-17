# Enter your code here. Read input from STDIN. Print output to STDOUT

# Logic-1
from itertools import groupby
for k,v in groupby(input()):
    print((len(list(v)),int(k)),end=' ')

# Logic-2
from itertools import groupby
print(*((len(list(v)),int(k)) for k,v in groupby(input())))