#딕셔너리
d = {'Tomas' : 13, 'Jane' : 9}

#요소추가- Mike가 10살 추가
d['Mike'] = 9
print(d)

#모든 키 가져오기 ---keys()
print(d.keys())
print(list(d.keys())) # 리스트 자료로 변

#모든 값(value) 가져오기 --values()
print(d.values())
print(list(d.values()))

#모든 키와 모든  값 가져오기
for key, val in d.items():
    print(key, ':', val)
