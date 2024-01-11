s = input()
for i in range(len(s)):
    if s[i] not in 'aeiou':
        print(s[i], end='')