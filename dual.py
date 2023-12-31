from town             import Town
from character        import 캐릭터
from weapon           import 제작_진검, 제작_엑스칼리버
from color            import bcolors
from create_character import create_character

import random

import unicodedata

def fill_str_with_space(input_s="", max_size=60, fill_char=" "):
    """
    - 길이가 긴 문자는 2칸으로 체크하고, 짧으면 1칸으로 체크함. 
    - 최대 길이(max_size)는 40이며, input_s의 실제 길이가 이보다 짧으면 
    남은 문자를 fill_char로 채운다.
    """
    l = 0 
    for c in input_s:
        if unicodedata.east_asian_width(c) in ['F', 'W']:
            l+=2
        else: 
            l+=1
    return input_s+fill_char*(max_size-l)

class DualInfo():
    def __init__(self, 캐릭터_1, 캐릭터_2):
        if 캐릭터_1.속도 > 캐릭터_2.속도:
            self.선공캐릭터 = 캐릭터_1
            self.후공캐릭터 = 캐릭터_2
        elif 캐릭터_1.속도 == 캐릭터_2.속도:
            if random.randint(1, 10) <= 5:
                self.선공캐릭터 = 캐릭터_1
                self.후공캐릭터 = 캐릭터_2
            else:
                self.선공캐릭터 = 캐릭터_2
                self.후공캐릭터 = 캐릭터_1
        else:
            self.선공캐릭터 = 캐릭터_2
            self.후공캐릭터 = 캐릭터_1
        self.선공캐릭터정보 = {}
        self.선공캐릭터정보['이름']                     = self.선공캐릭터.이름
        self.선공캐릭터정보['레벨']                     = self.선공캐릭터.레벨
        self.선공캐릭터정보['무기이름']                 = self.선공캐릭터.무기.이름
        self.선공캐릭터정보['무기강화레벨']             = self.선공캐릭터.무기.강화레벨
        self.선공캐릭터정보['HP']                       = self.선공캐릭터.HP
        self.선공캐릭터정보['공격력최종증폭최소데미지'] = self.선공캐릭터.공격력+self.선공캐릭터.무기.최종증폭*self.선공캐릭터.무기.최종최소데미지
        self.선공캐릭터정보['공격력최종증폭최대데미지'] = self.선공캐릭터.공격력+self.선공캐릭터.무기.최종증폭*self.선공캐릭터.무기.최종최대데미지
        self.후공캐릭터정보 = {}
        self.후공캐릭터정보['이름']                     = self.후공캐릭터.이름
        self.후공캐릭터정보['레벨']                     = self.후공캐릭터.레벨
        self.후공캐릭터정보['무기이름']                 = self.후공캐릭터.무기.이름
        self.후공캐릭터정보['무기강화레벨']             = self.후공캐릭터.무기.강화레벨
        self.후공캐릭터정보['HP']                       = self.후공캐릭터.HP
        self.후공캐릭터정보['공격력최종증폭최소데미지'] = self.후공캐릭터.공격력+self.후공캐릭터.무기.최종증폭*self.후공캐릭터.무기.최종최소데미지
        self.후공캐릭터정보['공격력최종증폭최대데미지'] = self.후공캐릭터.공격력+self.후공캐릭터.무기.최종증폭*self.후공캐릭터.무기.최종최대데미지

    def 출력(self):
        선공캐릭터정보 = self.선공캐릭터정보
        후공캐릭터정보 = self.후공캐릭터정보
        출력최대길이 = 60
        
        print('='*(출력최대길이) + ' '*6 + '='*(출력최대길이))
        for _ in range(1):
            선공출력내용 = fill_str_with_space(f'{선공캐릭터정보["이름"]}(Lv.{선공캐릭터정보["레벨"]})', 출력최대길이, ' ')
            후공출력내용 = fill_str_with_space(f'{후공캐릭터정보["이름"]}(Lv.{후공캐릭터정보["레벨"]})', 출력최대길이, ' ')
            print(선공출력내용, end='')
            print('  vs  ', end='')
            print(후공출력내용)
        print('='*(출력최대길이) + ' '*6 + '='*(출력최대길이))


def 듀얼공방(선공캐릭터, 후공캐릭터, 선공캐릭터_HP, 후공캐릭터_HP):
    출력최대길이 = 60
    #----------------------------------------------------------------------------------------------------
    # 선공
    공격 = random.choice(선공캐릭터.스킬리스트 + 선공캐릭터.무기.무기스킬리스트)
    공격이름  = f'{공격.이름}'
    if   공격.등급 == 2: 공격이름_ = f'{bcolors.OKGREEN}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 3: 공격이름_ = f'{bcolors.OKBLUE}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 4: 공격이름_ = f'{bcolors.FAIL}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 5: 공격이름_ = f'{bcolors.HEADER}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 6: 공격이름_ = f'{bcolors.WARNING}{공격이름}{bcolors.ENDC}'
    else:                공격이름_ = 공격이름
    선공캐릭터최종데미지, 치명타적중 = 선공캐릭터.최종데미지()
    선공캐릭터최종데미지            *= 공격.증폭
    선공캐릭터최종데미지            += 공격.데미지
    선공캐릭터최종데미지             = int(선공캐릭터최종데미지)
    최종피해            , 회피성공   = 후공캐릭터.최종피해(선공캐릭터최종데미지, 선공캐릭터.명중)
    막은피해                         = 선공캐릭터최종데미지 - 최종피해
    선공캐릭터최종데미지_ = f'{bcolors.FAIL}{선공캐릭터최종데미지}{bcolors.ENDC}'
    막은피해_             = f'{bcolors.OKBLUE}{선공캐릭터최종데미지 - 최종피해}{bcolors.ENDC}'
    if 치명타적중: 선공캐릭터최종데미지_ = f'{bcolors.UNDERLINE}{선공캐릭터최종데미지_}{bcolors.ENDC}'
    if 회피성공:   막은피해_             = f'{bcolors.UNDERLINE}{막은피해_}{bcolors.ENDC}'

    후공캐릭터_HP -= 최종피해
    print('-'*출력최대길이 + ' '*6 + '-'*출력최대길이)
    #-------------------- Line 1 --------------------
    선공출력내용 = fill_str_with_space(f'{bcolors.BOLD}{선공캐릭터.이름}{bcolors.ENDC} Lv.{선공캐릭터.레벨}', 출력최대길이-7+8, ' ')
    print(선공출력내용, end='OFFENSE  =>  ')
    후공출력내용 = fill_str_with_space(f'{bcolors.BOLD}{후공캐릭터.이름}{bcolors.ENDC} Lv.{후공캐릭터.레벨}', 출력최대길이-7+8, ' ')
    print(후공출력내용, end='DEFENSE\n')
    #-------------------- Line 2 --------------------
    print(f'HP : {선공캐릭터_HP} / {선공캐릭터.HP}', end='')
    print(' '*(출력최대길이-len(f'HP : {선공캐릭터_HP} / {선공캐릭터.HP}')-len(f'{str(선공캐릭터최종데미지)}')), end='')
    print(f'{선공캐릭터최종데미지_}', end='')
    print(' '*6, end='')
    print(f'HP : {후공캐릭터_HP} / {후공캐릭터.HP}', end='')
    print(' '*(출력최대길이-len(f'HP : {후공캐릭터_HP} / {후공캐릭터.HP}')-len(f'{str(막은피해)}')), end='')
    print(f'{막은피해_}')
    #-------------------- Line 3 --------------------
    print(' '*(출력최대길이-2*len(공격이름)) + 공격이름_)
    #------------------------------------------------
    print('-'*출력최대길이 + ' '*6 + '-'*출력최대길이)
    if 후공캐릭터_HP <= 0:
        print(fill_str_with_space(f'{선공캐릭터.이름} WIN', 출력최대길이+6, ' '), end='')
        print(f'{후공캐릭터.이름} LOSE')
        return (1, 선공캐릭터_HP, 0)
    #----------------------------------------------------------------------------------------------------
    # 후공
    공격 = random.choice(후공캐릭터.스킬리스트 + 후공캐릭터.무기.무기스킬리스트)
    공격이름  = f'{공격.이름}'
    if   공격.등급 == 2: 공격이름_ = f'{bcolors.OKGREEN}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 3: 공격이름_ = f'{bcolors.OKBLUE}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 4: 공격이름_ = f'{bcolors.FAIL}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 5: 공격이름_ = f'{bcolors.HEADER}{공격이름}{bcolors.ENDC}'
    elif 공격.등급 == 6: 공격이름_ = f'{bcolors.WARNING}{공격이름}{bcolors.ENDC}'
    else:                공격이름_ = 공격이름
    후공캐릭터최종데미지, 치명타적중 = 후공캐릭터.최종데미지()
    후공캐릭터최종데미지            *= 공격.증폭
    후공캐릭터최종데미지            += 공격.데미지
    후공캐릭터최종데미지             = int(후공캐릭터최종데미지)
    최종피해            , 회피성공   = 선공캐릭터.최종피해(후공캐릭터최종데미지, 후공캐릭터.명중)
    막은피해                         = 후공캐릭터최종데미지 - 최종피해
    후공캐릭터최종데미지_ = f'{bcolors.FAIL}{후공캐릭터최종데미지}{bcolors.ENDC}'
    막은피해_             = f'{bcolors.OKBLUE}{후공캐릭터최종데미지 - 최종피해}{bcolors.ENDC}'
    if 치명타적중: 후공캐릭터최종데미지_ = f'{bcolors.UNDERLINE}{후공캐릭터최종데미지_}{bcolors.ENDC}'
    if 회피성공:   막은피해_             = f'{bcolors.UNDERLINE}{막은피해_}{bcolors.ENDC}'

    선공캐릭터_HP -= 최종피해
    print('-'*출력최대길이 + ' '*6 + '-'*출력최대길이)
    #-------------------- Line 1 --------------------
    선공출력내용 = fill_str_with_space(f'{bcolors.BOLD}{선공캐릭터.이름}{bcolors.ENDC} Lv.{선공캐릭터.레벨}', 출력최대길이-7+8, ' ')
    print(선공출력내용, end='DEFENSE  <=  ')
    후공출력내용 = fill_str_with_space(f'{bcolors.BOLD}{후공캐릭터.이름}{bcolors.ENDC} Lv.{후공캐릭터.레벨}', 출력최대길이-7+8, ' ')
    print(후공출력내용, end='OFFENSE\n')
    #-------------------- Line 2 --------------------
    print(f'HP : {선공캐릭터_HP} / {선공캐릭터.HP}', end='')
    print(' '*(출력최대길이-len(f'HP : {선공캐릭터_HP} / {선공캐릭터.HP}')-len(f'{str(막은피해)}')), end='')
    print(f'{막은피해_}', end='')
    print(' '*6, end='')
    print(f'HP : {후공캐릭터_HP} / {후공캐릭터.HP}', end='')
    print(' '*(출력최대길이-len(f'HP : {후공캐릭터_HP} / {후공캐릭터.HP}')-len(f'{str(후공캐릭터최종데미지)}')), end='')
    print(f'{후공캐릭터최종데미지_}')
    #-------------------- Line 3 --------------------
    print(' '*(2*출력최대길이+6-2*len(공격이름)) + 공격이름_)
    #------------------------------------------------
    print('-'*출력최대길이 + ' '*6 + '-'*출력최대길이)
    if 선공캐릭터_HP <= 0:
        print(fill_str_with_space(f'{선공캐릭터.이름} LOSE', 출력최대길이+6, ' '), end='')
        print(f'{후공캐릭터.이름} WIN')
        return (1, 0, 후공캐릭터_HP)
    return (0, 선공캐릭터_HP, 후공캐릭터_HP)
    

def dual(캐릭터_1, 캐릭터_2):
    출력최대길이  = 60
    캐릭터_1.출력()
    캐릭터_2.출력()
    듀얼정보      = DualInfo(캐릭터_1, 캐릭터_2)
    듀얼정보.출력()
    선공캐릭터    = 듀얼정보.선공캐릭터
    후공캐릭터    = 듀얼정보.후공캐릭터
    선공캐릭터_HP = 선공캐릭터.HP
    후공캐릭터_HP = 후공캐릭터.HP

    결과 = [[캐릭터_1.이름, 0], [캐릭터_2.이름, 0]]

#    print(f'==================================================')
#    print(f'선공   : {선공캐릭터.이름}(Lv.{선공캐릭터.레벨}) [{선공캐릭터.무기.이름}(Lv.{선공캐릭터.무기.강화레벨})]')
#    print(f'HP     : {선공캐릭터.HP}')
#    print(f'데미지 : {int(선공캐릭터.공격력+선공캐릭터.무기.최종증폭*선공캐릭터.무기.최종최소데미지)} - {int(선공캐릭터.공격력+선공캐릭터.무기.최종증폭*선공캐릭터.무기.최종최대데미지)}')
#    print(f'후공   : {후공캐릭터.이름}(Lv.{후공캐릭터.레벨}) [{후공캐릭터.무기.이름}(Lv.{후공캐릭터.무기.강화레벨})]')
#    print(f'HP     : {후공캐릭터.HP}')
#    print(f'데미지 : {int(후공캐릭터.공격력+후공캐릭터.무기.최종증폭*후공캐릭터.무기.최종최소데미지)} - {int(후공캐릭터.공격력+후공캐릭터.무기.최종증폭*후공캐릭터.무기.최종최대데미지)}')
#    print(f'==================================================')

    turn = 0
    while True:
        turn += 1
        print(f'{bcolors.OKCYAN}Turn {turn}{bcolors.ENDC}')
        끝, 선공캐릭터_HP, 후공캐릭터_HP = 듀얼공방(선공캐릭터, 후공캐릭터, 선공캐릭터_HP, 후공캐릭터_HP)
        if 끝 and 후공캐릭터_HP<=0:
            if 선공캐릭터.이름 == 캐릭터_1.이름: 결과[0][1] += 1
            else:                                결과[1][1] += 1
            return 선공캐릭터.이름
        elif 끝 and 선공캐릭터_HP<=0:
            if 후공캐릭터.이름 == 캐릭터_1.이름: 결과[0][1] += 1
            else:                                결과[1][1] += 1
            return 후공캐릭터.이름

        선공캐릭터_HP += 선공캐릭터.회복
        print(fill_str_with_space(f'{선공캐릭터.이름} {bcolors.OKGREEN}HP +{선공캐릭터.회복}{bcolors.ENDC}', 출력최대길이+15, ' '), end='')
        후공캐릭터_HP += 후공캐릭터.회복
        print(f'{후공캐릭터.이름} {bcolors.OKGREEN}HP +{후공캐릭터.회복}{bcolors.ENDC}')
        print()
            
if __name__ == '__main__':
    create_character()
    캐릭터_1 = Town.캐릭터딕셔너리['성레기']
    캐릭터_2 = Town.캐릭터딕셔너리['갓종']
    캐릭터_1.무기.출력()
    캐릭터_2.무기.출력()

    결과 = [[캐릭터_1.이름, 0], [캐릭터_2.이름, 0]]

    for _ in range(1):
        if dual(캐릭터_1, 캐릭터_2) == 캐릭터_1.이름:
            결과[0][1] += 1
        else:
            결과[1][1] += 1

    print(결과)
