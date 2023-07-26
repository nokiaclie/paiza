import io
import sys

_INPUT = """\
1
200
3
50
200
300
"""
sys.stdin = io.StringIO(_INPUT)
# ------------------------------------------
# paiza 二分探索 2/9 
# n人の生徒が受けた、10^9 点満点のテストの採点結果 A_1,A_2,...,A_nがあります。
# あなたは合格点を自由に設定することができます。
# 合格点が k点のとき、k点以上を取った生徒が合格で、k点未満を取った生徒が不合格です。
# q個の整数 k_1, k_2, ..., k_q が与えられます。
# 各k_iについて、合格点が k_i のときに合格する生徒の人数を答えてください。
# なお、n, q の最大値はいずれも 200,000 です。
import bisect
def binary_search(A,n,k):
    left,right = 0,n-1
    while left <= right:
        mid = (left + right)//2
        if A[mid] == k:
            return n - mid
            # 合格点と一致するものが複数あればその数値のリスト順位を返す
            # return n-bisect(A,k) # これやるなら最初からつかえばいい
        elif A[mid] > k:
            right = mid -1
        else:
            left = mid +1
    # 合格点に一致する得点がない場合は
    return n - mid

n = int(input())
A = [int(x) for x in input().split()]
A = sorted(A)
print(A)
q = int(input())
for _ in range(q):
    k = int(input())
    print(k,binary_search(A,n,k))



