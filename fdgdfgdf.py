from pygame import *
back = (255, 182, 193) 
win_width = 600
win_height = 400
window = display.set_mode((win_width, win_height))
window.fill(back)
window.blit(background,(0,0))
game = True
finish = False 
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(FPS)