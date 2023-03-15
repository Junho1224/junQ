# 지능형 기차

# a 내 린사람 수
# b 탄 사람 수

train = []
people = 0

for i in range(4):
    a, b = map(int, input().split())
    people = people - a + b
    train.append(people)
    
print(max(train))
