#1~100까지의 자연수 중 배수의 개수를 계산하는 함수를 정의하시오
# 배수를 구하는 함수를 정의하고 사용
# 배수의 개수 구하기
def times(x) :
    for i in range(1,101):
        global count
        if i % x ==0:
            count += 1
            print(i, end=' ')



count = 0
times(3)
print("배수의 개수 : %d" % count)

