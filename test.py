"""
이것저것 테스트 코드

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""


import pprint
import time
from classes.DBMS import DataManager
from classes.Instruction import *
from classes.Task import *
from classes.FileIO import FileIO
import sys
import time
import config
import os
from libs import utilbox

class W:
    MakeFile = 1 # DBMS 파일 생성 테스트
    FileIO_M_E_Test = 2 # FileIO Class 생성, 수정 테스트
    FileIO_Test_EditJson = 3 # FileIO Class 수정 테스트
    EditFileUser = 4 # DBMS - Instruction User 생성, 닉네임변경, 약관(개인정보, 정책, 마케팅) 동의/철회, 플리 추가(생성X) x2, 북마크 추가 x2
    __OldE = float('NaN') # EditFileUser 구버전
    MassiveQueueJobs = 5 # 대량 큐 작업

WHAT = W.MassiveQueueJobs

if __name__ == '__main__':
    print()
    print(config.LOGO.TEST)
    print(WHAT)
    if WHAT == W.MakeFile:
        MAX = 2000
        DBMS = DataManager.instance()
        st = time.time()
        for i in range(MAX):
            DBMS.put(data=CreateInstruction.create_account(i, f'{i}', (True, False, True)))

        while True:
            if os.path.isfile(f"DB//user//{MAX-1}.json"):
                ed = time.time()
                print(f'{ed-st=}s')
                break

    elif WHAT == W.FileIO_M_E_Test:
        FileIO.make_json(
            path="DB//user//", 
            name="test1", 
            data = {
                "InstructName" : 'create_account',
                "Identifier" : 1,
                "user_id" : 1,
                "nickname" : 'one',
                "terms" : {
                    "policy_privacy" : True,
                    "terms_of_service" : True,
                    "marketing_consent" : True
                },
                "playlist" : [ ],
                "bookmark" : [ ]
                }
            )
        print("MakeJson")
        time.sleep(3)

        FileIO.edit_json(
            path="DB//user//test1.json", 
            update_data={
                    "InstructName" : 'add_playlist',
                    "Identifier" : 1,
                    "playlist" : [
                        utilbox.new_uuid()
                    ]
                }
            )

        print("AddPlaylist1")
        time.sleep(3)

        FileIO.edit_json(
            path="DB//user//test1.json", 
            update_data={
                    "InstructName" : 'add_playlist',
                    "Identifier" : 1,
                    "playlist" : [
                        utilbox.new_uuid(),
                        
                    ]
                }
            )

        print("AddPlaylist2")
        time.sleep(3)

    elif WHAT == W.FileIO_Test_EditJson:
        print(
                FileIO.edit_json(
                    path = "DB//user//1",
                    update_data={"A":20}
                )
        )

    elif WHAT == float('nan'): # 미사용
        aft_func = lambda args, result, comment : print(f"    {args=}, {result=}, {comment=}")
        aft_func_arg = ("from AfterFunc 일1일1이2오5", )

        DBMS = DataManager.instance()

        st = time.time()

        print("\n--------------------------------\n\n> create_account")
        DBMS.put(data= (put_data := CreateInstruction.create_account(1125, f'일일이오', (True, True, True))), after_func=aft_func, after_func_args=aft_func_arg)
        print([i.queue for i in DBMS.QueueManager.queue.values()])
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))

        print("\n--------------------------------\n\n> alter_nickname")
        input()
        DBMS.put(data= (put_data := CreateInstruction.alter_nickname(1125, '이리리오')), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))


        print("\n--------------------------------\n\n>alter_terms_pp")
        input()
        DBMS.put(data= (put_data := CreateInstruction.alter_terms_pp(1125, False)), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))

        print("\n--------------------------------\n\n>alter_terms_tos")
        input()
        DBMS.put(data= (put_data := CreateInstruction.alter_terms_tos(1125, False)), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))

        print("\n--------------------------------\n\n>alter_trems_mc")
        input()
        DBMS.put(data= (put_data := CreateInstruction.alter_trems_mc(1125, False)), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))


        print("\n--------------------------------\n\n>add_playlist")
        input()
        DBMS.put(data= (put_data := CreateInstruction.add_playlist(1125, utilbox.new_uuid())), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))

        print("\n--------------------------------\n\n>add_bookmark")
        input()
        DBMS.put(data= (put_data := CreateInstruction.add_bookmark(1125, utilbox.new_uuid())), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))


        print("\n--------------------------------\n\n>add_playlist2")
        input()
        DBMS.put(data= (put_data := CreateInstruction.add_playlist(1125, utilbox.new_uuid())), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))

        print("\n--------------------------------\n\n>add_bookmark2")
        input()
        DBMS.put(data= (put_data := CreateInstruction.add_bookmark(1125, utilbox.new_uuid())), after_func=aft_func, after_func_args=aft_func_arg)
        time.sleep(2)
        pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))


        input()

    elif WHAT == W.EditFileUser:
        aft_func = lambda args, result, comment : print(f"    {args=}, {result=}, {comment=}")
        aft_func_arg = ("from AfterFunc 일1일1이2오5", )

        DBMS = DataManager.instance()

        TEST_LIST = {
            "create_account": CreateInstruction.create_account(1125, f'일일이오', (True, True, True)),

            "alter_nickname": CreateInstruction.alter_nickname(1125, '이리리오'),

            "alter_terms_pp": CreateInstruction.alter_terms_pp(1125, False),
            "alter_terms_tos": CreateInstruction.alter_terms_tos(1125, False),
            "alter_terms_mc": CreateInstruction.alter_trems_mc(1125, False),

            "add_playlist1": CreateInstruction.add_playlist(1125, "TestUUID-EMP3-4743-a854-b4612e75aecb"),
            "add_bookmark1": CreateInstruction.add_bookmark(1125, "TestUUID-EMP3-4743-a854-b4612e75aecb"),

            "add_playlist2": CreateInstruction.add_playlist(1125, utilbox.new_uuid()),
            "add_bookmark2": CreateInstruction.add_bookmark(1125, utilbox.new_uuid()),

        }

        for k, v in TEST_LIST.items():
            print(f"\n--------------------------------\n\n> {k}")
            input("Press any key to start.")
            DBMS.put(data= (put_data := v), after_func=aft_func, after_func_args=aft_func_arg)
            # print("\nQueue=\n")
            # pprint.pprint([i.queue for i in DBMS.QueueManager.queue.values()])
            time.sleep(1.2)
            pprint.pprint(DBMS.StatusManager.get_task(put_data.get('Identifier')))
        time.sleep(3)
        DBMS.stop()

    elif WHAT == W.MassiveQueueJobs:
        aft_func = None
        aft_func_arg = None

        DBMS = DataManager.instance()

        print("대량 큐 작업")
        st = time.time()
        for i in range(1, 2001):
            put_data = CreateInstruction.create_account(i, f'{i}?t={time.time()}', (True, False, True))
            DBMS.put(data=put_data, after_func=aft_func, after_func_args=aft_func_arg)

        while True:
            if sum([i.qsize() for i in DBMS.QueueManager.queue.values()]) == 0:
                print(time.time()-st,"s")
                break

        for i in range(1, 6):
            print(f'{5-i}초 뒤 DBMS 종료')
            time.sleep(1)
        
        DBMS.stop()