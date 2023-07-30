import time
import typing
from queue import Queue
import config
from dataclasses import dataclass

@dataclass
class Task:
    id: str
    data: dict
    status: typing.Literal['waiting', 'in progress', 'done']
    result: typing.Union[None, bool]
    comment: typing.Union[None, str]
    after_func: typing.Union[None, typing.Callable[[tuple, typing.Union[None, bool], typing.Union[None, str], typing.Any], typing.Any] ]
    after_func_args: typing.Union[tuple, None]

class StatusManager():
    """작업을 추적하기 위해, 작업 객체는 작업에 대한 정보와 상태를 포함하고, 작업이 완료되면 해당 객체의 상태를 업데이트. / 
    작업 객체에 status : '대기 중(waiting)', '진행 중(in progress)', '완료(done)' | result : 대기/실행: None, 성공: True, 실패: False
    와 같은 상태를 부여하여 작업 상태를 확인 가능
    """
    __Status = dict() # StatusManager.__Status or cls.__Status

    @classmethod
    @property
    def status(cls):
        return cls.__Status

    @classmethod 
    def add_task(cls, id: str, data: dict, after_func: typing.Union[None, typing.Callable[[tuple, typing.Union[None, bool], typing.Union[None, str], typing.Any], typing.Any] ], after_func_args: tuple) -> str:
        """새로운 DB 작업을 추가하는 메서드

        Args:
            id (typing.Union[str, int]): 작업의 식별자 -> playlist uuid / user id

            data (dict): DBMS 용 명령어 (Classes.Instruction.CreatInstruction)

            after_func (typing.Union[None, typing.Callable[[tuple, typing.Union[None, bool], typing.Union[None, str], typing.Any], typing.Any] ]): None 또는 해당 작업이 완료 (status.done) 될 때 실행할 함수 

            after_func_args (tuple): None 또는 after_func 함수의 변수 
        """

        new_task = Task(
            id = id,
            data = data,
            status = 'waiting',
            result = None,
            comment = None,
            after_func = after_func,
            after_func_args = after_func_args,
        ) 
        cls.status.update({id: new_task})

    @classmethod 
    def get_task(cls, id: str) -> Task:
        try:
            task = cls.status[id]
        except KeyError:
            raise TaskNotFound
        else:
            task = cls.status[id]
            return task

    @classmethod 
    def set_task(cls, id: str, status: typing.Literal['waiting', 'in progress', 'done'], result: typing.Union[None, bool] = None, comment: typing.Union[None, str] = None):
        task = cls.get_task(id=id)
        task.status = status
        task.result = result
        task.comment = comment
        if task.status == "done" and task.after_func != None:
            task.after_func(task.after_func_args, task.result, task.comment)



class QueueManager():
    """각 스레드에 균등하게 작업을 분배 시키기 위해 요청이 들어오면 작업이 가장 적은 큐를 선택하여 요청을 추가 하는 형태로 작동하는 Class

    - 추가 과정
    작업 큐에 해당 파일 UUID, ID가 있는지 확인
    있을 경우, 해당 작업 큐에 파일 수정 작업을 추가
    없을 경우, 작업이 가장 적은 큐를 선택하여 파일 수정 작업을 추가

    """
    def __init__(self) -> None:
        self.__task_queue = dict()
        self.__task_id_queue = dict()
        for i in range(config.DBMS.task_thread_count): # 이 작업이 필요하기 때문에 __task_queue 와 __task_id_queue 를 클래스 변수로 선언하지 않음
            self.__task_queue.update({i: Queue()})
            self.__task_id_queue.update({i: list()})

    @property
    def queue(self) -> dict:
        return self.__task_queue
    
    @property
    def id_queue(self) -> dict:
        return self.__task_id_queue

    def _check_id_queue(self, id: str) -> typing.Union[None, int]:
        """id가 self.__task_id_queue 에 있는지 검사 -> 없음(none) or Queue 번호
        """
        for i in range(config.DBMS.task_thread_count):
            if id in self.id_queue[i]:
                return i
        else:
            return None

    def _dlt_id_queue(self, id: str) -> bool:
        for i in range(config.DBMS.task_thread_count):
            if id in self.id_queue[i]:
                self.id_queue[i].remove(id)
                return True
        else:
            return False

    def _get_smallest_queue(self) -> typing.Tuple[Queue, int]:
        count = dict()
        for i in range(config.DBMS.task_thread_count):
            count.update({i: self.queue[i].qsize()})

        min_index = min(count, key=count.get)

        return self.queue[min_index], min_index

    def put_task(self, id: str, data: dict) -> None:
        checkValue = self._check_id_queue(id)
        # 만약 있을 경우
        if type(checkValue) == int:
            self.queue[checkValue].put(data, timeout=80)
            self.id_queue[checkValue].append(id)

        # 만약 없을 경우
        elif checkValue == None:
            sm_queue, sm_index = self._get_smallest_queue()
            sm_queue.put(data, timeout=80)
            self.id_queue[sm_index].append(id)

    def get_task(self, thread_number: int) -> dict:
        if self.queue[thread_number].qsize == 0:
            return None
        task: dict = self.queue[thread_number].get(timeout=80)
        self._dlt_id_queue(task.get('Identifier'))
        return task

    def get_current_tasks_count(self):
        return sum([i.qsize() for i in self.queue.values()])


    def _debug_prt_jobs_in_each_queue_count(self) -> None:
        """## DEBUG FUNC
        - 각 큐에 있는 작업 개수와 총 작업 개수, 큐 개수 출력
        - config.DEBUG가 True 일 경우에만 작동

        """
        if config.DEBUG:
            print(f"EachQueueSize: {(task := [i.qsize() for i in self.queue.values()])} | TotalTaskCount: {sum(task)} | QueueCount: {config.DBMS.task_thread_count}")



class TaskNotFound(Exception):
    def __init__(self, task_id: str, data: dict) -> None:
        super().__init__(f'Not Fount Task({task_id}) - {data}')

