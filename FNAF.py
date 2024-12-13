import pygame
import os


pygame.init()

pygame.mixer.init()

current_dir = os.path.dirname(__file__)
# Get the absolute path of the MP3 file
mp3_file = "FNAF GAME/AMBIENCE.mp3"
# Load and play the MP3 file
pygame.mixer.music.load(mp3_file)
pygame.mixer.music.play(-1, 0.0)  # -1 means loop indefinitely, 0.0 means start from the beginning

pygame.time.wait(1050)

WIDTH, HEIGHT = 1280, 720       # SCREEN RESOLUTION using 720p for simplicity's sake
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FNAF Camera System Test")

# load sound effects
door_sound = pygame.mixer.Sound("FNAF GAME/door slam.mp3")
camera_sound = pygame.mixer.Sound("FNAF GAME/camera open.mp3")
camera_switch_sound = pygame.mixer.Sound("FNAF GAME/camera switch.mp3")

# load images
images = {}
image_paths = {
    pygame.K_1: "FNAF GAME/IMAGES/CAM1.png",
    pygame.K_2: "FNAF GAME/IMAGES/CAM2.png",
    pygame.K_3: "FNAF GAME/IMAGES/CAM3.png",
}
security_image_path = "FNAF GAME/IMAGES/SECURITY ROOM.png"

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

# Main loop - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
running = True
clock = pygame.time.Clock()

while running:
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
    if door_states["left"] != previous_door_states["left"]:
        door_sound.play()  # Play left door sound
        previous_door_states["left"] = door_states["left"]  # Update previous state

    if door_states["right"] != previous_door_states["right"]:
        door_sound.play()  # Play right door sound
        previous_door_states["right"] = door_states["right"]  # Update previous state

    screen.fill((0, 0, 0))  # Fill the screen with black to clear the previous frame

    if current_image:  # Draws the current image on the screen
        screen.blit(current_image, (0, 0))
    else:
        screen.blit(security_image, (0, 0))  # If no image, draw security room

    # Draw door images at the bottom corners
    if current_image == security_image:
        if door_states["left"]:
            screen.blit(doors[pygame.K_a], (0, HEIGHT - doors[pygame.K_a].get_height()))  # Draw left door at bottom left
        if door_states["right"]:
            screen.blit(doors[pygame.K_d], (WIDTH - doors[pygame.K_d].get_width(), HEIGHT - doors[pygame.K_d].get_height()))  # Draw right door at bottom right

    pygame.display.flip()  # Updates display for new frame

    clock.tick(30)  # 30 fps limiter

# Quit Pygame
pygame.quit()