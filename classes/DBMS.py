"""
## classes.FileIO.py  
It's manage files in/out and protecting from json encoder and decoder's error

### func, class and value

* DataManager (class)

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

import dataclasses
import copy
import pprint
import queue
import time
import typing
import ujson
import threading
import config
from multipledispatch import dispatch
from queue import Queue
from classes import Task
from classes.Logger import Logger
import concurrent.futures

class Counter:
    COUNT = 0
    TIME = int(time.time())

global COUNTER
COUNTER = Counter() 


class DataManager():
    _instance = None
    def __init__(self) -> None:
        raise RuntimeError("Please Call instance() instead.")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            Logger.set('Creating new DBMS instance', detail='DBMS.instance')
            
            cls._instance = cls.__new__(cls)
            cls._startTime = time.time()
            cls.__running = True
            Logger.info(f'Starting DBMS <{cls.__running=}, {cls._startTime=}>', detail='DBMS.instance')

            cls.__StatusManager = Task.StatusManager()
            cls.__QueueManager = Task.QueueManager()

            new_thread_updater = threading.Thread(target=cls.update, name=f"DBMS_UPDATER", args=(cls._instance,))
            # new_thread.daemon = False # 메인 스레드가 종료되어도 I/O 작업은 계속하고 마침
            new_thread_updater.start()

            if config.DEBUG: threading.Thread(target=cls._debug_print_task_count, name=f"DBMS_COUNTER", args=(cls._instance, )).start()

            # cls.update(cls._instance) # multiprocessing
        return cls._instance


    @property
    def StatusManager(self):
        return self.__StatusManager

    @property
    def QueueManager(self):
        return self.__QueueManager

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, value: bool):
        self.__running = value

    def put(self, data: dict, after_func: typing.Callable[[tuple, typing.Union[None, bool], typing.Union[None, str]], typing.Any], after_func_args: tuple):
        """입력 함수

        Args:
            id (typing.Union[int, str]): playlist uuid(str) or discord user id(int)

            data (dict): {"Instruct" : Instruction.~ , "Identifier" : user_id | playlist_uuid, ...}

            after_func (typing.Callable[[tuple, typing.Union[None, bool], typing.Union[None, str]], typing.Any]): 해당 작업이 완료 (status.done) 될 때 실행할 함수

            after_func_args (tuple): 해당 함수의 변수 
        """

        id = data.get('Identifier')
        # 작업 큐 추가
        self.QueueManager.put_task(id=id, data=data)

        # 상태 추가
        self.StatusManager.add_task(id=id, data=data, after_func=after_func, after_func_args=after_func_args)


    def update(self, *args):
        Logger.info('Start DBMS.update()', detail="DBMS.update")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            while True:
                if not self.running: executor.shutdown(); break

                for i in range(config.DBMS.task_thread_count):
                    if not self.running: break

                    if self.QueueManager.queue[i].qsize() != 0:
                        # self.QueueManager._debug_prt_jobs_in_each_queue_count()
                        data = self.QueueManager.get_task(thread_number=i)

                        # # 멀티 스레딩
                        # new_thread = threading.Thread(target=data.get('Instruct'), name=f"thread.{i}?{data.get('Identifier')}", args=(data, ))
                        # new_thread.daemon = False # 메인 스레드가 종료되어도 I/O 작업은 계속하고 마침
                        # new_thread.start()

                        # 멀티 프로세싱
                        self.StatusManager.set_task(id = data.get('Identifier'), status='in progress')  
                        executor.submit(data.get('Instruct'), data)
                        # print(f'start threading / {data.get("InstructName")} / in thread.{i}. to {data.get("Identifier")}')
                        
                        # creat file / 1s
                        if config.DEBUG and COUNTER.TIME == int(time.time()):
                            COUNTER.COUNT += 1
                        else:
                            COUNTER.COUNT = 0
                            COUNTER.TIME = int(time.time())
        # executor.shutdown()


    def stop(self):
        """## DBMS.stop
        - DBMS Shutdown Worker thread로 호출하여 작업중 종료되는 일이 없도록 제어(DBMS.__shutdown_worker)
        """
        shutdown_thread = threading.Thread(target=self.__shutdown_worker, name=f"ShutdownWorker?t={time.time()}", args=(self, ))
        shutdown_thread.daemon = False
        Logger.warn('Waiting for DBMS shutdown...', name='DBMS', detail='stop')
        shutdown_thread.start()

    def __shutdown_worker(self, *args):
        """DBMS.QueueManager의 각 queue 들이 비워질 때까지 0.2 초 간격으로 검사하고, 그 후 DBMS를 종료
        """
        waiting_time = 0.0
        while True:
            Logger.warn(f'Waiting for all DBMS works are finished... for {waiting_time:.1f}s', name='DBMS', detail='__shutdown_worker.daemonThread')
            if self.QueueManager.get_current_tasks_count() == 0:
                self.running = False
                Logger.info(f'DBMS shutdown successful...', name='DBMS', detail='__shutdown_worker.daemonThread')

                break

            time.sleep(0.1)
            waiting_time += 0.1


    def _debug_print_task_count(self, *args):
        while True: 
            if not self.running: break

            Logger.debug(f"DBMS SPEED : {COUNTER.COUNT} file/s", detail='DBMS_COUNTER')

            if COUNTER.TIME != int(time.time()):
                COUNTER.COUNT = 0
                COUNTER.TIME = int(time.time())

            time.sleep(1)


# test code
if __name__ == '__main__':
    # dbms = DataManager.instance()
    ...




"""
- 기존

if 유저 가입을 요청하려면
data = CreateInstruction.create_account(필수데이터) # CreateInstruction를 통해 create_account 명령에 알맞는 dict 생성
DataManager.put(discord_user_id, data) # DataManager 가 요청을 받고 queue에 추가 후 리턴으로 체커를 알려줌 (추후 이것으로 처리여부 확인)

DataManager의 update 를 통해 자동으로 체커를 다른 변수에 저장하고, DataManager.create_account((체커가 제거된 data) UserInstruction) 요청
    -> 반환이 True 라면 DataManager.add_checker_in_list(변수로 보관된 체커)

후에 유저에게 완료 여부를 보여주기위해 DataManager.check(체커) 를 최대 15초 동안 1초에 한번 날림

---------------
- 수정 2023/5/27


- 준비

1. Instruction.CreateInstruction.~ 으로 요청데이터(명령어 종류, 사용자 정보, 작업에 필요한 데이터를 포함)를 생성

- 요청

1. 생성된 요청 데이터를 DBMS에 PUT
2. 작업 큐(Task.QueueMananger.put_task)에 작업 요청 추가
3. 작업 요청의 상태 추가 (Task.StatusManager.add_task)

- 실행

1. 작업 요청 상태 - 실행 중 변경
2. 분배된 작업요청을 멀티프로세싱(multiprocessing) 으로 실행

- 완료

1. 작업 요청 상태 - 완료/실패/comment 변경 (해당 함수에서 추가 / Instruction.Instruction)


"""


