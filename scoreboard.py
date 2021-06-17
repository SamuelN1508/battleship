import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ScoreBoard(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="alice blue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="alice blue")
		self.main_frame.pack(expand=True)

		self.scoreboard_number=1
		self.scoreboard_iid=0

		gameData = self.config.gameData

		for data in gameData:
			self.scoreboard_iid+=1
			self.scoreboard_number+=1

		image = Image.open(self.config.you_win_logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.side
		image = image.resize((int(image_w//ratio),int(image_h//ratio)))

		self.you_win_logo = ImageTk.PhotoImage(image)
		self.label_scoreboard_logo = tk.Label(self.main_frame, image=self.you_win_logo)
		self.label_scoreboard_logo.pack(padx=10, pady=50)

		self.btn_play = tk.Button(self.main_frame, text="Play", font=("Arial", 18, "bold"), command=lambda:self.game.create_board())
		self.btn_play.pack(pady=5)

		self.btn_mainMenu = tk.Button(self.main_frame, text="Main Menu", font=("Arial", 18, "bold"), command=lambda:self.game.change_page('mainMenu'))
		self.btn_mainMenu.pack(pady=5)

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 18, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(pady=5)
