# --coding:utf-8--
# File: game_functions.py
# Author: dxj728
# Time: 2019年12月29日22时
# 说明：

import sys
import pygame
from player import *

def check_event(screen, view_manager, player):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():
		# 处理游戏退出
		if event.type == pygame.QUIT:
			sys.exit()
		# 处理按键被按下的事件
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# 当角色的left_shoot_time为0时（上一枪发射结束），角色才能发射下一枪
				if player.left_shoot_time <= 0:
					player.add_buttet(view_manager)
			# 玩家按下向上键，表示跳起来
			if event.key == pygame.K_UP:
				player.is_jump = True
			# 玩家按下向右键，表示向右移动
			if event.key == pygame.K_RIGHT:
				player.move = MOVE_RIGHT
			# 玩家按下向左键，表示向左移动
			if event.key == pygame.K_LEFT:
				player.move = MOVE_LEFT
		# 处理按键被松开的事件
		if event.type == pygame.KEYUP:
			# 玩家松开向右键，表示向右站立
			if event.key == pygame.K_RIGHT:
				player.move = MOVE_STAND
			# 玩家松开向左键，表示向左站立
			if event.key == pygame.K_LEFT:
				player.move = MOVE_STAND



def update_screen(screen, view_manager, mm, player):
	'''处理更新游戏界面的方法'''
	# 随机生成怪物
	mm.generate_monster(view_manager)
	# 处理角色的逻辑
	player.logic(screen)
	# 如果游戏角色已死，则判断出玩家失败
	if player.is_die():
		print('game fail')
	# 检测所有怪物是否将要死亡
	mm.check_monster(view_manager, player)

	# 绘制背景图片
	screen.blit(view_manager.map, (0, 0))
	player.draw(screen)
	# 绘制怪物
	mm.draw_monster(screen, view_manager)
	# 更新屏幕显示,放在最后一行
	pygame.display.flip()


