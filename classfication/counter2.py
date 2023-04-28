# 객체 지향언어 - 캡슐화(정보은닉),상속,다형성
# Counter 클래스 만들기
# 멤버 변수에 직접 접근하지 않음 - 정보은닉(캡슐화)
# 함수 안에 멤버 변수를 작성
# 외부에서는 함수에 접근

class Counter:

    def __init__(self):
        self.x = 0  # 인스턴스 변수
        self.x += 1

    def get_count(self):
        return self.x

c1 = Counter()
print(c1.get_count())  #1

c2 = Counter()
print(c2.get_count())  #1

c3 = Counter()
print(c3.get_count())  #1

"""
class Counter:
    def __init__(self):
        self.x = 0   #인스턴스 변수
        self.x += 1  #x에 1증가

    def get_count(self):
        return  self.x

c1 = Counter()  # 객체 생성
print(c1.get_count())  #1

c2 = Counter()
print(c2.get_count()) 
"""
