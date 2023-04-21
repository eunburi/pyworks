#수학 모듈 - math
#절대값,올림,내림,제곱근,원주율,random
import math

#math
print(math.pi)#원주율
print(math.ceil(2.54)) #정수로 올림
print(math.floor(4.923))#내림(버림)
print(int(math.sqrt(25))) #제곱근

#내장 함수
print(round(11.78))

#절대값
print(abs(-10))

#절대값을 함수로 만들기
#1번 :)
'''
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


print(my_abs(-5)) # -5 -> -(-5) , 5 -> 5
print(my_abs(5))
'''
# 2번 알고리즘:)
def my_abs2(x):
    y = x * x
    return math.sqrt(y)


print(int(my_abs2(-7)))
print(int(my_abs2(9)))
