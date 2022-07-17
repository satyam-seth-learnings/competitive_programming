S=input()
l=""
u=""
n=""
for i in S:
    if i.islower():
        l+=i
    elif i.isupper():
        u+=i
    elif i.isnumeric():
        n+=i
odd=''
even=''
for j in n:
    if int(j)%2!=0:
        odd+=j
    else:
        even+=j
odd=''.join(sorted(odd))
even=''.join(sorted(even))
n=odd+even
print("".join(sorted(l)),"".join(sorted(u)),n,sep="")