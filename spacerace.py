###Imports
import pygame
import pygame.freetype
import random
import sys

#Pygame Init
pygame.init()
pygame.freetype.init
font = pygame.freetype.SysFont("Comic Sans MS", 50)
win_size = (600,800)
black = (0,0,0)
white = (255,255,255)
carryOn = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Space Race")

#Ship class
class ship:
    def __init__(self, x):
        self.speed = 2
        self.y = 750
        self.x = x
        self.r = 8
        self.score = 0
    def reset(self):
        self.y = 750
    def move_up(self):
        if self.y >= 50:
            self.y -= self.speed
    def move_down(self):
        if self.y <= 750:
            self.y += self.speed
    def check_win(self):
        if self.y >= 50:
            return True
    def draw_ship(self):
        pygame.draw.circle(screen, white, (self.x, self.y), self.r)

#Middle timer class
class timer:
    def __init__(self, win_size):
        self.screen_y = win_size[1]
        self.screen_x = win_size[0]
        self.tot_time = 120
        self.w = 15
        self.x = self.screen_x/2 - self.w/2
        self.y = 0
        self.h = self.screen_y
    def move_down(self):
        if self.y <= (self.screen_y):
            self.y += self.screen_y/(self.tot_time * 60)
    def draw(self):
        pygame.draw.rect(screen, white, (self.x, (self.y), self.w, self.h))


#Score board class
class score_board:
    def __init__(self, p1_score, p2_score):
        self.p1 = p1_score
        self.p2 = p2_score
    def score_update(self, p1_score, p2_score):
        self.p1 = p1_score
        self.p2 = p2_score
    def draw(self):
        pygame.draw.rect(screen, white, (200, 700, 200, 100))
        pygame.draw.rect(screen, black, (210, 710, 180, 90))
        font.render_to(screen, (240, 750), str(self.p1), white)
        font.render_to(screen, (340, 750), str(self.p2), white)

#Aestropid class
class astro:
    def __init__(self):
        self.dir = (random.randrange(1,3))
        if self.dir == 1:
            self.x = 50
        elif self.dir == 2:
            self.x = 550
        self.y = random.randrange(75 ,600)
        self.speed = 2
        self.r = 5
    def move(self):
        if self.dir == 1:
            self.x += self.speed
        elif self.dir == 2:
            self.x -= self.speed
    def draw(self):
        pygame.draw.circle(screen, white, (self.x, self.y), self.r)

#Game logic
def main():
    
    #define one pesky var
    astro_timer = 0
    astro_list = []

    #object creation
    right_ship = ship(450)
    left_ship = ship(150)
    game_timer = timer(win_size)
    score = score_board(left_ship.score, right_ship.score)

    #main loop
    while carryOn:



        #Keypresses
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
                right_ship.move_down()
        if keys[pygame.K_UP]:
                right_ship.move_up()
        if keys[pygame.K_w]:
                left_ship.move_up()
        if keys[pygame.K_s]:
                left_ship.move_down()
    
        #Main game logic
        screen.fill(black)
        game_timer.move_down()
        if right_ship.y == 50:
            right_ship.reset()
            right_ship.score += 1
        if left_ship.y == 50:
            left_ship.reset()
            left_ship.score += 1
        score.score_update(left_ship.score, right_ship.score)
        game_timer.move_down()
        
        #End of game sequence
        if game_timer.y >= 799:
            winner = ""
            if left_ship.score > right_ship.score:
                winner = "P1 wins!"
            elif right_ship.score > left_ship.score:
                winner = "P2 wins!"
            else:
                winner = "Draw!"
            while True:
                font.render_to(screen, (175, 300), winner + " " + str(left_ship.score) + ":" + str(right_ship.score), white)
                font.render_to(screen, (100, 400), "press D to play again", white)
                pygame.display.flip()
                clock.tick(60)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d]:
                    main()
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit()

        #Aestroid spawning logic
        astro_timer += 1
        if astro_timer % 6 == 0:
            astro_list.append(astro())
            astro_list.append(astro())
            astro_list.append(astro())



        #Astro logic
        for i in astro_list:
            i.move()
            if i.x >= 700 == 1:
                astro_list.pop(astro_list.index(i))
            elif i.x <= 0 and i.dir == 2:
                astro_list.pop(astro_list.index(i))
        
        #Collision detection
        for astro_col in astro_list:
            diff_y = astro_col.y - left_ship.y
            diff_x = astro_col.x - left_ship.x
            if abs(diff_y) < 20:
                if abs(diff_x) < 20:
                    left_ship.reset()
            diff_y2 = astro_col.y - right_ship.y
            diff_x2 = astro_col.x - right_ship.x
            if abs(diff_y2) < 20:
                if abs(diff_x2) < 20:
                    right_ship.reset()

        #Drawings
        right_ship.draw_ship()
        left_ship.draw_ship()
        score.draw()
        game_timer.draw()
        for astros in astro_list:
            astros.draw()
        #Pygame ending init
        pygame.display.flip()
        clock.tick(60)

main()

pygame.quit()
sys.exit()
