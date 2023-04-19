#자료구조 - 딕셔너리(dictionary)
#{key : value}
#순서가 없다. 인덱싱으느 하지 않음

'''
person = {'name': '오상식', 'age': 35, 'phone' : '010-1234-5678'}
print(person)

# 특정 요소 출력
print("이름 :", person['name'])

# 요소 추가
person['email'] = 'green@green.com'

#요소 삭제
#del person['phone']
person.pop('phone') #'key'로 삭

#요소 수정
person['age'] = 30

#전체 출력
for key in person:
    #print(키,값)
    print(key,':' , person[key])
'''

#용어사전
#try ~ except

try:
    print('⊙ㅅ⊙용어 사전⊙ㅅ⊙')
    word = input("단어를 입력하세요 : ")

    dic = {
        "이진수" : "컴퓨터가 사용하는 0과 1로 이루어진 수",
        "버그" : "프로그램이 적절하게 동작하는 데 실패하거나 오류가 발생하는 코드",
        "알고리즘" : "어떤 문제를 해겨라기 위해 정해진 일련의 절차"
    }

    #print(dic['이진수'])
    definition = dic[word]
    print(definition)

except:
    print("정의된 단어가 없습니다.")

"""
#용어사전(while true)

While True:
    word = input("단어를 입력하세요 : ")

    if word == "이진수":
        print("컴퓨터가 사용하는 0과 1로 이루어진 수")
    elif word == "버그":
        print("프로그램이 적절하게 동작하는 데 실패하거나 오류가 발생하는 코드")
        break
    elif word == "알고리즘":
        print("어떤 문제를 해겨라기 위해 정해진 일련의 절차")
    else:
       print("정의된 단어가 없습니다.")
        
"""    
