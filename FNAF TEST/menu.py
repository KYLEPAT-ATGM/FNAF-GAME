import tkinter as tk
from tkinter import ttk
import pygame


class FNAFMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nightmera")
        
        # Set window size and center it
        window_width = 1920
        window_height = 1080
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Set dark theme colors
        self.root.configure(bg='black')
        style = ttk.Style()
        style.configure('Custom.TButton', 
                       background='#2b2b2b',
                       foreground='white',
                       font=('Arial', 12, 'bold'),
                       padding=10)
        
        # Create main container
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True)
        
        # Title
        title_label = tk.Label(main_frame,
                             text="Nightmera",
                             font=('Arial', 24, 'bold'),
                             fg='red',
                             bg='black')
        title_label.pack(pady=20)
        
        # Night selection
        self.selected_night = tk.StringVar(value="Night 1")
        night_frame = tk.Frame(main_frame, bg='black')
        night_frame.pack(pady=20)
        
        tk.Label(night_frame,
                text="Select Night:",
                font=('Arial', 14),
                fg='white',
                bg='black').pack()
        
        nights = ["Night 1", "Night 2", "Night 3", "Night 4"]
        night_menu = ttk.OptionMenu(night_frame, self.selected_night, "Night 1", *nights)
        night_menu.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg='black')
        button_frame.pack(pady=20)
        
        start_button = tk.Button(button_frame,
                               text="New Game",
                               command=self.start_game,
                               font=('Arial', 12, 'bold'),
                               bg='#2b2b2b',
                               fg='white',
                               width=20,
                               height=2)
        start_button.pack(pady=10)
        
        
        
        quit_button = tk.Button(button_frame,
                              text="Quit",
                              command=self.root.destroy,
                              font=('Arial', 12, 'bold'),
                              bg='#2b2b2b',
                              fg='white',
                              width=20,
                              height=2)
        quit_button.pack(pady=10)
        
        # Version number
        version_label = tk.Label(self.root,
                               text="v1.0",
                               font=('Arial', 10),
                               fg='gray',
                               bg='black')
        version_label.pack(side='bottom', pady=10)
    
    def start_game(self):
        selected_night = self.selected_night.get()
        night_number = int(selected_night.split()[1])
        
        # Close the menu
        self.root.destroy()
        
        # Initialize Pygame and start the game
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        
        import main
        if night_number == 1:
            main.night_one()
        elif night_number == 2:
            main.night_two()
        elif night_number == 3:
            main.night_three()
        elif night_number == 4:
            main.night_four()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    menu = FNAFMenu()
    menu.run()