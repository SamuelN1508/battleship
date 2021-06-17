import tkinter as tk
from PIL import Image, ImageTk


class LoginPage(tk.Frame):
	
	def __init__(self, parent, Game):
		
		self.game = Game
		self.config = Game.config

		super().__init__(parent)
		self.configure(bg="black")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, width=self.config.side, height=self.config.side, bg="black")
		self.main_frame.pack(expand=True)

		image = Image.open(self.config.logo_path)
		image_w, image_h = image.size
		ratio = image_w/self.config.side
		image = image.resize((int(image_w//ratio),int(image_h//ratio)))

		self.logo = ImageTk.PhotoImage(image)
		self.label_logo = tk.Label(self.main_frame, image=self.logo)
		self.label_logo.pack(padx=10, pady=5)

		self.label_username = tk.Label(self.main_frame, text="username", anchor="w" ,font=("Arial", 18, "bold"), bg="black", fg="white")
		self.label_username.pack(fill="both")

		self.var_username = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable=self.var_username)
		self.entry_username.pack(fill="x")

		self.label_password = tk.Label(self.main_frame, text="password", anchor="w",font=("Arial", 18, "bold"), bg="black", fg="white")
		self.label_password.pack(fill="both")

		self.var_password = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*", textvariable=self.var_password)
		self.entry_password.pack(fill="x")

		self.btn_login = tk.Button(self.main_frame, text="LOGIN", font=("Arial", 18, "bold"), bg="black", fg="white",command=lambda:self.game.auth_login())
		self.btn_login.pack(pady=5, padx=10)

