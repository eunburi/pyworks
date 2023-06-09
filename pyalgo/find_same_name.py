# 동명이인 찾기 - 중복값 찾기

def find_same_name(a):
    same_name = set()  # 중복값 기억할 빈 집합 생성
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                #중복값 추가
                same_name.add(a[i])
    return same_name
# 리스트로 사용 : same_name=[], same_name.append(a[i]도 가능함

'''
i=0 j=1 name[0] == name[1]  False
    j=2 name[0] == name[2]  False
    j=3 name[0] == name[3]  Fasle
    
i=1 j=2 name[1] == name[2]  False
    j=3 name[1] == name[3]  True    {'콩쥐'} - 중복값찾음
    
i=2 j=3 name[2] == name[3]  False

'''
name = ['흥부', '콩쥐', '놀부', '콩쥐', '놀부']

print(find_same_name(name))




#print(f"중복된 단어는 : {same_name}")