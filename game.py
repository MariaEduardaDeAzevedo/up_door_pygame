import pygame
from time import sleep
import datetime

pygame.init()

height = 765
width = 1365


#imagens
block = pygame.image.load('grass.png')
dirt = pygame.image.load('dirt.png')
door = pygame.image.load('door.png')
door_top = pygame.image.load('door_top.png')
door_open = pygame.image.load('door_open.png')
door_open_top = pygame.image.load('door_open_top.png')
coin = pygame.image.load('moeda.png')
yellow_key = pygame.image.load('chave_amarela.png')
life = pygame.image.load('vida.png')
but_save_up = pygame.image.load('botao_c.png')
but_save_down = pygame.image.load('botao_b.png')
im_spikes = pygame.image.load('espinhos.png')
#sons
coin_sound = pygame.mixer.Sound('som_moeda.ogg')
hurt_sound = pygame.mixer.Sound('crash.ogg')
back_sound = pygame.mixer.Sound('back.ogg')
pass_sound = pygame.mixer.Sound('nova_fase.ogg')

def game(pers, opt, name):
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    #Música de Fundo
    back_sound.play()
    back_sound.set_volume(opt['volume'])
    
    #comandos
    up = None
    right = None
    left = None
    if opt['comandos'] == 1:
        up = pygame.K_UP
        right = pygame.K_RIGHT
        left = pygame.K_LEFT
    elif opt['comandos'] == 2:
        up = pygame.K_w
        right = pygame.K_d
        left = pygame.K_a
    elif opt['comandos'] == 3:
        up = pygame.K_SPACE
        right = pygame.K_RIGHT
        left = pygame.K_LEFT
    elif opt['comandos'] == 2:
        up = pygame.K_SPACE
        right = pygame.K_d
        left = pygame.K_a
    
    font = pygame.font.Font('Digitalt.ttf', 30)
    infos_pers = None

    if pers == 1 or pers == None:
        infos_pers = ['lisa_icon.png', 'lisa_anda_1_r.png', 'lisa_anda_1_l.png', 'lisa_anda_2_l.png',
              'lisa_anda_2_r.png', 'lisa_parada_1.png', 'lisa_parada_2.png', 'lisa_pula_1.png',
              'lisa_pula_2.png', 'lisa_dano.png']
    elif pers == 2:
        infos_pers = ['will_icon.png', 'will_anda_1_r.png', 'will_anda_1_l.png', 'will_anda_2_l.png',
              'will_anda_2_r.png', 'will_parada_1.png', 'will_parada_2.png', 'will_pula_1.png',
              'will_pula_2.png', 'will_dano.png']
    elif pers == 3:
        infos_pers = ['louis_icon.png', 'louis_anda_1_r.png', 'louis_anda_1_l.png', 'louis_anda_2_l.png',
              'louis_anda_2_r.png', 'louis_parada_1.png', 'louis_parada_2.png', 'louis_pula_1.png',
              'louis_pula_2.png', 'louis_dano.png']
    elif pers == 4:
        infos_pers = ['tom_icon.png', 'tom_anda_1_r.png', 'tom_anda_1_l.png', 'tom_anda_2_l.png',
              'tom_anda_2_r.png', 'tom_parada_1.png', 'tom_parada_2.png', 'tom_pula_1.png',
              'tom_pula_2.png', 'tom_dano.png']

    elif pers == 5:
        infos_pers = ['zombie_icon.png', 'zombie_anda_1_r.png', 'zombie_anda_1_l.png', 'zombie_anda_2_l.png',
              'zombie_anda_2_r.png', 'zombie_parada_1.png', 'zombie_parada_2.png', 'zombie_pula_1.png',
              'zombie_pula_2.png', 'zombie_dano.png']


    #personagem
    icon = pygame.image.load(infos_pers[0])
    walk_1_r = pygame.image.load(infos_pers[1])
    walk_1_l = pygame.image.load(infos_pers[2])
    walk_2_l = pygame.image.load(infos_pers[3])
    walk_2_r = pygame.image.load(infos_pers[4])
    stoped_1 = pygame.image.load(infos_pers[5])
    stoped_2 = pygame.image.load(infos_pers[6])
    jump_1 = pygame.image.load(infos_pers[7])
    jump_2 = pygame.image.load(infos_pers[8])
    hurt = pygame.image.load(infos_pers[9])
    

    def level_1():
        plats = (((range(569, 690), 460), (630, 570)),
                 ((range(690, 760), 460), (700, 570)),
                 ((range(359, 480), 380),(420, 490)),
                 ((range(-100, 60), 180),(0, 290)),
                 ((range(9, 130), 180), (70, 290)),
                 ((range(79, 200), 180), (140, 290)),
                 ((range(219,340), 260),(280,370)),
                 ((range(219,340), 60),(280,170)),
                 ((range(340,410), 60),(350,170)),
                 ((range(410,480), 60),(420,170)),
                 ((range(480,550), 60),(490,170)),
                 ((range(550,620), 60),(560,170)),
                 ((range(779,900), 60),(840,170)),
                 ((range(900,970), 60),(910,170)),
                 ((range(970,1040), 60),(980,170)),
                 ((range(1129,1250), 60),(1190,170)),
                 ((range(1250,1320), 60),(1260,170)),
                 ((range(1320,1390), 60),(1330,170)),
                 ((range(779,900), 260),(840,370)),
                 ((range(900, 970), 260),(910,370)),
                 ((range(970, 1040), 260),(980,370)),
                 ((range(1040, 1110), 260),(1050,370)),
                 ((range(1110, 1180), 260),(1120,370)),
                 ((range(1180, 1250), 260),(1190,370)),
                 ((range(1250, 1320), 260),(1260,370)),
                 ((range(1320, 1390), 260),(1330,370)),
                 ((range(489, 620), 260),(560,370)),
                 ((range(620, 690), 260),(630,370)))

        save = (1190, 300)

        coins = [(228, 640), (298, 640), (368, 640), (858, 320), (928, 320), (998, 320), (18, 240), (88, 240), (158, 240),
                 (508, 120), (578,120), (648, 120)]

        keys = [(1260, 320)]

        spikes = [((range(910, 981), 130), (910, 100))]

        need = (10, 1)

        return (plats, save, coins, keys, need, spikes)


    def level_2():

        plats = (((range(849, 970), 460), (910, 570)),
                 ((range(970, 1040), 460), (980, 570)),
                 ((range(1129, 1250), 380),(1190, 490)),
                 ((range(1250, 1320), 380),(1260, 490)),
                 ((range(1320, 1390), 380),(1330, 490)),
                 ((range(919, 1040), 300),(980, 410)),
                 ((range(1129, 1250), 220),(1190, 330)),
                 ((range(709, 830), 180),(770, 290)),
                 ((range(-100, 60), 300),(0, 410)),
                 ((range(60, 130), 300),(70, 410)),
                 ((range(130, 200), 300),(140, 410)),
                 ((range(200, 270), 300),(210, 410)),
                 ((range(270, 340), 300),(280, 410)),
                 ((range(340, 410), 300),(350, 410)),
                 ((range(410, 480), 300),(420, 410)),
                 ((range(480, 550), 300),(490, 410)),
                 ((range(550, 620), 300),(560, 410)),
                 ((range(499, 620), 60),(560, 170)),
                 ((range(219, 340), 60),(280, 170)),
                 ((range(340, 410), 60),(350, 170)),
                 ((range(9, 130), 60),(70, 170)),
                 ((range(1199, 1320), 60),(1260, 170)),
                 ((range(1320, 1390 ), 60),(1330, 170)),
                 ((range(849, 970), 60),(910, 170)),
                 ((range(970, 1040), 60),(980, 170)),
                 ((range(1040, 1110), 60),(1050, 170)))

        save = (1190, 260)

        coins = [(1208, 440), (1270, 440), (998, 360), (798, 240), (578, 360), (508, 360), (298, 120), (368, 120)]

        keys = [(0, 360),(70, 140)]

        spikes = [((range(1050, 1121), 640),(1050, 620)), ((range(1120, 1191), 640),(1120, 620)),
                  ((range(1190, 1261), 640),(1190, 620)), ((range(1260, 1331), 640),(1260, 620)),
                  ((range(1330, 1500), 640),(1330, 620)), ((range(70, 141), 360),(70, 340)),
                  ((range(420, 491), 360),(420, 340))]

        need = (5, 2)
        
        return (plats, save, coins, keys, need, spikes)


    def level_3():

        plats = (((range(219, 340), 460), (280, 570)),
                 ((range(429, 550), 460), (490, 570)),
                 ((range(709, 830), 460), (770, 570)),
                 ((range(-100, 60), 340), (0, 450)),
                 ((range(60, 130), 340), (70, 450)),
                 ((range(130, 200), 340), (140, 450)),
                 ((range(219, 340), 220),(280, 330)),
                 ((range(79, 200), 100),(140, 210)),
                 ((range(359, 480), 100),(420, 210)),
                 ((range(480, 550), 100),(490, 210)),
                 ((range(550, 620), 100),(560, 210)),
                 ((range(639, 760), 100),(700, 210)),
                 ((range(760, 830), 100),(770, 210)),
                 ((range(830, 900), 100),(840, 210)),
                 ((range(989, 1110), 180),(1050, 290)),
                 ((range(1110, 1080), 180),(1120, 290)),
                 ((range(1129, 1250), 60),(1190, 170)),
                 ((range(1250, 1320), 60),(1260, 170)),
                 ((range(1320, 1390), 60),(1330, 170)))

        coins = [(858, 640), (928, 640), (998, 640), (1068, 640), (1138, 640), (1208, 640), (298, 280),
                 (298, 230), (298, 180), (298, 120), (18, 400), (18, 350), (18, 300), (88, 400), (88, 350),
                 (88, 300),(368, 470), (438, 470)]

        keys = [(290, 70), (805, 160), (1050, 210)]
        
        save = (1260, 620)

        spikes = [((range(280, 351), 640),(280, 620)), ((range(350, 421), 640),(350, 620)),
                  ((range(420, 491), 640),(420, 620)), ((range(490, 561), 640),(490, 620)),
                  ((range(560, 631), 640),(560, 620)), ((range(630, 701), 640),(630, 620)),
                  ((range(700, 771), 640),(700, 620)), ((range(490, 560), 160),(490, 140)),
                  ((range(700, 770), 160),(700, 140)), ((range(1120, 1190), 240),(1120, 220))]

        need = (12, 3)
        
        return (plats, save, coins, keys, need, spikes)

    def level_4():
        plats = (((range(149, 270), 460),(210, 570)),
                 ((range(359, 480), 380),(420, 490)),
                 ((range(569, 690), 300),(630, 410)),
                 ((range(849, 970), 300),(910, 410)),
                 ((range(1129, 1250), 300),(1190, 410)),
                 ((range(-100, 60), 380),(0, 490)),
                 ((range(1199, 1320), 60),(1260, 170)),
                 ((range(1320, 1390), 60),(1330, 170)),
                 ((range(149, 270), 300),(210, 410)),
                 ((range(-100, 60), 220),(0, 330)),
                 ((range(149, 270), 140),(210, 250)),
                 ((range(-100, 60), 60),(0, 170)),
                 ((range(359, 480), 60),(420, 170)),
                 ((range(639, 760), 60), (700, 170)),
                 ((range(919, 1040), 60),(980, 170)))

        coins = [(18, 440), (18, 280), (18, 120), (788, 300), (1208, 290), (1208, 240), (508, 420),
                 (438, 120), (718, 120), (998, 120), (578, 30), (858, 30), (1138, 30), (140, 450),
                 (140, 360), (140, 280), (140, 200)]

        keys = [(228, 110), (1068, 300)]
        
        save = (1190, 340)

        spikes = [((range(280, 351), 640),(280, 620)), ((range(350, 421), 640),(350, 620)),
                  ((range(420, 491), 640),(420, 620)), ((range(490, 561), 640),(490, 620)),
                  ((range(560, 631), 640),(560, 620)), ((range(630, 701), 640),(630, 620)),
                  ((range(700, 771), 640),(700, 620)), ((range(770, 841), 640),(770, 620)),
                  ((range(840, 911), 640),(840, 620)), ((range(910, 981), 640),(910, 620)),
                  ((range(980, 1051), 640),(980, 620)), ((range(1050, 1121), 640),(1050, 620)),
                  ((range(1120, 1191), 640),(1120, 620)), ((range(1190, 1261), 640),(1190, 620)),
                  ((range(1260, 1331), 640),(1260, 620)), ((range(1330, 1500), 640),(1330, 620))]

        need = (15, 2)
        
        return (plats, save, coins, keys, need, spikes)


    def end():
        end_font = pygame.font.Font('Digitalt.ttf', 90)
        res = f'FIM DE JOGO! SUA PONTUAÇÃO: {pnts}'
        lab_res = end_font.render(res, True, (255, 189, 74))

        return screen.blit(lab_res, (10, height//2))

        
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN) 
    pygame.display.set_caption('UP DOOR!')

    #personagem
    skin = [10, 580]
    mode = stoped_1

    #chão
    ground = list()
    sub_ground = list()
    x = 0
    for e in range(21):
        ground.append((x,690))
        x += 70
        
    x = 0
    for e in range(21):
        sub_ground.append((x, 760))
        x += 70
        
    clock = pygame.time.Clock()

    is_jumping = False
    jump_lim = 120
    jumping = 0
    surfaces = [(range(-100, 1500), 580)]
    coins = list()
    keys = list()
    spikes = list()
    direct = 1
    in_surf = True
    surf = 580
    level = 1
    fall = 0
    lifes = 4
    is_dead = False
    save_coo = None
    is_save = False
    c_coins = 0
    c_keys = 0
    need = (0, 0)
    pnts = 0
    #score/nível/itens/tutorial
    score = f'Pontos: {pnts}   Nível: {level}'
    score_lab = font.render(score, True, (255, 189, 74))
    items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
    items_lab = font.render(items, True, (255, 189, 74))

    if level == 1:
        for e in level_1()[2]:
            coins.append(e)

        for e in level_1()[3]:
            keys.append(e)


    door_pos = (1310, 60)

    #Gameloop
    is_pause = False
    
    while True:
        screen.fill((0, 255, 255))
        
        #morte
        if is_dead:
            skin[0] = 10
            skin[1] = 580
            if not is_save:
                level = 1
                for i in range(len(surfaces)-1, 0, -1):
                    surfaces.pop(i)
                for i in range(len(coins)-1, -1, -1):
                    coins.pop(i)
                for i in range(len(keys)-1, -1, -1):
                    keys.pop(i)
                for i in range(len(spikes)-1, -1, -1):
                    spikes.pop(i)
                pnts = 0
                c_keys = 0
                c_coin = 0    
                
            else:
                if level != 1:
                    pnts -= 60*pnts//100
                else:
                    pnts = 0

                for i in range(len(surfaces)-1, 0, -1):
                    surfaces.pop(i)
                for i in range(len(coins)-1, -1, -1):
                    coins.pop(i)
                for i in range(len(keys)-1, -1, -1):
                    keys.pop(i)
                for i in range(len(spikes)-1, -1, -1):
                    spikes.pop(i)
                
            score = f'Pontos: {pnts}   Nível: {level}'
            score_lab = font.render(score, True, (255, 189, 74))
            c_coin = 0
            c_keys = 0
            items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
            items_lab = font.render(items, True, (255, 189, 74))
            
            if level == 1:
                for e in level_1()[2]:
                    coins.append(e)

                for e in level_1()[3]:
                    keys.append(e)

            elif level == 2:
                for e in level_2()[2]:
                    coins.append(e)

                for e in level_2()[3]:
                    keys.append(e)

            elif level == 3:
                for e in level_3()[2]:
                    coins.append(e)

                for e in level_3()[3]:
                    keys.append(e)

            elif level == 4:
                for e in level_4()[2]:
                    coins.append(e)
                    
                for e in level_4()[3]:
                    keys.append(e)
                    
            is_dead = False
            is_save = False
            

        #level    
        if level == 1:
            for e in level_1()[0]:
                surfaces.append(e[0])
                screen.blit(block, e[1])

            for e in level_1()[5]:
                spikes.append(e[0])
                screen.blit(im_spikes, e[1])

            save_coo = level_1()[1]
            
            if not is_save:
                screen.blit(but_save_up, save_coo)
            else:
                screen.blit(but_save_down, save_coo)

            need = level_1()[4]
            items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
            items_lab = font.render(items, True, (255, 189, 74))

        elif level == 2:
            for e in level_2()[0]:
                surfaces.append(e[0])
                screen.blit(block, e[1])

            for e in level_2()[5]:
                spikes.append(e[0])
                screen.blit(im_spikes, e[1])
                
            save_coo = level_2()[1]

            if not is_save:
                screen.blit(but_save_up, save_coo)
            else:
                screen.blit(but_save_down, save_coo)

            need = level_2()[4]
            items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
            items_lab = font.render(items, True, (255, 189, 74))


        elif level == 3:
            for e in level_3()[0]:
                surfaces.append(e[0])
                screen.blit(block, e[1])

            for e in level_3()[5]:
                spikes.append(e[0])
                screen.blit(im_spikes, e[1])
                
            save_coo = level_3()[1]

            if not is_save:
                screen.blit(but_save_up, save_coo)
            else:
                screen.blit(but_save_down, save_coo)

            need = level_3()[4]
            items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
            items_lab = font.render(items, True, (255, 189, 74))


        elif level == 4:
            for e in level_4()[0]:
                surfaces.append(e[0])
                screen.blit(block, e[1])

            for e in level_4()[5]:
                spikes.append(e[0])
                screen.blit(im_spikes, e[1])
                
            save_coo = level_4()[1]

            if not is_save:
                screen.blit(but_save_up, save_coo)
            else:
                screen.blit(but_save_down, save_coo)

            need = level_4()[4]
            items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
            items_lab = font.render(items, True, (255, 189, 74))

        elif level == 5:
            end()

            #################################

            
        if mode == jump_1 and in_surf:
            mode = stoped_1
        elif mode == jump_2 and in_surf:
            mode = stoped_2
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == up and not is_pause:
                    if is_jumping == False and down == False:
                        is_jumping = True
                        if direct == 1:
                            mode = jump_1
                        elif direct == 2:
                            mode = jump_2

                elif event.key == pygame.K_ESCAPE:
                    file = open('ranking.txt', 'a')
                    player = name
                    if name == '':
                        player = 'Anônimo'
                    file.write(f'{player} - {pnts}\n')
                    file.close()
                    pygame.quit()

                elif event.key == pygame.K_p:
                    if not is_pause:
                        is_pause = True
                    else:
                        is_pause = False

        if is_pause:
            screen.blit(font.render('PAUSADO', True, (255, 189, 74)), (width//2, height//2))

        if pygame.key.get_pressed()[right] and not is_pause:
            if skin[0] <= 1300:
                skin[0] += 25
                direct = 1
            if not in_surf:
                mode = jump_1
            elif mode == walk_1_r:
                mode = walk_2_r
            elif mode == walk_2_r:
                mode = walk_1_r
            else:
                mode = walk_1_r
                
        elif pygame.key.get_pressed()[left] and not is_pause:
            if skin[0] >= 10:
                skin[0] -= 25
                direct = 2
            if not in_surf:
                mode = jump_2
            elif mode == walk_1_l:
                mode = walk_2_l
            elif mode == walk_2_l:
                mode = walk_1_l
            else:
                mode = walk_1_l
        else:
            if mode == walk_1_r or mode == walk_2_r:
                mode = stoped_1
            elif mode == walk_1_l or mode == walk_2_l:
                mode = stoped_2
                
        if is_jumping and not is_pause:
            fall = 0
            if jumping == jump_lim:
                is_jumping = False
            else:
                skin[1] -= 40
                jumping += 40
                in_surf = False
        else:
            down = True
            for s in surfaces:
                if skin[1] == s[1] and skin[0] in s[0]:
                    down = False
                    jumping = 0
                    in_surf = True
                    surf = s[1] - 110 
                    break
            if down and not is_pause:
                in_surf = False
                skin[1] += 40
                jumping -= 40
                fall += 40
         
        for pos in ground:
            screen.blit(block, pos)

        for pos in sub_ground:
            screen.blit(dirt, pos)
            
        if lifes == 4:
            screen.blit(life, (50, 0))
            screen.blit(life, (100, 0))
            screen.blit(life, (150, 0))
        elif lifes == 3:
            screen.blit(life, (50, 0))
            screen.blit(life, (100, 0))
        elif lifes == 2:
            screen.blit(life, (50, 0))
        elif lifes == 0:
            is_dead = True
            c_coins = 0
            lifes = 4

        if skin[1] + 110 in range(save_coo[1], save_coo[1] + 70) and skin[0]+40 in range(save_coo[0], save_coo[0]+70) and not is_jumping:
            is_save = True
            pnts += 50
            score = f'Pontos: {pnts}   Nível: {level}'
            score_lab = font.render(score, True, (255, 189, 74))
            
        for e in range(len(coins)-1, -1, -1):
            if (skin[0] + 40 or skin[0] + 30 or skin[0] + 20 or skin[0] + 10 or skin[0] + 80 or skin[0] + 70 or skin[0] + 60 or skin[0] + 50 or skin[0]) in range(coins[e][0], coins[e][0] + 37) and (skin[1] + 55 or  skin[1] + 45 or skin[1] + 35 or skin[1] + 25 or skin[1] + 15 or skin[1] + 5 or skin[1] + 110 or skin[1] + 100 or skin[1] + 90 or skin[1] + 80 or skin[1] + 70 or skin[1] + 60 or skin[1]) in range(coins[e][1] - 36, coins[e][1] + 1): 
                coin_sound.play()
                coin_sound.set_volume(opt['volume'])
                c_coins += 1
                score = f'Pontos: {pnts}   Nível: {level}'
                score_lab = font.render(score, True, (255, 189, 74))
                pnts += 10
                coins.pop(e)
                break

        for e in range(len(keys)-1, -1, -1):
            if (skin[0] + 40 or skin[0] + 80 or skin[0]) in range(keys[e][0], keys[e][0] + 37) and (skin[1] + 55 or skin[1] + 110 or skin[1]) in range(keys[e][1] - 36, keys[e][1]  + 1): 
                c_keys += 1
                keys.pop(e)
                break

        for e in spikes:
            if (skin[1] + 110 == e[1] or  skin[1] + 55 <= e[1] <= skin[1] + 110) and (skin[0] + 40 or skin[0] + 80 or skin[0]) in e[0] and not is_jumping:
                mode = hurt 
                screen.blit(mode, (skin[0], skin[1]))
                pygame.display.update()
                hurt_sound.play()
                hurt_sound.set_volume(opt['volume'])
                sleep(0.3)
                lifes -= 1
                fall = 0
                skin[0] = 10
                skin[1] = 580
                if direct == 1:
                    mode = stoped_1
                elif direct == 2:
                    mode = stoped_2
                break
        
        if skin[0] >= door_pos[0] and skin[1] <= door_pos[1] and c_coins >= need[0] and c_keys >= need[1] and level < 5:
            is_save = False
            level += 1
            lifes = 4
            skin[0] = 10
            skin[1] = 580
            c_coins = 0
            c_keys = 0
            score = f'Pontos: {pnts}   Nível: {level}'
            score_lab = font.render(score, True, (255, 189, 74))
            items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
            items_lab = font.render(items, True, (255, 189, 74))
            back_sound.stop()
            pass_sound.play()
            pass_sound.set_volume(opt['volume'])
            screen.blit(door_open_top, (1295, 30))
            screen.blit(door_open, (1295, 100))
            pygame.display.update()
            sleep(1)
            back_sound.play()
            back_sound.set_volume(opt['volume'])
            
            for i in range(len(surfaces)-1, 0, -1):
                surfaces.pop(i)
            for i in range(len(coins)-1, -1, -1):
                coins.pop(i)
            for i in range(len(keys)-1, -1, -1):
                keys.pop(i)
            for i in range(len(spikes)-1, -1, -1):
                spikes.pop(i)

            if level == 2:
                for e in level_2()[2]:
                    coins.append(e)

                for e in level_2()[3]:
                    keys.append(e)

            elif level == 3:
                for e in level_3()[2]:
                    coins.append(e)

                for e in level_3()[3]:
                    keys.append(e)

            elif level == 4:
                for e in level_4()[2]:
                    coins.append(e)

                for e in level_4()[3]:
                    keys.append(e)

        items = f'COINS: {c_coins}/{need[0]}   KEYS: {c_keys}/{need[1]}'
        items_lab = font.render(items, True, (255, 189, 74))
                
        screen.blit(items_lab, (1065, 0))
        screen.blit(icon, (0, 0))
        screen.blit(door_top, (1295, 30))
        screen.blit(door, (1295, 100))
        screen.blit(score_lab, (15, 47))

        for k in keys:
            screen.blit(yellow_key, k)

        for c in coins:
            screen.blit(coin, c)
        
        if fall >= 320 and in_surf:
            mode = hurt 
            screen.blit(mode, (skin[0], skin[1]))
            pygame.display.update()
            hurt_sound.play()
            hurt_sound.set_volume(opt['volume'])
            sleep(0.3)
            lifes -= 1
            fall = 0
            if direct == 1:
                mode = stoped_1
            elif direct == 2:
                mode = stoped_2

        else:
            screen.blit(mode, (skin[0], skin[1]))

        if in_surf:
            fall = 0
                
        clock.tick(11)
        
        pygame.display.update()
        





