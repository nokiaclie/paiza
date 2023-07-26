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

n = int(input())
a = list(map(int,input().split()))
q = int(input())
# k = [int(input()) for i in range(q)]

for i in range(q):
    k = int(input())
    print(f'k={k:2d}',end=" ")
    l = 0
    r = n-1
    isInclude = False
    while l <= r:
        mid = (l+r)//2
        print(f'a[{mid}]={a[mid]}',end = " ")
        if a[mid] == k:
            isInclude = True
            break
        elif  a[mid] > k:
            # 中央値がおおきかったら右端を中央-1にする
            r = mid -1
        else:
            l = mid +1
    print(isInclude)
    

