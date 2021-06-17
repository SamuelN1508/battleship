import json

class Game_Statistic:

	def __init__(self):
		self.win = False 
		self.score = 100
		self.steps = 0

	def reset_gameStat(self):
		self.win = False 
		self.score = 100
		self.steps = 0
