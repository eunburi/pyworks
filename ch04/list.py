#리스트
a = [1, 2, 3, 4]


#리스트에 5를 추가
a.append(5)


#5를 삭제
a.pop() # 맨 뒤에 삭제

print(a)



# a리스트의 합계와 평균
sum_v = 0

for i in a:
    sum_v += i
print(sum_v)


avg_v = sum_v / len(a) #a의 평균
print(f'[a] 합계 : {sum_v}')
print(f'[a] 평균 : {avg_v}')

#내장함수

print(sum(a))

b = [1, 2, 3, 4] #튜플을 더함
print(sum(b))




#리스트 복
a2 =[] #빈 a2리스트 생성
"""
a2 = a #직접 복사
print(a2)
"""
# for ~ in로 복사
"""
for i in a:
    a2.append(i)
print(a2)
"""

#3의 배수로 복사
for i in a:
    a2.append(3 * i)
print(a2)

#a리스트에서 홀수만 저장
a3 = []
for i in a:
    if i % 2 == 1:
    #if i % 2 != 0:
        a3.append(i)
print(a3)

#
