from datetime import datetime
import os
from typing import Literal
import config

class Logger:
    _instance = None
    log_format = "{}{} / [{}] [{}]: {}{}"

    def _getTimeFormat():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    def _log(log: str, level: Literal["debug", "info", "warn", "error", "crit"], name: str) -> None:
        """(내부함수)"""
        print(Logger.log_format.format(config.Logger.log_color[level][0], (formated_time := Logger._getTimeFormat()), level.upper(), name, log, config.Logger.log_color[level][1]))

        if config.Logger.SaveLog: 
            Logger._save(msg = Logger.log_format.format('', formated_time, level.upper(), name, log, ''), level=level)

    def _save(msg: str, level: Literal["debug", "info", "warn", "error", "crit"]):
        if level == 'debug': FilePrefix = 'debug'
        elif level == 'info': FilePrefix = 'info'
        elif level == 'warn': FilePrefix = 'warn'
        elif level == 'error' or level == 'crit' : FilePrefix = 'error'
        else: FilePrefix = f'notSetLevel.{level}'

        time_text = datetime.now().strftime("%Y-%m-%d")

        if not (os.path.isdir(f"{config.Logger.SaveLogPath}{time_text}")):
                os.makedirs(os.path.join(f"{config.Logger.SaveLogPath}{time_text}"))

        if not os.path.isfile(f"{config.Logger.SaveLogPath}{time_text}/{FilePrefix}_" + time_text + ".log"):
            f = open(f"{config.Logger.SaveLogPath}{time_text}/{FilePrefix}_" + time_text + ".log", "w", encoding="utf-8")
        else:
            f = open(f"{config.Logger.SaveLogPath}{time_text}/{FilePrefix}_" + time_text + ".log", "a", encoding="utf-8")
        f.write(msg + "\n")
        f.close()




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
