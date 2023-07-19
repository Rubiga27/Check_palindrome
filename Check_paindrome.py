def check_palindrome(A,start,end):
    if start>end:
        return 1
    if A[start]!=A[end]:
        return 0
    else:
        return check_palindrome(A,start+1,end-1)
A=str(input(""))
print(check_palindrome(A,0,len(A)-1))

"""
Input 1:
A = "naman"
Input 2:
A = "strings"


Output 1:
1
Output 2:
0
"""





