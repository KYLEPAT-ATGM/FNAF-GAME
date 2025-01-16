
import tkinter as tk
from tkinter import ttk, messagebox
import pygame
from PIL import Image, ImageTk
import time

class IntroAnimation:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load('FNAF GAME/moo.mp3')

        # Screen setup
        self.display_size = pygame.display.Info().current_w, pygame.display.Info().current_h - 50
        self.screen = pygame.display.set_mode(self.display_size)

        self.barn = pygame.image.load('barn.png')
        self.news = pygame.image.load('news.png')

        # Center the images
        self.centered_barn = [(self.display_size[0] - self.barn.get_width()) / 2, 
                              (self.display_size[1] - self.barn.get_height()) / 2]
        self.centered_news = [(self.display_size[0] - self.news.get_width()) / 2, 
                              (self.display_size[1] - self.news.get_height()) / 2]
        
        self.skip_animation = False

        self.font = pygame.font.SysFont('Fira Code', 30, 'bold')  # Use a system font

    def check_for_skip(self):
        """Check if the skip key (Spacebar or Numpad Enter) is pressed."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.skip_animation = True
                    break 

    def draw_skip_text(self):
        """Draw the 'Press SPACE to skip' text on the screen."""
        text_surface = self.font.render("BACKSPACE TO SKIP INTRO", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=(self.display_size[0] // 2, self.display_size[1] - 50))  # Bottom center
        self.screen.blit(text_surface, text_rect)

    def fade_in_out_barn(self):
        pygame.time.delay(1000)  # Delay for 1 second
        for i in range(0, 255, 5):  # Fade in
            self.check_for_skip()  # Check for skip key press
            if self.skip_animation:
                break
            self.screen.fill((10, 10, 10))
            self.barn.set_alpha(i)
            self.screen.blit(self.barn, self.centered_barn)
            self.draw_skip_text()
            pygame.display.update()
            pygame.time.delay(10)  # Short delay for smooth transition

        if not self.skip_animation:
            pygame.mixer.music.play()
            pygame.time.delay(2000)  # Delay for 2 seconds
            for i in range(255, 0, -5):  # Fade out
                self.check_for_skip()  # Check for skip key press
                if self.skip_animation:
                    break
                self.screen.fill((10, 10, 10))
                self.barn.set_alpha(i)
                self.screen.blit(self.barn, self.centered_barn)
                self.draw_skip_text()
                pygame.display.update()
                pygame.time.delay(10) 

    def zoom_in_news(self):
        scale_factor = 0.1
        while scale_factor <= 1.0:
            self.check_for_skip()  # Check for skip key press
            if self.skip_animation:
                break
            self.screen.fill((0, 0, 0))
            scaled_news = pygame.transform.scale(self.news, 
                                                  (int(self.news.get_width() * scale_factor), 
                                                   int(self.news.get_height() * scale_factor)))
            centered_scaled_news = [(self.screen.get_width() - scaled_news.get_width()) / 2, 
                                    (self.screen.get_height() - scaled_news.get_height()) / 2]
            self.screen.blit(scaled_news, centered_scaled_news)
            pygame.display.update()
            scale_factor += 0.05
            pygame.time.delay(10)

        if not self.skip_animation:
            start_time = pygame.time.get_ticks()  # Get the current time
            while pygame.time.get_ticks() - start_time < 4000:  # Wait for 5000 milliseconds (5 seconds)
                self.check_for_skip()  # Check for skip key press
                if self.skip_animation:
                    break
                pygame.time.delay(10)

    def run(self):
        if self.skip_animation:
            return
        
        self.fade_in_out_barn()
        if not self.skip_animation:
            self.zoom_in_news()

def scale_value(easy_value, max_value, difficulty):
    """Scale a value based on difficulty level (1–10)."""
    return easy_value + (max_value - easy_value) * (difficulty - 1) / 9

def run_menu(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((50, 50, 50))  # Example menu background color
        pygame.display.update()

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
        # Load and resize background image
        # Add these to your __init__ method
        self.current_page = 0
        self.total_pages = 5  # Number of pages you want
        self.controls_panel = None
        self.custom_night_frame = None

        try:
            bg_image = Image.open('FNF.png')
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            bg_image = bg_image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.root.configure(bg='black')

        # Window setup for fullscreen
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg='black')

        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.place(relx=0.92, rely=0.72, anchor='center')  # Positioned at bottom-right

        title_label = tk.Label(self.main_frame,
                               text="𝙽𝚒𝚐𝚑𝚝𝚖𝚎𝚛𝚊",
                               font=('Arial', 40, 'bold'),
                               fg='red',
                               bg='black')
        title_label.pack(pady=20)

        self.selected_night = tk.StringVar(value="Night 1")
        night_frame = tk.Frame(self.main_frame, bg='black')
        night_frame.pack(pady=20)

        tk.Label(night_frame,
                text="ꜱᴇʟᴇᴄᴛ ɴɪɢʜᴛ:",
                font=('Arial', 20),
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

        controls_button = tk.Button(button_frame,
                                    text="Information",
                                    command=self.show_controls,
                                    font=('Arial', 12, 'bold'),
                                    bg='#2b2b2b',
                                    fg='white',
                                    width=20,
                                    height=2)
        controls_button.pack(pady=10)

        credits_button = tk.Button(button_frame,
                                   text="Credits",
                                   command=self.show_credits,
                                   font=('Fira Code', 12, 'bold'),
                                   bg='#2b2b2b',
                                   fg='white',
                                   width=20,
                                   height=2)
        credits_button.pack(pady=10)

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
                                font=('Arial', 10, 'bold'),
                                fg='black',
                                bg='light grey')
        version_label.pack(side='bottom', pady=10)

    def show_credits(self):
        """Display the credits in appreciation of those who contributed"""
        # Check if the credits panel already exists
        if hasattr(self, 'credit_panel'):
            # If it exists, toggle its visibility
            if self.credit_panel.winfo_ismapped():
                self.credit_panel.place_forget()  # Hide the panel
            else:
                self.credit_panel.place(relx=0.5, rely=0.5, anchor='center', width=700, height=550)  # Show the panel
            return

        # Create a credits panel
        self.credit_panel = tk.Frame(self.root, bg='dark grey', bd=2, relief='ridge')
        self.credit_panel.place(relx=0.5, rely=0.5, anchor='center', width=700, height=550)  # Center the panel with fixed size

        # Add a label for the credits text
        credit_text = (
            'Artist: Estelle Pat\n'
            'Coders: Kyle Pat & Johnny Ren\n'
            'VFX & Inspiration: FNAF by Scott Cawthon'
        )
        credit_labels = tk.Label(self.credit_panel,
                                text=credit_text,
                                font=('Arial', 15, 'bold'),
                                fg='black',
                                bg='dark grey',
                                justify='left')
        credit_labels.pack(pady=20, padx=20)

        # Add a Close button
        close_button = tk.Button(self.credit_panel,
                                text="Close",
                                command=lambda: self.credit_panel.place_forget(),
                                font=('Arial', 12, 'bold'),
                                bg='#2b2b2b',
                                fg='white',
                                width=15,
                                height=2)
        close_button.pack(pady=15, side='bottom')

        self.custom_night_frame = None

    def show_controls(self):
        """Display the controls and information panel."""
        
        # Create the controls panel if it doesn't exist
        if not hasattr(self, 'controls_panel') or self.controls_panel is None:
            # Create the controls panel
            self.controls_panel = tk.Frame(self.root, bg='dark grey', bd=2, relief='ridge')
            self.controls_panel.place(relx=0.5, rely=0.5, anchor='center', width=700, height=550)

            self.content_label = tk.Label(
                self.controls_panel,
                text="",
                font=("Arial", 15),
                justify="left",
                anchor="nw",
                wraplength=680,  # Slightly less than panel width to account for padding
                bg=self.controls_panel["bg"],  # Match panel's background color
                fg="black",  # Set text color to black
                borderwidth=0,  # Remove borders
                padx=10,  # Add padding for a polished look
                pady=10
            )
            self.content_label.place(relx=0.5, rely=0.05, anchor="n")  # Adjust 'rely' for vertical position

            # Add navigation buttons
            button_frame = tk.Frame(self.controls_panel, bg='dark grey')
            button_frame.pack(pady=15, side='bottom')

            back_button = tk.Button(button_frame,
                                    text="<",
                                    command=self.previous_page,
                                    font=('Arial', 12, 'bold'),
                                    bg='#2b2b2b',
                                    fg='white',
                                    width=10,
                                    height=2)
            back_button.pack(side='left')

            close_button = tk.Button(button_frame,
                                    text="Close",
                                    command=lambda: self.controls_panel.place_forget(),
                                    font=('Arial', 12, 'bold'),
                                    bg='#2b2b2b',
                                    fg='white',
                                    width=10,
                                    height=2)
            close_button.pack(side='left')

            next_button = tk.Button(button_frame,
                                    text=">",
                                    command=self.next_page,
                                    font=('Arial', 12, 'bold'),
                                    bg='#2b2b2b',
                                    fg='white',
                                    width=10,
                                    height=2)
            next_button.pack(side='left')

            # Add page indicator
            self.page_indicator = tk.Label(button_frame,
                                        text=f"Page {self.current_page + 1}/{self.total_pages}",
                                        font=('Arial', 12),
                                        bg='dark grey',
                                        fg='black')
            self.page_indicator.pack(side='bottom', pady=5)

            # Update initial content
            self.update_page_content()
        else:
            # If it exists, toggle its visibility
            if self.controls_panel.winfo_ismapped():
                self.controls_panel.place_forget()  # Hide the panel
            else:
                self.controls_panel.place(relx=0.5, rely=0.5, anchor='center', width=700, height=550)  # Show the panel

    def get_page_content(self, page_number):
        """Return content for the specified page number."""
        content = {
            0: ('Game Controls\n\n'
                '[A] - Close/Open Left Door\n'
                '[D] - Close/Open Right Door \n'
                '[S] - Check Vent\n'
                '[F] - Flash Vent (Only if Vent Is Open)\n'
                '[Space]- Open Camera Screen\n'
                '[1,2,3,4,5,6] - View Cameras (Only If Camera Screen Is Open)\n'
                '[Esc] - Close Game'),
            
            1: ('About The Animatronics\n\n'
                'Penny - [ANIMATRONIC 1] - Moves in probability intervals,\n'
                'when they reach CAM 2, you must shut the door before\n'
                '5 seconds of them reaching it, or you will die.\n'
                'Resets after 8 seconds of door closed.'),
            
            2: ('Egg - [ANIMATRONIC 2] - Starts in CAM 7 and moves to' 
                'CAM 4 after being reset. You must stay on their camera\n'
                'for 5 seconds to reset, if not reset, after certain time,\n'
                'they will attack on CAM 1 where user must close door,\n'
                'or you will die. Resets at door after 8 seconds.'),

            3: ('Wolfington - [ANIMATRONIC 3] - Stays in CAM 3 and'
                ' will move to vent after camera was flipped enough times.\n'
                'When in vents, flash them for 5 seconds to reset.'),

            4: ('Others\n\n'
                'If you see the light bulb blink, that means that an animatronic\n'
                'has moved position.\n\n'
                'If you hear running sounds, that means that\n'
                'an animatronic is moving towards you')
        }
        return content.get(page_number, "Error: Page not found")

    def update_page_content(self):
        """Update the content based on current page."""
        content = self.get_page_content(self.current_page)
        self.content_label.config(text=content)
        self.page_indicator.config(text=f"Page {self.current_page + 1}/{self.total_pages}")

    def next_page(self):
        """Move to the next page if available."""
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.update_page_content()

    def previous_page(self):
        """Move to the previous page if available."""
        if self.current_page > 0:
            self.current_page -= 1
            self.update_page_content()

    def validate_difficulty(self, value):
        """Validate that the difficulty is between 1 and 10"""
        try:
            num = int(value)
            return 1 <= num <= 10
        except ValueError:
            return False

    def open_custom_night(self):
        """Open the custom night configuration screen"""
        # If custom night frame exists, clear it. If not, create it
        if self.custom_night_frame is not None:
            self.custom_night_frame.destroy()
        
        # Create new custom night frame
        self.custom_night_frame = tk.Frame(self.root, bg='black')
        self.custom_night_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Create the content
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

        # Add buttons
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
        """Return to the main menu"""
        if self.custom_night_frame:
            self.custom_night_frame.place_forget()
            self.custom_night_frame.destroy()
            self.custom_night_frame = None
        self.main_frame.place(relx=0.92, rely=0.72, anchor='center')

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
        global_power_settings = {
            key: scale_value(self.global_power_easy[key], self.global_power_max[key], difficulties['global'])
            for key in self.global_power_easy
        }
        penny_settings = {
            key: scale_value(self.penny_easy[key], self.penny_max[key], difficulties['penny'])
            for key in self.penny_easy
        }
        egg_settings = {
            key: scale_value(self.egg_easy[key], self.egg_max[key], difficulties['egg'])
            for key in self.egg_easy
        }
        wolfington_settings = {
            key: scale_value(self.wolfington_easy[key], self.wolfington_max[key], difficulties['wolfington'])
            for key in self.wolfington_easy
        }

        # Close the menu
        self.root.destroy()

        # Initialize Pygame and start the game
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        
        # Start game directly without loading screen for custom night
        import main
        main.custom_night(global_power_settings, penny_settings, egg_settings, wolfington_settings)

    def start_game(self):
        selected_night = self.selected_night.get()
        night_number = int(selected_night.split()[1])
        
        self.root.destroy()
        
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        
        # Create and run loading screen before starting the game
        loading_screen = SimpleLoadingScreen()
        loading_complete = loading_screen.run()
        
        if loading_complete:
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

import pygame
import time

import pygame
import time

class SimpleLoadingScreen:
    def __init__(self):
        pygame.init()
        
        # Screen setup
        self.display_size = pygame.display.Info().current_w, pygame.display.Info().current_h - 50
        self.screen = pygame.display.set_mode(self.display_size)
        self.bobby = pygame.image.load("bobby.png")
        self.centered_bobby = [(self.display_size[0] - self.bobby.get_width()) / 2, 
                              (self.display_size[1] - self.bobby.get_height()) / 2]

        self.BLACK = (0, 0, 0)
        
    def draw(self):
        # Fill the screen with black
        self.screen.fill(self.BLACK)
        # Draw the image on the screen
        self.screen.blit(self.bobby, self.centered_bobby)
        pygame.transform.scale(self.bobby , (self.display_size[0], self.display_size[1]))
        # Update the display
        pygame.display.update()
    
    def run(self):
        # Draw the loading screen
        self.draw()
        # Keep the loading screen visible for 3 seconds
        time.sleep(3)
        # Return True to indicate loading is complete
        return True

if __name__ == "__main__":
    pygame.init()
    splash = IntroAnimation()
    splash.run()
    pygame.quit()
    menu = FNAFMenu()
    menu.run()