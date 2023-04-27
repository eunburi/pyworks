# SuperSonicAirplane 클래스 생성


from classfication.airplane import Airplane
#AIRPLANE을 상속받음

class SuperSonicAirplane(Airplane):
    # 1Q번 - NORMAL, 2번 - SUPERSONIC
    NORMAL = 1 #상수결정
    SUPERSONIC = 2

    #모드 - 멤버변수
    def __init__(self):
        self.fly_model = SuperSonicAirplane.NORMAL


    def fly(self):
        if self.fly_model == SuperSonicAirplane.SUPERSONIC:
            print("초음속으로 비행합니다.")
        else:
            super().fly()

sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_model = SuperSonicAirplane.SUPERSONIC # 모드변경
sa.fly()
sa.land()