from system.function.initial import initial_loading
from .sequence               import character_file_sequence

def api():
    # 마을에 모든 캐릭터 로딩
    print('########## 마을에 모든 캐릭터 로딩 ##########')
    initial_loading()

    # 파일에서 캐릭터 불러오기
    print('########## 파일에서 캐릭터 불러오기 ##########')
    만패       = character_file_sequence('만패')

    print(만패.__dict__)

    return 만패.__dict__
