from pygame import *
back = (255, 182, 193) 
win_width = 600
win_height = 400
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False 
clock = time.Clock()
FPS = 60
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
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player('1.png', 10, 100, 60, 65, 4)
racket2 = Player('2.png', 520, 100, 60, 65, 4)
ball = GameSprite('pngwing.com.png', 280, 200, 25, 25, 4)
dx = 4
dy = 4

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))

score_left = 0
score_right = 0








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
        ball.rect.x += dx
        ball.rect.y += dy
        ball.reset()
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            dx *= -1.
        if ball.rect.y < 0 or ball.rect.y > win_height-40:
            dy *= -1.
        
        score_l = font.render(str(score_left), True, (0, 0, 0))
        score_r = font.render(str(score_right), True, (0, 0, 0))
        window.blit(score_l, (10, 10))
        window.blit(score_r, (win_width-25, 10))

