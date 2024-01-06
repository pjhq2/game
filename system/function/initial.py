import os

from object.Town      import 마을
from object.Character import 캐릭터

def get_all_character():
    if not os.path.isdir('./save'):
        os.mkdir('./save')
    캐릭터파일리스트 = os.listdir('./save')
    캐릭터리스트     = []
    for 캐릭터파일 in 캐릭터파일리스트:
        캐릭터이름 = 캐릭터파일[:-5]
        캐릭터리스트.append(캐릭터().불러오기(캐릭터이름))
    return 캐릭터리스트

def initial_loading():
    모든캐릭터 = get_all_character()
    마을.모두저장(모든캐릭터)

if __name__ == '__main__':
    initial_loading()
    for 캐릭터이름 in 마을.캐릭터딕셔너리.keys():
        print(캐릭터이름)
 