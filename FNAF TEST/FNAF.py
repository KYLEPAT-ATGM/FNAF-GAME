import pygame
import os
import random
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

current_dir = os.path.dirname(__file__)
# Get the absolute path of the MP3 file
mp3_file = "FNAF GAME/AMBIENCE.mp3"
# Load and play the MP3 file
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.play(-1, 0.0)  # -1 means loop indefinitely, 0.0 means start from the beginning

pygame.time.wait(1050)

WIDTH, HEIGHT = 1920, 1080      # SCREEN RESOLUTION using 1080p for simplicity's sake
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FNAF Camera System Test")

font_size = 36  # You can adjust the size as needed
font = pygame.font.Font(None, font_size)

# load sound effects
door_sound = pygame.mixer.Sound("FNAF GAME/door slam.mp3")
camera_sound = pygame.mixer.Sound("FNAF GAME/camera open.mp3")
camera_switch_sound = pygame.mixer.Sound("FNAF GAME/camera switch.mp3")
jumpscare_sound = pygame.mixer.Sound("FNAF GAME/jumpscare sound.mp3")
power_out_sound = pygame.mixer.Sound("FNAF GAME/power out.mp3")
power_out_music = pygame.mixer.Sound("FNAF GAME/power out music.mp3")

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
security_image_path = "FNAF GAME/IMAGES/SECURITY ROOM.png"
jumpscare_image_path = "FNAF GAME/IMAGES/JUMPSCARE.png"

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

if os.path.exists(jumpscare_image_path): #load security room then from the path (essentially locates it before it loads)
    jumpscare_image = pygame.image.load(jumpscare_image_path)
else:
    print(f"file not found: {jumpscare_image_path}")
    jumpscare_image = None # sets to no image if cant find

for door, path in security_door_paths.items(): # Load images from file paths and store them in the 'doors'
    if os.path.exists(path):
        doors[door] = pygame.image.load(path)   #load image from file path based on
    else:
        print(f"file not found: {path}")

current_image = security_image  # states beginning image that was loaded

camera_open = False  #tracks whether the camera is open
current_camera = None #tracks the current camera

door_states = {  # Tracks the state of each door (True for closed, False for open)
    "left": False,
    "right": False,
}
previous_door_states = {
    "left": False,
    "right": False,
}

                                                                                                                # Animatronic 1 movement variables (RNG ONE)(you can change chance here)
animatronic1_camera_sequence = [pygame.K_5, pygame.K_6, pygame.K_2]  # Cameras the animatronic moves through
animatronic1_current_camera = 0  # Start at the first camera
animatronic1_probability = 0.01  # Initial chance to move
animatronic1_probability_increment = 0.01  # Increment per second

animatronic1_image_path = "FNAF GAME/IMAGES/ANIMATRONIC1.png"
if os.path.exists(animatronic1_image_path):
    animatronic1_image = pygame.image.load(animatronic1_image_path)
else:
    print(f"file not found: {animatronic1_image_path}")
    animatronic1_image = None

animatronic1_at_door_time = 0  #track time if animatronic1 is at door
animatronic1_reset_time = 0    #track time until animatronic disappear

def render_outlined_text(surface, text, font, x, y, text_color, outline_color, outline_thickness=2):        #I FOUND THIS ONLINE BUT IT WORKS SO IM NOT COMPLAINING
    """Renders text with an outline at the given position."""
    for dx in range(-outline_thickness, outline_thickness + 1): # Render the outline
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:  # skip the center (original position)
                outline_surface = font.render(text, True, outline_color)
                surface.blit(outline_surface, (x + dx, y + dy))
   
    text_surface = font.render(text, True, text_color)   # Render the actual text
    surface.blit(text_surface, (x, y))



# Main loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
running = True
clock = pygame.time.Clock()
frame_counterANI1 = 0 #add more if more animatronics based on frame count
global_power = 101      
idle_power = 0.00366666667     
camera_power = 0.008                                            #WORK ON GLOBAL POWER HERE
door_power = 0.01
both_doors_power = 0.115


while running:
    frame_counterANI1 += 1
    global_power -= idle_power
    current_time1 = pygame.time.get_ticks()
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

    if global_power <= 0:                       #POWER OUT 
        pygame.mixer.music.stop()
        camera_open = False
        current_camera = security_image
        door_states["left"] = False
        door_states["right"] = False
        """
        power_out_sound.play()      #PLAY FOR 10 SECONDS
        power_out_music.play()      #PLAY FOR 13 SECONDS
        """
        screen.fill((0, 0, 0))
        screen.blit(jumpscare_image, (0, 0))
        jumpscare_sound.play()
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Stop the game if the user closes the window
            running = False

        if event.type == pygame.KEYDOWN:     # USE THIS FOR CAMERA NUMBER INPUTS FROM KEYBOARD
            if event.key in images and camera_open: #check if a key is same as camera num
                current_image = images[event.key]   #update the current camera to the user inputted key
                current_camera = event.key  #update the current camera to the user inputted key
                camera_switch_sound.play()
            if event.key == pygame.K_SPACE:
                camera_sound.play()
                if camera_open: #if the camera is open
                    current_image = security_image  # IF the camera is open, close it and display the security image
                    camera_open = False #set camera state closed
                else:
                    current_image = images[pygame.K_1]  #open the camera, display the first camera image always
                    current_camera = pygame.K_1
                    camera_open = True  #set camera state open
            if current_image == security_image:
                #toggle left door                                                           DOOOOOORRRSSS PLEASE FIX
                if event.key == pygame.K_a:
                    door_states["left"] = not door_states["left"]
                
                #toggle right door
                if event.key == pygame.K_d:
                    door_states["right"] = not door_states["right"]

    
    # Play door sound if the door state has changed
    if door_states["left"] != previous_door_states["left"]:  #checks if the change was from true to false or false to true
        door_sound.play()  # Play left door sound
        previous_door_states["left"] = door_states["left"]  # Update previous state

    if door_states["right"] != previous_door_states["right"]:
        door_sound.play()  # Play right door sound
        previous_door_states["right"] = door_states["right"]  # Update previous state

    # Animatronic movement logic
    
    if frame_counterANI1 >= 30:  # Check every 30 frames (about once per second at 30 FPS)
        frame_counterANI1 = 0
        if random.random() < animatronic1_probability:  # Animatronic decides to move
            animatronic1_probability = 0.01  # Reset probability after movement
            animatronic1_current_camera += 1
        else:
            animatronic1_probability += animatronic1_probability_increment

     # Check animatronic at camera 2 (door camera)
    if animatronic1_current_camera == 2:
        if animatronic1_at_door_time == 0:
            animatronic1_at_door_time = current_time1

        door_open = not door_states["right"]

        if door_open and current_time1 - animatronic1_at_door_time >= 5000: #s how jumpscare image if longer 5 second
            pygame.mixer.music.stop()
            screen.fill((0, 0, 0))
            screen.blit(jumpscare_image, (0, 0))
            jumpscare_sound.play()
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

        elif not door_open:
            if animatronic1_reset_time == 0:
                animatronic1_reset_time = current_time1

            if current_time1 - animatronic1_reset_time >= 10000:
                animatronic1_current_camera = 0
                animatronic1_at_door_time = 0
                animatronic1_reset_time = 0
    else:
        animatronic1_at_door_time = 0
        animatronic1_reset_time = 0

    screen.fill((0, 0, 0))  # Fill the screen with black to clear the previous frame

    if current_image:  # Draws the current image on the screen
        screen.blit(current_image, (0, 0))
    else:
        screen.blit(security_image, (0, 0))  # If no image, draw security room

    # Don't draw animatronic when showing the security room
    if current_image != security_image:
        if animatronic1_current_camera < len(animatronic1_camera_sequence):
            animatronic1_camera_key = animatronic1_camera_sequence[animatronic1_current_camera]
            if current_camera == animatronic1_camera_key and animatronic1_image:
                screen.blit(animatronic1_image, (WIDTH // 2 - animatronic1_image.get_width() // 2, HEIGHT // 2 - animatronic1_image.get_height() // 2))

    # Draw door images at the bottom corners
    if current_image == security_image:
        if door_states["left"]:
            screen.blit(doors[pygame.K_a], (0, HEIGHT - doors[pygame.K_a].get_height()))  # Draw left door at bottom left
        if door_states["right"]:
            screen.blit(doors[pygame.K_d], (WIDTH - doors[pygame.K_d].get_width(), HEIGHT - doors[pygame.K_d].get_height()))  # Draw right door at bottom right
    
    power_percent = int(global_power)
    power_text = f"POWER: {power_percent}%"
    render_outlined_text(
        screen,
        power_text,
        font,
        10,  # X position (left margin)
        HEIGHT - font_size - 10,  # Y position (bottom margin)
        (255, 255, 255),  # White interior
        (0, 0, 0),  # Black outline
        2,  # Outline thickness
    )

    pygame.display.flip()  # Updates display for new frame

    clock.tick(30)  # 30 fps limiter

# Quit Pygame
pygame.quit()
