import tkinter as tk 
from PIL import Image, ImageTk

class MainMenu(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="white")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="white")
		self.main_frame.pack(expand=True)

		image = Image.open(self.config.main_menu_logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.side
		image = image.resize((int(image_w//ratio),int(image_h//ratio)))

		self.main_menu_logo = ImageTk.PhotoImage(image)
		self.label_main_menu_logo = tk.Label(self.main_frame, image=self.main_menu_logo)
		self.label_main_menu_logo.pack(padx=10, pady=50)

		self.btn_play = tk.Button(self.main_frame, text="Play", font=("Arial", 18, "bold"), command=lambda:self.game.create_board())
		self.btn_play.pack(fill="x")

		self.btn_exit = tk.Button(self.main_frame, text="Exit", font=("Arial", 18, "bold"), command=lambda:self.game.exit())
		self.btn_exit.pack(fill="x")
