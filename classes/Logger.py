from datetime import datetime
import os
from typing import Literal
import config

raise("다음에 ONLY SAVE 기능 만들기")

class Logger:
    _instance = None
    COUNT = False
    log_format = "{}{} / [{}.{}] [{}]: {}{}"
    save_level = ["debug", "info", "warn", "error"]
    level_type = ["debug", "info", "warn", "error", "crit", "set"]

    def _getTimeFormat():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]


    def _log(log: str, level: Literal["debug", "info", "warn", "error", "crit", "set"], name: str) -> None:
        """(실제 LOG 출력 내부함수)"""
        Logger._count() # COUNT 가 존재하는지 확인
        print(Logger.log_format.format(config.Logger.log_color[level][0], (formated_time := Logger._getTimeFormat()), level.upper(), Logger.COUNT, name, log, config.Logger.log_color[level][1]))

        if config.Logger.SaveLog: 
            Logger._save(msg = Logger.log_format.format('', formated_time, level.upper(), Logger.COUNT, name, log, ''), level=level)


    def _save(msg: str, level: Literal["debug", "info", "warn", "error", "crit", "set"]):
        """(로그 파일 저장 관리 내부함수)"""
        if level in Logger.save_level:
            FilePrefix = level
        # if level == 'debug': FilePrefix = 'debug'
        # elif level == 'info': FilePrefix = 'info'
        # elif level == 'warn': FilePrefix = 'warn'
        # elif level == 'error' or level == 'crit' : FilePrefix = 'error'
        elif level == 'crit' : FilePrefix = 'error'
        elif level == 'set' : FilePrefix = 'info'
        else: FilePrefix = f'notSetLevel.{level}'

        time_text = datetime.now().strftime("%Y-%m-%d")
        dir_path = f"{config.Logger.SaveLogPath}{time_text}"

        if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))

        if not os.path.isfile(f"{dir_path}/{Logger.COUNT}_{FilePrefix}_" + time_text + ".log"):
            f = open(f"{dir_path}/{Logger.COUNT}_{FilePrefix}_" + time_text + ".log", "w", encoding="utf-8")
        else:
            f = open(f"{dir_path}/{Logger.COUNT}_{FilePrefix}_" + time_text + ".log", "a", encoding="utf-8")
        f.write(msg + "\n")
        f.close()


    def _count():
        if type(Logger.COUNT) == int:
            return

        time_text = datetime.now().strftime("%Y-%m-%d")
        dir_path = f"{config.Logger.SaveLogPath}{time_text}"
    
        if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))

        file_list = os.listdir(f"{dir_path}/")
        file_list_count = [file for file in file_list if file.endswith(".count")]

        if len(file_list_count) == 0:
            Logger.COUNT = 0
            with open(f"{dir_path}/{Logger.COUNT}.count", "w", encoding="utf-8") as f:
                f.write(f'{Logger._getTimeFormat()}' + "\n")

        else:
            count = int(file_list_count[0].split('.')[0])
            os.rename(f'{dir_path}/{count}.count', f'{dir_path}/{count+1}.count')

            Logger.COUNT = count+1

            with open(f"{dir_path}/{Logger.COUNT}.count", "a", encoding="utf-8") as f:
                f.write(f'{Logger._getTimeFormat()}' + "\n")

        Logger.set(log=f'SET LOGGER COUNT > {Logger.COUNT}', name='Logger', detail='count')


    def debug(log: str, name: str = config.NAME, detail: str = 'main'):
        """- 디버그 로그"""
        Logger._log(log=log, level='debug', name=f'{name}.{detail}')

    def info(log: str, name: str = config.NAME, detail: str = 'main'):
        """- 일반적인 로그"""
        Logger._log(log=log, level='info', name=f'{name}.{detail}')

    def warn(log: str, name: str = config.NAME, detail: str = 'main'):
        """- 경고 로그"""
        Logger._log(log=log, level='warn', name=f'{name}.{detail}')

    def error(log: str, name: str = config.NAME, detail: str = 'main'):
        """- 대처 가능한 오류 로그"""
        Logger._log(log=log, level='error', name=f'{name}.{detail}')

    def crit(log:str, name: str = config.NAME, detail: str = 'main'):
        """- 치명적인 오류 로그"""
        Logger._log(log=log, level='crit', name=f'{name}.{detail}')

    def set(log:str, name: str = config.NAME, detail: str = 'main'):
        """- 설정 기록 로그"""
        Logger._log(log=log, level='set', name=f'{name}.{detail}')
