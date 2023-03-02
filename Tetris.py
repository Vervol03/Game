import pygame, sys, random, time, random
import emoji,pygame.freetype

SIZE = 20
class figur:
    def __init__(self):
        self.next = d[random.choice(list(d))]
        self.figur = d[random.choice(list(d))]
        for i in range(random.randint(0,2)):
            self.next = list(zip(*self.next[::-1]))
            self.figur = list(zip(*self.figur[::-1]))
        self.h = 10
        self.x = 90
        self.pph= 0
        self.ppx= 0
        self.pole = [[1 if j==20 or i>=10 else 0 for i in range(11)]for j in range(21)]
        self.r = False
        self.l = False
        self.n = False
        self.stop = True
        self.game_over=False

    def new(self):
        self.pph = int((self.h-10)/SIZE)
        self.ppx = int((self.x-10)/SIZE)

def draw(arr):
    for i,line in enumerate(arr):
        for j,el in enumerate(line):
            if el == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(f.x+SIZE*i, f.h+SIZE*j, 19, 19),1)
def draw_next():
    f.h = 70; f.x = 230
    for i,line in enumerate(f.next):
        for j,el in enumerate(line):
            if el == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(f.x+SIZE*i, f.h+SIZE*j, 19, 19),1)
def draw_pole():
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(9, 9, 200, 400))
    for i in range(len(f.pole)-1):
        for j in range(len(f.pole[i])-1):
            if f.pole[i][j] == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(10+SIZE*j, 10+SIZE*i, 19, 19),1)
def colision():
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if f.pole[f.pph+j+1][f.ppx+i] == 1: return False
    return True
def logic():
    for i in range(len(f.figur)):
        for j in range(len(f.figur[i])):
            if f.figur[i][j] == 1:
                f.new()
                f.pole[f.pph+j][f.ppx+i] = 1
def logic_left(dire):
    chek = True
    if dire == 'l': ppx = int((f.x-10-20)/SIZE)
    if dire == 'r': ppx = int((f.x-10+20)/SIZE)
    pph = int((f.h-10+10)/SIZE)
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if f.pole[pph+j][ppx+i] == 1: chek = False
    pph = int((f.h-10+20)/SIZE)
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if f.pole[pph+j][ppx+i] == 1: chek = False
    return chek
def logic_nize():
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if f.pole[f.pph+j+2][f.ppx+i] == 1: return False
    return True
def logic_turn():
    new_figur = list(zip(*f.figur[::-1]))
    chek = True
    x = 0
    h = 0
    w_f = len(new_figur)
    for i,line in enumerate(new_figur):
        for j,el in enumerate(line):
            if el == 1 and i > len(f.figur)-1:
                f.new()
                try:
                    if f.pole[f.pph+j][f.ppx+i]==1: x -= 20
                except IndexError: x -= 20
    
    for i,line in enumerate(new_figur):
        for j,el in enumerate(line):
            if el == 1 and j > len(f.figur[0])-1:
                f.new()
                try:
                    if f.pole[f.pph+j][f.ppx+i]==1: h -= 20
                except IndexError: h -= 20
    
        
    for i,line in enumerate(new_figur):
        for j,el in enumerate(line):
            if el == 1 :
                pph = int((f.h-10+h)/SIZE)
                ppx = int((f.x-10+x)/SIZE)
                if f.pole[pph+j][ppx+i]==1:chek=False

    if chek:
        f.x +=x; f.h+=h
        f.figur = list(zip(*f.figur[::-1])) 
def del_pole():
    for rm in range(20):
        if f.pole[rm] == [1,1,1,1,1,1,1,1,1,1,1]:
            f.pole.pop(rm)
            f.pole.insert(0,[0,0,0,0,0,0,0,0,0,0,1])
def new():
    logic()
    f.figur= f.next
    while f.figur == f.next:
        f.next = d[random.choice(list(d))]
    for i in range(random.randint(0,2)):
        f.next=list(zip(*f.next[::-1]))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(220,50,120,120))
    draw_next()
    f.h = 10
    f.x = 90
    del_pole()
def new_game():
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(0, 0, 350, 450),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(8, 8, 203, 403),1)
    f.pole = [[1 if j==20 or i>=10 else 0 for i in range(11)]for j in range(21)]
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(240, 10, 82, 35),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(240, 10, 82, 35),1)
    img = pygame.image.load('game/Game/smail.jpg').convert()
    rect = img.get_rect()
    rect.center = 309, 27
    screen.blit(img, rect)
    screen.blit(pygame.font.Font(None, 36).render('Next', 1, (255, 255, 255)), (245, 15))
    draw_next();f.x = 90;f.h = 10; f.r = False; f.l = False; f.n = False; f.stop = True
    f.game_over=False

pygame.init()
pygame.display.set_caption("Tetrise")
screen = pygame.display.set_mode((350, 420)) 
d = {'r':[[1,1],[1,1]],
    'l':[[1,1,1,1]],
    't':[[0,1,0],[1,1,1]],
    'h':[[1,1],[1,0],[1,0]],
    'rh':[[1,1],[0,1],[0,1]],
    'p':[[1,0],[1,1],[0,1]],
    'rp':[[0,1],[1,1],[1,0]],}
f = figur()
new_game()
img = pygame.image.load('game/Game/payk.jpg').convert()
rect = img.get_rect()
rect.center = 279, 324
screen.blit(img, rect)

while True:
    if f.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL: new_game()
        pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(40, 175, 139, 35),0)
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(40, 175, 139, 35),1)
        screen.blit(pygame.font.Font(None, 36).render('Game over', 1, (255, 255, 255)), (45, 180))
        pygame.display.update()
        time.sleep(0.1)
    if not f.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    f.l = True
                if event.key == pygame.K_RIGHT:
                    f.r = True
                if event.key == pygame.K_DOWN: 
                    f.n = True
                if event.key == pygame.K_UP:
                    logic_turn()
                if event.key == pygame.K_SPACE:
                    f.stop = False if f.stop else True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    f.l = False
                if event.key == pygame.K_RIGHT:
                    f.r = False
                if event.key == pygame.K_DOWN: 
                    f.n = False
        if f.stop:
            if f.pole[0].count(1)>1:f.game_over = True
            draw_pole()
            draw(f.figur)
            if colision():
                if logic_nize() and f.n: 
                    f.h+=10
                if f.r and logic_left('r'): 
                    f.x+=20
                if f.l and logic_left('l') and f.x > 10:
                    f.x-=20
                f.h+=10
            else: new()
            pygame.display.flip()
            time.sleep(0.1)
        else:
            pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(70, 175, 82, 35),0)
            pygame.draw.rect(screen,(255,255,255),pygame.Rect(70, 175, 82, 35),1)
            screen.blit(pygame.font.Font(None, 36).render('Pause', 1, (255, 255, 255)), (75, 180))
            pygame.display.flip()