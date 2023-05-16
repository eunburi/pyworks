"""
# hangman 게임
- 단어의 각 글자 자리에 짧은 선이 그려진다.
- 글자 1개를 맞추면 글자가 표시되고,추가로 계속 맞추면 글자가 표시
- 틀리면 기호가 1번 줄어든다.
- 전체 글자를 입력하여 맞추면 프로그램 바로 종료됨
"""
import random

words = ['dog', 'cat', 'monkey', 'chicken', 'frog', 'horse']
lives_remaining = 10    # 남은 기회(전역변수)
guessed_letters = ''    # 추측된 단어를 저장할 변수

def pick_a_word():
    word = random.choice(words)
    return word

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining:' + str(lives_remaining ))
    guess = input("Guess a letter or whole word?") # 철자 입력 or 단어
    return guess

def print_word_with_blanks(word):
    #print("아직 구현되지 않음")
    display_word = '' # 추측된 단어나 철자를 표시할 변수
    for letter in word:
        if guessed_letters.find(letter) > -1:   #글자를 찾음
            display_word = display_word + letter #단어를 추가해서 저장
        else: #글자를 찾지 못함
            display_word += '-' #blank (밑줄)을 추가함
    print(display_word)

def process_guess(guess,word):
    global lives_remaining #지역변수인데 전역변수화ㅏ 함(global)
    global guessed_letters
    lives_remaining = lives_remaining - 1 # 기회가 1줄어듬
    guessed_letters += guess #컴이 추측한 단어에 게이머가 입력한 글자가 추가됨
    if guess == word:
        return True # print("You win! Well Done!")를 즉시 실행
    return False    #True를 반환하면 바로 종료

def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):  # 추측해서 맞췄을때
            print("You win! Well Done!")
            break
        if lives_remaining == 0:   # 틀렸을때
            print("You are Hung")
            print("The word was: " + word)
            break
play()