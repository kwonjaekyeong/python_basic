# 트럼프카드 준비
types = list(♠♥♣♦)
nums = list('A23456789')+['10']+ list('JQK')
cards = [i+j for i in types for j in nums]
# 셔플
import random
randon.shuffle(cards)
print(cards[:8])
print('나의 카드', cards[:8:2])
print('컴퓨터의 카드, cards[1:9:2])
# 카드 합산
# 내카드 합산 : 최초 2개
# 최초 2장 추출
my_first_cards =cards[:8:2][:2]
print(my_first_card )
# -> 정수값 추출 : 멤버 하나씩 추출-> 슬라이싱 or 추출 or 분해
# 합산값
sum =0
for n in my_first_card:
    # 타입을 제거(0번째 문자)
    tmp = n[1:] 
    if tmp == 'A' or tmp== 'J', tmp== 'Q' tmp== 'K'
        #-> 합하기
        if   tmp == 'A': sum +-1
        elif tmp== 'J': sum +-1
        elif tmp== 'Q': sum +-1
        elif tmp== 'K': sum +-1
        pass
##################################################################
# A~K 까지 키로 보고, 이를 통해 값을 획득하면 간단하게 합산처리 
# 이를 위해 점수 변환표를 준비한다
score_table = dict()
for key in nums:
    # 1~13값을 차례대로 넣어라
    score_table[key] = nums.index(key) + 1
print(score_table) 

score_table = dict()
for key in nums:
    k = 1
    # 1~13값을 차례대로 넣어라
    score_table[key] = k
    k += 1
print(score_table)
#======================================
# 합산값
sum = 0
for n in my_first_card:
    sum +=score_table[n[1:]]
print('s')










    



else: # 기본형이 정수
    print(int(tmp))
    #sum +=int(tmp)
# -> 합하기