import random


def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def getBallAndStrike(guess, answer):
    strikes = 0
    balls = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strikes += 1
        elif guess[i] in answer:
            balls += 1
            
    return strikes, balls

def start():
    print('게임 시작!')
    answer = generate_number()

    while True:
        guess = input('입력해주세요 (숫자 3자리)')
        if len(guess) != 3 or not guess.isdigit():
            guess = input('잘못된 입력입니다. 다시 입력해주세요 (숫자 3자리)')
            continue
        guess = [int(x) for x in guess]
        strikes, balls = getBallAndStrike(guess, answer)

        if strikes == 0 and balls == 0:
            print('아웃 ㅋㅋ')
        
        else: print('strike: ', strikes, 'balls: ', balls)

        print('사실 정답은: ', answer)

if __name__ == "__main__":
    start()