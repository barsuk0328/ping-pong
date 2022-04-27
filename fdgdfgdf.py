from pygame import *
back = (255, 182, 193) 
win_width = 600
win_height = 400
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False 
clock = time.Clock()
FPS = 165
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < win_width - 99:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player('1.png', 20, 100, 60, 65, 3)
racket2 = Player('2.png', 500, 100, 60, 65, 3)
ball = GameSprite('pngwing.com.png', 280, 200, 40, 40, 4)



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()

    display.update()
    clock.tick(FPS)
