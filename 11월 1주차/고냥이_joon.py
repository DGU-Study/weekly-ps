# 고냥이
n = int(input())
letter = input().strip()

ans,left, right = 0,0,0
sets = set(letters[left])

if len(letter) == 1:
  print(1)
if len(set(letter)) <= n:
  print(len(letter))

while left < len(letter) and right < len(letter):
  if right == len(letter)-1:
    ans = max(ans,right-left+1)
    break
    
  sets.add(letter[right])
  if len(sets) == n:
    ans = max(ans,right-left+1)
    right += 1
  elif len(sets) > n:
    sets.clear()
    left += 1
    sets.add(letter[left])
    right = left +1
  else:
    right += 1
print(ans)