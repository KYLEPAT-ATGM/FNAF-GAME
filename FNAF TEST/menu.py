import tkinter as tk
from tkinter import ttk, messagebox
import pygame

def scale_value(easy_value, max_value, difficulty):
    """Scale a value based on difficulty level (1–10)."""
    return easy_value + (max_value - easy_value) * (difficulty - 1) / 9

class FNAFMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nightmera")
        
        # Configuration dictionaries
        self.global_power_easy = {
            "idle_power": 0.00281,
            "camera_power": 0.003,
            "door_power": 0.0025,
            "both_doors_power": 0.0055,
            "door_bang_power": 0.01,
            "vent_flash_power": 0.003,
        }

        self.global_power_max = {
            "idle_power": 0.00561,
            "camera_power": 0.008,
            "door_power": 0.007,
            "both_doors_power": 0.0145,
            "door_bang_power": 0.035,
            "vent_flash_power": 0.008,
        }

        self.penny_easy = {
            "probability": 0.0025,
            "increment": 0.0005,
        }

        self.penny_max = {
            "probability": 0.02,
            "increment": 0.02,
        }

        self.egg_easy = {
            "time_not_looked": 60000,
        }

        self.egg_max = {
            "time_not_looked": 15000,
        }

        self.wolfington_easy = {
            "camera_open_count": 50,
        }

        self.wolfington_max = {
            "camera_open_count": 8,
        }
        
        # Window setup
        window_width = 1920
        window_height = 1080
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        self.root.configure(bg='black')
        style = ttk.Style()
        style.configure('Custom.TButton', 
                       background='#2b2b2b',
                       foreground='white',
                       font=('Arial', 12, 'bold'),
                       padding=10)
        
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(expand=True)
        
        title_label = tk.Label(self.main_frame,
                             text="Nightmera",
                             font=('Arial', 24, 'bold'),
                             fg='red',
                             bg='black')
        title_label.pack(pady=20)
        
        self.selected_night = tk.StringVar(value="Night 1")
        night_frame = tk.Frame(self.main_frame, bg='black')
        night_frame.pack(pady=20)
        
        tk.Label(night_frame,
                text="Select Night:",
                font=('Arial', 14),
                fg='white',
                bg='black').pack()
        
        nights = ["Night 1", "Night 2", "Night 3", "Night 4"]
        night_menu = ttk.OptionMenu(night_frame, self.selected_night, "Night 1", *nights)
        night_menu.pack(pady=10)
        
        button_frame = tk.Frame(self.main_frame, bg='black')
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
        
        extra_button = tk.Button(button_frame,
                               text="Extra",
                               command=self.open_custom_night,
                               font=('Arial', 12, 'bold'),
                               bg='#2b2b2b',
                               fg='white',
                               width=20,
                               height=2)
        extra_button.pack(pady=10)
        
        quit_button = tk.Button(button_frame,
                              text="Quit",
                              command=self.root.destroy,
                              font=('Arial', 12, 'bold'),
                              bg='#2b2b2b',
                              fg='white',
                              width=20,
                              height=2)
        quit_button.pack(pady=10)
        
        version_label = tk.Label(self.root,
                               text="v1.0",
                               font=('Arial', 10),
                               fg='gray',
                               bg='black')
        version_label.pack(side='bottom', pady=10)

        controls_text = (
            "[A] - LEFT DOOR\n"
            "[D] - RIGHT DOOR\n"
            "[SPACEBAR] - CAMERA MODE\n"
            "[1,2,3,4,5,6,7] - CAMERA KEYS (Only works in camera mode)\n"
            "[S] - VENT MODE\n"
            "[F] - FLASH VENT (Only works in vent mode)"
        )
        controls_label = tk.Label(self.root,
                                text="CONTROLS\n\n" + controls_text,
                                font=('Arial', 12),
                                fg='white',
                                bg='black',
                                justify='left')
        controls_label.pack(anchor='nw', padx=10, pady=10)

        self.custom_night_frame = None

    def validate_difficulty(self, value):
        """Validate that the difficulty is between 1 and 10"""
        try:
            num = int(value)
            return 1 <= num <= 10
        except ValueError:
            return False

    def open_custom_night(self):
        self.main_frame.pack_forget()
        
        if self.custom_night_frame:
            for widget in self.custom_night_frame.winfo_children():
                widget.destroy()
        else:
            self.custom_night_frame = tk.Frame(self.root, bg='black')
        
        self.custom_night_frame.pack(expand=True)
        
        tk.Label(self.custom_night_frame,
                text="CUSTOM NIGHT",
                font=('Arial', 14, 'bold'),
                fg='red',
                bg='black').pack(anchor='center', padx=10, pady=10)

        # Validation command
        vcmd = (self.root.register(self.validate_difficulty), '%P')

        # Create difficulty inputs with validation
        difficulties = [
            ("Global Power Difficulty", "global_difficulty"),
            ("Penny Difficulty", "penny_difficulty"),
            ("Egg Difficulty", "egg_difficulty"),
            ("Wolfington Difficulty", "wolfington_difficulty")
        ]

        for label_text, var_name in difficulties:
            frame = tk.Frame(self.custom_night_frame, bg='black')
            frame.pack(pady=5)
            
            tk.Label(frame,
                    text=f"{label_text} (1-10):",
                    font=('Arial', 12),
                    fg='white',
                    bg='black').pack(side='left', padx=5)
            
            spinbox = tk.Spinbox(frame, 
                               from_=1, 
                               to=10, 
                               validate='all', 
                               validatecommand=vcmd,
                               width=5)
            spinbox.delete(0, 'end')
            spinbox.insert(0, "1")
            spinbox.pack(side='left', padx=5)
            setattr(self, var_name, spinbox)

        tk.Button(self.custom_night_frame,
                text="Start Night",
                command=self.start_custom_night,
                font=('Arial', 12, 'bold'),
                bg='#2b2b2b',
                fg='white',
                width=20,
                height=2).pack(pady=20)

        tk.Button(self.custom_night_frame,
                text="Back",
                command=self.back_to_main_menu,
                font=('Arial', 12, 'bold'),
                bg='#2b2b2b',
                fg='white',
                width=20,
                height=2).pack(pady=10)

    def back_to_main_menu(self):
        if self.custom_night_frame:
            self.custom_night_frame.pack_forget()
        self.main_frame.pack(expand=True)

    def start_custom_night(self):
        # Get and validate difficulties
        try:
            difficulties = {
                'global': int(self.global_difficulty.get()),
                'penny': int(self.penny_difficulty.get()),
                'egg': int(self.egg_difficulty.get()),
                'wolfington': int(self.wolfington_difficulty.get())
            }
            
            if not all(1 <= d <= 10 for d in difficulties.values()):
                raise ValueError("All difficulties must be between 1 and 10")
                
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
            return

        # Scale the difficulties
        global_power = {
            key: scale_value(self.global_power_easy[key], self.global_power_max[key], difficulties['global'])
            for key in self.global_power_easy
        }

        penny = {
            key: scale_value(self.penny_easy[key], self.penny_max[key], difficulties['penny'])
            for key in self.penny_easy
        }

        egg = {
            key: scale_value(self.egg_easy[key], self.egg_max[key], difficulties['egg'])
            for key in self.egg_easy
        }

        wolfington = {
            key: scale_value(self.wolfington_easy[key], self.wolfington_max[key], difficulties['wolfington'])
            for key in self.wolfington_easy
        }

        # Close the menu
        self.root.destroy()

        # Initialize Pygame and start the game
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        import main
        main.custom_night(global_power, penny, egg, wolfington)

    def start_game(self):
        selected_night = self.selected_night.get()
        night_number = int(selected_night.split()[1])
        
        self.root.destroy()
        
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