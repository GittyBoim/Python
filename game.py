import pygame
import excel

pygame.init()
finish = False
screen = pygame.display.set_mode([990, 652])
playerX = 300
playerY = 450
planX = 0
plan1X = 300
plan2X = 600
flag = True
flag1 = True
flag2 = True
shotY = 380
ifShoot = False
input_box = pygame.Rect(300, 400, 200, 32)
input_text = ""


# הפונקציה מקבלת את מיקום העכבר, מיקום אובייקט וטווח לחיצה ומחזירה אם הלחיצה היתה בטווח
def ifPos(x, y, x1, y1, distanceX, distanceY):
    if distanceX >= x - x1 > 0 and distanceY >= y - y1 > 0:
        return True
    return False


font = pygame.font.Font(None, 32)
user_input = "enter user name"

# לולאה שיוצרת את מסך הכניסה-הכנסת שם משתמש
# ויצירת חשבון השתמש בexcel

while not finish:
    screen.fill((255, 255, 255))
    text_surface = font.render(user_input, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(990 // 2, 652 // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                finish = True
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.unicode:
                if user_input == "enter user name":
                    user_input = event.unicode
                else:
                    user_input += event.unicode

excel.typeName(user_input)
finish = False
#הלולאה יוצרת את מסך המשחק
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if ifPos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], playerX, playerY, 200, 100):
                    ifShoot = True
                    shotY = playerY + 80
                if ifPos(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 786, 580, 140, 50):
                    finish = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX -= 40
            elif event.key == pygame.K_RIGHT:
                playerX += 40
            elif event.key == pygame.K_DOWN:
                playerY += 40
            elif event.key == pygame.K_UP:
                playerY -= 40

    if playerX > 900:
        playerX = 900
    elif playerX < 0:
        playerX = 0
    if playerY > 600:
        playerY = 600
    elif playerY < 0:
        playerY = 0

    if planX < 0 or planX > 880:
        flag = not flag

    if flag:
        planX += 4
    else:
        planX -= 4

    if plan1X < 0 or plan1X > 880:
        flag1 = not flag1

    if flag1:
        plan1X += 5
    else:
        plan1X -= 5

    if plan2X < 0 or plan2X > 880:
        flag2 = not flag2

    if flag2:
        plan2X += 6
    else:
        plan2X -= 6

    img = pygame.image.load('sea.png')
    screen.blit(img, [0, 0])

    playerImage = pygame.image.load('boat.png')
    playerImage.set_colorkey([255, 239, 2])
    screen.blit(playerImage, [playerX, playerY])

    planImage = pygame.image.load('plan.png')
    planImage.set_colorkey([255, 239, 2])
    screen.blit(planImage, [planX, 70])

    planImage1 = pygame.image.load('plan.png')
    planImage1.set_colorkey([255, 239, 2])
    screen.blit(planImage1, [plan1X, 150])

    planImage1 = pygame.image.load('plan.png')
    planImage1.set_colorkey([255, 239, 2])
    screen.blit(planImage1, [plan2X, 250])

    button_surface = font.render("End Game", True, (0, 0, 0))
    button_rect = button_surface.get_rect(center=(850, 600))
    frame_rect = button_rect.inflate(20, 20)
    frame_surface = pygame.Surface(frame_rect.size)
    frame_surface.fill((255, 255, 255))
    pygame.draw.rect(frame_surface, (0, 0, 0), frame_surface.get_rect(), 2)
    screen.blit(frame_surface, frame_rect)
    screen.blit(button_surface, button_rect)

    shotY -= 15

    if ifShoot:
        pygame.draw.circle(screen, [0, 0, 0], [playerX + 100, shotY], 10)
        if ifPos(playerX + 100, shotY, planX, 70, 120, 20):
            planX = 0
            pygame.mixer.init()
            pygame.mixer.music.load('applause.mp3')
            pygame.mixer.music.play()
            excel.update(True)
            ifShoot = False
        if ifPos(playerX + 100, shotY, plan1X, 150, 120, 20):
            plan1X = 0
            pygame.mixer.init()
            pygame.mixer.music.load('applause.mp3')
            pygame.mixer.music.play()
            excel.update(True)
            ifShoot = False
        if ifPos(playerX + 100, shotY, plan2X, 250, 120, 20):
            plan2X = 0
            pygame.mixer.init()
            pygame.mixer.music.load('applause.mp3')
            pygame.mixer.music.play()
            excel.update(True)
            ifShoot = False

    if shotY <= 0 and ifShoot:
        pygame.mixer.init()
        pygame.mixer.music.load('pikon.mp3')
        pygame.mixer.music.play()
        excel.update(False)
        ifShoot = False

    pygame.display.flip()

excel.sumPoints()
pygame.quit()
