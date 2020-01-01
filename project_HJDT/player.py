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

# 定义角色的最高生命值
MAX_HP = 50
# 定义控制角色动作的常量
# 此处控制该角色值包含站立， 跑动，跳跃等动作
ACTION_STAND_RIGHT = 1
ACTION_STAND_LEFT = 2
ACTION_RUN_RIGHT = 3
ACTION_RUN_LEFT = 4
ACTION_JUMP_RIGHT = 5
ACTION_JUMP_LEFT = 6
# 定义角色向右移动的常量
DIR_RIGHT = 1
# 定义角色向左移动的常量
DIR_LEFT = 2
# 定义控制该角色移动的常量
# 此处控制该角色只包含站立，向左移动，向右移动三种移动方式
MOVE_STAND = 0
MOVE_RIGHT = 1
MOVE_LEFT = 2
MAX_LEFT_SHOOT_TIME = 6

class Player(Sprite):
	def __init__(self, view_manager, name, hp):
		super().__init__()
		self.name = name		# 保存角色名字的成员变量
		self.hp = hp		# 保存橘色生命值的成员变量
		self.view_manager = view_manager
		# 保存角色所使用的枪支类型（后续可考虑更换）
		self.gun = 0
		# 保存角色当前动作的成员变量（默认向右站立）
		self.action = ACTION_RUN_RIGHT
		# 代表角色X坐标的属性
		self._x = -1
		# 代表角色Y坐标的属性
		self.y = -1
		# 保存角色发射的所有子弹
		self.bullet_list = Group()
		# 保存角色移动方式的成员变量
		self.MOVE = MOVE_STAND
		# 控制射击状态的保留计数器
		# 每当角色发射一枪时，left_shoot_time都会被设置为MAX_LEFT_SHOOT_TIME,然后递减
		# 只有当left_shoot_time变为0时，角色才能发射下一枪
		self.left_shoot_time = 0
		# 保存角色是否跳跃的属性
		self._is_jump = False
		# 保存角色是否能跳到最高处的成员变量
		self.is_jump_max = False
		self.jump_stop_count = 0
		# 当前正在绘制角色腿部动画的第几帧
		self.index_leg = 0
		# 当前正在绘制的角色头部动画的第几帧
		self.index_head = 0
		# 当前正在绘制的头部图片的X坐标
		self.current_head_draw_x = 0
		# 当前正在绘制的头部图片的Y坐标
		self.current_head_draw_y = 0
		# 当前正在绘制的脚部动画帧的图片
		self.current_leg_bitmap = None
		# 当前正在绘制的头部动画帧的图片
		self.current_head_bitmap = None
		# 控制动画刷新的速度变量
		self.draw_count = 0
		# 加载中文字体
		self.font = pygame.font.Font("images/msyh.ttf", 20)

	# 计算角色的当前方向，action变量的值为奇数代表向右
	def get_dir(self):
		return DIR_RIGHT if self.action % 2 == 1 else DIR_LEFT

	def get_x(self):
		return self._x

	def set_x(self, x_val):
		self._x = x_val % (self.view_manager.map.get_width() + self.view_manager.X_DEFAULT)
		# 如果角色一定到屏幕最左边
		if self._x < self.view_manager.X_DEFAULT:
			self._x = self.view_manager.X_DEFAULT

	x = property(get_x, set_x)

	def get_is_jump(self):
		return self._is_jump

	def set_is_jump(self, jump_val):
		self._is_jump = jump_val
		self.jump_stop_count = 6

	is_jump = property(get_is_jump, set_is_jump)

	# 返回该角色在游戏界面上的位移
	def shift(self):
		if self.x <= 0 or self.y <= 0:
			self.init_position()
		return self.view_manager.X_DEFAULT - self.x

	# 绘制角色的名字，头像，生命值的方法
	def draw_head(self, screen):
		if self.view_manager.head == None:
			return
		# 对图片执行镜像（第二个参数控制水平镜像，第三个参数控制垂直镜像）
		head_mirror = pygame.transform.flip(self.view_manager.head, True, False)
		# 绘制头像
		screen.blit(head_mirror, (0, 0))
		# 将名字渲染成图片
		name_image = self.font.render(self.name, True, (230, 23, 23))
		# 绘制名字
		screen.blit(name_image, (self.view_manager.head.get_width(), 10))
		# 将生命值渲染成图片
		hp_image = self.font.render("HP:" + str(self.hp), True, (230, 23, 23))
		# 绘制生命值
		screen.blit(hp_image, (self.view_manager.head.get_width(), 30))


























