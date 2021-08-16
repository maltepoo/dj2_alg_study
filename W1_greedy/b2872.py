#2872. 우리집엔 도서관이 있어
import sys
T = int(input())
books = [int(sys.stdin.readline())]
cnt = 0

for i in range(1, T):
    books.append(int(sys.stdin.readline()))

for j in range(T):
    if books[-1-j] == T:
        T -= 1
    else:
        cnt += 1
print(cnt)

