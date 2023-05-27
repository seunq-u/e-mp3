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
    """업을 추적하기 위해, 작업 객체는 작업에 대한 정보와 상태를 포함하고, 작업이 완료되면 해당 객체의 상태를 업데이트. / 
    작업 객체에 status : '대기 중(waiting)', '진행 중(in progress)', '완료(done)' | result : 대기/실행: None, 성공: True, 실패: False
    와 같은 상태를 부여하여 작업 상태를 확인 가능
    """
    def __init__(self) -> None:
        self.__Status = dict()

    @property
    def status(self):
        return self.__Status

    def add_task(self, id: str, data: dict) -> None:
        new_task = Task(
            id = id,
            data = data,
            status = 'waiting',
            result = None
        )
        self.status.update({id: new_task})

    def get_task(self, id: str) -> Task:
        try:
            task = self.status[id]
        except KeyError:
            raise TaskNotFound
        else:
            return task

    def set_task(self, id: str, status: typing.Literal['waiting', 'in progress', 'done'], result: typing.Union[None, bool], comment: typing.Union[None, str] = None):
        task = self.get_task(id=id)
        task.status = status
        task.result = result
        task.comment = comment




class QueueManager():
    """각 스레드에 균등하게 작업을 분배 시키기 위해 요청이 들어오면 작업이 가장 적은 큐를 선택하여 요청을 추가 하는 형태로 작동하는 Class
    """
    def __init__(self) -> None:
        self.__task_queue = dict()
        for i in range(config.DBMS.task_thread_count):
            self.__task_queue.update({i: Queue()})

    @property
    def queue(self) -> dict:
        return self.__task_queue

    def get_smallest_queue(self) -> Queue:
        count = dict()
        for i in range(config.DBMS.task_thread_count):
            count.update({i: self.queue[i].qsize()})
        return self.queue[min(count)]

    def put_task(self, data: dict) -> None:
        self.get_smallest_queue().put(data, timeout=80)

    def get_task(self, thread_number: int) -> dict:
        task: Queue = self.queue[thread_number]
        return task.get(timeout=80)



class TaskNotFound(Exception):
    def __init__(self, task_id: str, data: dict) -> None:
        super().__init__(f'Not Fount Task({task_id}) - {data}')