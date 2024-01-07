from system.function.initial import initial_loading
from .sequence               import character_file_sequence

def temp():
    # 마을에 모든 캐릭터 로딩
    print('########## 마을에 모든 캐릭터 로딩 ##########')
    initial_loading()

    # 파일에서 캐릭터 불러오기
    print('########## 파일에서 캐릭터 불러오기 ##########')
    만패       = character_file_sequence('만패')

    for key, value in character_info(만패).items():
        if key == '무기':
            character_info(만패)['무기'] = get_weapon_info(value)
        elif key == '스킬리스트':
            for j, 스킬 in enumerate(character_info(만패)['스킬리스트']):
                character_info(만패)['스킬리스트'][j] = get_skill_info(스킬)
        elif key == '인벤토리':
                character_info(만패)['인벤토리'] = get_inventory_info(value)
        elif key == '모자':
            character_info(만패)['모자'] = get_armor_info(value)
        elif key == '갑옷':
            character_info(만패)['갑옷'] = get_armor_info(value)
        elif key == '장갑':
            character_info(만패)['장갑'] = get_armor_info(value)
        elif key == '신발':
            character_info(만패)['신발'] = get_armor_info(value)
        elif key == '코어':
            character_info(만패)['코어'] = get_armor_info(value)
    
    return character_info(만패)

def character_info(캐릭터):
    if 캐릭터 == None:
        return 캐릭터
    else:
        return 캐릭터.__dict__

def get_inventory_info(인벤토리):
    if 인벤토리 == None:
        return 인벤토리
    else:
        inventory_info = 인벤토리.__dict__
        for key in inventory_info.keys():
            if key == '목록':
                for i, 아이템 in enumerate(inventory_info['목록']):
                    if 아이템 == None:
                        continue
                    elif 아이템.유형 == '무기':
                        inventory_info['목록'][i] = get_weapon_info(아이템)
                    elif 아이템.유형 == '소비':
                        inventory_info['목록'][i] = get_consumption_info(아이템)
                    else:
                        inventory_info['목록'][i] = get_armor_info(아이템)
        return inventory_info

def get_weapon_info(무기):
    if 무기 == None:
        return 무기
    else:
        weapon_info = 무기.__dict__
        for key in weapon_info.keys():
            if key == '무기스킬리스트':
                    for i, 무기스킬 in enumerate(weapon_info['무기스킬리스트']):
                        weapon_info['무기스킬리스트'][i] = get_skill_info(무기스킬)            
        return weapon_info

def get_armor_info(방어구):
    if 방어구 == None:
        return 방어구
    else:
        armor_info = 방어구.__dict__
        return armor_info

def get_consumption_info(소비):
    if 소비 == None:
        return 소비
    else:
        consumption_info = 소비.__dict__
        return consumption_info

def get_skill_info(스킬):
    if 스킬 == None:
        return 스킬
    else:
        skill_info = 스킬.__dict__
        return skill_info
    