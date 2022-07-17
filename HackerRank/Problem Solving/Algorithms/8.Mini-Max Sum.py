# Logic-1

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sm=sum(arr)
    print(sm-max(arr),sm-min(arr))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# Logic-2

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the miniMaxSum function below.
# def miniMaxSum(arr):
#     if (all([arr[i]==arr[i+1] for i in range(len(arr)-1)])):
#         mx_mn_sum=0
#         for i in range(len(arr)-1):
#             mx_mn_sum+=arr[i]
#         print(mx_mn_sum,mx_mn_sum)
#     else:
#         mx=max(arr)
#         mn=min(arr)
#         mx_sum=mn_sum=0
#         for i in arr:
#             if i!=mx:
#                 mx_sum+=i
#             if i!=mn:
#                 mn_sum+=i
#         print(mx_sum,mn_sum)

# if __name__ == '__main__':
#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)
