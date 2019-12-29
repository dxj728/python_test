# --coding:utf-8--
# File: monster.py
# Author: dxj728
# Time: 2019年12月15日18时
# 说明：python3.5环境

import pygame
import sys
from random import randint
from pygame.sprite import Sprite
from pygame.sprite import Group
from bullet import *

# 怪物速度
COMMON_SPEED_THRESHOLD = 10
# 人的速度
MAN_SPEED_THRESHOLD = 8

# 定义代表怪物类型的常量
TYPE_BOMB = 1
TYPE_FLY = 2
TYPE_MAN = 3

class Monster(Sprite):
	def __init__(self, view_manager, tp=TYPE_BOMB):
		super().__init__()
		self.type = tp		# 定义怪物类型
		self.x = 0		# 怪物的X坐标属性
		self.y = 0  	# 怪物的Y坐标属性
		self.is_die = False		# 怪物是否已死亡
		self.start_x = 0		# 怪物图片左上角的X坐标
		self.start_y = 0  		# 怪物图片左上角的Y坐标
		self.end_x = 0		# 怪物右下角的X坐标
		self.end_y = 0  	# 怪物右下角的Y坐标
		self.draw_count = 0		# 控制动画刷新的速度
		self.draw_index = 0		# 定义当前正在绘制怪物动画的第几帧的变量
		'''
			用于记录死亡的动画只用绘制一次，不用重复绘制
			每当怪物死亡时，该变量都会被初始化为等于死亡动画的总帧数
			当怪物的死亡动画帧播放完成后，该变量的值变为0
		'''
		self.die_max_draw_count = sys.maxsize
		self.bullet_list = Group() 		#定义怪物发射的子弹
		'''
			根据怪物的类型来初始化怪物的X，Y坐标
			怪物是炸弹或敌人：怪物的Y坐标与玩家角色的Y坐标相同
			怪物是飞机: 根据屏幕高度随机生成怪物的Y坐标
		'''
		if self.type == TYPE_BOMB or self.type == TYPE_MAN:
			self.y = view_manager.Y_DEFAULT
		elif self.type == TYPE_FLY:
			self.y = view_manager.screen_height * 50 / 100 - randint(0, 99)
		# 随机计算怪物的X坐标
		self.x = view_manager.screen_width + randint(0, view_manager.screen_width >> 1) - (view_manager.screen_width >> 2)

	# 绘制这怪物的方法
	def draw(self, screen, view_manager):
		# 如果怪物是炸弹，则绘制炸弹
		if self.type == TYPE_BOMB:
			self.draw_anim(screen, view_manager, view_manager.bomb2_images if self.is_die else view_manager.bomb_images)
		# 如果怪物是飞机，则绘制飞机
		elif self.type == TYPE_FLY:
			self.draw_anim(screen, view_manager, view_manager.fly_die_images if self.is_die else view_manager.fly_images)
		# 如果怪物是人，则绘制人
		elif self.type == TYPE_MAN:
			self.draw_anim(screen, view_manager, view_manager.man_die_images if self.is_die else view_manager.man_images)
		else:
			pass

	# 根据怪物的动画帧图片来绘制怪物动画
	def draw_anim(self, screen, view_manager, bitmap_arr):
		# 如果怪物已死亡，且没有播放过死亡动画
		# (self.die_max_draw_count 等于初始值，表明未播放过死亡动画)
		if self.is_die and self.die_max_draw_count == sys.maxsize:
			# 将die_max_draw_count设置为与死亡动画的总帧数相等
			self.die_max_draw_count = len(bitmap_arr)
		self.draw_index %= len(bitmap_arr)
		# 获取当前绘制的动画帧对应的位图
		bitmap = bitmap_arr[self.draw_index]
		if bitmap == None:
			return
		draw_x = self.x
		# 对绘制怪物动画帧位图的X坐标进行微调
		if self.is_die:
			if self.type == TYPE_BOMB:
				draw_x = self.x - 50
			elif self.type == TYPE_MAN:
				draw_x = self.x + 50
		# 对绘制怪物动画帧位图的Y坐标进行微调
		draw_y = self.y - bitmap.get_height()
		# 绘制怪物动画帧的位图
		screen.blit(bitmap, (draw_x, draw_y))
		self.start_x = draw_x
		self.start_y = draw_y
		self.end_x = self.start_x + bitmap.get_width()
		self.end_y = self.start_y + bitmap.get_height()
		self.draw_count = self.draw_count + 1
		# 控制人，飞机发射子弹的速度
		if self.draw_count >= (COMMON_SPEED_THRESHOLD if self.type == TYPE_MAN else MAN_SPEED_THRESHOLD):
			# 如果怪物是人，则只在第三帧发射子弹
			if self.type == TYPE_MAN and self.draw_index == 2:
				self.add_bullet()
			# 如果怪物是飞机，则只在最后一帧才发射子弹
			if self.type == TYPE_FLY and self.draw_index == len(bitmap_arr) - 1:
				self.add_bullet()
			self.draw_index = self.draw_index + 1
			self.draw_count = 0
		# 每播放死亡动画的一帧，self.die_max_draw_count 就减1
		# 每当self.die_max_draw_count等于0时，表明死亡动画播放完成
		if self.is_die:
			self.die_max_draw_count = self.die_max_draw_count -1
		# 绘制子弹
		self.draw_bullets(screen, view_manager)

	# 判断怪物是否被子弹打中的方法
	def is_hurt(self, x, y):
		return self.start_x < x < self.end_x and self.start_y < y < self.end_y

	'''
		根据怪物类型获取子弹类型，不同的怪物发射不同的子弹
		return 0 表示该种怪物不发射子弹
	'''
	def bullet_type(self):
		if self.type == TYPE_BOMB:
			return 0
		elif self.type == TYPE_FLY:
			return BULLET_TYPE_3
		elif self.type == TYPE_MAN:
			return BULLET_TYPE_2
		else:
			return 0

	# 定义发射子弹的方法
	def add_bullet(self):
		# 如果没有子弹
		if self.bullet_type() <= 0:
			return
		# 计算子弹的X,Y坐标
		draw_x = self.x
		draw_y = self.y - 60
		# 如果怪物是飞机，则重新计算飞机发射的子弹的Y坐标
		if self.type == TYPE_FLY:
			draw_y = self.y - 30
		# 创建子弹对象
		bullet = Bullet(self.bullet_type(), draw_x, draw_y, player.DIR_LEFT)
		# 将子弹对象添加到该怪物发射的子弹Group中
		self.bullet_list.add(bullet)

	# 更新子弹的位置，将所有子弹的X坐标减少shift距离
	def update_shift(self, shift):
		self.x = self.x - shift
		for bullet in self.bullet_list:
			if bullet != None:
				bullet.x = bullet - shift


	# 绘制子弹的方法
	def draw_bullets(self, screen, view_manager):
		# 遍历该怪物发射的所有子弹
		for bullet in self.bullet_list.copy():
			# 如果子弹已经越过了屏幕
			if bullet.x <= 0 or bullet.x > view_manager.screen_width:
				# 删除已经移出屏幕的子弹
				self.bullet_list.remove(bullet)
		# 绘制所有子弹
		for bullet in self.bullet_list.sprites():
			# 获取子弹对应的位图
			bitmap = bullet.bitmap(view_manager)
			if bitmap == None:
				continue
			# 子弹移动
			bullet.move()
			# 绘制子弹位图
			screen.blit(bitmap, (bullet.x, bullet.y))



