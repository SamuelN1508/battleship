import tkinter as tk
import sys
from config import Config
from main_menu import MainMenu
from player import Player
from board import Board
from loginPage import LoginPage
from scoreboard import ScoreBoard
from game_statistic import Game_Statistic
from ship import Ship
from loginPage import LoginPage

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config
		self.ship = Game.ship
		self.game_statistic = Game.game_statistic

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)
		self.create_container()
		self.pages = {}
		self.create_scoreboard()
		self.create_mainMenu()
		self.create_loginPage()

	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)
		self.ship.generate_answer()

	def create_loginPage(self):
		self.pages['loginPage'] = LoginPage(self.container, self)

	def create_mainMenu(self):
		self.pages['mainMenu'] = MainMenu(self.container, self)

	def create_scoreboard(self):
		self.pages['ScoreBoard'] = ScoreBoard(self.container, self)

	def change_page(self, page):
		page = self.pages[page]
		page.tkraise()

	def auth_login(self):
		username = self.pages['loginPage'].var_username.get()
		password = self.pages['loginPage'].var_password.get()
		granted = self.config.login(username, password)
		if granted:
			self.change_page('mainMenu')

	def insert_data(self):
		player_name = self.pages['loginPage'].var_username.get()
		self.config.gameData_counter+=1
		self.pages['ScoreBoard'].scoreboard_iid = self.pages['ScoreBoard'].scoreboard_iid+1
		self.pages['ScoreBoard'].scoreboard_number = self.pages['ScoreBoard'].scoreboard_number+1
		gameData_label = f"data{self.config.gameData_counter}"
		self.config.gameData[gameData_label] = {
			"name" : player_name,
			"score" : self.game_statistic.score,
			"steps" : self.game_statistic.steps
		}
		self.config.save_gameData(self.config.gameData_path)
		self.config.save_gameData_counter(self.config.gameData_counter)

	def exit(self):
		sys.exit()

class Battleship:

	def __init__(self):
		self.config = Config()
		self.game_statistic = Game_Statistic()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			self.game_statistic.steps+= 1
			return True
		else:
			self.game_statistic.steps+= 1
			self.game_statistic.score+= -4
			return False

	def button_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			self.window.insert_data()
			self.game_statistic.reset_gameStat()
			self.window.change_page('ScoreBoard')

	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()