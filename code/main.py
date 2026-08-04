import pygame
import random
from os.path import join
class player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect=self.image.get_frect(center=(window_width/2, window_height/2))
        self.player_direction = pygame.math.Vector2()
        self.player_speed = 300 #player speed
        
    def update(self,dt):
        keys = pygame.key.get_pressed() # Get the state of all keyboard keys
        self.player_direction.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) # Set the x-direction based on left/right arrow keys
        self.player_direction.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP]) # Set y-direction based on up/down arrow keys
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center += self.player_direction * self.player_speed * dt
        
        recent_keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
        if recent_keys[pygame.K_SPACE]:  # Check if the spacebar is pressed
            print("spacebar pressed")  # Print a message to the console when the spacebar is pressed
class star(pygame.sprite.Sprite):
    def __init__(self,groups, surf): 
        super().__init__(groups)  #dunder init
        self.image=surf
        self.rect=self.image.get_frect(center=(random.randint(0, window_width), random.randint(0, window_height)))
        
#general setup
pygame.init()
window_width, window_height = 1280 ,720
screen =pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("space shooter")
running = True

#to manage frame rate 
clock=pygame.time.Clock()

#surface-stores pixels and can be drawn on the screen
all_sprites=pygame.sprite.Group() # Create a group to hold all sprites
star_surf=pygame.image.load(join("images", "star.png")).convert_alpha()  # Load the star image
for i in range(20):  # Create 20 star instances
    star(all_sprites, star_surf) 
player=player(all_sprites) 

meteor_surf=pygame.image.load(join("images", "meteor.png")).convert_alpha() # Load the meteor image
meteor_rect=meteor_surf.get_frect(center=(window_width/2, window_height/2))

laser_surf=pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect=laser_surf.get_frect(bottomleft=(20,window_height-20))
                                
while running:
    dt=clock.tick(120)/1000  # print(dt)#to see the actual delta time from actual movement
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    all_sprites.update(dt)  # Update all sprites in the group
    
    #draw the game
    screen.fill("darkgray") # Fill the screen with dark gray color
    
    # Draw all 20 stars
    # for pos in star_positions:
    #     screen.blit(star_surf, pos)  # Draw each star at its random position
        
    
    all_sprites.draw(screen)  # Draw all sprites in the group onto the screen
    pygame.display.update() #flip is used to update a specific portion of the screen, while update is used to update the entire screen
pygame.quit(  )   