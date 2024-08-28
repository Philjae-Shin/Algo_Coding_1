c = "abcdefghijklmnopqrstuvwxyz"

# 1
# S = list(input())
# for i in c:
#     if i in S:
#         print(S.index(i), end=' ')
#     else:
#         print(-1, end=' ')

# 2
S = input()

for x in c:
    print(S.find(x), end=' ')
