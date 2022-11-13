#문자열 교체
letters = input()
length = len(letters)
cnt_a = letters.count('a')
max_a = letters[:cnt_a].count('a')

letters *= 2
cnt = max_a

for i in range(1,length):
  if letters[i-1] == 'a':
    cnt -= 1
  
  if letters[i + cnt_a - 1] == 'a':
    cnt += 1

  max_a = max(max_a, cnt)

print(cnt_a - max_a)