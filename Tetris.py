import pygame, sys, random, time, random, math

SIZE = 20
class figur:
    def __init__(self):
        self.next = d[random.choice(list(d))]
        self.figur = d[random.choice(list(d))]
        for i in range(random.randint(0,2)):
            self.next = list(zip(*self.next[::-1]))
            self.figur = list(zip(*self.figur[::-1]))
        self.pole = [[1 if j==20 or i>=10 else 0 for i in range(11)]for j in range(21)]
        self.h = 10
        self.x = 90
        self.pph= 0
        self.ppx= 0
        self.r = False
        self.l = False
        self.n = False
        self.stop = True
        self.game_over=False
        self.scor = 0
        self.time = 0.09

    def new(self):
        self.pph = int((self.h-10)/SIZE)
        self.ppx = int((self.x-10)/SIZE)

def draw(arr):
    for i,line in enumerate(arr):
        for j,el in enumerate(line):
            if el == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(f.x+SIZE*i, f.h+SIZE*j, 19, 19),1)
        
def draw_next():
    f.h = 116; f.x = 241
    w = abs(len(f.next)-4)*10
    h = abs(len(f.next[0])-4)*10
    for i,line in enumerate(f.next):
        for j,el in enumerate(line):
            if el == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(f.x+SIZE*i+w, f.h+SIZE*j+h, 19, 19),1)

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
    pph = int((f.h+10)/SIZE)
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if f.pole[pph+j][ppx+i] == 1: chek = False
    pph = int((f.h)/SIZE)
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
    # новая повёрнутая фигура
    new_figur = list(zip(*f.figur))[::-1]
    chek = True; x = 0; h = 0; l=0
    
    # цикл в котором проверяеться на сколько должна подвинуться фигура по координате x
    for i,line in enumerate(new_figur):
        for j,el in enumerate(line):
            if el == 1 and i > len(f.figur)-1:
                f.pph = int((f.h-10)/SIZE)
                f.ppx = int((f.x-10)/SIZE)
                try:
                    if f.pole[f.pph+j][f.ppx+i]==1: x -= 20
                except IndexError: x -= 20
    
    # цикл в котором проверяеться на сколько должна подвинуться фигура по координате y
    for i,line in enumerate(new_figur):
        for j,el in enumerate(line):
            if el == 1 and j > len(f.figur[0])-1:
                f.pph = int((f.h-10)/SIZE)
                f.ppx = int((f.x-10)/SIZE)
                try:
                    if f.pole[f.pph+j][f.ppx+i]==1: 
                        h -= 20
                        if f.h%20==10:
                            h += 10
                except IndexError: h -= 20
    
    # цикл в котором проверяеться находится ли новая фигура в положении где уже есть фигуры 
    for i,line in enumerate(new_figur):
        for j,el in enumerate(line):
            if el == 1 :
                pph = int((f.h-10+h)/SIZE)
                ppx = int((f.x-10+x)/SIZE)
                if f.pole[pph+j][ppx+i]==1:
                    chek=False
    
    # условие 
    if chek:
        f.x +=x; f.h+=h
        f.figur = list(zip(*f.figur))[::-1]



def del_pole():
    x = 0
    for rm in range(20):
        if f.pole[rm] == [1,1,1,1,1,1,1,1,1,1,1]:
            f.pole.pop(rm)
            f.pole.insert(0,[0,0,0,0,0,0,0,0,0,0,1])
            f.time -= 0.001
            x += 1
    if x == 1:f.scor += 100
    if x == 2:f.scor += 300
    if x == 3:f.scor += 700
    if x == 4:f.scor += 1500
    
def new():
    logic()
    f.figur= f.next
    while f.figur == f.next: f.next = d[random.choice(list(d))]
    for i in range(random.randint(0,2)): f.next=list(zip(*f.next[::-1]))
    pygame.draw.rect(screen,( 0, 0, 0),pygame.Rect(238,115,85,85),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(238,113,85,85),2)
    draw_next(); f.h = 10; f.x = 90; del_pole()
    pygame.draw.rect(screen,( 0, 0, 0),pygame.Rect(230,45,100,25),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(230,43,100,25),2)
    screen.blit(pygame.font.Font(None,30).render("{:7d}".format(f.scor),1,(255, 255, 255)),(240, 46))
    img = pygame.image.load('game\Game\payk.png').convert()
    ect = img.get_rect();rect.center = 279, 324;screen.blit(img, rect)
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(0, 411, 500, 100),0)

def new_game():
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(0, 0, 350, 450),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(8, 8, 203, 403),1)
    f.pole = [[1 if j==20 or i>=10 else 0 for i in range(11)]for j in range(21)]
    
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(230, 45, 100, 25),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(230, 43, 100, 25),2)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(230, 10, 100, 35),2)
    screen.blit(pygame.font.Font(None, 36).render('Score ', 1, (255, 255, 255)), (235, 15))
    img = pygame.image.load('game\Game\star.png').convert()
    rect = img.get_rect();rect.center = 315, 27;screen.blit(img, rect)
    pygame.draw.rect(screen,( 0, 0, 0),pygame.Rect(230,45,100,25),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(230,43,100,25),2)
    screen.blit(pygame.font.Font(None,30).render("{:7d}".format(f.scor),1,(255, 255, 255)),(240, 46))
    
    pygame.draw.rect(screen,( 0, 0, 0),pygame.Rect(238,78,85,35),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(238,80,85,35),2)
    img = pygame.image.load('game\Game\smail.jpg').convert()
    rect = img.get_rect();rect.center = 308, 97;screen.blit(img, rect)
    
    screen.blit(pygame.font.Font(None, 36).render('Next', 1, (255, 255, 255)), (245, 85))
    pygame.draw.rect(screen,( 0, 0, 0),pygame.Rect(238,115,85,85),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(238,113,85,85),2)
    
    img = pygame.image.load('game\Game\payk.png').convert()
    rect = img.get_rect();rect.center = 279, 324;screen.blit(img, rect)
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(0, 411, 500, 100),0)
    draw_next(); f.game_over = False; f.scor = 0; f.time = 0.09
    f.x = 90;f.h = 10; f.r = False; f.l = False; f.n = False; f.stop = True

def game_over():
    pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(42, 175, 139, 35),0)
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(42, 175, 139, 35),2)
    screen.blit(pygame.font.Font(None, 36).render('Game over', 1, (255, 255, 255)), (47, 180))
    pygame.display.update()

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
f = figur(); new_game()
img = pygame.image.load('game\Game\payk.png').convert()
rect = img.get_rect();rect.center = 279, 324;screen.blit(img, rect)
timer = pygame.time.get_ticks(); l = 0

while True:
    if f.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL: new_game()
        game_over()
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
            if f.pole[0].count(1)>1: f.game_over = True
            draw_pole()
            draw(f.figur)
            if colision():
                l = 0
                if logic_nize() and f.n:
                    f.h+=10
                if f.r and logic_left('r'): 
                    f.x+=20
                if f.l and logic_left('l') and f.x > 10:
                    f.x-=20
                f.h+=10
            else:
                if l == 0:
                    timer = pygame.time.get_ticks()
                    l = 1
                if pygame.time.get_ticks()-timer>200:
                    new()
                if f.r and logic_left('r'): 
                    f.x+=20
                if f.l and logic_left('l') and f.x > 10:
                    f.x-=20
            pygame.display.flip()
            time.sleep(f.time)
        else:
            pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(70, 175, 82, 35),0)
            pygame.draw.rect(screen,(255,255,255),pygame.Rect(70, 175, 82, 35),2)
            screen.blit(pygame.font.Font(None, 36).render('Pause', 1, (255, 255, 255)), (75, 180))
            pygame.display.flip()