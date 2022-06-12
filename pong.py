import pygame
from random import randint
import os
import time

pygame.init()

win_size = (800,800)

BLACK = (0,0,0)
WHITE = (255,255,255)

carryOn = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("Pong")
 
class paddle:
    def __init__(self, x):
        self.speed = 10
        self.y = 250
        self.x = x
        self.w = 15
        self.h = 100
    def reset(self):
        self.y = 250
    def move_up(self):
        if self.y >= 50:
            self.y -= self.speed
    def move_down(self):
        if self.y <= 550:
            self.y += self.speed
    def drawpaddle(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.w, self.h))

class ball:
    def __init__(self):
        self.speed = 10
        self.x = 400
        self.y = 250
        self.velocity = [randint(4,8),randint(-8,8)]

    def update(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    def drawball(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 3)


right_paddle = paddle(700)
left_paddle = paddle(100)
game_ball = ball()


while carryOn:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
            right_paddle.move_down()
    if keys[pygame.K_UP]:
            right_paddle.move_up()
    if keys[pygame.K_w]:
            left_paddle.move_up()
    if keys[pygame.K_s]:
            left_paddle.move_down()
    screen.fill(BLACK)

    if game_ball.x>=600:
        game_ball.velocity[0] = -game_ball.velocity[0]
    if game_ball.x<=0:
        game_ball.velocity[0] = -game_ball.velocity[0]
    if game_ball.y>490:
        game_ball.velocity[1] = -game_ball.velocity[1]
    if game_ball.y<0:
        game_ball.velocity[1] = -game_ball.velocity[1] 

    game_ball.update()
    game_ball.drawball()
    right_paddle.drawpaddle()
    left_paddle.drawpaddle()

    pygame.display.flip()
    clock.tick(60)







