import random

# 3 6 9

'''
사용하는 input() 함수를 통해 해당 숫자 혹은 3, 6, 9가 들어가는 곳에서는 "짝"을 입력하여야 함
'''

value = 1

while True:
    # 사용자에게 입력 요청
    user = input("해당하는 숫자 입력: ")

    # 3, 6, 9가 포함되어 있나 확인
    if '3' in str(value) or '6' in str(value) or '9' in str(value):
        if user != "짝":
            print("틀렸습니다! 게임 종료.")
            break
    else:
        if user != str(value):
            print("틀렸습니다! 게임 종료.")
            break

    # 다음 숫자로 이동
    value += 1