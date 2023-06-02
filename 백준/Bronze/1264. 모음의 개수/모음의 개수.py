#1264 모음의 개수
while True:
    a = input()
    if a == '#':
        break
    count = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in a:
        if i in vowel:
            count+=1
    print(count)
            