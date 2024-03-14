accountName = '준식'
accountBalance = 100
accountPassword = 'coc'


def check_password():
    p = input('비번 입력: ')
    if p != accountPassword:
        print('잘못된 비밀번호입니다')
        return False
    print()
    return True


while True:
    print()
    print('잔고 확인: b')
    print('입금: d')
    print('출금: w')
    print('정보 확인: s')
    print('종료: q')

    action = input('input: ').lower()[0]
    print()

    match action:
        case 'b':
            if not check_password():
                continue
            print('잔고: ', accountBalance)
        case 'd':
            if not check_password():
                continue

            deposit_amount = input('입금할 금액을 입력하세요: ')
            deposit_amount = int(deposit_amount)

            if deposit_amount < 0:
                print('입금액이 잘못되었습니다: 음수가 되어야만 합니다')
                continue

            accountBalance += deposit_amount
            print('입금 완료')

        case 'w':
            if not check_password():
                continue

            withdrawal_amount = input('출금할 금액을 입력하세요: ')
            withdrawal_amount = int(withdrawal_amount)

            if withdrawal_amount < 0:
                print('출금액이 잘못되었습니다: 음수가 되어야만 합니다')
                continue

            if withdrawal_amount > accountBalance:
                print('잔고가 부족합니다')
                continue

            accountBalance -= withdrawal_amount
            print('출금 완료')

        case 's':
            print('계좌 정보')
            print('이름: ', accountName)
            print('잔고: ', accountBalance)

        case 'q':
            break
