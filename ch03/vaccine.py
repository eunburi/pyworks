birth_year = input("출생년도를 입력하세요")
age = 2023 - int(birth_year)+1

print(age)
if age >= 20 and age <65:
    print("백신 접종 대상")
    #print(birth_year)
    #접종대상 출생년도 끝자리 비교
    # if~ elif ~ else
    birth_year = str(birth_year)
    if birth_year[-1] == "1" or birth_year[-1] == "6":
        print("월요일")
    elif birth_year[-1] == "2" or  birth_year[-1] == "7":
        print("화요일")
    elif birth_year[-1] == "3" or birth_year[-1] == "8":
        print("수요일")
    elif birth_year[-1] == "4" or birth_year[-1] == "9":
         print("목요일")
    elif birth_year[-1] == "5" or birth_year[-1] == "0":
         print("금요일")
else:
    print("하반기 일정 확인")
    

