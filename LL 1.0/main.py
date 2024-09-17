import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("Lacuna's Labyrinth")

# image load
square_b = square_b_skin = pygame.image.load('img/player.png').convert()
square_o = square_o_skin = pygame.image.load('img/player_o.png').convert()
square_a = square_a_skin = pygame.image.load('img/player_a.png').convert()
square_p = square_p_skin = pygame.image.load('img/player_p.png').convert()

keyimg = pygame.image.load('img/key.png').convert_alpha()
exit_img = exit_imgstart = pygame.image.load('img/exit.png').convert_alpha()
restart_img = pygame.image.load('img/restart.png').convert_alpha()
x_img = pygame.image.load('img/x button.png').convert_alpha()
Larrow = pygame.image.load('img/left arrow.png').convert_alpha()
Rarrow = pygame.image.load('img/right arrow.png').convert_alpha()

# scale for skins
square_b_skin = pygame.transform.scale(square_b_skin, (50, 50))
square_o_skin = pygame.transform.scale(square_o_skin, (50, 50))
square_a_skin = pygame.transform.scale(square_a_skin, (50, 50))
square_p_skin = pygame.transform.scale(square_p_skin, (50, 50))
square_b = pygame.transform.scale(square_b, (25, 25))
square_o = pygame.transform.scale(square_o, (25, 25))

# scale
square_b = pygame.transform.scale(square_b, (25, 25))
x_img = pygame.transform.scale(x_img, (70, 75))
keyimg = pygame.transform.scale(keyimg, (45, 21))
restart_img = pygame.transform.scale(restart_img, (340, 92))
exit_img = pygame.transform.scale(exit_img, (188, 92))
exit_imgstart = pygame.transform.scale(exit_img, (188, 92))
Larrow = pygame.transform.scale(Larrow, (54, 78))
Rarrow = pygame.transform.scale(Rarrow, (54, 78))

pygame.mixer.music.load("img/toon.mp3")
pygame.mixer.music.play(-1)

# classes
class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        # mouse position
        pos = pygame.mouse.get_pos()

        # mouse over button and click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = square_b
        self.square_hitbox = pygame.Rect(x, y, 24, 24)

    def move(self):
        keys = pygame.key.get_pressed()
        # these are all just 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= 4
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += 4
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= 4
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += 4

    def collide(self):
        if self.y <= 10:
            self.y = 10

        # top right and bottom right x-axis
        if screen.get_at((self.x, self.y)) == (0, 0, 0, 255) or screen.get_at(
                (self.x + self.image.get_width(), self.y + self.image.get_height())) == (0, 0, 0, 255):
            self.x -= 4

        # top left and bottom left x-axis
        if screen.get_at((self.x + self.image.get_width(), self.y)) == (0, 0, 0, 255) or screen.get_at(
                (self.x, self.y + self.image.get_height())) == (0, 0, 0, 255):
            self.x += 4

        # bottom left and bottom right y-axis
        if screen.get_at((self.x, self.y + self.image.get_height())) == (0, 0, 0, 255) or screen.get_at(
                (self.x + self.image.get_width(), self.y + self.image.get_height())) == (0, 0, 0, 255):
            self.y -= 2

        # top left and top right y-axis
        if screen.get_at((self.x + self.image.get_width(), self.y)) == (0, 0, 0, 255) or screen.get_at(
                (self.x, self.y)) == (0, 0, 0, 255):
            self.y += 3

        # top right corner
        if screen.get_at((self.x + 24, self.y)) == (0, 0, 0, 255):
            self.y += 2
            self.x -= 4

        # bottom left corner
        if screen.get_at((self.x, self.y + 24)) == (0, 0, 0, 255):
            self.y -= 1
            self.x += 4

        # top left corner
        if screen.get_at((self.x, self.y)) == (0, 0, 0, 255):
            self.y += 1
            self.x += 4

        # bottom right corner
        if screen.get_at((self.x + 24, self.y + 24)) == (0, 0, 0, 255):
            self.y -= 2
            self.x -= 4

        # left middle
        if screen.get_at((self.x, self.y + 12)) == (0, 0, 0, 255):
            self.x += 1

        # top middle
        if screen.get_at((self.x + 12, self.y)) == (0, 0, 0, 255):
            self.y += 1

        # right middle
        if screen.get_at((self.x + 24, self.y + 12)) == (0, 0, 0, 255):
            self.x -= 1

        # bottom middle
        if screen.get_at((self.x + 12, self.y + 24)) == (0, 0, 0, 255):
            self.y -= 1

    def draw(self):
        self.square_hitbox.x = self.x
        self.square_hitbox.y = self.y
        screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.square_hitbox, 2)

class key:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = keyimg
        self.key_hitbox = pygame.Rect(x, y, 50, 24)

    def draw(self):
        self.key_hitbox.x = self.x
        self.key_hitbox.y = self.y
        screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.key_hitbox, 2)


class GameState:
    def __init__(self):
        self.state = 'mainmenu'

    def mainmenu(self):
        global eng, spa, running, lang_select, volume, menutimer
        screen.fill((203, 228, 241))

        # music volume
        mixer.music.set_volume(volume / 100)

        # images
        eng_img = pygame.image.load('img/eng.png').convert()
        spa_img = pygame.image.load('img/spa.png').convert()
        title = pygame.image.load('img/title.png').convert()
        start_img = pygame.image.load('img/start.png').convert_alpha()
        credits_img = pygame.image.load('img/credits.png').convert_alpha()
        options_img = pygame.image.load('img/options.png').convert_alpha()
        lang_background = pygame.image.load('img/gray-background.png').convert_alpha()

        # image scale & opacity
        eng_img = pygame.transform.scale(eng_img, (62, 40))
        spa_img = pygame.transform.scale(spa_img, (62, 40))
        title = pygame.transform.scale(title, (618, 222))
        options_img = pygame.transform.scale(options_img, (280, 91))
        start_img = pygame.transform.scale(start_img, (315, 126))
        credits_img = pygame.transform.scale(credits_img, (378, 126))
        lang_background = pygame.transform.scale(lang_background, (screen.get_width(), screen.get_height()))
        lang_background.set_alpha(250)

        # buttons
        english_button = Button(400, 350, eng_img, 2)
        spanish_button = Button(800, 350, spa_img, 2)
        title_button = Button(320, 30, title, 1)
        start_button = Button(500, 270, start_img, 0.75)
        options_button = Button(482, 380, options_img, 1)
        credits_button = Button(482, 488, credits_img, 0.75)
        exit_button = Button(525, 600, exit_imgstart, 1)

        # main menu code

        if title_button.draw():
            pass

        if credits_button.draw() and not lang_select and menutimer >= 10:
            menutimer = 0
            self.state = 'creditsmenu'

        if exit_button.draw() and not lang_select and menutimer >= 10:
            menutimer = 0
            running = False

        if start_button.draw() and not lang_select and menutimer >= 10:
            menutimer = 0
            self.state = 'levelselect'

        if options_button.draw() and menutimer >= 10:
            menutimer = 0
            self.state = 'optionsmenu'

        if not lang_select:
            menutimer += 1

        if lang_select:
            # text for the language selection
            lang_font = pygame.font.Font('fieldguide.ttf', 55)
            language1eng = lang_font.render("Select your Language", True, (255, 255, 255))
            language1spa = lang_font.render("Elige tu idioma", True, (255, 255, 255))
            screen.blit(lang_background, (0, 0))
            screen.blit(language1eng, (420, 150))
            screen.blit(language1spa, (500, 250))

            if english_button.draw():
                eng = True
                spa = False
                lang_select = False

            if spanish_button.draw():
                spa = True
                eng = False
                lang_select = False

    def creditsmenu(self):

        # credits
        screen.fill((203, 228, 241))
        credits_font = pygame.font.Font('fieldguide.ttf', 55)
        credit1_text = credits_font.render("Lacuna's Labyrinth", True, (0, 0, 0))
        credit2_text = credits_font.render("Team Members:", True, (0, 0, 0))
        credit3_text = credits_font.render("Lead Programmer and Art Designer: Corey Stuckey", False, (0, 0, 0))
        credit4_text = credits_font.render("Sound Design and Media Coordinator: Jakeb Ranew", False, (0, 0, 0))
        credit5_text = credits_font.render("English Voice Actor: Clinton Thornburg", False, (0, 0, 0))
        credit6_text = credits_font.render("Spanish Voice Actor: Ethan Gael Delfin-Uscanga", False, (0, 0, 0))
        credit7_text = credits_font.render("Ghastly Games", True, (0, 0, 0))

        screen.blit(credit1_text, (100, 75))
        screen.blit(credit2_text, (100, 150))
        screen.blit(credit3_text, (100, 225))
        screen.blit(credit4_text, (100, 300))
        screen.blit(credit5_text, (100, 375))
        screen.blit(credit6_text, (100, 450))
        screen.blit(credit7_text, (100, 525))

        # buttons
        x_button = Button(1150, 10, x_img, 1)

        if x_button.draw():
            self.state = 'mainmenu'

    def optionsmenu(self):
        global windowedshown, fullscreenshown, screen, volume, b_timer
        screen.fill((25, 25, 25))

        b_timer += 1

        larrow = pygame.image.load("img/left arrow.png").convert_alpha()
        rarrow = pygame.image.load("img/right arrow.png").convert_alpha()
        larrow = pygame.transform.scale(larrow, (80, 130))
        rarrow = pygame.transform.scale(rarrow, (80, 130))

        apply = pygame.image.load("img/apply.png").convert_alpha()
        apply = pygame.transform.scale(apply, (180, 78))

        # Code for exiting the options menu
        esc_font = pygame.font.Font('FieldGuide.ttf', 72)
        credit7_text = esc_font.render('Press [ESC] to Exit', True, (255, 255, 255))

        volume_font = pygame.font.Font('FieldGuide.ttf', 72)
        volume_text = volume_font.render(f'Volume: {volume}', True, (255, 255, 255))

        windowed_text = esc_font.render('Windowed', True, (255, 255, 255))
        fullscreen_text = esc_font.render('Fullscreen', True, (255, 255, 255))

        # Main code for the options menu
        left_button2 = Button(100, 400, larrow, 1)
        right_button2 = Button(500, 400, rarrow, 1)
        left_button3 = Button(700, 400, larrow, 1)
        right_button3 = Button(1150, 400, rarrow, 1)
        applybut = Button(240, 530, apply, 1)

        screen.blit(volume_text, (800, 415))

        controls_font = pygame.font.Font('FieldGuide.ttf', 48)
        controls1_font = pygame.font.Font('FieldGuide.ttf', 96)
        # controls for keyboard
        controls1key = controls_font.render('[ESC] : Exit or Pause', True, (255, 255, 255))
        controls2key = controls_font.render('[W], [A], [S], [D] : To Move', True, (255, 255, 255))
        controls3key = controls_font.render('[UP], [LEFT], [DOWN], [RIGHT] : To Move', True,
                                            (255, 255, 255))
        controls5key = controls1_font.render('Controls:', True, (255, 255, 255))

        # controls blitting
        screen.blit(controls1key, (10, 200))
        screen.blit(controls2key, (10, 280))
        screen.blit(controls3key, (10, 120))
        screen.blit(controls5key, (10, 10))

        # code for the buttons for volume and fullscreen
        if left_button2.draw():
            fullscreenshown = False
            windowedshown = True

        if right_button2.draw():
            windowedshown = False
            fullscreenshown = True

        if volume >= 100:
            volume = 100
        if volume <= 0:
            volume = 0

        if left_button3.draw() and b_timer >= 8 and volume >= 1:
            b_timer = 0
            volume -= 1

        if right_button3.draw() and b_timer >= 8 and volume <= 99:
            b_timer = 0
            volume += 1

        if windowedshown:
            screen.blit(windowed_text, (210, 410))
        if fullscreenshown:
            screen.blit(fullscreen_text, (195, 410))

        if applybut.draw() and b_timer >= 60:
            b_timer = 0
            if fullscreenshown:
                screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
            if windowedshown:
                screen = pygame.display.set_mode((1280, 720), pygame.HWSURFACE | pygame.DOUBLEBUF)

        screen.blit(credit7_text, (350, 630))

        if keys[pygame.K_ESCAPE]:
            b_timer = 0
            self.state = 'mainmenu'

    def levelselect(self):
        global skinnum, skintimer, level_2_lock, level_3_lock
        screen.fill((203, 228, 241))

        # image load
        lock = pygame.image.load('img/lock.png').convert_alpha()
        instructions = pygame.image.load('img/instructions.png').convert()
        level1icon_img = level2icon_img = level3icon_img = pygame.image.load('img/level icon.png').convert()
        thornburg = pygame.mixer.Sound('img/thornburg.mp3')
        delphin = pygame.mixer.Sound('img/delphin.mp3')

        # image Scale
        level1icon_img = pygame.transform.scale(level1icon_img, (110, 110))
        level2icon_img = pygame.transform.scale(level2icon_img, (110, 110))
        level3icon_img = pygame.transform.scale(level3icon_img, (110, 110))
        level2iconblock_img = pygame.transform.scale(level2icon_img, (200, 200))
        level3iconblock_img = pygame.transform.scale(level3icon_img, (200, 200))
        instructions = pygame.transform.scale(instructions, (644, 273))
        lock = pygame.transform.scale(lock, (200, 200))

        # Buttons
        level1_button = Button(125, 50, level1icon_img, 1.8)
        level2_button = Button(525, 50, level2icon_img, 1.8)
        level3_button = Button(925, 50, level3icon_img, 1.8)
        larrow_button = Button(800, 500, Larrow, 1)
        rarrow_button = Button(1050, 500, Rarrow, 1)
        x_button = Button(1175, 10, x_img, 1)

        # text for the language selection
        levelfont = pygame.font.Font('fieldguide.ttf', 125)
        level1font = levelfont.render("1", True, (255, 255, 255))
        level2font = levelfont.render("2", True, (255, 255, 255))
        level3font = levelfont.render("3", True, (255, 255, 255))

        screen.blit(instructions, (20, 400))
        if level1_button.draw():
            player.x = 190
            player.y = 25
            self.state = 'level1'
            if eng:
                thornburg.play()
            else:
                delphin.play()
        screen.blit(level1font, (200, 85))

        if not level_2_lock:
            if level2_button.draw():
                player.x = 30
                player.y = 25
                self.state = 'level2'
            screen.blit(level2font, (600, 85))
        if level_2_lock:
            screen.blit(level2iconblock_img, (525, 50))
            screen.blit(lock, (524, 29))

        if not level_3_lock:
            if level3_button.draw():
                player.x = 30
                player.y = 25
                self.state = 'level3'
            screen.blit(level3font, (1000, 85))
        if level_3_lock:
            screen.blit(level3iconblock_img, (925, 50))
            screen.blit(lock, (924, 29))

        if x_button.draw():
            self.state = 'mainmenu'

        # skins stuff
        skintimer += 1
        if larrow_button.draw() and skintimer > 10:
            skinnum -= 1
            skintimer = 0

        if rarrow_button.draw() and skintimer > 10:
            skinnum += 1
            skintimer = 0

        if skinnum == 1:
            screen.blit(square_b_skin, (925, 510))
            player.image = square_b

        if skinnum == 2:
            screen.blit(square_o_skin, (925, 510))
            player.image = square_o

        if skinnum == 3:
            screen.blit(square_a_skin, (925, 510))
            player.image = square_a

        if skinnum == 4:
            screen.blit(square_p_skin, (925, 510))
            player.image = square_p

        if skinnum < 1:
            skinnum = 4

        if skinnum > 4:
            skinnum = 1

    def level1(self):
        global level_2_lock
        screen.fill((203, 228, 241))

        # image load
        lvl1_img = pygame.image.load('img/14 by 14.png').convert()
        lvl1_img = pygame.transform.scale(lvl1_img, (1000, 720))

        screen.blit(lvl1_img, (150, 0))
        key1.x = 1075
        key1.y = 675
        key1.draw()
        player.draw()
        player.move()
        # player.collide()

        if keys[pygame.K_ESCAPE]:
            self.state = 'levelselect'

        if player.square_hitbox.colliderect(key1.key_hitbox):
            self.state = 'levelselect'
            level_2_lock = False
            player.x = 190
            player.y = 25

    def level2(self):
        global level_3_lock
        screen.fill((203, 228, 241))

        # image load
        lvl2_img = pygame.image.load('img/25 by 14.PNG').convert()
        lvl2_img = pygame.transform.scale(lvl2_img, (1280, 720))

        screen.blit(lvl2_img, (0, 0))
        key1.x = 1220
        key1.y = 675
        key1.draw()
        player.draw()
        player.move()
        # player.collide()

        if keys[pygame.K_ESCAPE]:
            self.state = 'levelselect'

        if player.square_hitbox.colliderect(key1.key_hitbox):
            self.state = 'levelselect'
            level_3_lock = False
            player.x = 190
            player.y = 25

    def level3(self):
        screen.fill((203, 228, 241))

        # image load
        lvl3_img = pygame.image.load('img/25 by 14 lvl 3.png').convert()
        lvl3_img = pygame.transform.scale(lvl3_img, (1280, 720))

        screen.blit(lvl3_img, (0, 0))
        key1.x = 1210
        key1.y = 675
        key1.draw()
        player.draw()
        player.move()
        # player.collide()

        if keys[pygame.K_ESCAPE]:
            self.state = 'levelselect'

        if player.square_hitbox.colliderect(key1.key_hitbox):
            self.state = 'game_over'
            player.x = 190
            player.y = 25

    def game_over(self):
        global running
        screen.fill((203, 228, 241))

        # image load
        game_over_picture = pygame.image.load('img/game over.png').convert()
        game_over_picture = pygame.transform.scale(game_over_picture, (900, 550))

        # Buttons
        restart_button_end = Button(250, 600, restart_img, 1)
        exit_button_end = Button(850, 600, exit_img, 1)

        screen.blit(game_over_picture, (200, 25))
        if restart_button_end.draw():
            self.state = 'levelselect'

        if exit_button_end.draw():
            running = False

    def state_manager(self):
        state_methods = {
            'mainmenu': self.mainmenu,
            'creditsmenu': self.creditsmenu,
            'optionsmenu': self.optionsmenu,
            # levels
            'levelselect': self.levelselect,
            'level1': self.level1,
            'level2': self.level2,
            'level3': self.level3,
            'game_over': self.game_over,
        }

        method = state_methods.get(self.state)
        if method:
            method()


# classes
player = Player(190, 25)
key1 = key(1075, 675)

# refrences
level_2_lock = True
level_3_lock = True
skinnum = 1
skintimer = 0

# beginning language selection
lang_select = True
eng = False
spa = False
menutimer = 0

# controller & options menu
windowedshown = True
fullscreenshown = False
b_timer = 0
volume = 50

# FPS
FPS = 60
clock = pygame.time.Clock()
game_state = GameState()

# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    game_state.state_manager()
    keys = pygame.key.get_pressed()

    pygame.display.flip()
pygame.quit()
