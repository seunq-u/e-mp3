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

class StatusManager():
    """작업을 추적하기 위해, 작업 객체는 작업에 대한 정보와 상태를 포함하고, 작업이 완료되면 해당 객체의 상태를 업데이트. / 
    작업 객체에 status : '대기 중(waiting)', '진행 중(in progress)', '완료(done)' | result : 대기/실행: None, 성공: True, 실패: False
    와 같은 상태를 부여하여 작업 상태를 확인 가능
    """
    __Status = dict()

    @classmethod
    @property
    def status(cls):
        return cls.__Status

    @classmethod 
    def add_task(cls, id: str, data: dict) -> None:
        new_task = Task(
            id = id,
            data = data,
            status = 'waiting',
            result = None,
            comment = None
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
        for i in range(config.DBMS.task_thread_count):
            self.__task_queue.update({i: Queue()})
            self.__task_id_queue.update({i: list()})

    @property
    def queue(self) -> dict:
        return self.__task_queue
    
    @property
    def id_queue(self) -> dict:
        return self.__task_id_queue

    def _check_id_queue(self, id: typing.Union[str, int]) -> typing.Union[None, int]:
        """id가 self.__task_id_queue 에 있는지 검사
        """
        for i in range(config.DBMS.task_thread_count):
            if id in self.id_queue[i]:
                return i
        else:
            return None

    def _dlt_id_queue(self, id: typing.Union[str, int]) -> bool:
        for i in range(config.DBMS.task_thread_count):
            if id in self.id_queue[i]:
                self.id_queue[i].remove(id)
                return True
        else:
            return False

    def _get_smallest_queue(self) -> tuple[Queue, int]:
        count = dict()
        for i in range(config.DBMS.task_thread_count):
            count.update({i: self.queue[i].qsize()})
        
        min_index = min(count, key=count.get)
        
        return self.queue[min_index], min_index



    def put_task(self, id: typing.Union[str, int], data: dict) -> None:
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



class TaskNotFound(Exception):
    def __init__(self, task_id: str, data: dict) -> None:
        super().__init__(f'Not Fount Task({task_id}) - {data}')