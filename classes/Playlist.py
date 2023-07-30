"""
# <classes.Playlist.py>
## E-Mp3 Bot Playlist 클래스

* BasePlaylist
* Official
* **User**

###### ⓒ 2023. ManGGo.ß STUDIO All rights reserved.
"""

import time
import typing
import cv2
import numpy as np
import requests
import textwrap
import threading
import io
import matplotlib.pyplot as plt
import orjson
import discord
import uuid
from abc import ABC, abstractmethod
from colorthief import ColorThief
from datetime import datetime
from urllib.request import urlopen
from PIL import ImageFont, ImageDraw, ImageEnhance
from PIL import Image as PIL_Image




class BasePlaylist(ABC):
    def load_music(self):
        """lavalink를 통해 음악을 로드
        """

class Queue():
    pass

class Official(BasePlaylist):
    pass

class User(BasePlaylist):
    pass


