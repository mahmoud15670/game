import pygame
import random

# المفاتيح اللى هنستخدمها
from pygame import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# دا عباره عن الكائن  Sprite الطيارة بتورث من كلاس 
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player,self).__init__()
        self.surf = pygame.image.load('pla.png')
        self.rect = self.surf.get_rect()

    #الحركه بتاعت الطيارة 
    def update(self, pressed_keys) -> None:
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            # move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            # move_up_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
            # move_up_sound.play()
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            # move_up_sound.play()

        # علشان الطيارة متطلعش بره
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# الدبابات ورثه برضو من نفس الكائن
class Enemy(pygame.sprite.Sprite):
    def __init__(self, time) -> None:
        super(Enemy, self).__init__()
        self.surf = pygame.image.load('tanks.png')
        self.rect = self.surf.get_rect(
            # علشان كل طيارة تطلع من حته مختلفة عشوائى
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        # علشان اعلى السرعة من كل ليفل
        if 600*2 > time >= 600:
            self.speed = 13
        elif time >=600*2:
            self.speed = 23
        else:
            self.speed = 8

    # الحركة من اليمين لشمال وفى الاخر يموت
    def update(self) -> None:
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# الزراير
class Button():
    def __init__(self) -> None:
        self.surf = pygame.Surface((200,50))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()


# تعريف اللعبة
pygame.init()
# الوقت الخاص
clock = pygame.time.Clock()
# اسم الللعبة فى الشاشة
pygame.display.set_caption('mahmoud ghallab game')
# علشان تناسب كل الشاشات اتوماتيك
SCREEN_SIZE = pygame.display.get_desktop_sizes()
# ظبط الحدود
SCREEN_WIDTH = SCREEN_SIZE[0][0] - 20
SCREEN_HEIGHT = SCREEN_SIZE[0][1] - 70

def main():
    # الشاشة بتاعت اللعب
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # الخلفية
    bg = pygame.image.load('bg.jpg')
    clash = pygame.image.load('plas.png')
    # المزيكا
    pygame.mixer.music.load('sm.wav')
    # تشتغل مرة لو عايز علطول يبقى -1
    pygame.mixer.music.play(loops=1)
    move_up_sound = pygame.mixer.Sound('smw_1-up.wav')
    collision_sound = pygame.mixer.Sound('re.wav')

    # انشاء حدث لاضافة عدو
    ADDENEMY = pygame.USEREVENT + 1
    #  ظبط وقت لتشغيل الحدث كل 250 ميلي ثانية يعنى كل ربع ثانية
    pygame.time.set_timer(ADDENEMY, 250)

    player = Player()
    #  عمل جروب لاعداء علشان لما نقتل واحد يتشال من هنا ويتمسح
    enemies = pygame.sprite.Group()
    # جروب كل الكائنات
    all_sprites = pygame.sprite.Group()
    # نحت الاعب فى الجروب
    all_sprites.add(player)
    # القايمة اللى فيها الزراير تطلع ف الاخر
    manu = pygame.Surface((600, 50))
    # علشان اخليها شفافة اي حاجة لونها اسود تتشال
    manu.set_colorkey((0,0,0), RLEACCEL)
    rebutton = Button()
    exbutton = Button()
    # زرار الخروج بعد زرارالاعادة ب 400 بكسل
    exbutton.rect[0] = rebutton.rect[0] + 400

    running = True
    # العداد
    time = 1
    #  تعريف الخط نوع وحجم
    font = pygame.font.Font(None, 50)
    # الكتابة على الزراير
    replay = pygame.font.Font.render(font,'play again',False,'white', 'black')
    ex = pygame.font.Font.render(font,'exit',False,'white', 'black')
    rebutton.surf.blit(replay, (17,7))
    exbutton.surf.blit(ex, (100, 7))
    manu.blit(rebutton.surf,rebutton.rect)
    manu.blit(exbutton.surf,exbutton.rect)

# لوب اللعبة
    while running:
        # زراير الفارة
        mouse = pygame.mouse.get_pressed(3)
        # مكان المؤشر
        curser = pygame.mouse.get_pos()

        # لوب الاحداث
        for event in pygame.event.get():
            #  ESCAPE الضغط على زرار 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            # الخروج من البرنامج باى طريقة سوا الاكس اللى فوق 
            elif event.type == QUIT:
                running = False
            # انشاء العدو واضافته فى الجروبات
            elif event.type == ADDENEMY:
                new_enemy = Enemy(time)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
        # ظبط الخلفية
        screen.blit(bg, (0,0))
        # الازرار المضغوطة
        pressed_keys = pygame.key.get_pressed()
        # تحريك الطيارة
        player.update(pressed_keys)
        # تحريك الدبابات
        enemies.update()
        # لوب فى الجروبات لرسمهم فى الشاشة
        for object in all_sprites:
            screen.blit(object.surf, object.rect)
        # لو حصل اصطدام يين الكائن (الطيارة و الدبابات)
        if pygame.sprite.spritecollideany(player, enemies):
            # امسح الطيارة
            player.kill()
            # طلع القايمة
            screen.blit(manu, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2))
            # لو زرار الفارة اضغط
            if mouse[0] == True:
                # لو المؤشر على الزرار
                if curser[0] >= rebutton.rect[0] + SCREEN_WIDTH/3 and curser[0] <= rebutton.rect[2] + SCREEN_WIDTH/3 and curser[1] >= rebutton.rect[1] + SCREEN_HEIGHT/2 and curser[1] <= rebutton.rect[3] + SCREEN_HEIGHT/2 :
                    main()
                elif curser[0] >= exbutton.rect[2] + SCREEN_WIDTH/3 and curser[0] <= exbutton.rect[0] + 400 + SCREEN_WIDTH/3 and curser[1] >= exbutton.rect[1] + SCREEN_HEIGHT/2 and curser[1] <= exbutton.rect[3] + SCREEN_HEIGHT/2:
                    running = False
                    break
            # move_up_sound.stop()
            # collision_sound.play()
            # انتظر 0.8 ثانية علشان اضغط الزرار
            pygame.time.wait(80)
            # running = False
        # كتابة العداد على الشاشة
        text = pygame.font.Font.render(font,f'{round(time/(60))}s',False,'white', 'black')
        screen.blit(text, (SCREEN_WIDTH/2,0))
        # اظهار الشاشة كلها
        pygame.display.flip()
        # زود العداد
        time += 1
        # سرعة الفريمات بتاعت اللعبة
        clock.tick(60)
    # كتابة النتيجة النهائيه
    text = pygame.font.Font.render(font,f'your score is {round(time/(60))}s',False,'white', 'black')
    screen.blit(text, (SCREEN_WIDTH/2,0))
    pygame.display.flip()
    pygame.mixer.music.stop()
    # استنى 8 ث علشان نشوف النتيجة
    pygame.time.wait(8000)
    pygame.mixer.quit()

if __name__ == '__main__':
    main()