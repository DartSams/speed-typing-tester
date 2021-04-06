import pygame
import sys
from datetime import datetime
import random
import time

pygame.init()
width,height=1000,500
screen=pygame.display.set_mode((width,height))
FPS=pygame.time.Clock()
active=False
text=pygame.font.SysFont('comicsans',40)
sentence=''
box_width=400
run=True
start_bg=pygame.transform.scale(pygame.image.load(r"PyGame\speed typing\assets\start screen.jfif"),(width,height))


lst=["Everyone ate the same thing.","Are you kidding?","I'm looking for my key.",
"You can't miss it","Can she endure a long trip?","I promise you I'll keep you safe.",
"You must take his age into account.","I heard that a woman stabbed a man for eating her lunch.",
"I will go, rain or shine.","	You'd better eat everything that's on your plate.",
"I can't stand this pain.","How old do you think she is?","When did you buy it?",
"What would you like to drink?","It wasn't expensive.","Why do you think he said so?",
"Everybody except Joe went to the party.","The taxi picked up two passengers."]

test_sentence=random.choice(lst)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if start_screen.collidepoint(pos):
                run=False
                screen.fill((255,255,255))
                game_screen=pygame.transform.scale(pygame.image.load(r"PyGame\speed typing\assets\background.png"),(width,height-100))
                screen.blit(game_screen,(0,20))



        if event.type==pygame.KEYDOWN:
            if len(sentence)==1:
                start_time = time.time()
                print('starting now')


            sentence+=event.unicode
            

            if event.key==13:
                print(sentence)
                sentence=''

            if event.key==8:
                sentence=sentence[:-1]
    

    keys=pygame.key.get_pressed()
    if run==False:
        screen.fill((255,255,255))
        game_screen=pygame.transform.scale(pygame.image.load(r"PyGame\speed typing\assets\background.png"),(width,height-100))
        screen.blit(game_screen,(0,20))

    test_text_sentence=text.render(f"{test_sentence}",1,(0,0,0))
    screen.blit(test_text_sentence,(5,5))


    type_area=pygame.draw.rect(screen,(0,0,0),(0,height-100,width,height+100))
    player_typing=text.render(f"{sentence}" ,1,(255,255,255))
    screen.blit(player_typing,(type_area.width-type_area.width+20,type_area.height+340))

    if len(sentence)==len(test_sentence):
        print(sentence)
        sentence=''
        end_time = time.time()
        print(f"you took {round(end_time-start_time,5)} seconds to finish")
        test_sentence=''



        if len(lst)==0:
            print('finished all test')
            test_sentence=''
            pygame.quit()
            sys.exit()

        else:
            test_sentence=random.choice(lst)
    
    if run==True:
        start_screen=screen.blit(start_bg,(0,0))
        start_game=text.render(f"Click any where to begin" ,1,(255,255,255))
        screen.blit(start_game,(width//2-180,height-110))

    pygame.display.flip()
    FPS.tick(120)



