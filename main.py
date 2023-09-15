import pygame
import sys

pygame.init()
窗口大小=宽,高=640,480
窗口=pygame.display.set_mode(窗口大小)
白色="#FFFFFF"
黑色="#000000"
人=pygame.image.load("图/doctor.png")
球=pygame.transform.scale(人,(150,150))
球域=球.get_rect()
速度=[1,1]
时钟=pygame.time.Clock()

while True:
    时钟.tick(12)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    球域=球域.move(速度)
    if 球域.left < 0 or 球域.right>宽:
        速度[0]=-速度[0]
    if 球域.top < 0 or 球域.bottom>高:
        速度[1]=-速度[1]
    窗口.fill(白色)
    窗口.blit(球,球域)
    pygame.display.flip()
#pygame.quit()