import logging
from typing import Literal
from datetime import datetime
import config

log_format = "{}시 {}분 {}초 / [{}{}{}] [{}]: {}"

log_color = {
    "debug" : ('\033[90m', '\033[0m'),
    "info" : ('\033[92m', '\033[0m'),
    "warn" : ('\033[93m', '\033[0m'),
    "error" : ('\033[91m', '\033[0m'),
    "crit" : ('\033[5m\033[1m\033[4m\033[3m\033[31m', '\033[0m')
}

def _getNow():
    now = datetime.now()
    data = {
    'hour' : now.strftime('%H'),
    'minute' : now.strftime('%M'),
    'second' : now.strftime('%S'),
    }
    return data

def _log(log: str, level: Literal["debug", "info", "warn", "error", "crit"], name: str) -> None:
    """(내부함수)"""
    now = _getNow()
    print(log_format.format(now["hour"], now["minute"], now["second"], log_color[level][0], level.upper(), log_color[level][1], name, log))

def debug(log: str, name: str = config.NAME, detail: str = 'main'):
    """- 디버그 로그"""
    _log(log=log, level='debug', name=f'{name}.{detail}')

def info(log: str, name: str = config.NAME, detail: str = 'main'):
    """- 일반적인 로그"""
    _log(log=log, level='info', name=f'{name}.{detail}')

def warn(log: str, name: str = config.NAME, detail: str = 'main'):
    """- 경고 로그"""
    _log(log=log, level='warn', name=f'{name}.{detail}')

def error(log: str, name: str = config.NAME, detail: str = 'main'):
    """- 대처 가능한 오류 로그"""
    _log(log=log, level='error', name=f'{name}.{detail}')

def crit(log:str, name: str = config.NAME, detail: str = 'main'):
    """- 치명적인 오류 로그"""
    _log(log=log, level='crit', name=f'{name}.{detail}')
