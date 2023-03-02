import pygame, sys, random, time, random

SIZE = 20

class figur:
    def __init__(self):
        self.next = d[random.choice(list(d))]
        self.figur = d[random.choice(list(d))]
        for i in range(random.randint(0,2)):
            self.next = list(zip(*self.next[::-1]))
            self.figur = list(zip(*self.figur[::-1]))
        self.h = 10; self.x = 90
        self.pph= 0; self.ppx= 0
    def new(self):
        self.pph = int((self.h-10)/SIZE)
        self.ppx = int((self.x-10)/SIZE)

def draw(arr):
    for i,line in enumerate(arr):
        for j,el in enumerate(line):
            if el == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(f.x+SIZE*i, f.h+SIZE*j, 19, 19),1)

def draw_next():
    f.h = 40; f.x = 250
    for i,line in enumerate(f.next):
        for j,el in enumerate(line):
            if el == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(f.x+SIZE*i, f.h+SIZE*j, 19, 19),1)

def draw_pole():
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(9, 9, 200, 400))
    for i in range(len(pole)-1):
        for j in range(len(pole[i])-1):
            if pole[i][j] == 1:
                pygame.draw.rect(screen,(255,255,255),pygame.Rect(10+SIZE*j, 10+SIZE*i, 19, 19),1)

def colision():
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if pole[f.pph+j+1][f.ppx+i] == 1: return False
    return True

def logic():
    for i in range(len(f.figur)):
        for j in range(len(f.figur[i])):
            if f.figur[i][j] == 1:f.new();pole[f.pph+j][f.ppx+i] = 1
    

def logic_left(direction):
    if direction == 'l': m =- 1
    else : m = 1
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if pole[f.pph+j][f.ppx+i+m] == 1: return False
    return True

def logic_n():
    for i,line in enumerate(f.figur):
        for j,el in enumerate(line):
            if el == 1:
                f.new()
                if pole[f.pph+j+1][f.ppx+i] == 1: return False
    return True

def del_pole():
    for rm in range(20):
        if pole[rm] == aaa:
            pole.pop(rm)
            pole.insert(0,[0,0,0,0,0,0,0,0,0,0,1])

def new():
    logic()
    f.figur= f.next
    f.next = d[random.choice(list(d))]
    for i in range(random.randint(0,2)):f.next=list(zip(*f.next[::-1]))
    pygame.draw.rect(screen,( 0, 0, 0),pygame.Rect(220, 0,200,400))
    draw_next(); f.h = 10;f.x = 90; del_pole()

d = {'r':[[1,1],[1,1]],'l':[[1,1,1,1]],'t':[[0,1,0],[1,1,1]],'h':[[1,1],[1,0],[1,0]],
    'rh':[[1,1],[0,1],[0,1]],'p':[[1,0],[1,1],[0,1]],'rp':[[0,1],[1,1],[1,0]],}

pygame.init()
screen = pygame.display.set_mode((350, 420)) 
pygame.draw.rect(screen,(  0,  0,  0),pygame.Rect(0, 0, 350, 450),0)
pygame.draw.rect(screen,(255,255,255),pygame.Rect(8, 8, 203, 403),1)

pole = [[1 if j==20 or i>=10 else 0 for i in range(11)]for j in range(21)]
f = figur()
draw_next()
f.x = 90; f.h = 10

aaa = [1,1,1,1,1,1,1,1,1,1,1]; r = False; l = False; n = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: l = True
            if event.key == pygame.K_RIGHT:r = True
            if event.key == pygame.K_DOWN: n = True
            if event.key == pygame.K_UP:
                f.figur = list(zip(*f.figur[::-1]))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: l = False
            if event.key == pygame.K_RIGHT:r = False
            if event.key == pygame.K_DOWN: n = False
    if logic_n() and n: f.h+=10
    if logic_left('r')and r: f.x+=20
    if logic_left('l')and l and f.x>10:f.x-=20
    draw_pole()
    draw(f.figur)
    if colision(): f.h+=10
    else: new()
    pygame.display.flip()
    time.sleep(0.1)