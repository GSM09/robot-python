import random
# 3 6 9
"""
사용하는 input() 함수를 통해 해당 숫자 혹은 3, 6, 9가 들어가는 곳에서는 "짝"을 입력하여야 함
"""
value = 1
my_turn = True

def 사용자():
    user = input("해당하는 숫자 입력: ")
    return user

def 확인(value, user):
    if '3' in str(value) or '6' in str(value) or '9' in str(value):
        if user != "짝":
            print("틀렸습니다! 게임 종료.")
            return False
    else:
        if user != str(value):
            print("틀렸습니다! 게임 종료.")
            return False
    return True

def 다음():
    global value, my_turn
    value += 1
    my_turn = not my_turn

def 컴퓨터():

# 무한 반복하게 만들고, 사용자가 틀린 값 입력 시 에러 출력
while value:
    if my_turn:
        # 사용자 입력
        user_input = 사용자()

        # 3, 6, 9가 포함되어 있나 확인
        if not 확인(value, user_input):
            break

        # 다음 차례로 이동
        다음()

        # 컴퓨터 입력
        # 다음 차례로 이동