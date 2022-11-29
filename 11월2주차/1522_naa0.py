s = list(input())
cnt = s.count('a')
len = len(s)
ans = float('inf')

for i in range(cnt - 1, len):
    ans = min(ans, s[i - cnt + 1 : i + 1].count('b'))

for i in range(0, cnt - 1):
    ans = min(ans, (s[i - cnt + 1:] + s[:i + 1]).count('b'))

print(ans)
