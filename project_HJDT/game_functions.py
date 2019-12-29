# --coding:utf-8--
# File: game_functions.py
# Author: dxj728
# Time: 2019年12月29日22时
# 说明：

import sys
import pygame

def check_event(screen, view_manager):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():
		# 处理游戏退出
		if event.type == pygame.QUIT:
			sys.exit()

def update_screen(screen, view_manager, mm):
	'''处理更新游戏界面的方法'''
	# 随机生成怪物
	mm.generate_monster(view_manager)
	# 绘制背景图片
	screen.blit(view_manager.map, (0, 0))
	# 绘制怪物
	mm.draw_monster(screen, view_manager)
	# 更新屏幕显示,放在最后一行
	pygame.display.flip()


