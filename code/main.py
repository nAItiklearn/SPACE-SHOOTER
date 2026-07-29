# import pygame
# import random
# from os.path import join

# #general setup
# pygame.init()
# window_width, window_height = 1280 ,720
# screen =pygame.display.set_mode((window_width, window_height))
# pygame.display.set_caption("space shooter")
# running = True

# #to manage frame rate 
# clock=pygame.time.Clock()

# #surface
# surf = pygame.Surface((100, 200))
# surf.fill("black")  # Fill surface so it's visible against the dark background
# x=100 

# #importing images
# player_surf=pygame.image.load(join("images", "player.png")).convert_alpha() # Load the player image and convert it for better performance
# player_rect = player_surf.get_frect(center=(window_width/2, window_height/2))

# player_direction= pygame.math.Vector2(20,-10) #direction vector for the player
# player_speed=100 #player spee)

# star_surf=pygame.image.load(join("images", "star.png")).convert_alpha() # Load the star 

# meteor_surf=pygame.image.load(join("images", "meteor.png")).convert_alpha() # Load the meteor image
# meteor_rect=meteor_surf.get_frect(center=(window_width/2, window_height/2))

# laser_surf=pygame.image.load(join("images", "laser.png")).convert_alpha()
# laser_rect=laser_surf.get_frect(bottomleft=(20,window_height-20))
                                
# # Generate 20 random star positions before the game loop
# star_positions = [(random.randint(0, window_width), random.randint(0, window_height)) for _ in range(20)]   #THIS IS USED WHEN U DONT HAVE TO MOVE THE STARS

# while running:
#     dt=clock.tick(120)/1000
#     print(dt)#to see the actual delta time from actual movement
#     #event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#     #draw the game
#     screen.fill("darkgray") # Fill the screen with dark gray color
    
    
    
#     # Draw all 20 stars
#     for pos in star_positions:
#         screen.blit(star_surf, pos)  # Draw each star at its random position
        
    
#     #player movement
#     if player_rect.bottom>window_height or player_rect.top<0:
#         player_direction.y *= -1
#     if player_rect.right>window_width or player_rect.left<0:
#       player_direction.x *=-1
        
#     player_rect.center += player_direction*player_speed*dt
#     screen.blit(player_surf,player_rect.topleft)
    
#     screen.blit(meteor_surf, meteor_rect)
#     screen.blit(laser_surf,laser_rect)

    
   
    
   
#     pygame.display.update() 
#     #flip is used to update a specific portion of the screen, while update is used to update the entire screen
# pygame.quit(  )   