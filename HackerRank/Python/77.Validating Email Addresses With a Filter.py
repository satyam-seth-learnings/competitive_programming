# Logic-1
# def fun(s):
#     # return True if s is a valid email, else return False
#     letters=[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
#     digits=[str(i) for i in range(0,10)]
#     da_un=['-','_']
#     try:
#         a=s.partition('@')
#         username=a[0]
#         websitename,_,extension=a[-1].rpartition('.')
#     except:
#         return False
#     if not (username and websitename and extension):
#         return False
#     for c in username:
#         if c not in letters+digits+da_un:
#             return False
#     for c in websitename:
#         if c not in letters+digits:
#             return False
#     if len(extension)>3:
#         return False
#     return True

# Logic-2
def fun(s):
    # return True if s is a valid email, else return False
    try:
        username,mail=s.split('@')
        site,extension=mail.split('.')
    except ValueError:
        return False

    if username.replace('-','').replace('_','').isalnum()==False:
        return False
    elif site.isalnum()==False:
        return False
    elif len(extension)>3:
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)