# Pong - playing Pong in Python and Pygame, to learn both. I'll finish it some day...
# Pong © 2021 by George Moore is licensed under Attribution-NonCommercial-ShareAlike 4.0 International

import pygame
import os

COURT_WIDTH = 1200
COURT_HEIGHT = 800
COURT_WALL_COLOUR = pygame.Color("white")
COURT_WALL_THICKNESS = 20

GAME_WIDTH  = COURT_WIDTH
GAME_HEIGHT = COURT_HEIGHT
GAME_BG_COLOUR = pygame.Color("black")
GAME_FRAMERATE = 400

PADDLE_LENGTH = 100
PADDLE_WIDTH = 10
PADDLE_COLOUR = pygame.Color("white")
PADDLE_START_Y = COURT_HEIGHT//2-PADDLE_LENGTH//2

BALL_COLOUR = pygame.Color("white")
BALL_RADIUS = 10
BALL_START_X = COURT_WIDTH-PADDLE_WIDTH-BALL_RADIUS
BALL_START_Y = COURT_HEIGHT//2


# Draws court area 
class Court:
    
    def __init__(self, new_court_width, new_court_height, new_court_thickness, new_court_colour):
        self.__court_width = new_court_width
        self.__court_height = new_court_height
        self.draw_walls(game_screen, new_court_thickness, new_court_colour)

    def draw_walls(self, game_screen, wall_thickness, wall_colour):
        self.__wall_thickness = wall_thickness
        self.__wall_colour = wall_colour
        pygame.draw.rect(game_screen, wall_colour, pygame.Rect(0,0,self.__court_width,self.__wall_thickness))
        pygame.draw.rect(game_screen, wall_colour, pygame.Rect(0,0,self.__wall_thickness,self.__court_height))
        pygame.draw.rect(game_screen, wall_colour, pygame.Rect(0,self.__court_height-self.__wall_thickness,self.__court_width,self.__court_height))

    def get_width(self):
        return self.__court_width

    def get_height(self):
        return self.__court_height

class Paddle:

    def __init__(self, new_paddle_length, new_paddle_width, new_paddle_colour, new_paddle_y_position):
        self.__length = new_paddle_length
        self.__width = new_paddle_width
        self.__colour = new_paddle_colour
        self.__y_position = new_paddle_y_position
        # self.update_position()
            
    def __draw(self):
        print ("Drawing: ", self.__y_position)
        pygame.draw.rect(game_screen, self.__colour, pygame.Rect(game_court.get_width()-self.__width, self.__y_position, self.__width, self.__length))

    def update_position(self):
        # Erase Paddle
        self.__colour = GAME_BG_COLOUR
        self.__draw()

        # Move Paddle, if up else down                
        self.__mouse_y_position = pygame.mouse.get_pos()[1]
        if self.__mouse_y_position < self.__y_position:
            self.__y_position -= self.__y_position - self.__mouse_y_position
        elif self.__mouse_y_position > self.__y_position:
            self.__y_position +=  self.__mouse_y_position - self.__y_position

        # Redraw Paddle
        self.__colour = PADDLE_COLOUR
        self.__draw()
        

class Ball:

    def __init__(self, new_ball_colour, new_ball_x_position, new_ball_y_position, new_ball_radius):
        pygame.draw.circle(game_screen, new_ball_colour, (new_ball_x_position, new_ball_y_position), new_ball_radius)

os.system('clear')
print("\n\n\nSTART" )

# Game screen setup
pygame.init()
game_screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
game_screen.fill(GAME_BG_COLOUR)

#Court setup
game_court = Court(COURT_WIDTH, COURT_HEIGHT, COURT_WALL_THICKNESS, COURT_WALL_COLOUR)

#Paddle setup
game_paddle = Paddle(PADDLE_LENGTH, PADDLE_WIDTH, PADDLE_COLOUR, PADDLE_START_Y)

#Ball setup
game_ball = Ball(BALL_COLOUR, BALL_START_X, BALL_START_Y, BALL_RADIUS)

# Game loop
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    # game_clock.tick(GAME_FRAMERATE)
    pygame.display.flip()
    # game_ball.update()
    if e.type == pygame.MOUSEMOTION:
        game_paddle.update_position()
pygame.quit()




# game_ball = Ball(COURT_WIDTH-BALL_RADIUS, COURT_HEIGHT//2-BALL_RADIUS//2, -BALL_VELOCITY, -BALL_VELOCITY)
# game_ball.show(GAME_FG_COLOUR, BALL_RADIUS)

# game_paddle = Paddle()
# game_paddle.show(GAME_FG_COLOUR)

# game_clock = pygame.time.Clock()
# counter = 0


# class Ball:

#     BALL_RADIUS = 10
#     BALL_VELOCITY = 10
    
#     def __init__(self,x,y, vx, vy):
#         self.x = x
#         self.y = y 
#         self.vx = vx
#         self.vy = vy

#     def show (self, ball_colour, ball_radius):
#         global game_screen
#         pygame.draw.circle(game_screen, ball_colour, (self.x, self.y), ball_radius)

#     def update(self):
#         newx = self.x + BALL_VELOCITY
#         newy = self.y + BALL_VELOCITY
#         self.show(GAME_FG_COLOUR, BALL_RADIUS)
        # if newx < COURT_BORDER+self.BALL_RADIUS:
        #     self.vx = -self.vx
        # elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
        #         self.vy = -self.vy
        # else: 
        #     self.show(GAME_BG_COLOUR)
        #     self.x = self.x + self.vx
        #     self.y = self.y + self.vy
        #     self.show(GAME_FG_COLOUR)

# class Paddle:
    
#     PADDLE_LENGTH = 100
#     PADDLE_WIDTH = 10
#     PADDLE_INITIAL_POSITION = COURT_HEIGHT-COURT_HEIGHT//2

#     def __init__(self):
#         self.y = PADDLE_INITIAL_POSITION

#     def show(self, paddle_colour):
#         global game_screen
#         pygame.draw.rect(game_screen, paddle_colour, pygame.Rect(COURT_WIDTH-PADDLE_WIDTH, COURT_HEIGHT//2-PADDLE_LENGTH//2, PADDLE_WIDTH, PADDLE_LENGTH))
    
#     def update(self):
#         self.show(pygame.Color(GAME_BG_COLOUR))
#         self.y = pygame.mouse.get_pos()[1]
#         self.show(pygame.Color(GAME_FG_COLOUR))
