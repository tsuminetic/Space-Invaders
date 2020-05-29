import pygame as pyg
import random
from pygame import mixer

# import time

pyg.init()

game = True

while game is True:
    win = pyg.display.set_mode((600, 800))
    pyg.display.set_caption("Space Invader")
    iconimg = pyg.image.load("icon.png")
    pyg.display.set_icon(iconimg)
    backimg = pyg.image.load("back.png")

    mixer.music.load('background.wav')
    mixer.music.play(-1)

    score = 0

    enemylevs = 'enemy2.png'

    bullimg = pyg.image.load("bullet.png")
    bullimg = pyg.transform.scale(bullimg, (10, 40))

    enbullimg = pyg.image.load("enbulet.png")
    enbullimg = pyg.transform.scale(enbullimg, (10, 40))

    enemy1 = pyg.image.load(enemylevs)
    enemy1 = pyg.transform.scale(enemy1, (50, 30))
    enemy2 = pyg.image.load(enemylevs)
    enemy2 = pyg.transform.scale(enemy2, (50, 30))
    enemy3 = pyg.image.load(enemylevs)
    enemy3 = pyg.transform.scale(enemy3, (50, 30))
    enemy4 = pyg.image.load(enemylevs)
    enemy4 = pyg.transform.scale(enemy4, (50, 30))
    enemy5 = pyg.image.load(enemylevs)
    enemy5 = pyg.transform.scale(enemy5, (50, 30))
    enemy6 = pyg.image.load(enemylevs)
    enemy6 = pyg.transform.scale(enemy6, (50, 30))

    playerx = 240
    playery = 550
    playervel = 10

    enemyx = random.randint(0, 400)
    enemyy = 30
    enemyvel = 7

    enemy1x = random.randint(0, 400)
    enemy2x = random.randint(0, 400)
    enemy3x = random.randint(0, 400)
    enemy4x = random.randint(0, 400)
    enemy5x = random.randint(0, 400)
    enemy6x = random.randint(0, 400)

    enemy1y = 130
    enemy2y = 180
    enemy3y = 230
    enemy4y = 280
    enemy5y = 330
    enemy6y = 380

    enemy1vel = 5
    enemy2vel = 5
    enemy3vel = 5
    enemy4vel = 5
    enemy5vel = 5
    enemy6vel = 5

    bullx = 0
    bully = 550
    bullvel = 40
    bull_state = "ready"

    enbullx = 0
    enbully = 30
    enbull_state = "ready"

    delay = 3

    playerhealth = 100
    enemyhealth = 100
    textx = 10
    texty = 10
    font = pyg.font.Font('Franchise.ttf', 40)

    enemyh1 = 100
    enemyh2 = 100
    enemyh3 = 100
    enemyh4 = 100
    enemyh5 = 100
    enemyh6 = 100

    smolenemydown = 50


    def game_over():
        font_e = pyg.font.Font('airstrikelaser.ttf', 70)
        over_text = font_e.render("Game Over", True, (255, 255, 255))
        win.blit(over_text, (90, 300))


    def you_win():
        font_ew = pyg.font.Font('airstrikelaser.ttf', 80)
        win_text = font_ew.render("You Win", True, (255, 255, 255))
        win.blit(win_text, (110, 300))


    def scoree(x, y):
        text = "Score: " + str(score)
        scor_e = font.render(text, True, (255, 255, 255))
        win.blit(scor_e, (x, y))


    run = True
    while run:
        pyg.time.delay(delay)

        win.fill((0, 0, 0))
        win.blit(backimg, (0, 0))


        # pyg.draw.rect(win, (0, 0, 0), (x,y,width,height))

        # bullimg = pyg.image.load("bullet.png")
        # bullimg = pyg.transform.scale(bullimg, (10, 30))
        # win.blit(bullimg, (bullx, bully))

        def bull(x, y):
            global bull_state
            bull_state = "fire"
            win.blit(bullimg, (x + 45, y))


        def enbull(x, y):
            global enbull_state
            enbull_state = "fire"
            win.blit(enbullimg, (x + 75, y + 45))


        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
                game = False

        keys = pyg.key.get_pressed()

        if keys[pyg.K_d] and playerx + playervel < 510:
            playerx += playervel

        if keys[pyg.K_a] and playerx > 0:
            playerx -= playervel

        # if keys[pyg.K_w] and playery > enemyy + 100:
        #   playery -= playervel
        #  bully -= playervel

        # if keys[pyg.K_s] and playery + playervel < 620:
        #   playery += playervel
        #  bully += playervel

        if keys[pyg.K_SPACE]:

            if bull_state == "ready":
                bullsound = mixer.Sound('laser.wav')
                bullsound.play()
                bullx = playerx
                bull(bullx, bully)

            # if score >= 100:
            if random.choice(["no", "yes"]) == "yes":
                if enbull_state == "ready":
                    bullsound = mixer.Sound('laser.wav')
                    bullsound.play()
                    enbullx = enemyx
                    enbull(enbullx, enbully)

        if enemyhealth != 0:
            if enemyx + 10 < 430:
                if enemyx > 418 or enemyx < 12:
                    enemyx += enemyvel
                    # if crashes 10
                    enemyvel = -7
                    # if enemyy < 450:
                    #   enemyy += 20
                elif enemyx > 0:
                    enemyx -= enemyvel
                    if enemyx > 410:
                        enemyvel = 7
                        # if enemyy < 450:
                        #   enemyy += 20

        if enemy1x + 2 < 560:
            if enemy1x >= 557 or enemy1x <= 0:
                enemy1x += enemy1vel
                enemy1vel = -5
                if enemy1y < 560:
                    enemy1y += smolenemydown
            elif enemy1x > 0:
                enemy1x -= enemy1vel
                if enemy1x > 550:
                    enemy1vel = 5
                    if enemy1y < 560:
                        enemy1y += smolenemydown

        if enemy2x + 2 < 560:
            if enemy2x >= 557 or enemy2x <= 0:
                enemy2x += enemy2vel
                enemy2vel = -5
                if enemy2y < 560:
                    enemy2y += smolenemydown
            elif enemy2x > 0:
                enemy2x -= enemy2vel
                if enemy2x > 550:
                    enemy2vel = 5
                    if enemy2y < 560:
                        enemy2y += smolenemydown

        if enemy3x + 2 < 560:
            if enemy3x >= 557 or enemy3x <= 0:
                enemy3x += enemy3vel
                enemy3vel = -5
                if enemy3y < 560:
                    enemy3y += smolenemydown
            elif enemy3x > 0:
                enemy3x -= enemy3vel
                if enemy3x > 550:
                    enemy3vel = 5
                    if enemy3y < 560:
                        enemy3y += smolenemydown

        if enemy4x + 2 < 560:
            if enemy4x >= 557 or enemy4x <= 0:
                enemy4x += enemy4vel
                enemy4vel = -5
                if enemy4y < 560:
                    enemy4y += smolenemydown
            elif enemy4x > 0:
                enemy4x -= enemy4vel
                if enemy4x > 550:
                    enemy4vel = 5
                    if enemy4y < 560:
                        enemy4y += smolenemydown

        if enemy5x + 2 < 560:
            if enemy5x >= 557 or enemy5x <= 0:
                enemy5x += enemy5vel
                enemy5vel = -5
                if enemy5y < 560:
                    enemy5y += smolenemydown
            elif enemy5x > 0:
                enemy5x -= enemy5vel
                if enemy5x > 550:
                    enemy5vel = 5
                    if enemy5y < 560:
                        enemy5y += smolenemydown

        if enemy6x + 2 < 560:
            if enemy6x >= 557 or enemy6x <= 0:
                enemy6x += enemy6vel
                enemy6vel = -5
                if enemy6y < 560:
                    enemy6y += smolenemydown
            elif enemy6x > 0:
                enemy6x -= enemy6vel
                if enemy6x > 550:
                    enemy6vel = 5
                    if enemy6y < 560:
                        enemy6y += smolenemydown

        if bully < 0:
            bully = playery
            bull_state = "ready"

        if bull_state == "fire":
            bull(bullx, bully)
            bully -= bullvel

        if enbully > 800:
            enbully = enemyy
            enbull_state = "ready"

        if enbull_state == "fire":
            enbull(enbullx, enbully)
            enbully += bullvel

        abullimg = pyg.image.load("bullet.png")
        abullimg = pyg.transform.scale(abullimg, (10, 30))
        win.blit(abullimg, (playerx + 45, playery))

        playerimg = pyg.image.load("spaceship.png")
        playerimg = pyg.transform.scale(playerimg, (100, 100))
        win.blit(playerimg, (playerx, playery))

        enemyimg = pyg.image.load("enemy.png")
        enemyimg = pyg.transform.scale(enemyimg, (180, 110))
        win.blit(enemyimg, (enemyx, enemyy))

        win.blit(enemy1, (enemy1x, enemy1y))
        win.blit(enemy2, (enemy2x, enemy2y))
        win.blit(enemy3, (enemy3x, enemy3y))
        win.blit(enemy4, (enemy4x, enemy4y))
        win.blit(enemy5, (enemy5x, enemy5y))
        win.blit(enemy6, (enemy6x, enemy6y))

        if enemyy + 90 > playery and enemyx + 115 > playerx and enemyx - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))

        boomplace = random.choice([20, 30, 40, 50, 60, 70, 80])

        if enemyy + boomplace > bully and enemyx + 125 > bullx and enemyx - 40 < bullx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (100, 100))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            enemyhealth -= 0.2
            # if enemyhealth == 0:
        #     toboomimg = pyg.image.load("boom.png")
        #    toboomimg = pyg.transform.scale(toboomimg, (300, 300))
        #   win.blit(toboomimg, (enemyx - 70, enemyy - 40))
        #  enemyx = random.randint(0, 420)
        # enemyy = random.randint(30, 50)
        # enemyhealth = 100

        # toboomimg2 = pyg.image.load("boom.png")
        # toboomimg2= pyg.transform.scale(toboomimg2, (300, 300))
        # win.blit(toboomimg2, (enemyx, enemyy))

        # print(score)

        if enemy1y + 20 > bully and enemy1x - 15 > bullx and enemy1x - 25 < bullx and enemy1y < 530:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (80, 80))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            if score < 50:
                enemy1x = random.randint(0, 400)
                enemy1y = 130
                score += 1
            if score >= 50 and score < 100:
                lev2 = random.choice(['0', '1'])
                if lev2 == "1":
                    enemy1x = random.randint(0, 400)
                    enemy1y = 130
                    score += 1
            if score >= 100:
                lev2 = random.choice(['0', '0', '1', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1

        if enemy2y + 20 > bully and enemy2x - 15 > bullx and enemy2x - 25 < bullx and enemy2y < 530:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (80, 80))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            if score < 50:
                enemy2x = random.randint(0, 400)
                enemy2y = 180
                score += 1
            if score >= 50 and score < 100:
                lev2 = random.choice(['0', '1'])
                if lev2 == "1":
                    enemy2x = random.randint(0, 400)
                    enemy2y = 180
                    score += 1
            if score >= 100:
                lev2 = random.choice(['0', '0', '1', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1

        if enemy3y + 20 > bully and enemy3x - 15 > bullx and enemy3x - 25 < bullx and enemy3y < 530:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (80, 80))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            if score < 50:
                enemy3x = random.randint(0, 400)
                enemy3y = 230
                score += 1
            if score >= 50 and score < 100:
                lev2 = random.choice(['0', '1'])
                if lev2 == "1":
                    enemy3x = random.randint(0, 400)
                    enemy3y = 230
                    score += 1
            if score >= 100:
                lev2 = random.choice(['0', '0', '1', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1

        if enemy4y + 20 > bully and enemy4x - 15 > bullx and enemy4x - 25 < bullx and enemy4y < 530:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (80, 80))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            if score < 50:
                enemy4x = random.randint(0, 400)
                enemy4y = 280
                score += 1
            if score >= 50 and score < 100:
                lev2 = random.choice(['0', '1'])
                if lev2 == "1":
                    enemy4x = random.randint(0, 400)
                    enemy4y = 280
                    score += 1
            if score >= 100:
                lev2 = random.choice(['0', '0', '1', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1

        if enemy5y + 20 > bully and enemy5x - 15 > bullx and enemy5x - 25 < bullx and enemy5y < 530:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (80, 80))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            if score < 50:
                enemy5x = random.randint(0, 400)
                enemy5y = 330
                score += 1
            if score >= 50 and score < 100:
                lev2 = random.choice(['0', '1'])
                if lev2 == "1":
                    enemy5x = random.randint(0, 400)
                    enemy5y = 330
                    score += 1
            if score >= 100:
                lev2 = random.choice(['0', '0', '1', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1

        if enemy6y + 20 > bully and enemy6x - 15 > bullx and enemy6x - 25 < bullx and enemy6y < 530:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            toboomx = bullx
            toboomy = bully

            toboomimg = pyg.image.load("boom.png")
            toboomimg = pyg.transform.scale(toboomimg, (80, 80))
            win.blit(toboomimg, (toboomx, toboomy))
            bully = playery
            bull_state = "ready"

            if score < 50:
                enemy6x = random.randint(0, 400)
                enemy6y = 380
                score += 1
            if score >= 50 and score < 100:
                lev2 = random.choice(['0', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1
            if score >= 100:
                lev2 = random.choice(['0', '0', '1', '1'])
                if lev2 == "1":
                    enemy6x = random.randint(0, 400)
                    enemy6y = 380
                    score += 1

        if enemy1y + 30 > playery and enemy1x + 15 > playerx and enemy1x - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            playerhealth = 0
            game_over()

        if enemy2y + 30 > playery and enemy2x + 15 > playerx and enemy2x - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            win.blit(boomimg, (playerx, playery))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            playerhealth = 0
            game_over()

        if enemy3y + 30 > playery and enemy3x + 15 > playerx and enemy3x - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            playerhealth = 0
            game_over()

        if enemy4y + 30 > playery and enemy4x + 15 > playerx and enemy4x - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            playerhealth = 0
            game_over()

        if enemy5y + 30 > playery and enemy5x + 15 > playerx and enemy5x - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            playerhealth = 0
            game_over()

        if enemy6y + 30 > playery and enemy6x + 15 > playerx and enemy6x - 50 < playerx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            playerhealth = 0
            game_over()

        # if level==3:

        scoree(textx, texty)

        if playery - 50 < enbully and playerx - 60 < enbullx and playerx + 30 > enbullx:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            playerhealth -= 3

            print(playerhealth)

        if playerhealth <= 100 and playerhealth > 90:
            hellimg = pyg.image.load("health 100.png")
            helimg = pyg.transform.scale(hellimg, (300, 300))
            win.blit(helimg, (150, 540))

        if playerhealth <= 90 and playerhealth >= 75:
            hellimg = pyg.image.load("health 75.png")
            helimg = pyg.transform.scale(hellimg, (300, 300))
            win.blit(helimg, (150, 540))

        if playerhealth < 75 and playerhealth >= 50:
            hellimg = pyg.image.load("health 50.png")
            helimg = pyg.transform.scale(hellimg, (300, 300))
            win.blit(helimg, (150, 540))

        if playerhealth < 50 and playerhealth >= 25:
            hellimg = pyg.image.load("health 25.png")
            helimg = pyg.transform.scale(hellimg, (300, 300))
            win.blit(helimg, (150, 540))

        if playerhealth < 25 and playerhealth >= 2:
            hellimg = pyg.image.load("health 10.png")
            helimg = pyg.transform.scale(hellimg, (300, 300))
            win.blit(helimg, (150, 540))

        if playerhealth <= 2:
            boomsound = mixer.Sound('explosion.wav')
            boomsound.play()
            hellimg = pyg.image.load("health 0.png")
            helimg = pyg.transform.scale(hellimg, (300, 300))
            win.blit(helimg, (150, 540))
            boomimg = pyg.image.load("boom.png")

            boomimg = pyg.transform.scale(boomimg, (100, 100))
            win.blit(boomimg, (playerx, playery))
            win.blit(boomimg,
                     (playerx + random.choice([10, 20, 30, 40, 50]), playery + random.choice([10, 20, 30, 40, 50])))
            enemy1y = 4000
            enemy2y = 4000
            enemy3y = 4000
            enemy4y = 4000
            enemy5y = 4000
            enemy6y = 4000
            game_over()

        if enemyhealth <= 0:
            where_ = random.choice([40, 50, 60, -40, -50, -60])
            where__ = random.choice([10, 20, 60, -10, -20, -30])

            toboomimgwin2 = pyg.image.load("boom.png")
            toboomimgwin2 = pyg.transform.scale(toboomimgwin2, (200, 200))

            win.blit(toboomimgwin2, (enemyx + where_, enemyy + where__))

            toboomimgwin = pyg.image.load("boom.png")
            toboomimgwin = pyg.transform.scale(toboomimgwin, (300, 300))

            win.blit(toboomimgwin, (enemyx - 70, enemyy - 40))

            enemy1y = -100000
            enemy2y = -100000
            enemy3y = -100000
            enemy4y = -100000
            enemy5y = -100000
            enemy6y = -100000
            you_win()

        if enemyx < 0 or enemyx > 600:
            enemyx = random.randint(0, 400)

        if enemy1x < -10 or enemy1x > 600:
            enemy1x = random.randint(0, 400)

        if enemy2x < -10 or enemy2x > 600:
            enemy2x = random.randint(0, 400)

        if enemy3x < -10 or enemy3x > 600:
            enemy3x = random.randint(0, 400)

        if enemy4x < -10 or enemy4x > 600:
            enemy4x = random.randint(0, 400)

        if enemy5x < -10 or enemy5x > 600:
            enemy5x = random.randint(0, 400)

        if enemy6x < -10 or enemy6x > 600:
            enemy6x = random.randint(0, 400)

        pyg.display.update()

    pyg.quit()

    # enemy1y = 130
    # enemy2y = 180
    # enemy3y = 230
    # enemy4y = 280
    # enemy5y = 330
    # enemy6y = 380
