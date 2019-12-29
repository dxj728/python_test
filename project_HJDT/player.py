# --coding:utf-8--
# File: player.py
# Author: dxj728
# Time: 2019年12月29日23时
# 说明：

import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
import pygame.font

from bullet import *
import monster_manager as mm

# 定义角色向右移动的常量
DIR_RIGHT = 1
# 定义角色向左移动的常量
DIR_LEFT = 2