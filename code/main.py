import pygame
import random
from os.path import join
class player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load(join("images", "player.png")).convert_alpha()
        self.image=pygame.transform.scale(self.image, (100, 100))  # Scale the player image to 100x100 pixels
        self.rect=self.image.get_frect(center=(window_width/2, window_height/2))
        self.player_direction = pygame.math.Vector2()
        self.player_speed =300 #player speed
        ##cooldown timer
        self.can_shoot = True  # Flag to track if the player can shoot
        self.laser_shoot_time = 0  # Time when the last laser was shot
        self.cooldown_duration = 200  # Cooldown duration 
          
        
    def laser_timer(self):
        if not self.can_shoot:  # Check if the player cannot shoot
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:  # Check if the cooldown duration has passed
                self.can_shoot = True  # Allow the player to shoot again
               
    def update(self,dt):
        keys = pygame.key.get_pressed() # Get the state of all keyboard keys
        self.player_direction.x = int(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) # Set the x-direction based on left/right arrow keys
        self.player_direction.y = int(keys[pygame.K_DOWN] - keys[pygame.K_UP]) # Set y-direction based on up/down arrow keys
        self.player_direction = self.player_direction.normalize() if self.player_direction else self.player_direction
        self.rect.center += self.player_direction * self.player_speed * dt
        
        recent_keys = pygame.key.get_pressed()  # Get the state of all keyboard keys
        if recent_keys[pygame.K_SPACE] and self.can_shoot:  # Check if the spacebar is pressed
            laser(laser_surf,self.rect.midtop, (all_sprites,laser_sprites))  # Create a new laser instance
            self.can_shoot = False  # Set the can_shoot flag to False to prevent rapid firing
            self.laser_shoot_time = pygame.time.get_ticks()  # Update the last shoot time
         
        self.laser_timer()  # Call the laser_timer method to handle cooldown logic
class star(pygame.sprite.Sprite):
    def __init__(self,groups, surf): 
        super().__init__(groups)  #dunder init
        self.image=surf
        self.rect=self.image.get_frect(center=(random.randint(0, window_width), random.randint(0, window_height)))
        
class laser(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(center=pos)
    def update(self,dt):
        self.rect.centery-=300*dt
        if self.rect.bottom<0:
            self.kill()  # Remove the laser sprite from all groups when it goes off-screen
class meteor(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(center=pos)
        self.spawn_time = pygame.time.get_ticks()  # Get the current time in milliseconds
        self.lifetime = 4000  # Set the lifetime of the meteor in milliseconds (2 seconds)
        self.direction = pygame.math.Vector2(random.uniform(-0.5, 0.5), 1) # Random direction for the meteor
        self.speed = random.randint(100, 300)  # Random speed for the meteor
    def update(self,dt):
        self.rect.center += self.direction * self.speed * dt
        current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
        if current_time - self.spawn_time >= self.lifetime:  # Check if the meteor's lifetime has expired
            self.kill()  # Remove the meteor sprite from all groups
            
def collisions():
    global running
    collisions_sprites = pygame.sprite.spritecollide(player,meteor_sprites, True)  # Check for collisions between meteors and other sprites
    if collisions_sprites:
        running = False  # Stop the game if a collision occurs
          
    for laser_sprite in laser_sprites:
              collided_sprites= pygame.sprite.spritecollide(laser_sprite, meteor_sprites, True)  # Check for collisions between lasers and meteors
              if collided_sprites:
                  laser_sprite.kill()  # Remove the laser sprite from all groups when a collision occurs
        
def display_score():
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds
    text_surface = font.render(str(current_time//1000), True, 'yellow')  # Render the score text
    text_rect = text_surface.get_rect(midbottom=(window_width/2, window_height-0))  # Get the rectangle for positioning the score text
    screen.blit(text_surface, text_rect)
#general setup
pygame.init()
window_width, window_height = 1280 ,720
screen =pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("space shooter")
running = True

#to manage frame rate 
clock=pygame.time.Clock()

#import
star_surf=pygame.image.load(join("images", "star.png")).convert_alpha()# Load the star image
star_surf=pygame.transform.scale(star_surf, (200, 200))  # Scale the star image to 20x20 pixels
meteor_surf=pygame.image.load(join("images", "meteor.png")).convert_alpha() # Load the meteor image
laser_surf=pygame.image.load(join("images", "laser.png")).convert_alpha()
font=pygame.font.Font(join("images", "Oxanium-Bold.ttf"), 20)  # Create a font object for rendering text
text_surface=font.render('hi niche',True,'white')  # Render the text "text" in red color
#sprites 
all_sprites=pygame.sprite.Group() # Create a group to hold all sprites
meteor_sprites=pygame.sprite.Group() # Create a group to hold meteor sprites
laser_sprites=pygame.sprite.Group() # Create a group to hold laser sprites
for i in range(20):  # Create 20 star instances
    star(all_sprites, star_surf) 
player=player(all_sprites) 


#custom events- meteor event
meteor_event=pygame.event.custom_type()  # Create a custom event type for meteor spawning
pygame.time.set_timer(meteor_event,  500)  # Set a timer to trigger '

while running:
    dt=clock.tick(120)/1000  # print(dt)#to see the actual delta time from actual movement
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type== meteor_event:
            x ,y=random.randint(0, window_width), random.randint(-200,-100)  # Generate random x and y coordinates for the meteor
            meteor(meteor_surf, (x,y), (all_sprites, meteor_sprites))  # Create a new meteor instance at the specified position
            
    #update sprites   
    all_sprites.update(dt)  # Update all sprites in the group
    collisions()  # Check for collisions between sprites
    
        
        
    #draw
    screen.fill("black") # Fill the screen with dark gray color
    all_sprites.draw(screen)  # Draw all sprites in the group onto the screen
    
    display_score()  # Display the score on the screen
    pygame.display.update() #flip is used to update a specific portion of the screen, while update is used to update the entire screen
pygame.quit(  )   