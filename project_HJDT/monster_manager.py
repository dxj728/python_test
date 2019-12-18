# --coding:utf-8--
# File: monster_manager.py
# Author: dxj728
# Time: 2019年12月15日23时
# 说明：怪物管理

from random import randint
from pygame.sprite import Group
from monster import Monster

# 保存所有死掉的怪物，保存它们是为了绘制死亡动画，绘制完成后清除这些怪物
die_monster_list = Group()
# 保存所有或者的怪物
monster_list = Group()

# 随机生成并添加怪物的函数
def generate_monster(view_manager):
	if len(monster_list) < 3 + randint(0, 2):
		# 创建新怪物
		monster = Monster(view_manager, randint(1, 3))
		monster_list.add(monster)

# 更新怪物与子弹的坐标的函数
def update_posistion(screen, view_manager, player, shift):
	# 定义一个list列表，保存所有将要被删除的怪物
	del_list = []
	for monster in monster_list.sprites():		# todo: Group().sprites()
		monster.draw_bullets(screen, view_manager)
		# 更新怪物、怪物所有子弹的位置
		monster.update_shift()
		# 如果怪物的X坐标越界，则将怪物添加到del_list列表中
		if monster.x < 0:
			del_list.append(monster)
	# 删除del_list列表中的所有怪物
	monster_list.remove(del_list)
	del_list.clear()
	# 遍历所有已死的怪物Group
	for monster in die_monster_list.sprites():
		# 更新怪物，怪物所有子弹的位置
		monster.update_shift(shift)
		# 如果怪物的X坐标越界，则将怪物添加到del_list列表中
		if monster.x < 0:
			del_list.append(monster)
	# 删除del_list列表中的所有怪物
	die_monster_list.remove(del_list)

# 绘制所有怪物的函数
def draw_monster(screen, view_manager):
	# 遍历所有活着的怪物，绘制活着的怪物
	for monster in monster_list.sprites():
		# 绘制怪物
		monster.draw(screen, view_manager)
	del_list = []
	# 遍历所有已死亡的怪物，绘制已死亡的怪物
	for monster in die_monster_list.sprites():
		# 绘制怪物
		monster.draw(screen, view_manager)
		# 当怪物的die_max_draw_count返回0时，表明该怪物已经死亡
		# 且该怪物的死亡动画的所有帧都播放完成，将他们彻底删除
		if monster.die_max_draw_count <= 0:
			del_list.append(monster)
	die_monster_list.remove(del_list)

