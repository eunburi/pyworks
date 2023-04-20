#함수 - return이 있는 함수#함수

def one_up():  #1을 더하는 함수
    x = 0    #지역 변수
    x = x + 1
    return x

def square(x):  # 제곱수를 계산
    val =  x * x
    return val

def add(x,y): # 두 수를 더하는 함수
    val = x + y
    return val


#print(one_up()) #1
#print(one_up()) #1 //2가 나와며 안됨! 실행할때마다 새롭게 시작되어야함~

print(square(2)) #4

result = square(3)
print(result) #9

print(add(3,4)) #7


