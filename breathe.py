import pygame
from sys import exit
pygame.init()
def decrease():
    radius=92
    for i in range(82,1,-1):
        radius-=1
        pygame.time.delay(40)
        pygame.draw.circle(screen,lpink,(400,300),120)
        pygame.draw.circle(screen,'Pink',(400,300),100,10)
        pygame.draw.circle(screen,'White',(400,300),radius)
        pygame.display.update()
        clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
def increase():
    radius=10
    for i in range(1,82):
        radius+=1
        pygame.time.delay(40)
        pygame.draw.circle(screen,'White',(400,300),radius)
        pygame.display.update()
        clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    decrease()
screen_width,screen_height=800,600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Breathing Animation")
lpink=(242,153,241)
running=True
clock=pygame.time.Clock()
while True:
    screen.fill('Black')
    pygame.draw.circle(screen,lpink,(400,300),120)
    pygame.draw.circle(screen,'Pink',(400,300),100,10)
    increase()
