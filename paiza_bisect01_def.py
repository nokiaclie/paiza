import io
import sys

_INPUT = """\
10
3 11 18 25 40 58 69 81 88 99
5
11
100
2
41
69
"""
sys.stdin = io.StringIO(_INPUT)
# ------------------------------------------
# paiza 二分探索 1/9 
# ソートされた数列 A = (A_1, A_2, ..., A_n) と、q 個の整数 k_1, k_2, ..., k_q が
# 与えられます。各 k_i について、数列 A に含まれているなら Yes と、含まれていないなら No と出力してください。
def binary_search(A,n,k):
    # print(len(A))
    left, right = 0,n-1
    while left <= right:
        mid = (left+right)//2
        if A[mid] == k:
            return True
        elif A[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input())
A = [int(x) for x in input().split()]
q = int(input())

for _ in range(q):
    k = int(input())
    if binary_search(A,n,k):
        print("Yes")
    else:
        print("No")
    
    

