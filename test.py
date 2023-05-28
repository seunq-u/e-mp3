"""
이것저것 테스트 코드

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""


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
    MakeFile = 1, # DBMS 파일 생성 테스트
    FileIO_M_E_Test = 2, # FileIO Class 생성, 수정 테스트
    FileIO_Test_edit_json = 3, # FileIO Class 수정 테스트
    Edit_File_User = 4, # DBMS - Instruction User 생성, 닉네임변경, 약관(개인정보, 정책, 마케팅) 동의/철회, 플리 추가(생성X) x2, 북마크 추가 x2


WHAT = W.Edit_File_User

if __name__ == '__main__':
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

    elif WHAT == W.FileIO_Test_edit_json:
        print(
                FileIO.edit_json(
                    path = "DB//user//1",
                    update_data={"A":20}
                )
        )

    elif WHAT == W.Edit_File_User:
        DBMS = DataManager.instance()
        st = time.time()
        DBMS.put(data=CreateInstruction.create_account(1125, f'일일이오', (True, True, True)))
        print([i.queue for i in DBMS.QueueManager.queue.values()])
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n> alter_nickname")
        input()
        DBMS.put(data=CreateInstruction.alter_nickname(1125, '이리리오'))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n>alter_terms_pp")
        input()
        DBMS.put(data=CreateInstruction.alter_terms_pp(1125, False))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n>alter_terms_tos")
        input()
        DBMS.put(data=CreateInstruction.alter_terms_tos(1125, False))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n>alter_trems_mc")
        input()
        DBMS.put(data=CreateInstruction.alter_trems_mc(1125, False))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))


        print("\n>add_playlist")
        input()
        DBMS.put(data=CreateInstruction.add_playlist(1125, utilbox.new_uuid()))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n>add_bookmark")
        input()
        DBMS.put(data=CreateInstruction.add_bookmark(1125, utilbox.new_uuid()))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n>add_playlist2")
        input()
        DBMS.put(data=CreateInstruction.add_playlist(1125, utilbox.new_uuid()))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))

        print("\n>add_bookmark2")
        input()
        DBMS.put(data=CreateInstruction.add_bookmark(1125, utilbox.new_uuid()))
        time.sleep(2)
        print(DBMS.StatusManager.get_task(1125))