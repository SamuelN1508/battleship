import json

class Config:

	def __init__(self):

		self.app_title = "Battleship"
		self.row = 5
		self.column = 5
		base = 160
		ratio = 5
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"
		self.init_img_btn = "img/init_img.jpg"
		self.final_img_btn = "img/final_img.png"
		self.win_img_btn = "img/win_img.png"
		self.logo_path = "img/logo.png"
		self.main_menu_logo_path = "img/main_menu_logo.png"
		self.you_win_logo_path = "img/you_win_logo.png"
		self.users_path = "json/users.json"
		self.gameData_path = "json/gameData.json"
		self.gameData_counter_path = "json/gameData_counter.json"
		self.gameData = self.load_gameData(self.gameData_path)
		self.gameData_counter = self.load_gameData_counter(self.gameData_counter_path)

	def login(self, username, password):
		users = self.load_userData(self.users_path)
		if username in users:
			if password == users[username]["password"]:
				return True
			else:
				return False
		else:
			return False

	def load_userData(self, users_path):
		with open(users_path, "r") as json_data:
			userData = json.load(json_data)
		return userData

	def load_gameData(self, gameData_path):
		with open(self.gameData_path, "r") as json_data:
			gameData = json.load(json_data)
		return gameData

	def save_gameData(self, gameData_path):
		with open(self.gameData_path, "w") as json_data:
			json.dump(self.gameData, json_data)

	def load_gameData_counter(self, gameData_counter_path):
		with open(self.gameData_counter_path, "r") as json_data:
			gameData_counter = json.load(json_data)
		return gameData_counter

	def save_gameData_counter(self, gameData_counter_path):
		with open(self.gameData_counter_path, "w") as json_data:
			json.dump(self.gameData_counter, json_data)
