# 순차 탐색
# 리스트의 첫번재 자료부터 하나씩 비교하면서 같은 값이 나오면
# 그 위치를 돌려주고(반환), 못찾으면 -1을 반환함

def search_list(a, x): #리스트,찾는값
    n = len(a)
    for i in range(0, n):
        if a[i] == x: #x값과 비교하여 갚으면
            return i    # 위치를 반환함
    return -1

def search_list2(a, x):
    same_num = []
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            same_num.append(i)

    if len(same_num) == 0:
        return "값을 찾을 수 없습니다."
    else:
        return same_num

def search_list3(a,x):
    same_num = []
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            same_num.append(i)

    if x not in a:
        return -1
    else:
        return same_num

    if len(same_num) == 0:
        return "값을 찾을 수 없습니다."
    else:
        return same_num

v = [60, 5, 33, 5, 12, 97, 24]

# 매개변수 - 리스트, 찾는값
print(search_list(v,5))  #1
print(search_list(v,12)) #3
print(search_list(v,100)) #3

#중복값 찾기
print(search_list2(v,5)) #[1,6]
print(search_list3(v,20))

"""
n = len(v)
for i in range(0, n ):
    if v[i] == 12:
        print("찾음")
"""

