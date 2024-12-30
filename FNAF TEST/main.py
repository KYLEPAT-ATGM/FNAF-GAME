import pygame
import os
import random
from threading import Timer


def night_one():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Get the absolute path of the MP3 file
    ambience_mp3 = "FNAF GAME/AMBIENCE.mp3"
    phone_mp3 = "FNAF GAME/phone night one.mp3"
    # Load and play the MP3 file

    # Play ambience sound on a loop
    ambience_channel = pygame.mixer.Channel(1)
    ambience_sound = pygame.mixer.Sound(ambience_mp3)
    ambience_channel.play(ambience_sound, loops=-1)

    # Play phone sound on a different channel
    phone_channel = pygame.mixer.Channel(2)
    phone_sound = pygame.mixer.Sound(phone_mp3)
    phone_channel.play(phone_sound)

    WIDTH, HEIGHT = 1920, 1080      # SCREEN RESOLUTION using 1080p for simplicity's sake
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nightmera")

    font_size = 36  # You can adjust the size as needed
    font = pygame.font.Font(None, font_size)

    # load sound effects
    door_sound = pygame.mixer.Sound("FNAF GAME/door slam.mp3")
    camera_sound = pygame.mixer.Sound("FNAF GAME/camera open.mp3")
    camera_switch_sound = pygame.mixer.Sound("FNAF GAME/camera switch.mp3")
    jumpscare_sound = pygame.mixer.Sound("FNAF GAME/jumpscare sound.mp3")
    power_out_sound = pygame.mixer.Sound("FNAF GAME/power out.mp3")                     #CURRENTLY DOES NOT WORK UNTIL I FIND A WAY TO LET MUSIC RUN AND PAUSE
    power_out_music = pygame.mixer.Sound("FNAF GAME/power out music.mp3")
    door_bang_sound = pygame.mixer.Sound("FNAF GAME/door bang.mp3")
    run_sound = pygame.mixer.Sound("FNAF GAME/run sound.mp3")
    vent_enter_sound = pygame.mixer.Sound("FNAF GAME/vent enter.mp3")

    #CAMERA BUTTON LOCATION #   https://pixspy.com/ USE THIS TO FIND PIXEL LOCATIONS
    camera_positions = {
        pygame.K_1: pygame.Rect(150, 479, 66, 47),  # Adjust these values based on the map layout
        pygame.K_2: pygame.Rect(322, 484, 72, 43),
        pygame.K_3: pygame.Rect(39, 312, 70, 44),
        pygame.K_4: pygame.Rect(195, 145, 77, 44),
        pygame.K_5: pygame.Rect(458, 149, 78, 44),
        pygame.K_6: pygame.Rect(341, 331, 74, 48),
        pygame.K_7: pygame.Rect(559, 275, 81, 51),
    }

    # load images
    images = {}
    image_paths = {
        pygame.K_1: "FNAF GAME/IMAGES/CAM1.png",
        pygame.K_2: "FNAF GAME/IMAGES/CAM2.png",
        pygame.K_3: "FNAF GAME/IMAGES/CAM3.png",
        pygame.K_4: "FNAF GAME/IMAGES/CAM4.png",
        pygame.K_5: "FNAF GAME/IMAGES/CAM5.png",
        pygame.K_6: "FNAF GAME/IMAGES/CAM6.png",
        pygame.K_7: "FNAF GAME/IMAGES/CAM7.png",
    }

    CAM1_ANI_image_path = "FNAF GAME/IMAGES/CAM1_ANI2.png"     #i think im stupid i didnt have to do this but i like it this way
    CAM2_ANI_image_path = "FNAF GAME/IMAGES/CAM2_ANI1.png"
    CAM3_ANI_image_path = "FNAF GAME/IMAGES/CAM3_ANI3.png"
    CAM4_ANI_image_path = "FNAF GAME/IMAGES/CAM4_ANI2.png"
    CAM5_ANI_image_path = "FNAF GAME/IMAGES/CAM5_ANI1.png"
    CAM6_ANI_image_path = "FNAF GAME/IMAGES/CAM6_ANI1.png"
    CAM7_ANI_image_path = "FNAF GAME/IMAGES/CAM7_ANI2.png"

    if os.path.exists(CAM1_ANI_image_path): 
        CAM1_ANI_image = pygame.image.load(CAM1_ANI_image_path)
    else:
        print(f"file not found: {CAM1_ANI_image_path}")
        CAM1_ANI_image = None 

    if os.path.exists(CAM2_ANI_image_path):
        CAM2_ANI_image = pygame.image.load(CAM2_ANI_image_path)
    else:
        print(f"file not found: {CAM2_ANI_image_path}")
        CAM2_ANI_image = None

    if os.path.exists(CAM3_ANI_image_path):
        CAM3_ANI_image = pygame.image.load(CAM3_ANI_image_path)
    else:
        print(f"file not found: {CAM3_ANI_image_path}")
        CAM3_ANI_image = None

    if os.path.exists(CAM4_ANI_image_path):
        CAM4_ANI_image = pygame.image.load(CAM4_ANI_image_path)
    else:
        print(f"file not found: {CAM4_ANI_image_path}")
        CAM4_ANI_image = None

    if os.path.exists(CAM5_ANI_image_path):
        CAM5_ANI_image = pygame.image.load(CAM5_ANI_image_path)
    else:
        print(f"file not found: {CAM5_ANI_image_path}")
        CAM5_ANI_image = None

    if os.path.exists(CAM6_ANI_image_path):
        CAM6_ANI_image = pygame.image.load(CAM6_ANI_image_path)
    else:
        print(f"file not found: {CAM6_ANI_image_path}")
        CAM6_ANI_image = None

    if os.path.exists(CAM7_ANI_image_path):
        CAM7_ANI_image = pygame.image.load(CAM7_ANI_image_path)
    else:
        print(f"file not found: {CAM7_ANI_image_path}")
        CAM7_ANI_image = None

    animatronic_images = {
        pygame.K_5: CAM5_ANI_image,
        pygame.K_6: CAM6_ANI_image,
        pygame.K_2: CAM2_ANI_image,
        pygame.K_7: CAM7_ANI_image,
        pygame.K_4: CAM4_ANI_image,
        pygame.K_1: CAM1_ANI_image,
        pygame.K_3: CAM3_ANI_image,
    }

    security_image_path = "FNAF GAME/IMAGES/SECURITY ROOM.png"
    jumpscare_image_path = "FNAF GAME/IMAGES/JUMPSCARE.png"

    vents = {}
    vent_image_paths = {
        pygame.K_s: "FNAF GAME/IMAGES/VENT0.png",
        pygame.K_f: "FNAF GAME/IMAGES/VENT1.png",
    }
    ani3_vent1_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT1.png"
    ani3_vent2_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT2.png"
    ani3_vent3_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT3.png"

    doors = {}                                                          #WORK ON THE DOORS I HAVE NO CLUE
    security_door_paths = {
        pygame.K_a: "FNAF GAME/IMAGES/SECURITY DOOR LEFT.png",
        pygame.K_d: "FNAF GAME/IMAGES/SECURITY DOOR RIGHT.png",
    }

    for key, path in image_paths.items(): # Load images from file paths and store them in the 'images' dictionary (THE KEY IS THE KEY PRESSED AND THE PATH IS THE VALUE WHICH IS WHERE THE IMAGE IS STORED)
        if os.path.exists(path):
            images[key] = pygame.image.load(path)   #load image from file path based on key corrrespond to CAMERA
        else:
            print(f"file not found: {path}")

    if os.path.exists(security_image_path): #load security room then from the path (essentially locates it before it loads)
        security_image = pygame.image.load(security_image_path)
    else:
        print(f"file not found: {security_image_path}")
        security_image = None # sets to no image if cant find

    if os.path.exists(jumpscare_image_path): 
        jumpscare_image = pygame.image.load(jumpscare_image_path)
    else:
        print(f"file not found: {jumpscare_image_path}")
        jumpscare_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent1_image_path):
        ani3_vent1_image = pygame.image.load(ani3_vent1_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent1_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent2_image_path):
        ani3_vent2_image = pygame.image.load(ani3_vent2_image_path)
    else:
        print(f"file not found: {ani3_vent2_image_path}")
        ani3_vent2_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent3_image_path):
        ani3_vent3_image = pygame.image.load(ani3_vent3_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent3_image = None # sets to no image if cant find

    for vent, path in vent_image_paths.items():
        if os.path.exists(path):
            vents[vent] = pygame.image.load(path) # load image from file path based on key
        else:
            print(f"file not found: {path}")
            vents[vent] = None

    for door, path in security_door_paths.items(): # Load images from file paths and store them in the 'doors'
        if os.path.exists(path):
            doors[door] = pygame.image.load(path)   #load image from file path based on
        else:
            print(f"file not found: {path}")

    current_image = security_image  # states beginning image that was loaded
    for i in range(2):
        camera_open = True
        camera_open = False  
    current_camera = None #tracks the current camera

    door_states = {  # Tracks the state of each door (True for closed, False for open)
        "left": False,
        "right": False,
    }
    previous_door_states = {
        "left": False,
        "right": False,
    }
    #- - - - - - - - - - - - - - - - - - - - - - - ANIMATRONIC LOGIC - - - - - - - - - - - - - - - - - - - - -
    """ANIMATRONIC 1""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 1 movement variables (RNG ONE)(you can change chance here)
    animatronic1_camera_sequence = [pygame.K_5, pygame.K_6, pygame.K_2]  # Cameras the animatronic moves through
    animatronic1_current_camera = 0  # Start at the first camera
    animatronic1_probability = 0.0025  # Initial chance to move
    animatronic1_probability_increment = 0.0005  # Increment per second



    animatronic1_at_door_time = 0  #track time if animatronic1 is at door

    """ANIMATRONIC 2""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 2 movement, (camera stare one) make him start at 2 am
    animatronic2_camera_sequence = [pygame.K_7, pygame.K_4, pygame.K_1]
    animatronic2_current_camera = 0
    look_at_time = 0
    time_not_looked = 0


    """ANIMATRONIC 3""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 3 movement, (starts at CAM 3 and moves to vent behind user) count times camera was opened
    animatronic3_camera_sequence = [pygame.K_3, ani3_vent1_image, ani3_vent2_image, ani3_vent3_image]
    animatronic3_current_camera = 0
    camera_open_count = 0


    def render_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_thickness=2):        #I FOUND THIS ONLINE BUT IT WORKS SO IM NOT COMPLAINING
        """Renders text with an outline at the given position."""
        for dx in range(-outline_thickness, outline_thickness + 1): # Render the outline
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:  # skip the center (original position)
                    outline_surface = font.render(text, True, outline_color)
                    surface.blit(outline_surface, (x + dx, y + dy))
    
        text_surface = font.render(text, True, text_color)   # Render the actual text
        surface.blit(text_surface, (x, y))

    # Initialize time tracking for clock (12 AM to 6 AM)
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)
    time_remaining = game_duration

    def format_game_time(ms):
        """Formats the game time from milliseconds into hours (12 AM to 6 AM)."""
        # Convert elapsed milliseconds to minutes
        minutes_elapsed = (game_duration - ms) // 1000 // 60
        # Determine the current hour
        hour = 12 + minutes_elapsed
        return f"{hour % 12 or 12} AM"  # Use 12 for the hour if it rolls over to 0

    """BLINK SCREEN FUNCTION"""
    def blink_screen(screen, start_time, blink_duration=200, blink_interval=300):
        #blinks at specified interval
        current_time = pygame.time.get_ticks()

        # Check if we need to display the black screen
        if current_time - start_time < blink_duration:
            screen.fill((0, 0, 0))  # Fill the screen with black
            pygame.display.flip()
        elif current_time - start_time < blink_duration + blink_interval:
            # Keep the screen black during the blink interval
            pass
        else:
            # After the interval, reset the screen back to normal (or white in this case)
            screen.fill((0, 0, 0))  # Set back to white or any other color/state
            pygame.display.flip()
            # Return the current time to simulate the blinking interval again
            return pygame.time.get_ticks()

        # Return the start time if we haven't finished blinking yet
        return start_time

    # Main loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)

    running = True
    clock = pygame.time.Clock()
    frame_counterANI1 = 0  # Add more if more animatronics based on frame count
    global_power = 101
    idle_power = 0.0028
    camera_power = 0.003                                            # WORK ON GLOBAL POWER HERE
    door_power = 0.0025
    both_doors_power = 0.0055
    door_bang_power = 0.01
    vent_flash_power = 0.003

    vent_flashing = False
    vent_open = False
    current_vent_image = vents[pygame.K_s]
    ani3_flash_time = 0

    vent_enter_sound_played = False
    run_sound_playing = False
    door_bang_sound_playing = False
    animatronic2_at_door_time = 0


    for i in range(2):  #I am quite literally using this because animatronic 2 only kills or resets when the left door was interacted with before the attack sequence, i dont know how to fix so i am using this please dont remove it will destroy it's logic
        door_states["left"] = not door_states["left"]
        door_states["right"] = not door_states["right"]

    power_out_started = False
    power_out_start_time = None
    power_out_stage = 0 

    while running:
        # TIME TRACKER
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_start_time  # Time passed since the game started

        # Calculate the remaining time directly
        time_remaining = game_duration - elapsed_time

        # Make sure time remaining doesn't go negative
        if time_remaining < 0:
            time_remaining = 0

        frame_counterANI1 += 1
        global_power -= idle_power
        

        if global_power < 0:
            global_power = 0
        if camera_open:
            global_power -= camera_power
        if door_states["left"]:
            global_power -= door_power  # Consume power for left door being closed
        if door_states["right"]:
            global_power -= door_power  # Consume power for right door being closed
        if door_states["left"] and door_states["right"]:
            global_power -= both_doors_power  # Additional power for both doors being closed
        if vent_flashing:
            global_power -= vent_flash_power

        if global_power <= 0 and not power_out_started:
            pygame.mixer.music.stop()
            camera_open = False
            current_image = security_image
            current_camera = None
            door_states["left"] = False
            door_states["right"] = False
            power_out_started = True
            power_out_start_time = pygame.time.get_ticks()
            power_out_stage = 1

        if power_out_started:
            elapsed_time = pygame.time.get_ticks() - power_out_start_time

            if power_out_stage == 1:
                if not pygame.mixer.get_busy():  # Ensure the previous music has stopped
                    power_out_sound.play()
                    power_out_stage = 2

            elif power_out_stage == 2:
                if elapsed_time >= 10000:  # Start the power-out music after 10 seconds
                    if not pygame.mixer.get_busy():  # Ensure no overlapping sounds
                        power_out_music.play()
                        power_out_stage = 3

            elif power_out_stage == 3:
                if elapsed_time >= 23000:  # Trigger jumpscare after total 23 seconds
                    if not pygame.mixer.get_busy():  # Ensure music has finished
                        screen.fill((0, 0, 0))
                        screen.blit(jumpscare_image, (0, 0))
                        jumpscare_sound.play()
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                        print("died by one")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Stop the game if the user closes the window
                running = False

            if event.type == pygame.KEYDOWN:     # USE THIS FOR CAMERA NUMBER INPUTS FROM KEYBOARD
                if not power_out_started:

                    if event.key == pygame.K_s:  #toggle vent only when in security room
                        if vent_open or current_image == security_image:  # Allow toggling vent mode only if in security room or vent mode is already open
                            vent_open = not vent_open
                        if vent_open:
                            current_vent_image = vents[pygame.K_s]       
                            current_image = None
                                                                                                    #CHECK IF OWKRWRWRRW
                        else:
                            current_vent_image = None
                            vent_flashing = False
                            if current_image == None:
                                current_image = security_image
                                
                    if event.key == pygame.K_f: #toggle flashed vent
                        if vent_open: #only allow flashlight in vent mode
                            vent_flashing = True
                            

                    if not vent_open:   #disable cam and door in vent mode
                        if event.key in images and camera_open: #check if a key is same as camera num
                            current_image = images[event.key]   #update the current camera to the user inputted key
                            current_camera = event.key  #update the current camera to the user inputted key
                            camera_switch_sound.play()
                        if event.key == pygame.K_SPACE:
                            camera_open_count += 1
                            camera_sound.play()
                            if camera_open:  # If the camera is open
                                current_image = security_image  # Close the camera and display the security image
                                camera_open = False  # Set camera state to closed
                            else:
                                if current_camera:  # Reopen to the last camera viewed
                                    current_image = images[current_camera]
                                else:  # Default to CAM1 if no previous camera exists
                                    current_camera = pygame.K_1
                                    current_image = images[current_camera]
                                camera_open = True  # Set camera state to open

                        if current_image == security_image:
                            #toggle left door                                                           
                            if event.key == pygame.K_a and not camera_open:
                                door_states["left"] = not door_states["left"]
                        
                        #toggle right door
                        if event.key == pygame.K_d and not camera_open:
                            door_states["right"] = not door_states["right"]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:  # Stop flashing when F key is released
                    vent_flashing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the bounds of any camera's clickable area
                if event.button == 1:  # Left mouse click
                    for camera_key, camera_rect in camera_positions.items():
                        if camera_rect.collidepoint(event.pos):
                            current_image = images[camera_key]  # Switch to the clicked camera
                            current_camera = camera_key
                            camera_switch_sound.play()

        # Play door sound if the door state has changed
        if door_states["left"] != previous_door_states["left"]:  #checks if the change was from true to false or false to true
            door_sound.play()  # Play left door sound
            previous_door_states["left"] = door_states["left"]  # Update previous state

        if door_states["right"] != previous_door_states["right"]:
            door_sound.play()  # Play right door sound
            previous_door_states["right"] = door_states["right"]  # Update previous state

        

        # Animatronic 1 movement logic
        if current_time >=60000:  # Start animatronic movement at 1 AM 
            if frame_counterANI1 >= 30:  # Check every 30 frames (about once per second at 30 FPS)
                frame_counterANI1 = 0
                if animatronic1_current_camera < len(animatronic1_camera_sequence):
                    if random.random() < animatronic1_probability:  # Animatronic decides to move
                        blink_screen(screen, 0)
                        animatronic1_probability = 0.0025  # Reset probability after movement
                        animatronic1_current_camera += 1
                    else:
                        animatronic1_probability += animatronic1_probability_increment

            #ANIMATRONIC 1 RESET FUNCTION
            if animatronic1_current_camera > len(animatronic1_camera_sequence):
                animatronic1_current_camera = 0

            if animatronic1_current_camera == 2:  # Check if animatronic is at Camera 2
                door_open = not door_states["right"]  # Animatronic checks the right door state

                if door_open:
                    if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                        animatronic1_at_door_time = pygame.time.get_ticks()
                    elif pygame.time.get_ticks() - animatronic1_at_door_time >= 5000:  # If the door is open for 5 seconds
                        screen.fill((0, 0, 0))
                        screen.blit(jumpscare_image, (0, 0))  # Show the jumpscare image
                        jumpscare_sound.play()  # Play jumpscare sound
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False  # End the game
                else:
                    if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                        animatronic1_at_door_time = pygame.time.get_ticks()
                    elif pygame.time.get_ticks() - animatronic1_at_door_time >= 8000:  # If the door is closed for 8 seconds
                        blink_screen(screen, 0)
                        animatronic1_current_camera = 0  # Reset animatronic to Camera 5
                        animatronic1_probability = 0.01  # Reset movement probability
                        animatronic1_at_door_time = 0  # Reset the door timer
                        

            else:
                animatronic1_at_door_time = 0  # Reset the timer if animatronic is not at Camera 2
        
        # Animatronic 2 look at logic and reset
        if animatronic2_current_camera < 0 or animatronic2_current_camera > 2:
            animatronic2_current_camera = 0


        if animatronic2_current_camera < len(animatronic2_camera_sequence):
            current_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
            
            if current_camera == current_camera_key:
                look_at_time += clock.get_time()  # Increment look_at_time by the time since the last frame
            else:
                look_at_time = 0  # Reset if not on the same camera

            if look_at_time >= 5000 and camera_open: 
                blink_screen(screen, 0)
                look_at_time = 0
                time_not_looked = 0
                animatronic2_current_camera += 1
                if animatronic2_current_camera == 2:
                    animatronic2_current_camera += 1

            
        if current_camera != animatronic2_current_camera:
            time_not_looked += clock.get_time()
        

    #animatronic 2 attack logic
        if time_not_looked >= 60000:  # Check if the animatronic can attack
            if not run_sound_playing:
                blink_screen(screen, 0)
                run_sound.play()
                run_sound_playing = True
            animatronic2_current_camera = 2

            door_open = not door_states["left"]

            if door_open:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic2_at_door_time >= 5000:  
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  
                    jumpscare_sound.play()  
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  
            else:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                
                current_time = pygame.time.get_ticks()
                if current_time - animatronic2_at_door_time >= 8000:  
                    if not door_bang_sound_playing:
                        door_bang_sound.play()
                        door_bang_sound_playing = True
                        global_power -= door_bang_power
                        blink_screen(screen, 0)
                        
                
                    time_not_looked = 0  # Reset time not looked only after the full 8 seconds
                    animatronic2_current_camera = 0
                    animatronic2_at_door_time = 0
                    run_sound_playing = False
                    door_bang_sound_playing = False
                    print("ani 2 reset")
        else:
            run_sound_playing = False             
            door_bang_sound_playing = False 
            animatronic2_at_door_time = 0             

        #ANIMATRONIC 3 MOVEMENT
        if animatronic3_current_camera == 0:
            if camera_open_count >= 40: # Check if the camera has been open 20 times                             
                animatronic3_current_camera = 1
                camera_open_count = 0
                if not vent_enter_sound_played:
                    vent_enter_sound.play()
                    vent_enter_sound_played = True
                ani3_last_move_time = pygame.time.get_ticks()
        else:
            vent_enter_sound_played = False

        # Animatronic 3 movement logic
        if animatronic3_current_camera in [1, 2, 3]:
            if not vent_flashing:
                if pygame.time.get_ticks() - ani3_last_move_time >= 10000:  # Move every 5 seconds
                    animatronic3_current_camera += 1
                    ani3_last_move_time = pygame.time.get_ticks()
        else:
            ani3_last_move_time = pygame.time.get_ticks()

        if animatronic3_current_camera > 3:  #Jumpscare if animatronic3_current_camera is greater than index 3
            screen.fill((0, 0, 0))
            screen.blit(jumpscare_image, (0, 0))
            jumpscare_sound.play()
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
            print("died by animatronic 3")

        # Flashing logic for Animatronic 3
        if vent_flashing:
            if animatronic3_current_camera in [1, 2, 3]:            
                ani3_flash_time += clock.get_time()
                if ani3_flash_time >= 5000:  # Reset animatronic 3 if flashed for 5 seconds
                    blink_screen(screen, 0)
                    animatronic3_current_camera = 0
                    ani3_flash_time = 0
                    ani3_last_move_time = pygame.time.get_ticks()
            else:
                current_vent_image = vents[pygame.K_f]
        else:
            ani3_flash_time = 0  # Reset flash time if not flashing                                                                                 

        #RENDERING SECTION FOR IMAGE RENDERING IF RENDERING WITH IMAGES - - - - - - - -- - - - - -- - - - - -- - - - - - - -- - - - - - -- - - - - - -

        screen.fill((0, 0, 0))  #Fill the screen with black to clear the previous frame

        if current_image:  # Draws the current image on the screen
            screen.blit(current_image, (0, 0))
        else:
            screen.blit(security_image, (0, 0))  # If no image, draw security room

        if vent_open and current_vent_image:
            screen.blit(current_vent_image, (0, 0))

        # Don't draw animatronic when showing the security room
        if current_image != security_image and not vent_open:
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                animatronic1_camera_key = animatronic1_camera_sequence[animatronic1_current_camera]
                if current_camera == animatronic1_camera_key:
                    animatronic_image = animatronic_images.get(animatronic1_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic2_current_camera < len(animatronic2_camera_sequence):
                animatronic2_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
                if current_camera == animatronic2_camera_key:
                    animatronic_image = animatronic_images.get(animatronic2_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic3_current_camera < len(animatronic3_camera_sequence):
                animatronic3_camera_key = animatronic3_camera_sequence[animatronic3_current_camera]
                if current_camera == animatronic3_camera_key:
                    animatronic_image = animatronic_images.get(animatronic3_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

        # Flashing logic for Animatronic 3 in vents
        if vent_flashing:
            if animatronic3_current_camera == 1 and ani3_vent1_image:
                screen.blit(ani3_vent1_image, (0, 0))
            elif animatronic3_current_camera == 2 and ani3_vent2_image:
                screen.blit(ani3_vent2_image, (0, 0))
            elif animatronic3_current_camera == 3 and ani3_vent3_image:
                screen.blit(ani3_vent3_image, (0, 0))
        else:
        # If not flashing, show the default vent image
            if vent_open:
                current_vent_image = vents[pygame.K_s]  # Default to VENT0
                screen.blit(current_vent_image, (0, 0))  # Show VENT0

        # Draw door images at the bottom corners
        if current_image == security_image:
            if door_states["left"]:
                screen.blit(doors[pygame.K_a], (0, HEIGHT - doors[pygame.K_a].get_height()))  # draw left door at bottom left
            if door_states["right"]:
                screen.blit(doors[pygame.K_d], (WIDTH - doors[pygame.K_d].get_width(), HEIGHT - doors[pygame.K_d].get_height()))  # Draw right door at bottom right
        
        power_percent = int(global_power)                       # POWER DISPLAY
        power_text = f"POWER: {power_percent}%"
        render_outlined_text(
            screen,
            power_text,
            font,
            10,  # X position 
            HEIGHT - font_size - 10,  # Yposition
            (255, 255, 255),  # white interior
            (0, 0, 0),  # black outline
            2,  # outline thickness
        )
        #print(time_remaining)#------------------------------------------------------------------------------------------------------------ENABLE THIS COMMENT TO SEE TIME REMAINING IN MILISECONDS---------
        # Format the clock and render it
        formatted_time = format_game_time(time_remaining)  # Get formatted time string using time_remaining
        render_outlined_text(
            screen,
            formatted_time,
            font,
            WIDTH - 150,  # X position
            10,  # Y position
            (255, 255, 255),  #white text
            (0, 0, 0),  #black outline
            2,  # outline thickness
        )

        if time_remaining == 0:
            render_outlined_text(
                screen,
                "YOU WIN!",
                font,
                WIDTH // 2 - 80,  #X position 
                HEIGHT // 2 - 50,  #Y position
                (0, 255, 0),  #geen text
                (0, 0, 0),  #black outline
                2,  #outline thickness
            )

        pygame.display.flip()  #update display for new frame

        clock.tick(30)  # 30 fps limiter

    # Quit Pygame
    pygame.quit()

def night_two():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Get the absolute path of the MP3 file
    ambience_mp3 = "FNAF GAME/AMBIENCE.mp3"
    # Load and play the MP3 file

    # Play ambience sound on a loop
    ambience_channel = pygame.mixer.Channel(1)
    ambience_sound = pygame.mixer.Sound(ambience_mp3)
    ambience_channel.play(ambience_sound, loops=-1)

    WIDTH, HEIGHT = 1920, 1080      # SCREEN RESOLUTION using 1080p for simplicity's sake
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nightmera")

    font_size = 36  # You can adjust the size as needed
    font = pygame.font.Font(None, font_size)

    # load sound effects
    door_sound = pygame.mixer.Sound("FNAF GAME/door slam.mp3")
    camera_sound = pygame.mixer.Sound("FNAF GAME/camera open.mp3")
    camera_switch_sound = pygame.mixer.Sound("FNAF GAME/camera switch.mp3")
    jumpscare_sound = pygame.mixer.Sound("FNAF GAME/jumpscare sound.mp3")
    power_out_sound = pygame.mixer.Sound("FNAF GAME/power out.mp3")                     #CURRENTLY DOES NOT WORK UNTIL I FIND A WAY TO LET MUSIC RUN AND PAUSE
    power_out_music = pygame.mixer.Sound("FNAF GAME/power out music.mp3")
    door_bang_sound = pygame.mixer.Sound("FNAF GAME/door bang.mp3")
    run_sound = pygame.mixer.Sound("FNAF GAME/run sound.mp3")
    vent_enter_sound = pygame.mixer.Sound("FNAF GAME/vent enter.mp3")

    #CAMERA BUTTON LOCATION #   https://pixspy.com/ USE THIS TO FIND PIXEL LOCATIONS
    camera_positions = {
        pygame.K_1: pygame.Rect(150, 479, 66, 47),  # Adjust these values based on the map layout
        pygame.K_2: pygame.Rect(322, 484, 72, 43),
        pygame.K_3: pygame.Rect(39, 312, 70, 44),
        pygame.K_4: pygame.Rect(195, 145, 77, 44),
        pygame.K_5: pygame.Rect(458, 149, 78, 44),
        pygame.K_6: pygame.Rect(341, 331, 74, 48),
        pygame.K_7: pygame.Rect(559, 275, 81, 51),
    }

    # load images
    images = {}
    image_paths = {
        pygame.K_1: "FNAF GAME/IMAGES/CAM1.png",
        pygame.K_2: "FNAF GAME/IMAGES/CAM2.png",
        pygame.K_3: "FNAF GAME/IMAGES/CAM3.png",
        pygame.K_4: "FNAF GAME/IMAGES/CAM4.png",
        pygame.K_5: "FNAF GAME/IMAGES/CAM5.png",
        pygame.K_6: "FNAF GAME/IMAGES/CAM6.png",
        pygame.K_7: "FNAF GAME/IMAGES/CAM7.png",
    }

    CAM1_ANI_image_path = "FNAF GAME/IMAGES/CAM1_ANI2.png"     #i think im stupid i didnt have to do this but i like it this way
    CAM2_ANI_image_path = "FNAF GAME/IMAGES/CAM2_ANI1.png"
    CAM3_ANI_image_path = "FNAF GAME/IMAGES/CAM3_ANI3.png"
    CAM4_ANI_image_path = "FNAF GAME/IMAGES/CAM4_ANI2.png"
    CAM5_ANI_image_path = "FNAF GAME/IMAGES/CAM5_ANI1.png"
    CAM6_ANI_image_path = "FNAF GAME/IMAGES/CAM6_ANI1.png"
    CAM7_ANI_image_path = "FNAF GAME/IMAGES/CAM7_ANI2.png"

    if os.path.exists(CAM1_ANI_image_path): 
        CAM1_ANI_image = pygame.image.load(CAM1_ANI_image_path)
    else:
        print(f"file not found: {CAM1_ANI_image_path}")
        CAM1_ANI_image = None 

    if os.path.exists(CAM2_ANI_image_path):
        CAM2_ANI_image = pygame.image.load(CAM2_ANI_image_path)
    else:
        print(f"file not found: {CAM2_ANI_image_path}")
        CAM2_ANI_image = None

    if os.path.exists(CAM3_ANI_image_path):
        CAM3_ANI_image = pygame.image.load(CAM3_ANI_image_path)
    else:
        print(f"file not found: {CAM3_ANI_image_path}")
        CAM3_ANI_image = None

    if os.path.exists(CAM4_ANI_image_path):
        CAM4_ANI_image = pygame.image.load(CAM4_ANI_image_path)
    else:
        print(f"file not found: {CAM4_ANI_image_path}")
        CAM4_ANI_image = None

    if os.path.exists(CAM5_ANI_image_path):
        CAM5_ANI_image = pygame.image.load(CAM5_ANI_image_path)
    else:
        print(f"file not found: {CAM5_ANI_image_path}")
        CAM5_ANI_image = None

    if os.path.exists(CAM6_ANI_image_path):
        CAM6_ANI_image = pygame.image.load(CAM6_ANI_image_path)
    else:
        print(f"file not found: {CAM6_ANI_image_path}")
        CAM6_ANI_image = None

    if os.path.exists(CAM7_ANI_image_path):
        CAM7_ANI_image = pygame.image.load(CAM7_ANI_image_path)
    else:
        print(f"file not found: {CAM7_ANI_image_path}")
        CAM7_ANI_image = None

    animatronic_images = {
        pygame.K_5: CAM5_ANI_image,
        pygame.K_6: CAM6_ANI_image,
        pygame.K_2: CAM2_ANI_image,
        pygame.K_7: CAM7_ANI_image,
        pygame.K_4: CAM4_ANI_image,
        pygame.K_1: CAM1_ANI_image,
        pygame.K_3: CAM3_ANI_image,
    }

    security_image_path = "FNAF GAME/IMAGES/SECURITY ROOM.png"
    jumpscare_image_path = "FNAF GAME/IMAGES/JUMPSCARE.png"

    vents = {}
    vent_image_paths = {
        pygame.K_s: "FNAF GAME/IMAGES/VENT0.png",
        pygame.K_f: "FNAF GAME/IMAGES/VENT1.png",
    }
    ani3_vent1_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT1.png"
    ani3_vent2_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT2.png"
    ani3_vent3_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT3.png"

    doors = {}                                                          #WORK ON THE DOORS I HAVE NO CLUE
    security_door_paths = {
        pygame.K_a: "FNAF GAME/IMAGES/SECURITY DOOR LEFT.png",
        pygame.K_d: "FNAF GAME/IMAGES/SECURITY DOOR RIGHT.png",
    }

    for key, path in image_paths.items(): # Load images from file paths and store them in the 'images' dictionary (THE KEY IS THE KEY PRESSED AND THE PATH IS THE VALUE WHICH IS WHERE THE IMAGE IS STORED)
        if os.path.exists(path):
            images[key] = pygame.image.load(path)   #load image from file path based on key corrrespond to CAMERA
        else:
            print(f"file not found: {path}")

    if os.path.exists(security_image_path): #load security room then from the path (essentially locates it before it loads)
        security_image = pygame.image.load(security_image_path)
    else:
        print(f"file not found: {security_image_path}")
        security_image = None # sets to no image if cant find

    if os.path.exists(jumpscare_image_path): 
        jumpscare_image = pygame.image.load(jumpscare_image_path)
    else:
        print(f"file not found: {jumpscare_image_path}")
        jumpscare_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent1_image_path):
        ani3_vent1_image = pygame.image.load(ani3_vent1_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent1_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent2_image_path):
        ani3_vent2_image = pygame.image.load(ani3_vent2_image_path)
    else:
        print(f"file not found: {ani3_vent2_image_path}")
        ani3_vent2_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent3_image_path):
        ani3_vent3_image = pygame.image.load(ani3_vent3_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent3_image = None # sets to no image if cant find

    for vent, path in vent_image_paths.items():
        if os.path.exists(path):
            vents[vent] = pygame.image.load(path) # load image from file path based on key
        else:
            print(f"file not found: {path}")
            vents[vent] = None

    for door, path in security_door_paths.items(): # Load images from file paths and store them in the 'doors'
        if os.path.exists(path):
            doors[door] = pygame.image.load(path)   #load image from file path based on
        else:
            print(f"file not found: {path}")

    current_image = security_image  # states beginning image that was loaded

    for i in range(2):
        camera_open = True
        camera_open = False 
    current_camera = None #tracks the current camera

    door_states = {  # Tracks the state of each door (True for closed, False for open)
        "left": False,
        "right": False,
    }
    previous_door_states = {
        "left": False,
        "right": False,
    }
    #- - - - - - - - - - - - - - - - - - - - - - - ANIMATRONIC LOGIC - - - - - - - - - - - - - - - - - - - - -
    """ANIMATRONIC 1""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 1 movement variables (RNG ONE)(you can change chance here)
    animatronic1_camera_sequence = [pygame.K_5, pygame.K_6, pygame.K_2]  # Cameras the animatronic moves through
    animatronic1_current_camera = 0  # Start at the first camera
    animatronic1_probability = 0.0025  # Initial chance to move
    animatronic1_probability_increment = 0.0025  # Increment per second



    animatronic1_at_door_time = 0  #track time if animatronic1 is at door

    """ANIMATRONIC 2""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 2 movement, (camera stare one) make him start at 2 am
    animatronic2_camera_sequence = [pygame.K_7, pygame.K_4, pygame.K_1]
    animatronic2_current_camera = 0
    look_at_time = 0
    time_not_looked = 0


    """ANIMATRONIC 3""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 3 movement, (starts at CAM 3 and moves to vent behind user) count times camera was opened
    animatronic3_camera_sequence = [pygame.K_3, ani3_vent1_image, ani3_vent2_image, ani3_vent3_image]
    animatronic3_current_camera = 0
    camera_open_count = 0


    def render_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_thickness=2):        #I FOUND THIS ONLINE BUT IT WORKS SO IM NOT COMPLAINING
        """Renders text with an outline at the given position."""
        for dx in range(-outline_thickness, outline_thickness + 1): # Render the outline
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:  # skip the center (original position)
                    outline_surface = font.render(text, True, outline_color)
                    surface.blit(outline_surface, (x + dx, y + dy))
    
        text_surface = font.render(text, True, text_color)   # Render the actual text
        surface.blit(text_surface, (x, y))

    # Initialize time tracking for clock (12 AM to 6 AM)
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)
    time_remaining = game_duration

    def format_game_time(ms):
        """Formats the game time from milliseconds into hours (12 AM to 6 AM)."""
        # Convert elapsed milliseconds to minutes
        minutes_elapsed = (game_duration - ms) // 1000 // 60
        # Determine the current hour
        hour = 12 + minutes_elapsed
        return f"{hour % 12 or 12} AM"  # Use 12 for the hour if it rolls over to 0

    """BLINK SCREEN FUNCTION"""
    def blink_screen(screen, start_time, blink_duration=200, blink_interval=300):
        #blinks at specified interval
        current_time = pygame.time.get_ticks()

        # Check if we need to display the black screen
        if current_time - start_time < blink_duration:
            screen.fill((0, 0, 0))  # Fill the screen with black
            pygame.display.flip()
        elif current_time - start_time < blink_duration + blink_interval:
            # Keep the screen black during the blink interval
            pass
        else:
            # After the interval, reset the screen back to normal (or white in this case)
            screen.fill((0, 0, 0))  # Set back to white or any other color/state
            pygame.display.flip()
            # Return the current time to simulate the blinking interval again
            return pygame.time.get_ticks()

        # Return the start time if we haven't finished blinking yet
        return start_time

    # Main loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)

    running = True
    clock = pygame.time.Clock()
    frame_counterANI1 = 0  # Add more if more animatronics based on frame count
    global_power = 101
    idle_power = 0.00327
    camera_power = 0.004                                            # WORK ON GLOBAL POWER HERE
    door_power = 0.003
    both_doors_power = 0.0065
    door_bang_power = 0.025
    vent_flash_power = 0.004

    vent_flashing = False
    vent_open = False
    current_vent_image = vents[pygame.K_s]
    ani3_flash_time = 0

    vent_enter_sound_played = False
    run_sound_playing = False
    door_bang_sound_playing = False
    animatronic2_at_door_time = 0


    for i in range(2):  #I am quite literally using this because animatronic 2 only kills or resets when the left door was interacted with before the attack sequence, i dont know how to fix so i am using this please dont remove it will destroy it's logic
        door_states["left"] = not door_states["left"]
        door_states["right"] = not door_states["right"]

    power_out_started = False
    power_out_start_time = None
    power_out_stage = 0 

    while running:
        # TIME TRACKER
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_start_time  # Time passed since the game started

        # Calculate the remaining time directly
        time_remaining = game_duration - elapsed_time

        # Make sure time remaining doesn't go negative
        if time_remaining < 0:
            time_remaining = 0

        frame_counterANI1 += 1
        global_power -= idle_power
        
        if global_power < 0:
            global_power = 0
        if camera_open:
            global_power -= camera_power
        if door_states["left"]:
            global_power -= door_power  # Consume power for left door being closed
        if door_states["right"]:
            global_power -= door_power  # Consume power for right door being closed
        if door_states["left"] and door_states["right"]:
            global_power -= both_doors_power  # Additional power for both doors being closed
        if vent_flashing:
            global_power -= vent_flash_power

        if global_power <= 0 and not power_out_started:
            pygame.mixer.music.stop()
            camera_open = False
            current_image = security_image
            current_camera = None
            door_states["left"] = False
            door_states["right"] = False
            power_out_started = True
            power_out_start_time = pygame.time.get_ticks()
            power_out_stage = 1

        if power_out_started:
            elapsed_time = pygame.time.get_ticks() - power_out_start_time

            if power_out_stage == 1:
                if not pygame.mixer.get_busy():  # Ensure the previous music has stopped
                    power_out_sound.play()
                    power_out_stage = 2

            elif power_out_stage == 2:
                if elapsed_time >= 10000:  # Start the power-out music after 10 seconds
                    if not pygame.mixer.get_busy():  # Ensure no overlapping sounds
                        power_out_music.play()
                        power_out_stage = 3

            elif power_out_stage == 3:
                if elapsed_time >= 23000:  # Trigger jumpscare after total 23 seconds
                    if not pygame.mixer.get_busy():  # Ensure music has finished
                        screen.fill((0, 0, 0))
                        screen.blit(jumpscare_image, (0, 0))
                        jumpscare_sound.play()
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                        print("died by one")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Stop the game if the user closes the window
                running = False

            if event.type == pygame.KEYDOWN:     # USE THIS FOR CAMERA NUMBER INPUTS FROM KEYBOARD
                if not power_out_started:

                    if event.key == pygame.K_s:  #toggle vent only when in security room
                        if vent_open or current_image == security_image:  # Allow toggling vent mode only if in security room or vent mode is already open
                            vent_open = not vent_open
                        if vent_open:
                            current_vent_image = vents[pygame.K_s]       
                            current_image = None
                                                                                                    #CHECK IF OWKRWRWRRW
                        else:
                            current_vent_image = None
                            vent_flashing = False
                            if current_image == None:
                                current_image = security_image
                                
                    if event.key == pygame.K_f: #toggle flashed vent
                        if vent_open: #only allow flashlight in vent mode
                            vent_flashing = True
                            

                    if not vent_open:   #disable cam and door in vent mode
                        if event.key in images and camera_open: #check if a key is same as camera num
                            current_image = images[event.key]   #update the current camera to the user inputted key
                            current_camera = event.key  #update the current camera to the user inputted key
                            camera_switch_sound.play()
                        if event.key == pygame.K_SPACE:
                            camera_open_count += 1
                            camera_sound.play()
                            if camera_open:  # If the camera is open
                                current_image = security_image  # Close the camera and display the security image
                                camera_open = False  # Set camera state to closed
                            else:
                                if current_camera:  # Reopen to the last camera viewed
                                    current_image = images[current_camera]
                                else:  # Default to CAM1 if no previous camera exists
                                    current_camera = pygame.K_1
                                    current_image = images[current_camera]
                                camera_open = True  # Set camera state to open

                        if current_image == security_image:
                            #toggle left door                                                           
                            if event.key == pygame.K_a and not camera_open:
                                door_states["left"] = not door_states["left"]
                        
                        #toggle right door
                        if event.key == pygame.K_d and not camera_open:
                            door_states["right"] = not door_states["right"]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:  # Stop flashing when F key is released
                    vent_flashing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the bounds of any camera's clickable area
                if event.button == 1:  # Left mouse click
                    for camera_key, camera_rect in camera_positions.items():
                        if camera_rect.collidepoint(event.pos):
                            current_image = images[camera_key]  # Switch to the clicked camera
                            current_camera = camera_key
                            camera_switch_sound.play()

        # Play door sound if the door state has changed
        if door_states["left"] != previous_door_states["left"]:  #checks if the change was from true to false or false to true
            door_sound.play()  # Play left door sound
            previous_door_states["left"] = door_states["left"]  # Update previous state

        if door_states["right"] != previous_door_states["right"]:
            door_sound.play()  # Play right door sound
            previous_door_states["right"] = door_states["right"]  # Update previous state

        

        # Animatronic 1 movement logic 
        if frame_counterANI1 >= 30:  # Check every 30 frames (about once per second at 30 FPS)
            frame_counterANI1 = 0
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                if random.random() < animatronic1_probability:  # Animatronic decides to move
                    blink_screen(screen, 0)
                    animatronic1_probability = 0.0025  # Reset probability after movement
                    animatronic1_current_camera += 1
                else:
                    animatronic1_probability += animatronic1_probability_increment

        #ANIMATRONIC 1 RESET FUNCTION
        if animatronic1_current_camera > len(animatronic1_camera_sequence):
            animatronic1_current_camera = 0

        if animatronic1_current_camera == 2:  # Check if animatronic is at Camera 2
            door_open = not door_states["right"]  # Animatronic checks the right door state

            if door_open:
                if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                    animatronic1_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic1_at_door_time >= 5000:  # If the door is open for 5 seconds
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  # Show the jumpscare image
                    jumpscare_sound.play()  # Play jumpscare sound
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  # End the game
            else:
                if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                    animatronic1_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic1_at_door_time >= 8000:  # If the door is closed for 8 seconds
                    blink_screen(screen, 0)
                    animatronic1_current_camera = 0  # Reset animatronic to Camera 5
                    animatronic1_probability = 0.01  # Reset movement probability
                    animatronic1_at_door_time = 0  # Reset the door timer
                    

        else:
            animatronic1_at_door_time = 0  # Reset the timer if animatronic is not at Camera 2
        
        # Animatronic 2 look at logic and reset
        if animatronic2_current_camera < 0 or animatronic2_current_camera > 2:
            animatronic2_current_camera = 0


        if animatronic2_current_camera < len(animatronic2_camera_sequence):
            current_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
            
            if current_camera == current_camera_key:
                look_at_time += clock.get_time()  # Increment look_at_time by the time since the last frame
            else:
                look_at_time = 0  # Reset if not on the same camera

            if look_at_time >= 5000 and camera_open: 
                blink_screen(screen, 0)
                look_at_time = 0
                time_not_looked = 0
                animatronic2_current_camera += 1
                if animatronic2_current_camera == 2:
                    animatronic2_current_camera += 1

            
        if current_camera != animatronic2_current_camera:
            time_not_looked += clock.get_time()
        

    #animatronic 2 attack logic
        if time_not_looked >= 45000:  # Check if the animatronic can attack
            if not run_sound_playing:
                blink_screen(screen, 0)
                run_sound.play()
                run_sound_playing = True
            animatronic2_current_camera = 2

            door_open = not door_states["left"]

            if door_open:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic2_at_door_time >= 5000:  
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  
                    jumpscare_sound.play()  
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  
            else:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                
                current_time = pygame.time.get_ticks()
                if current_time - animatronic2_at_door_time >= 8000:  
                    if not door_bang_sound_playing:
                        door_bang_sound.play()
                        door_bang_sound_playing = True
                        global_power -= door_bang_power
                        blink_screen(screen, 0)
                        
                
                    time_not_looked = 0  # Reset time not looked only after the full 8 seconds
                    animatronic2_current_camera = 0
                    animatronic2_at_door_time = 0
                    run_sound_playing = False
                    door_bang_sound_playing = False
                    print("ani 2 reset")
        else:
            run_sound_playing = False             
            door_bang_sound_playing = False 
            animatronic2_at_door_time = 0             

        #ANIMATRONIC 3 MOVEMENT
        if animatronic3_current_camera == 0:
            if camera_open_count >= 30:
                animatronic3_current_camera = 1
                camera_open_count = 0
                if not vent_enter_sound_played:
                    vent_enter_sound.play()
                    vent_enter_sound_played = True
                ani3_last_move_time = pygame.time.get_ticks()
        else:
            vent_enter_sound_played = False

        # Animatronic 3 movement logic
        if animatronic3_current_camera in [1, 2, 3]:
            if not vent_flashing:
                if pygame.time.get_ticks() - ani3_last_move_time >= 5000:  # Move every 5 seconds
                    animatronic3_current_camera += 1
                    ani3_last_move_time = pygame.time.get_ticks()
        else:
            ani3_last_move_time = pygame.time.get_ticks()

        if animatronic3_current_camera > 3:  #Jumpscare if animatronic3_current_camera is greater than index 3
            screen.fill((0, 0, 0))
            screen.blit(jumpscare_image, (0, 0))
            jumpscare_sound.play()
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
            print("died by animatronic 3")

        # Flashing logic for Animatronic 3
        if vent_flashing:
            if animatronic3_current_camera in [1, 2, 3]:             #ANIMATRONIC 3 IS BROKEN, FIX KILL RESET OR KILL, I DID NOT CHECK PLEASE MAKE SURE IT WORKS __+__++_++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                ani3_flash_time += clock.get_time()
                if ani3_flash_time >= 5000:  # Reset animatronic 3 if flashed for 8 seconds
                    blink_screen(screen, 0)
                    animatronic3_current_camera = 0
                    ani3_flash_time = 0
                    ani3_last_move_time = pygame.time.get_ticks()
            else:
                current_vent_image = vents[pygame.K_f]
        else:
            ani3_flash_time = 0  # Reset flash time if not flashing                                                                                 

        #RENDERING SECTION FOR IMAGE RENDERING IF RENDERING WITH IMAGES - - - - - - - -- - - - - -- - - - - -- - - - - - - -- - - - - - -- - - - - - -

        screen.fill((0, 0, 0))  #Fill the screen with black to clear the previous frame

        if current_image:  # Draws the current image on the screen
            screen.blit(current_image, (0, 0))
        else:
            screen.blit(security_image, (0, 0))  # If no image, draw security room

        if vent_open and current_vent_image:
            screen.blit(current_vent_image, (0, 0))

        # Don't draw animatronic when showing the security room
        if current_image != security_image and not vent_open:
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                animatronic1_camera_key = animatronic1_camera_sequence[animatronic1_current_camera]
                if current_camera == animatronic1_camera_key:
                    animatronic_image = animatronic_images.get(animatronic1_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic2_current_camera < len(animatronic2_camera_sequence):
                animatronic2_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
                if current_camera == animatronic2_camera_key:
                    animatronic_image = animatronic_images.get(animatronic2_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic3_current_camera < len(animatronic3_camera_sequence):
                animatronic3_camera_key = animatronic3_camera_sequence[animatronic3_current_camera]
                if current_camera == animatronic3_camera_key:
                    animatronic_image = animatronic_images.get(animatronic3_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

        # Flashing logic for Animatronic 3 in vents
        if vent_flashing:
            if animatronic3_current_camera == 1 and ani3_vent1_image:
                screen.blit(ani3_vent1_image, (0, 0))
            elif animatronic3_current_camera == 2 and ani3_vent2_image:
                screen.blit(ani3_vent2_image, (0, 0))
            elif animatronic3_current_camera == 3 and ani3_vent3_image:
                screen.blit(ani3_vent3_image, (0, 0))
        else:
        # If not flashing, show the default vent image
            if vent_open:
                current_vent_image = vents[pygame.K_s]  # Default to VENT0
                screen.blit(current_vent_image, (0, 0))  # Show VENT0

        # Draw door images at the bottom corners
        if current_image == security_image:
            if door_states["left"]:
                screen.blit(doors[pygame.K_a], (0, HEIGHT - doors[pygame.K_a].get_height()))  # draw left door at bottom left
            if door_states["right"]:
                screen.blit(doors[pygame.K_d], (WIDTH - doors[pygame.K_d].get_width(), HEIGHT - doors[pygame.K_d].get_height()))  # Draw right door at bottom right
        
        power_percent = int(global_power)                       # POWER DISPLAY
        power_text = f"POWER: {power_percent}%"
        render_outlined_text(
            screen,
            power_text,
            font,
            10,  # X position 
            HEIGHT - font_size - 10,  # Yposition
            (255, 255, 255),  # white interior
            (0, 0, 0),  # black outline
            2,  # outline thickness
        )
        #print(time_remaining)#------------------------------------------------------------------------------------------------------------ENABLE THIS COMMENT TO SEE TIME REMAINING IN MILISECONDS---------
        # Format the clock and render it
        formatted_time = format_game_time(time_remaining)  # Get formatted time string using time_remaining
        render_outlined_text(
            screen,
            formatted_time,
            font,
            WIDTH - 150,  # X position
            10,  # Y position
            (255, 255, 255),  #white text
            (0, 0, 0),  #black outline
            2,  # outline thickness
        )

        if time_remaining == 0:
            render_outlined_text(
                screen,
                "YOU WIN!",
                font,
                WIDTH // 2 - 80,  #X position 
                HEIGHT // 2 - 50,  #Y position
                (0, 255, 0),  #geen text
                (0, 0, 0),  #black outline
                2,  #outline thickness
            )

        pygame.display.flip()  #update display for new frame

        clock.tick(30)  # 30 fps limiter

    # Quit Pygame
    pygame.quit()

def night_three():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Get the absolute path of the MP3 file
    ambience_mp3 = "FNAF GAME/AMBIENCE.mp3"
    phone_mp3 = "FNAF GAME/phone night one.mp3"
    # Load and play the MP3 file

    # Play ambience sound on a loop
    ambience_channel = pygame.mixer.Channel(1)
    ambience_sound = pygame.mixer.Sound(ambience_mp3)
    ambience_channel.play(ambience_sound, loops=-1)

    WIDTH, HEIGHT = 1920, 1080      # SCREEN RESOLUTION using 1080p for simplicity's sake
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nightmera")

    font_size = 36  # You can adjust the size as needed
    font = pygame.font.Font(None, font_size)

    # load sound effects
    door_sound = pygame.mixer.Sound("FNAF GAME/door slam.mp3")
    camera_sound = pygame.mixer.Sound("FNAF GAME/camera open.mp3")
    camera_switch_sound = pygame.mixer.Sound("FNAF GAME/camera switch.mp3")
    jumpscare_sound = pygame.mixer.Sound("FNAF GAME/jumpscare sound.mp3")
    power_out_sound = pygame.mixer.Sound("FNAF GAME/power out.mp3")                     #CURRENTLY DOES NOT WORK UNTIL I FIND A WAY TO LET MUSIC RUN AND PAUSE
    power_out_music = pygame.mixer.Sound("FNAF GAME/power out music.mp3")
    door_bang_sound = pygame.mixer.Sound("FNAF GAME/door bang.mp3")
    run_sound = pygame.mixer.Sound("FNAF GAME/run sound.mp3")
    vent_enter_sound = pygame.mixer.Sound("FNAF GAME/vent enter.mp3")

    #CAMERA BUTTON LOCATION #   https://pixspy.com/ USE THIS TO FIND PIXEL LOCATIONS
    camera_positions = {
        pygame.K_1: pygame.Rect(150, 479, 66, 47),  # Adjust these values based on the map layout
        pygame.K_2: pygame.Rect(322, 484, 72, 43),
        pygame.K_3: pygame.Rect(39, 312, 70, 44),
        pygame.K_4: pygame.Rect(195, 145, 77, 44),
        pygame.K_5: pygame.Rect(458, 149, 78, 44),
        pygame.K_6: pygame.Rect(341, 331, 74, 48),
        pygame.K_7: pygame.Rect(559, 275, 81, 51),
    }

    # load images
    images = {}
    image_paths = {
        pygame.K_1: "FNAF GAME/IMAGES/CAM1.png",
        pygame.K_2: "FNAF GAME/IMAGES/CAM2.png",
        pygame.K_3: "FNAF GAME/IMAGES/CAM3.png",
        pygame.K_4: "FNAF GAME/IMAGES/CAM4.png",
        pygame.K_5: "FNAF GAME/IMAGES/CAM5.png",
        pygame.K_6: "FNAF GAME/IMAGES/CAM6.png",
        pygame.K_7: "FNAF GAME/IMAGES/CAM7.png",
    }

    CAM1_ANI_image_path = "FNAF GAME/IMAGES/CAM1_ANI2.png"     #i think im stupid i didnt have to do this but i like it this way
    CAM2_ANI_image_path = "FNAF GAME/IMAGES/CAM2_ANI1.png"
    CAM3_ANI_image_path = "FNAF GAME/IMAGES/CAM3_ANI3.png"
    CAM4_ANI_image_path = "FNAF GAME/IMAGES/CAM4_ANI2.png"
    CAM5_ANI_image_path = "FNAF GAME/IMAGES/CAM5_ANI1.png"
    CAM6_ANI_image_path = "FNAF GAME/IMAGES/CAM6_ANI1.png"
    CAM7_ANI_image_path = "FNAF GAME/IMAGES/CAM7_ANI2.png"

    if os.path.exists(CAM1_ANI_image_path): 
        CAM1_ANI_image = pygame.image.load(CAM1_ANI_image_path)
    else:
        print(f"file not found: {CAM1_ANI_image_path}")
        CAM1_ANI_image = None 

    if os.path.exists(CAM2_ANI_image_path):
        CAM2_ANI_image = pygame.image.load(CAM2_ANI_image_path)
    else:
        print(f"file not found: {CAM2_ANI_image_path}")
        CAM2_ANI_image = None

    if os.path.exists(CAM3_ANI_image_path):
        CAM3_ANI_image = pygame.image.load(CAM3_ANI_image_path)
    else:
        print(f"file not found: {CAM3_ANI_image_path}")
        CAM3_ANI_image = None

    if os.path.exists(CAM4_ANI_image_path):
        CAM4_ANI_image = pygame.image.load(CAM4_ANI_image_path)
    else:
        print(f"file not found: {CAM4_ANI_image_path}")
        CAM4_ANI_image = None

    if os.path.exists(CAM5_ANI_image_path):
        CAM5_ANI_image = pygame.image.load(CAM5_ANI_image_path)
    else:
        print(f"file not found: {CAM5_ANI_image_path}")
        CAM5_ANI_image = None

    if os.path.exists(CAM6_ANI_image_path):
        CAM6_ANI_image = pygame.image.load(CAM6_ANI_image_path)
    else:
        print(f"file not found: {CAM6_ANI_image_path}")
        CAM6_ANI_image = None

    if os.path.exists(CAM7_ANI_image_path):
        CAM7_ANI_image = pygame.image.load(CAM7_ANI_image_path)
    else:
        print(f"file not found: {CAM7_ANI_image_path}")
        CAM7_ANI_image = None

    animatronic_images = {
        pygame.K_5: CAM5_ANI_image,
        pygame.K_6: CAM6_ANI_image,
        pygame.K_2: CAM2_ANI_image,
        pygame.K_7: CAM7_ANI_image,
        pygame.K_4: CAM4_ANI_image,
        pygame.K_1: CAM1_ANI_image,
        pygame.K_3: CAM3_ANI_image,
    }

    security_image_path = "FNAF GAME/IMAGES/SECURITY ROOM.png"
    jumpscare_image_path = "FNAF GAME/IMAGES/JUMPSCARE.png"

    vents = {}
    vent_image_paths = {
        pygame.K_s: "FNAF GAME/IMAGES/VENT0.png",
        pygame.K_f: "FNAF GAME/IMAGES/VENT1.png",
    }
    ani3_vent1_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT1.png"
    ani3_vent2_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT2.png"
    ani3_vent3_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT3.png"

    doors = {}                                                          #WORK ON THE DOORS I HAVE NO CLUE
    security_door_paths = {
        pygame.K_a: "FNAF GAME/IMAGES/SECURITY DOOR LEFT.png",
        pygame.K_d: "FNAF GAME/IMAGES/SECURITY DOOR RIGHT.png",
    }

    for key, path in image_paths.items(): # Load images from file paths and store them in the 'images' dictionary (THE KEY IS THE KEY PRESSED AND THE PATH IS THE VALUE WHICH IS WHERE THE IMAGE IS STORED)
        if os.path.exists(path):
            images[key] = pygame.image.load(path)   #load image from file path based on key corrrespond to CAMERA
        else:
            print(f"file not found: {path}")

    if os.path.exists(security_image_path): #load security room then from the path (essentially locates it before it loads)
        security_image = pygame.image.load(security_image_path)
    else:
        print(f"file not found: {security_image_path}")
        security_image = None # sets to no image if cant find

    if os.path.exists(jumpscare_image_path): 
        jumpscare_image = pygame.image.load(jumpscare_image_path)
    else:
        print(f"file not found: {jumpscare_image_path}")
        jumpscare_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent1_image_path):
        ani3_vent1_image = pygame.image.load(ani3_vent1_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent1_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent2_image_path):
        ani3_vent2_image = pygame.image.load(ani3_vent2_image_path)
    else:
        print(f"file not found: {ani3_vent2_image_path}")
        ani3_vent2_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent3_image_path):
        ani3_vent3_image = pygame.image.load(ani3_vent3_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent3_image = None # sets to no image if cant find

    for vent, path in vent_image_paths.items():
        if os.path.exists(path):
            vents[vent] = pygame.image.load(path) # load image from file path based on key
        else:
            print(f"file not found: {path}")
            vents[vent] = None

    for door, path in security_door_paths.items(): # Load images from file paths and store them in the 'doors'
        if os.path.exists(path):
            doors[door] = pygame.image.load(path)   #load image from file path based on
        else:
            print(f"file not found: {path}")

    current_image = security_image  # states beginning image that was loaded

    for i in range(2):
        camera_open = True
        camera_open = False 
    current_camera = None #tracks the current camera

    door_states = {  # Tracks the state of each door (True for closed, False for open)
        "left": False,
        "right": False,
    }
    previous_door_states = {
        "left": False,
        "right": False,
    }
    #- - - - - - - - - - - - - - - - - - - - - - - ANIMATRONIC LOGIC - - - - - - - - - - - - - - - - - - - - -
    """ANIMATRONIC 1""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 1 movement variables (RNG ONE)(you can change chance here)
    animatronic1_camera_sequence = [pygame.K_5, pygame.K_6, pygame.K_2]  # Cameras the animatronic moves through
    animatronic1_current_camera = 0  # Start at the first camera
    animatronic1_probability = 0.0075  # Initial chance to move
    animatronic1_probability_increment = 0.0075  # Increment per second



    animatronic1_at_door_time = 0  #track time if animatronic1 is at door

    """ANIMATRONIC 2""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 2 movement, (camera stare one) make him start at 2 am
    animatronic2_camera_sequence = [pygame.K_7, pygame.K_4, pygame.K_1]
    animatronic2_current_camera = 0
    look_at_time = 0
    time_not_looked = 0


    """ANIMATRONIC 3""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 3 movement, (starts at CAM 3 and moves to vent behind user) count times camera was opened
    animatronic3_camera_sequence = [pygame.K_3, ani3_vent1_image, ani3_vent2_image, ani3_vent3_image]
    animatronic3_current_camera = 0
    camera_open_count = 0


    def render_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_thickness=2):        #I FOUND THIS ONLINE BUT IT WORKS SO IM NOT COMPLAINING
        """Renders text with an outline at the given position."""
        for dx in range(-outline_thickness, outline_thickness + 1): # Render the outline
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:  # skip the center (original position)
                    outline_surface = font.render(text, True, outline_color)
                    surface.blit(outline_surface, (x + dx, y + dy))
    
        text_surface = font.render(text, True, text_color)   # Render the actual text
        surface.blit(text_surface, (x, y))

    # Initialize time tracking for clock (12 AM to 6 AM)
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)
    time_remaining = game_duration

    def format_game_time(ms):
        """Formats the game time from milliseconds into hours (12 AM to 6 AM)."""
        # Convert elapsed milliseconds to minutes
        minutes_elapsed = (game_duration - ms) // 1000 // 60
        # Determine the current hour
        hour = 12 + minutes_elapsed
        return f"{hour % 12 or 12} AM"  # Use 12 for the hour if it rolls over to 0

    """BLINK SCREEN FUNCTION"""
    def blink_screen(screen, start_time, blink_duration=200, blink_interval=300):
        #blinks at specified interval
        current_time = pygame.time.get_ticks()

        # Check if we need to display the black screen
        if current_time - start_time < blink_duration:
            screen.fill((0, 0, 0))  # Fill the screen with black
            pygame.display.flip()
        elif current_time - start_time < blink_duration + blink_interval:
            # Keep the screen black during the blink interval
            pass
        else:
            # After the interval, reset the screen back to normal (or white in this case)
            screen.fill((0, 0, 0))  # Set back to white or any other color/state
            pygame.display.flip()
            # Return the current time to simulate the blinking interval again
            return pygame.time.get_ticks()

        # Return the start time if we haven't finished blinking yet
        return start_time

    # Main loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)

    running = True
    clock = pygame.time.Clock()
    frame_counterANI1 = 0  # Add more if more animatronics based on frame count
    global_power = 101
    idle_power = 0.00374
    camera_power = 0.005                                            # WORK ON GLOBAL POWER HERE
    door_power = 0.005
    both_doors_power = 0.0115
    door_bang_power = 0.05
    vent_flash_power = 0.005

    vent_flashing = False
    vent_open = False
    current_vent_image = vents[pygame.K_s]
    ani3_flash_time = 0

    vent_enter_sound_played = False
    run_sound_playing = False
    door_bang_sound_playing = False
    animatronic2_at_door_time = 0


    for i in range(2):  #I am quite literally using this because animatronic 2 only kills or resets when the left door was interacted with before the attack sequence, i dont know how to fix so i am using this please dont remove it will destroy it's logic
        door_states["left"] = not door_states["left"]
        door_states["right"] = not door_states["right"]

    power_out_started = False
    power_out_start_time = None
    power_out_stage = 0 

    while running:
        # TIME TRACKER
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_start_time  # Time passed since the game started

        # Calculate the remaining time directly
        time_remaining = game_duration - elapsed_time

        # Make sure time remaining doesn't go negative
        if time_remaining < 0:
            time_remaining = 0

        frame_counterANI1 += 1
        global_power -= idle_power
        
        if global_power < 0:
            global_power = 0
        if camera_open:
            global_power -= camera_power
        if door_states["left"]:
            global_power -= door_power  # Consume power for left door being closed
        if door_states["right"]:
            global_power -= door_power  # Consume power for right door being closed
        if door_states["left"] and door_states["right"]:
            global_power -= both_doors_power  # Additional power for both doors being closed
        if vent_flashing:
            global_power -= vent_flash_power

        if global_power <= 0 and not power_out_started:
            pygame.mixer.music.stop()
            camera_open = False
            current_image = security_image
            current_camera = None
            door_states["left"] = False
            door_states["right"] = False
            power_out_started = True
            power_out_start_time = pygame.time.get_ticks()
            power_out_stage = 1

        if power_out_started:
            elapsed_time = pygame.time.get_ticks() - power_out_start_time

            if power_out_stage == 1:
                if not pygame.mixer.get_busy():  # Ensure the previous music has stopped
                    power_out_sound.play()
                    power_out_stage = 2

            elif power_out_stage == 2:
                if elapsed_time >= 10000:  # Start the power-out music after 10 seconds
                    if not pygame.mixer.get_busy():  # Ensure no overlapping sounds
                        power_out_music.play()
                        power_out_stage = 3

            elif power_out_stage == 3:
                if elapsed_time >= 23000:  # Trigger jumpscare after total 23 seconds
                    if not pygame.mixer.get_busy():  # Ensure music has finished
                        screen.fill((0, 0, 0))
                        screen.blit(jumpscare_image, (0, 0))
                        jumpscare_sound.play()
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                        print("died by one")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Stop the game if the user closes the window
                running = False

            if event.type == pygame.KEYDOWN:     # USE THIS FOR CAMERA NUMBER INPUTS FROM KEYBOARD
                if not power_out_started:

                    if event.key == pygame.K_s:  #toggle vent only when in security room
                        if vent_open or current_image == security_image:  # Allow toggling vent mode only if in security room or vent mode is already open
                            vent_open = not vent_open
                        if vent_open:
                            current_vent_image = vents[pygame.K_s]       
                            current_image = None
                                                                                                    #CHECK IF OWKRWRWRRW
                        else:
                            current_vent_image = None
                            vent_flashing = False
                            if current_image == None:
                                current_image = security_image
                                
                    if event.key == pygame.K_f: #toggle flashed vent
                        if vent_open: #only allow flashlight in vent mode
                            vent_flashing = True
                            

                    if not vent_open:   #disable cam and door in vent mode
                        if event.key in images and camera_open: #check if a key is same as camera num
                            current_image = images[event.key]   #update the current camera to the user inputted key
                            current_camera = event.key  #update the current camera to the user inputted key
                            camera_switch_sound.play()
                        if event.key == pygame.K_SPACE:
                            camera_open_count += 1
                            camera_sound.play()
                            if camera_open:  # If the camera is open
                                current_image = security_image  # Close the camera and display the security image
                                camera_open = False  # Set camera state to closed
                            else:
                                if current_camera:  # Reopen to the last camera viewed
                                    current_image = images[current_camera]
                                else:  # Default to CAM1 if no previous camera exists
                                    current_camera = pygame.K_1
                                    current_image = images[current_camera]
                                camera_open = True  # Set camera state to open

                        if current_image == security_image:
                            #toggle left door                                                           
                            if event.key == pygame.K_a and not camera_open:
                                door_states["left"] = not door_states["left"]
                        
                        #toggle right door
                        if event.key == pygame.K_d and not camera_open:
                            door_states["right"] = not door_states["right"]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:  # Stop flashing when F key is released
                    vent_flashing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the bounds of any camera's clickable area
                if event.button == 1:  # Left mouse click
                    for camera_key, camera_rect in camera_positions.items():
                        if camera_rect.collidepoint(event.pos):
                            current_image = images[camera_key]  # Switch to the clicked camera
                            current_camera = camera_key
                            camera_switch_sound.play()

        # Play door sound if the door state has changed
        if door_states["left"] != previous_door_states["left"]:  #checks if the change was from true to false or false to true
            door_sound.play()  # Play left door sound
            previous_door_states["left"] = door_states["left"]  # Update previous state

        if door_states["right"] != previous_door_states["right"]:
            door_sound.play()  # Play right door sound
            previous_door_states["right"] = door_states["right"]  # Update previous state

        

        # Animatronic 1 movement logic 
        if frame_counterANI1 >= 30:  # Check every 30 frames (about once per second at 30 FPS)
            frame_counterANI1 = 0
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                if random.random() < animatronic1_probability:  # Animatronic decides to move
                    blink_screen(screen, 0)
                    animatronic1_probability = 0.0075  # Reset probability after movement
                    animatronic1_current_camera += 1
                else:
                    animatronic1_probability += animatronic1_probability_increment

        #ANIMATRONIC 1 RESET FUNCTION
        if animatronic1_current_camera > len(animatronic1_camera_sequence):
            animatronic1_current_camera = 0

        if animatronic1_current_camera == 2:  # Check if animatronic is at Camera 2
            door_open = not door_states["right"]  # Animatronic checks the right door state

            if door_open:
                if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                    animatronic1_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic1_at_door_time >= 5000:  # If the door is open for 5 seconds
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  # Show the jumpscare image
                    jumpscare_sound.play()  # Play jumpscare sound
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  # End the game
            else:
                if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                    animatronic1_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic1_at_door_time >= 8500:  # If the door is closed for 8 seconds
                    blink_screen(screen, 0)
                    animatronic1_current_camera = 0  # Reset animatronic to Camera 5
                    animatronic1_probability = 0.01  # Reset movement probability
                    animatronic1_at_door_time = 0  # Reset the door timer
                    

        else:
            animatronic1_at_door_time = 0  # Reset the timer if animatronic is not at Camera 2
        
        # Animatronic 2 look at logic and reset
        if animatronic2_current_camera < 0 or animatronic2_current_camera > 2:
            animatronic2_current_camera = 0


        if animatronic2_current_camera < len(animatronic2_camera_sequence):
            current_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
            
            if current_camera == current_camera_key:
                look_at_time += clock.get_time()  # Increment look_at_time by the time since the last frame
            else:
                look_at_time = 0  # Reset if not on the same camera

            if look_at_time >= 5000 and camera_open: 
                blink_screen(screen, 0)
                look_at_time = 0
                time_not_looked = 0
                animatronic2_current_camera += 1
                if animatronic2_current_camera == 2:
                    animatronic2_current_camera += 1

            
        if current_camera != animatronic2_current_camera:
            time_not_looked += clock.get_time()
        

    #animatronic 2 attack logic
        if time_not_looked >= 20000:  # Check if the animatronic can attack
            if not run_sound_playing:
                blink_screen(screen, 0)
                run_sound.play()
                run_sound_playing = True
            animatronic2_current_camera = 2

            door_open = not door_states["left"]

            if door_open:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic2_at_door_time >= 5000:  
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  
                    jumpscare_sound.play()  
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  
            else:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                
                current_time = pygame.time.get_ticks()
                if current_time - animatronic2_at_door_time >= 8500:  
                    if not door_bang_sound_playing:
                        door_bang_sound.play()
                        door_bang_sound_playing = True
                        global_power -= door_bang_power
                        blink_screen(screen, 0)
                        
                
                    time_not_looked = 0  # Reset time not looked only after the full 8 seconds
                    animatronic2_current_camera = 0
                    animatronic2_at_door_time = 0
                    run_sound_playing = False
                    door_bang_sound_playing = False
                    print("ani 2 reset")
        else:
            run_sound_playing = False             
            door_bang_sound_playing = False 
            animatronic2_at_door_time = 0             

        #ANIMATRONIC 3 MOVEMENT
        if animatronic3_current_camera == 0:
            if camera_open_count >= 20:
                animatronic3_current_camera = 1
                camera_open_count = 0
                if not vent_enter_sound_played:
                    vent_enter_sound.play()
                    vent_enter_sound_played = True
                ani3_last_move_time = pygame.time.get_ticks()
        else:
            vent_enter_sound_played = False

        # Animatronic 3 movement logic
        if animatronic3_current_camera in [1, 2, 3]:
            if not vent_flashing:
                if pygame.time.get_ticks() - ani3_last_move_time >= 5000:  # Move every 5 seconds
                    animatronic3_current_camera += 1
                    ani3_last_move_time = pygame.time.get_ticks()
        else:
            ani3_last_move_time = pygame.time.get_ticks()

        if animatronic3_current_camera > 3:  #Jumpscare if animatronic3_current_camera is greater than index 3
            screen.fill((0, 0, 0))
            screen.blit(jumpscare_image, (0, 0))
            jumpscare_sound.play()
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
            print("died by animatronic 3")

        # Flashing logic for Animatronic 3
        if vent_flashing:
            if animatronic3_current_camera in [1, 2, 3]:             #ANIMATRONIC 3 IS BROKEN, FIX KILL RESET OR KILL, I DID NOT CHECK PLEASE MAKE SURE IT WORKS __+__++_++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                ani3_flash_time += clock.get_time()
                if ani3_flash_time >= 5000:  # Reset animatronic 3 if flashed for 8 seconds
                    blink_screen(screen, 0)
                    animatronic3_current_camera = 0
                    ani3_flash_time = 0
                    ani3_last_move_time = pygame.time.get_ticks()
            else:
                current_vent_image = vents[pygame.K_f]
        else:
            ani3_flash_time = 0  # Reset flash time if not flashing                                                                                 

        #RENDERING SECTION FOR IMAGE RENDERING IF RENDERING WITH IMAGES - - - - - - - -- - - - - -- - - - - -- - - - - - - -- - - - - - -- - - - - - -

        screen.fill((0, 0, 0))  #Fill the screen with black to clear the previous frame

        if current_image:  # Draws the current image on the screen
            screen.blit(current_image, (0, 0))
        else:
            screen.blit(security_image, (0, 0))  # If no image, draw security room

        if vent_open and current_vent_image:
            screen.blit(current_vent_image, (0, 0))

        # Don't draw animatronic when showing the security room
        if current_image != security_image and not vent_open:
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                animatronic1_camera_key = animatronic1_camera_sequence[animatronic1_current_camera]
                if current_camera == animatronic1_camera_key:
                    animatronic_image = animatronic_images.get(animatronic1_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic2_current_camera < len(animatronic2_camera_sequence):
                animatronic2_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
                if current_camera == animatronic2_camera_key:
                    animatronic_image = animatronic_images.get(animatronic2_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic3_current_camera < len(animatronic3_camera_sequence):
                animatronic3_camera_key = animatronic3_camera_sequence[animatronic3_current_camera]
                if current_camera == animatronic3_camera_key:
                    animatronic_image = animatronic_images.get(animatronic3_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

        # Flashing logic for Animatronic 3 in vents
        if vent_flashing:
            if animatronic3_current_camera == 1 and ani3_vent1_image:
                screen.blit(ani3_vent1_image, (0, 0))
            elif animatronic3_current_camera == 2 and ani3_vent2_image:
                screen.blit(ani3_vent2_image, (0, 0))
            elif animatronic3_current_camera == 3 and ani3_vent3_image:
                screen.blit(ani3_vent3_image, (0, 0))
        else:
        # If not flashing, show the default vent image
            if vent_open:
                current_vent_image = vents[pygame.K_s]  # Default to VENT0
                screen.blit(current_vent_image, (0, 0))  # Show VENT0

        # Draw door images at the bottom corners
        if current_image == security_image:
            if door_states["left"]:
                screen.blit(doors[pygame.K_a], (0, HEIGHT - doors[pygame.K_a].get_height()))  # draw left door at bottom left
            if door_states["right"]:
                screen.blit(doors[pygame.K_d], (WIDTH - doors[pygame.K_d].get_width(), HEIGHT - doors[pygame.K_d].get_height()))  # Draw right door at bottom right
        
        power_percent = int(global_power)                       # POWER DISPLAY
        power_text = f"POWER: {power_percent}%"
        render_outlined_text(
            screen,
            power_text,
            font,
            10,  # X position 
            HEIGHT - font_size - 10,  # Yposition
            (255, 255, 255),  # white interior
            (0, 0, 0),  # black outline
            2,  # outline thickness
        )
        #print(time_remaining)#------------------------------------------------------------------------------------------------------------ENABLE THIS COMMENT TO SEE TIME REMAINING IN MILISECONDS---------
        # Format the clock and render it
        formatted_time = format_game_time(time_remaining)  # Get formatted time string using time_remaining
        render_outlined_text(
            screen,
            formatted_time,
            font,
            WIDTH - 150,  # X position
            10,  # Y position
            (255, 255, 255),  #white text
            (0, 0, 0),  #black outline
            2,  # outline thickness
        )

        if time_remaining == 0:
            render_outlined_text(
                screen,
                "YOU WIN!",
                font,
                WIDTH // 2 - 80,  #X position 
                HEIGHT // 2 - 50,  #Y position
                (0, 255, 0),  #geen text
                (0, 0, 0),  #black outline
                2,  #outline thickness
            )

        pygame.display.flip()  #update display for new frame

        clock.tick(30)  # 30 fps limiter

    # Quit Pygame
    pygame.quit()

def night_four():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    # Get the absolute path of the MP3 file
    ambience_mp3 = "FNAF GAME/AMBIENCE.mp3"
    phone_mp3 = "FNAF GAME/phone night one.mp3"
    # Load and play the MP3 file

    # Play ambience sound on a loop
    ambience_channel = pygame.mixer.Channel(1)
    ambience_sound = pygame.mixer.Sound(ambience_mp3)
    ambience_channel.play(ambience_sound, loops=-1)
    """
    # Play phone sound on a different channel
    phone_channel = pygame.mixer.Channel(2)                 YOU CAN ADD SOME INTERESTING DIALOGUE OR SMT IF U WANT
    phone_sound = pygame.mixer.Sound(phone_mp3)
    phone_channel.play(phone_sound)
    """
    WIDTH, HEIGHT = 1920, 1080      # SCREEN RESOLUTION using 1080p for simplicity's sake
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nightmera")

    font_size = 36  # You can adjust the size as needed
    font = pygame.font.Font(None, font_size)

    # load sound effects
    door_sound = pygame.mixer.Sound("FNAF GAME/door slam.mp3")
    camera_sound = pygame.mixer.Sound("FNAF GAME/camera open.mp3")
    camera_switch_sound = pygame.mixer.Sound("FNAF GAME/camera switch.mp3")
    jumpscare_sound = pygame.mixer.Sound("FNAF GAME/jumpscare sound.mp3")
    power_out_sound = pygame.mixer.Sound("FNAF GAME/power out.mp3")                     #CURRENTLY DOES NOT WORK UNTIL I FIND A WAY TO LET MUSIC RUN AND PAUSE
    power_out_music = pygame.mixer.Sound("FNAF GAME/power out music.mp3")
    door_bang_sound = pygame.mixer.Sound("FNAF GAME/door bang.mp3")
    run_sound = pygame.mixer.Sound("FNAF GAME/run sound.mp3")
    vent_enter_sound = pygame.mixer.Sound("FNAF GAME/vent enter.mp3")

    #CAMERA BUTTON LOCATION #   https://pixspy.com/ USE THIS TO FIND PIXEL LOCATIONS
    camera_positions = {
        pygame.K_1: pygame.Rect(150, 479, 66, 47),  # Adjust these values based on the map layout
        pygame.K_2: pygame.Rect(322, 484, 72, 43),
        pygame.K_3: pygame.Rect(39, 312, 70, 44),
        pygame.K_4: pygame.Rect(195, 145, 77, 44),
        pygame.K_5: pygame.Rect(458, 149, 78, 44),
        pygame.K_6: pygame.Rect(341, 331, 74, 48),
        pygame.K_7: pygame.Rect(559, 275, 81, 51),
    }

    # load images
    images = {}
    image_paths = {
        pygame.K_1: "FNAF GAME/IMAGES/CAM1.png",
        pygame.K_2: "FNAF GAME/IMAGES/CAM2.png",
        pygame.K_3: "FNAF GAME/IMAGES/CAM3.png",
        pygame.K_4: "FNAF GAME/IMAGES/CAM4.png",
        pygame.K_5: "FNAF GAME/IMAGES/CAM5.png",
        pygame.K_6: "FNAF GAME/IMAGES/CAM6.png",
        pygame.K_7: "FNAF GAME/IMAGES/CAM7.png",
    }

    CAM1_ANI_image_path = "FNAF GAME/IMAGES/CAM1_ANI2.png"     #i think im stupid i didnt have to do this but i like it this way
    CAM2_ANI_image_path = "FNAF GAME/IMAGES/CAM2_ANI1.png"
    CAM3_ANI_image_path = "FNAF GAME/IMAGES/CAM3_ANI3.png"
    CAM4_ANI_image_path = "FNAF GAME/IMAGES/CAM4_ANI2.png"
    CAM5_ANI_image_path = "FNAF GAME/IMAGES/CAM5_ANI1.png"
    CAM6_ANI_image_path = "FNAF GAME/IMAGES/CAM6_ANI1.png"
    CAM7_ANI_image_path = "FNAF GAME/IMAGES/CAM7_ANI2.png"

    if os.path.exists(CAM1_ANI_image_path): 
        CAM1_ANI_image = pygame.image.load(CAM1_ANI_image_path)
    else:
        print(f"file not found: {CAM1_ANI_image_path}")
        CAM1_ANI_image = None 

    if os.path.exists(CAM2_ANI_image_path):
        CAM2_ANI_image = pygame.image.load(CAM2_ANI_image_path)
    else:
        print(f"file not found: {CAM2_ANI_image_path}")
        CAM2_ANI_image = None

    if os.path.exists(CAM3_ANI_image_path):
        CAM3_ANI_image = pygame.image.load(CAM3_ANI_image_path)
    else:
        print(f"file not found: {CAM3_ANI_image_path}")
        CAM3_ANI_image = None

    if os.path.exists(CAM4_ANI_image_path):
        CAM4_ANI_image = pygame.image.load(CAM4_ANI_image_path)
    else:
        print(f"file not found: {CAM4_ANI_image_path}")
        CAM4_ANI_image = None

    if os.path.exists(CAM5_ANI_image_path):
        CAM5_ANI_image = pygame.image.load(CAM5_ANI_image_path)
    else:
        print(f"file not found: {CAM5_ANI_image_path}")
        CAM5_ANI_image = None

    if os.path.exists(CAM6_ANI_image_path):
        CAM6_ANI_image = pygame.image.load(CAM6_ANI_image_path)
    else:
        print(f"file not found: {CAM6_ANI_image_path}")
        CAM6_ANI_image = None

    if os.path.exists(CAM7_ANI_image_path):
        CAM7_ANI_image = pygame.image.load(CAM7_ANI_image_path)
    else:
        print(f"file not found: {CAM7_ANI_image_path}")
        CAM7_ANI_image = None

    animatronic_images = {
        pygame.K_5: CAM5_ANI_image,
        pygame.K_6: CAM6_ANI_image,
        pygame.K_2: CAM2_ANI_image,
        pygame.K_7: CAM7_ANI_image,
        pygame.K_4: CAM4_ANI_image,
        pygame.K_1: CAM1_ANI_image,
        pygame.K_3: CAM3_ANI_image,
    }

    security_image_path = "FNAF GAME/IMAGES/SECURITY ROOM.png"
    jumpscare_image_path = "FNAF GAME/IMAGES/JUMPSCARE.png"

    vents = {}
    vent_image_paths = {
        pygame.K_s: "FNAF GAME/IMAGES/VENT0.png",
        pygame.K_f: "FNAF GAME/IMAGES/VENT1.png",
    }
    ani3_vent1_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT1.png"
    ani3_vent2_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT2.png"
    ani3_vent3_image_path = "FNAF GAME/IMAGES/ANIMATRONIC3_VENT3.png"

    doors = {}                                                          #WORK ON THE DOORS I HAVE NO CLUE
    security_door_paths = {
        pygame.K_a: "FNAF GAME/IMAGES/SECURITY DOOR LEFT.png",
        pygame.K_d: "FNAF GAME/IMAGES/SECURITY DOOR RIGHT.png",
    }

    for key, path in image_paths.items(): # Load images from file paths and store them in the 'images' dictionary (THE KEY IS THE KEY PRESSED AND THE PATH IS THE VALUE WHICH IS WHERE THE IMAGE IS STORED)
        if os.path.exists(path):
            images[key] = pygame.image.load(path)   #load image from file path based on key corrrespond to CAMERA
        else:
            print(f"file not found: {path}")

    if os.path.exists(security_image_path): #load security room then from the path (essentially locates it before it loads)
        security_image = pygame.image.load(security_image_path)
    else:
        print(f"file not found: {security_image_path}")
        security_image = None # sets to no image if cant find

    if os.path.exists(jumpscare_image_path): 
        jumpscare_image = pygame.image.load(jumpscare_image_path)
    else:
        print(f"file not found: {jumpscare_image_path}")
        jumpscare_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent1_image_path):
        ani3_vent1_image = pygame.image.load(ani3_vent1_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent1_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent2_image_path):
        ani3_vent2_image = pygame.image.load(ani3_vent2_image_path)
    else:
        print(f"file not found: {ani3_vent2_image_path}")
        ani3_vent2_image = None # sets to no image if cant find

    if os.path.exists(ani3_vent3_image_path):
        ani3_vent3_image = pygame.image.load(ani3_vent3_image_path)
    else:
        print(f"file not found: {ani3_vent1_image_path}")
        ani3_vent3_image = None # sets to no image if cant find

    for vent, path in vent_image_paths.items():
        if os.path.exists(path):
            vents[vent] = pygame.image.load(path) # load image from file path based on key
        else:
            print(f"file not found: {path}")
            vents[vent] = None

    for door, path in security_door_paths.items(): # Load images from file paths and store them in the 'doors'
        if os.path.exists(path):
            doors[door] = pygame.image.load(path)   #load image from file path based on
        else:
            print(f"file not found: {path}")

    current_image = security_image  # states beginning image that was loaded

    for i in range(2):
        camera_open = True
        camera_open = False 
    current_camera = None #tracks the current camera

    door_states = {  # Tracks the state of each door (True for closed, False for open)
        "left": False,
        "right": False,
    }
    previous_door_states = {
        "left": False,
        "right": False,
    }
    #- - - - - - - - - - - - - - - - - - - - - - - ANIMATRONIC LOGIC - - - - - - - - - - - - - - - - - - - - -
    """ANIMATRONIC 1""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 1 movement variables (RNG ONE)(you can change chance here)
    animatronic1_camera_sequence = [pygame.K_5, pygame.K_6, pygame.K_2]  # Cameras the animatronic moves through
    animatronic1_current_camera = 0  # Start at the first camera
    animatronic1_probability = 0.01  # Initial chance to move
    animatronic1_probability_increment = 0.01  # Increment per second



    animatronic1_at_door_time = 0  #track time if animatronic1 is at door

    """ANIMATRONIC 2""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 2 movement, (camera stare one) make him start at 2 am
    animatronic2_camera_sequence = [pygame.K_7, pygame.K_4, pygame.K_1]
    animatronic2_current_camera = 0
    look_at_time = 0
    time_not_looked = 0


    """ANIMATRONIC 3""" # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                           # Animatronic 3 movement, (starts at CAM 3 and moves to vent behind user) count times camera was opened
    animatronic3_camera_sequence = [pygame.K_3, ani3_vent1_image, ani3_vent2_image, ani3_vent3_image]
    animatronic3_current_camera = 0
    camera_open_count = 0


    def render_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_thickness=2):        #I FOUND THIS ONLINE BUT IT WORKS SO IM NOT COMPLAINING
        """Renders text with an outline at the given position."""
        for dx in range(-outline_thickness, outline_thickness + 1): # Render the outline
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:  # skip the center (original position)
                    outline_surface = font.render(text, True, outline_color)
                    surface.blit(outline_surface, (x + dx, y + dy))
    
        text_surface = font.render(text, True, text_color)   # Render the actual text
        surface.blit(text_surface, (x, y))

    # Initialize time tracking for clock (12 AM to 6 AM)
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)
    time_remaining = game_duration

    def format_game_time(ms):
        """Formats the game time from milliseconds into hours (12 AM to 6 AM)."""
        # Convert elapsed milliseconds to minutes
        minutes_elapsed = (game_duration - ms) // 1000 // 60
        # Determine the current hour
        hour = 12 + minutes_elapsed
        return f"{hour % 12 or 12} AM"  # Use 12 for the hour if it rolls over to 0

    """BLINK SCREEN FUNCTION"""
    def blink_screen(screen, start_time, blink_duration=200, blink_interval=300):
        #blinks at specified interval
        current_time = pygame.time.get_ticks()

        # Check if we need to display the black screen
        if current_time - start_time < blink_duration:
            screen.fill((0, 0, 0))  # Fill the screen with black
            pygame.display.flip()
        elif current_time - start_time < blink_duration + blink_interval:
            # Keep the screen black during the blink interval
            pass
        else:
            # After the interval, reset the screen back to normal (or white in this case)
            screen.fill((0, 0, 0))  # Set back to white or any other color/state
            pygame.display.flip()
            # Return the current time to simulate the blinking interval again
            return pygame.time.get_ticks()

        # Return the start time if we haven't finished blinking yet
        return start_time

    # Main loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    game_start_time = pygame.time.get_ticks()  # Time when the game starts (0:00)
    game_duration = 6 * 60 * 1000  # 6 minutes (in milliseconds)

    running = True
    clock = pygame.time.Clock()
    frame_counterANI1 = 0  # Add more if more animatronics based on frame count
    global_power = 101
    idle_power = 0.00374
    camera_power = 0.008                                            # WORK ON GLOBAL POWER HERE
    door_power = 0.006
    both_doors_power = 0.0135
    door_bang_power = 0.01
    vent_flash_power = 0.008

    vent_flashing = False
    vent_open = False
    current_vent_image = vents[pygame.K_s]
    ani3_flash_time = 0

    vent_enter_sound_played = False
    run_sound_playing = False
    door_bang_sound_playing = False
    animatronic2_at_door_time = 0


    for i in range(2):  #I am quite literally using this because animatronic 2 only kills or resets when the left door was interacted with before the attack sequence, i dont know how to fix so i am using this please dont remove it will destroy it's logic
        door_states["left"] = not door_states["left"]
        door_states["right"] = not door_states["right"]

    power_out_started = False
    power_out_start_time = None
    power_out_stage = 0 

    while running:
        # TIME TRACKER
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - game_start_time  # Time passed since the game started

        # Calculate the remaining time directly
        time_remaining = game_duration - elapsed_time

        # Make sure time remaining doesn't go negative
        if time_remaining < 0:
            time_remaining = 0

        frame_counterANI1 += 1
        global_power -= idle_power
        
        if global_power < 0:
            global_power = 0
        if camera_open:
            global_power -= camera_power
        if door_states["left"]:
            global_power -= door_power  # Consume power for left door being closed
        if door_states["right"]:
            global_power -= door_power  # Consume power for right door being closed
        if door_states["left"] and door_states["right"]:
            global_power -= both_doors_power  # Additional power for both doors being closed
        if vent_flashing:
            global_power -= vent_flash_power

        if global_power <= 0 and not power_out_started:
            pygame.mixer.music.stop()
            camera_open = False
            current_image = security_image
            current_camera = None
            door_states["left"] = False
            door_states["right"] = False
            power_out_started = True
            power_out_start_time = pygame.time.get_ticks()
            power_out_stage = 1

        if power_out_started:
            elapsed_time = pygame.time.get_ticks() - power_out_start_time

            if power_out_stage == 1:
                if not pygame.mixer.get_busy():  # Ensure the previous music has stopped
                    power_out_sound.play()
                    power_out_stage = 2

            elif power_out_stage == 2:
                if elapsed_time >= 10000:  # Start the power-out music after 10 seconds
                    if not pygame.mixer.get_busy():  # Ensure no overlapping sounds
                        power_out_music.play()
                        power_out_stage = 3

            elif power_out_stage == 3:
                if elapsed_time >= 23000:  # Trigger jumpscare after total 23 seconds
                    if not pygame.mixer.get_busy():  # Ensure music has finished
                        screen.fill((0, 0, 0))
                        screen.blit(jumpscare_image, (0, 0))
                        jumpscare_sound.play()
                        pygame.display.flip()
                        pygame.time.wait(3000)
                        running = False
                        print("died by one")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Stop the game if the user closes the window
                running = False

            if event.type == pygame.KEYDOWN:     # USE THIS FOR CAMERA NUMBER INPUTS FROM KEYBOARD
                if not power_out_started:

                    if event.key == pygame.K_s:  #toggle vent only when in security room
                        if vent_open or current_image == security_image:  # Allow toggling vent mode only if in security room or vent mode is already open
                            vent_open = not vent_open
                        if vent_open:
                            current_vent_image = vents[pygame.K_s]       
                            current_image = None
                                                                                                    #CHECK IF OWKRWRWRRW
                        else:
                            current_vent_image = None
                            vent_flashing = False
                            if current_image == None:
                                current_image = security_image
                                
                    if event.key == pygame.K_f: #toggle flashed vent
                        if vent_open: #only allow flashlight in vent mode
                            vent_flashing = True
                            

                    if not vent_open:   #disable cam and door in vent mode
                        if event.key in images and camera_open: #check if a key is same as camera num
                            current_image = images[event.key]   #update the current camera to the user inputted key
                            current_camera = event.key  #update the current camera to the user inputted key
                            camera_switch_sound.play()
                        if event.key == pygame.K_SPACE:
                            camera_open_count += 1
                            camera_sound.play()
                            if camera_open:  # If the camera is open
                                current_image = security_image  # Close the camera and display the security image
                                camera_open = False  # Set camera state to closed
                            else:
                                if current_camera:  # Reopen to the last camera viewed
                                    current_image = images[current_camera]
                                else:  # Default to CAM1 if no previous camera exists
                                    current_camera = pygame.K_1
                                    current_image = images[current_camera]
                                camera_open = True  # Set camera state to open

                        if current_image == security_image:
                            #toggle left door                                                           
                            if event.key == pygame.K_a and not camera_open:
                                door_states["left"] = not door_states["left"]
                        
                        #toggle right door
                        if event.key == pygame.K_d and not camera_open:
                            door_states["right"] = not door_states["right"]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:  # Stop flashing when F key is released
                    vent_flashing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the bounds of any camera's clickable area
                if event.button == 1:  # Left mouse click
                    for camera_key, camera_rect in camera_positions.items():
                        if camera_rect.collidepoint(event.pos):
                            current_image = images[camera_key]  # Switch to the clicked camera
                            current_camera = camera_key
                            camera_switch_sound.play()

        # Play door sound if the door state has changed
        if door_states["left"] != previous_door_states["left"]:  #checks if the change was from true to false or false to true
            door_sound.play()  # Play left door sound
            previous_door_states["left"] = door_states["left"]  # Update previous state

        if door_states["right"] != previous_door_states["right"]:
            door_sound.play()  # Play right door sound
            previous_door_states["right"] = door_states["right"]  # Update previous state

        

        # Animatronic 1 movement logic 
        if frame_counterANI1 >= 30:  # Check every 30 frames (about once per second at 30 FPS)
            frame_counterANI1 = 0
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                if random.random() < animatronic1_probability:  # Animatronic decides to move
                    blink_screen(screen, 0)
                    animatronic1_probability = 0.01  # Reset probability after movement
                    animatronic1_current_camera += 1
                else:
                    animatronic1_probability += animatronic1_probability_increment

        #ANIMATRONIC 1 RESET FUNCTION
        if animatronic1_current_camera > len(animatronic1_camera_sequence):
            animatronic1_current_camera = 0

        if animatronic1_current_camera == 2:  # Check if animatronic is at Camera 2
            door_open = not door_states["right"]  # Animatronic checks the right door state

            if door_open:
                if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                    animatronic1_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic1_at_door_time >= 5000:  # If the door is open for 5 seconds
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  # Show the jumpscare image
                    jumpscare_sound.play()  # Play jumpscare sound
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  # End the game
            else:
                if animatronic1_at_door_time == 0:  # Start the timer if animatronic reaches the door
                    animatronic1_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic1_at_door_time >= 9000:  # If the door is closed for  seconds
                    blink_screen(screen, 0)
                    animatronic1_current_camera = 0  # Reset animatronic to Camera 5
                    animatronic1_probability = 0.01  # Reset movement probability
                    animatronic1_at_door_time = 0  # Reset the door timer
                    

        else:
            animatronic1_at_door_time = 0  # Reset the timer if animatronic is not at Camera 2
        
        # Animatronic 2 look at logic and reset
        if animatronic2_current_camera < 0 or animatronic2_current_camera > 2:
            animatronic2_current_camera = 0


        if animatronic2_current_camera < len(animatronic2_camera_sequence):
            current_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
            
            if current_camera == current_camera_key:
                look_at_time += clock.get_time()  # Increment look_at_time by the time since the last frame
            else:
                look_at_time = 0  # Reset if not on the same camera

            if look_at_time >= 5000 and camera_open: 
                blink_screen(screen, 0)
                look_at_time = 0
                time_not_looked = 0
                animatronic2_current_camera += 1
                if animatronic2_current_camera == 2:
                    animatronic2_current_camera += 1

            
        if current_camera != animatronic2_current_camera:
            time_not_looked += clock.get_time()
        

    #animatronic 2 attack logic
        if time_not_looked >= 20000:  # Check if the animatronic can attack
            if not run_sound_playing:
                blink_screen(screen, 0)
                run_sound.play()
                run_sound_playing = True
            animatronic2_current_camera = 2

            door_open = not door_states["left"]

            if door_open:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - animatronic2_at_door_time >= 5000:  
                    screen.fill((0, 0, 0))
                    screen.blit(jumpscare_image, (0, 0))  
                    jumpscare_sound.play()  
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False  
            else:
                if animatronic2_at_door_time == 0:  
                    animatronic2_at_door_time = pygame.time.get_ticks()
                
                current_time = pygame.time.get_ticks()
                if current_time - animatronic2_at_door_time >= 9000:  
                    if not door_bang_sound_playing:
                        door_bang_sound.play()
                        door_bang_sound_playing = True
                        global_power -= door_bang_power
                        blink_screen(screen, 0)
                        
                
                    time_not_looked = 0  # Reset time not looked only after the full 8 seconds
                    animatronic2_current_camera = 0
                    animatronic2_at_door_time = 0
                    run_sound_playing = False
                    door_bang_sound_playing = False
                    print("ani 2 reset")
        else:
            run_sound_playing = False             
            door_bang_sound_playing = False 
            animatronic2_at_door_time = 0             

        #ANIMATRONIC 3 MOVEMENT
        if animatronic3_current_camera == 0:
            if camera_open_count >= 10:
                animatronic3_current_camera = 1
                camera_open_count = 0
                if not vent_enter_sound_played:
                    vent_enter_sound.play()
                    vent_enter_sound_played = True
                ani3_last_move_time = pygame.time.get_ticks()
        else:
            vent_enter_sound_played = False

        # Animatronic 3 movement logic
        if animatronic3_current_camera in [1, 2, 3]:
            if not vent_flashing:
                if pygame.time.get_ticks() - ani3_last_move_time >= 5000:  # Move every 5 seconds
                    animatronic3_current_camera += 1
                    ani3_last_move_time = pygame.time.get_ticks()
        else:
            ani3_last_move_time = pygame.time.get_ticks()

        if animatronic3_current_camera > 3:  #Jumpscare if animatronic3_current_camera is greater than index 3
            screen.fill((0, 0, 0))
            screen.blit(jumpscare_image, (0, 0))
            jumpscare_sound.play()
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
            print("died by animatronic 3")

        # Flashing logic for Animatronic 3
        if vent_flashing:
            if animatronic3_current_camera in [1, 2, 3]:            
                ani3_flash_time += clock.get_time()
                if ani3_flash_time >= 6000:  # Reset animatronic 3 if flashed for 8 seconds
                    blink_screen(screen, 0)
                    animatronic3_current_camera = 0
                    ani3_flash_time = 0
                    ani3_last_move_time = pygame.time.get_ticks()
            else:
                current_vent_image = vents[pygame.K_f]
        else:
            ani3_flash_time = 0  # Reset flash time if not flashing                                                                                 

        #RENDERING SECTION FOR IMAGE RENDERING IF RENDERING WITH IMAGES - - - - - - - -- - - - - -- - - - - -- - - - - - - -- - - - - - -- - - - - - -

        screen.fill((0, 0, 0))  #Fill the screen with black to clear the previous frame

        if current_image:  # Draws the current image on the screen
            screen.blit(current_image, (0, 0))
        else:
            screen.blit(security_image, (0, 0))  # If no image, draw security room

        if vent_open and current_vent_image:
            screen.blit(current_vent_image, (0, 0))

        # Don't draw animatronic when showing the security room
        if current_image != security_image and not vent_open:
            if animatronic1_current_camera < len(animatronic1_camera_sequence):
                animatronic1_camera_key = animatronic1_camera_sequence[animatronic1_current_camera]
                if current_camera == animatronic1_camera_key:
                    animatronic_image = animatronic_images.get(animatronic1_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic2_current_camera < len(animatronic2_camera_sequence):
                animatronic2_camera_key = animatronic2_camera_sequence[animatronic2_current_camera]
                if current_camera == animatronic2_camera_key:
                    animatronic_image = animatronic_images.get(animatronic2_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

            if animatronic3_current_camera < len(animatronic3_camera_sequence):
                animatronic3_camera_key = animatronic3_camera_sequence[animatronic3_current_camera]
                if current_camera == animatronic3_camera_key:
                    animatronic_image = animatronic_images.get(animatronic3_camera_key)
                    if animatronic_image:
                        screen.blit(animatronic_image, (0, 0))  # Draw the animatronic image as the whole camera view

        # Flashing logic for Animatronic 3 in vents
        if vent_flashing:
            if animatronic3_current_camera == 1 and ani3_vent1_image:
                screen.blit(ani3_vent1_image, (0, 0))
            elif animatronic3_current_camera == 2 and ani3_vent2_image:
                screen.blit(ani3_vent2_image, (0, 0))
            elif animatronic3_current_camera == 3 and ani3_vent3_image:
                screen.blit(ani3_vent3_image, (0, 0))
        else:
        # If not flashing, show the default vent image
            if vent_open:
                current_vent_image = vents[pygame.K_s]  # Default to VENT0
                screen.blit(current_vent_image, (0, 0))  # Show VENT0

        # Draw door images at the bottom corners
        if current_image == security_image:
            if door_states["left"]:
                screen.blit(doors[pygame.K_a], (0, HEIGHT - doors[pygame.K_a].get_height()))  # draw left door at bottom left
            if door_states["right"]:
                screen.blit(doors[pygame.K_d], (WIDTH - doors[pygame.K_d].get_width(), HEIGHT - doors[pygame.K_d].get_height()))  # Draw right door at bottom right
        
        power_percent = int(global_power)                       # POWER DISPLAY
        power_text = f"POWER: {power_percent}%"
        render_outlined_text(
            screen,
            power_text,
            font,
            10,  # X position 
            HEIGHT - font_size - 10,  # Yposition
            (255, 255, 255),  # white interior
            (0, 0, 0),  # black outline
            2,  # outline thickness
        )
        #print(time_remaining)#------------------------------------------------------------------------------------------------------------ENABLE THIS COMMENT TO SEE TIME REMAINING IN MILISECONDS---------
        # Format the clock and render it
        formatted_time = format_game_time(time_remaining)  # Get formatted time string using time_remaining
        render_outlined_text(
            screen,
            formatted_time,
            font,
            WIDTH - 150,  # X position
            10,  # Y position
            (255, 255, 255),  #white text
            (0, 0, 0),  #black outline
            2,  # outline thickness
        )

        if time_remaining == 0:
            render_outlined_text(
                screen,
                "YOU WIN!",
                font,
                WIDTH // 2 - 80,  #X position 
                HEIGHT // 2 - 50,  #Y position
                (0, 255, 0),  #geen text
                (0, 0, 0),  #black outline
                2,  #outline thickness
            )

        pygame.display.flip()  #update display for new frame

        clock.tick(30)  # 30 fps limiter

    # Quit Pygame
    pygame.quit()