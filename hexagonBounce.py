import pygame
from math import sin, cos, pi
from sys import exit

# Initialize Pygame
pygame.init()

# Initialize Sounds
pygame.mixer.init()

# Defining sounds
s1 = pygame.mixer.Sound("S1.wav")
s2 = pygame.mixer.Sound("S2.wav")
s3 = pygame.mixer.Sound("S3.wav")
s4 = pygame.mixer.Sound("S4.wav")
s5 = pygame.mixer.Sound("S5.wav")
s6 = pygame.mixer.Sound("S6.wav")
s7 = pygame.mixer.Sound("S7.wav")
s8 = pygame.mixer.Sound("S8.wav")
s9 = pygame.mixer.Sound("S9.wav")
s10 = pygame.mixer.Sound("S10.wav")
s11 = pygame.mixer.Sound("S11.wav")
s12 = pygame.mixer.Sound("S12.wav")
s13 = pygame.mixer.Sound("S13.wav")
s14 = pygame.mixer.Sound("S14.wav")
s15 = pygame.mixer.Sound("S15.wav")


# Screen Stuff
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hexagon Animation")


# some variables
width = 3
vertex_count = 6

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

# frame rate
FPS = 60
clock = pygame.time.Clock()


# Hexagon
def draw_regular_polygon(surface, color, vertex_count,
						 radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position

    polygon = pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n),
		 y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)
    return polygon
    

rect = pygame.Rect(screen_width/2,screen_height/2,50,100)
x_cord = screen_width/2 - 60
y_cord = screen_height/2 - 58
size_x = 400
size_y = 400
rect_surf = pygame.Surface((size_x, size_y))
rect_surf.fill((0,0,0))

gradientOfColors = [(20,228,140),(22,226,139),(31,218,167),(33,216,198),(33,216,216),(33,206,216),(33,188,216),(33,170,216),(33,156,216),(33,138,216),(33,124,216),(34,102,215)]

class hexagon:
    
    def __init__(self, rad):
        self.rad = 70


    def animate(self, rad):
        self.markers = [10000]
        rad = 70
        if pygame.time.get_ticks() < self.markers[0]:
            draw_regular_polygon(rect_surf, gradientOfColors[0],6,rad,(70,70),2)
            print("new hexagon drawn")

        

        
        #print("First function is working")
        

    #if pygame.time.get_ticks() > markers[0] and pygame.time.get_ticks() < markers[1]:
        #x = screen_width/2 - p
        #y = screen_height/2 - p
        #draw_regular_polygon(screen, gradientOfColors[0],6,70,(x,y),2)
        #print("second function is working")
        

        

     
        


# bg and fg colors
bg_color = (0, 0, 0)
fg_color = (0, 255, 255)

hex_obj = hexagon(70)
rad = 70

while True:
    screen.fill(bg_color)
    screen.blit(rect_surf,(x_cord, y_cord))
    if x_cord < 700 and (pygame.time.get_ticks() > 300 and pygame.time.get_ticks() < 1400):
        x_cord += 1
        hex_obj.animate(70)
    elif (pygame.time.get_ticks() > 1400 and pygame.time.get_ticks() < 4000):
        x_cord -= 1
        rad = 400
        hex_obj.animate(rad)
    elif (pygame.time.get_ticks() > 4000 and pygame.time.get_ticks() < 7000):
        x_cord += 1

    print(x_cord)
    print(pygame.time.get_ticks())
    print(rad)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    draw_regular_polygon(screen, gradientOfColors[0], vertex_count,
                         min(1.5 * screen_width, 1.5 * screen_height) / 6, (screen_width / 2,screen_height / 2),
						 width)
    
    

    
    clock.tick(60)
    pygame.display.flip()
    
