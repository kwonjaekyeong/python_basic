GAME_TITLE_LEN_MAX = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN = 1
GAME_LEVEL_MIN = 9

# step1 게임이 시작하면 "Enjoy Game world" 라는 문구를 출력한다
# step2 
#   2-1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능하다." 문구 출력
#   2-2 사용자가 입력할때까지 무제한으로 대기한다
#   2-3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
#   2-4 20자이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다
#   2-5 20자 이내로 입력하면 gameTitle라는 변수에 게임 제목을 담고 다음 3단계로 진입한다
# step3
#   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
#   3-2 입력에 대한 처리는 step2와 동일하다
#   3-3 플레이어의 이름은 player_name이라는 변수에 담는다
# step4
#   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다"
#   4-2 입력에 대한 처리는 step2와 동일하나, 정수가 아니면 에러를 출력
#   4-3 게임 난이도는 game_level 이라는 변수에 담는다


# step 1
print("Enjoy Game world")

# step 2
while True:
    tmp = input('게임제목을 입력하시오 n\ 단, 20자 이내로 입력 가능하다') .strip()
    if not tmp:
        print('정확하게 입력하세요')
        pass
    elif tmp>20:
        print('20자가 초과되었습니다')
        pass
    else: 
        gameTitle = tmp 
        break
        pass
    pass

# step 3
while True :
    tmp = input('플레이어의 닉네임을 입력하세요, 단 %s 자로 제한한다' \n => % GAME_TITLE_LEN_MAX).strip()
    if not tmp:
        print('정확하게 입력하세요!')
        pass
    elif len(tmp)>PLAYER_NAME_LEN_MAX:
        print('%s 자가 초과되었습니다' % PLAYER_NAME_LEN_MAX)
        pass
    else: 
        player_name = tmp
        break
    pass

