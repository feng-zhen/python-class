# -*- coding: utf-8 -*-
# @Time : 2022-08-13 16:53
# @Author : 68599
# @FileName: class.py
# @Software: PyCharm

# import utility as ut
# import numpy as np
#
# dog = ut.Dog('小花', 5)
# print(dog.species)
# rt = ut.RussellTerrier('小白', 6)

from utility import Dog, Bulldog, RussellTerrier

dog = Dog('小花', 6)
print(dog.name)
bull_dog = Bulldog('小黑', 4)
# Python变量的命名规则，类名、变量名都用可以拼写的单词，类目每个单词首字母大写，变量名每个单词小写中间用下划线分隔开
russell_terrier = RussellTerrier('小白', 5)
