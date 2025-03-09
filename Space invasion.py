import pygame,sys
pygame.init()
WIDTH,HEIGHT=900,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space invasion")
screen.fill("white")
maxbullets= 3
bulletvl = 10
spaceimg=pygame.image.load("starsbg.png")
space=pygame.transform.scale(spaceimg,(WIDTH,HEIGHT))
healthfont=pygame.font.SysFont('comicsans',40)
winnerfont=pygame.font.SysFont('comicsans',100)
border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
redspaceship=pygame.image.load("spaceship1.png")
yellowhit=pygame.USEREVENT + 1
redhit=pygame.USEREVENT + 2
sw,sh=55,40
redship=pygame.transform.scale(redspaceship,(sw,sh))
redship1=pygame.transform.rotate(redship,90)
yellowspaceship=pygame.image.load("spaceship2.png")
yellowship=pygame.transform.scale(yellowspaceship,(sw,sh))
yellowship1=pygame.transform.rotate(yellowship,270)
pygame.display.update()
def draw(red,yellow,yellowhealth,redhealth,redbullets,yellowbullets):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",border)
    yellowhealthtext=healthfont.render('Health:'+str(yellowhealth),1,'yellow')
    redhealthtext=healthfont.render('Health:'+str(redhealth),1,'red')
    screen.blit(yellowhealthtext,(WIDTH-yellowhealthtext.get_width()-250,10))
    screen.blit(redhealthtext,(10,10))
    screen.blit(redship1,(red.x,red.y))
    screen.blit(yellowship1,(yellow.x,yellow.y))
    for bullet in redbullets:
        pygame.draw.rect(screen,"red",bullet)
    for bullet in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullet)
    pygame.display.update()
VEL=5
def yellowmovement(keys_pressed,yellow):
    if keys_pressed[pygame.K_UP] and yellow.y > 0:
        yellow.y-=VEL
    if keys_pressed[pygame.K_DOWN] and yellow.y + yellow.height < HEIGHT:
        yellow.y+=VEL
    if keys_pressed[pygame.K_LEFT] and yellow.x > border.x + border.width:
        yellow.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and yellow.x + yellow.width < WIDTH:
        yellow.x+=VEL
def redmovement(keys_pressed,red):
    if keys_pressed[pygame.K_s] and red.y + red.height < HEIGHT:
        red.y+=VEL
    if keys_pressed[pygame.K_w] and red.y > 0:
        red.y-=VEL
    if keys_pressed[pygame.K_a] and red.x > 0:
        red.x-=VEL
    if keys_pressed[pygame.K_d] and red.x + red.width < border.x:
        red.x+=VEL
def movebullets(yellowbullets,redbullets,red,yellow):
    for bullet in yellowbullets:
        bullet.x -= bulletvl
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(redhit))
            yellowbullets.remove(bullet)
        elif bullet.x < 0:
            yellowbullets.remove(bullet)
    for bullet in redbullets:
        bullet.x += bulletvl
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellowhit))
            redbullets.remove(bullet)
        elif bullet.x > WIDTH:
            redbullets.remove(bullet)
def drawwinner(abc):
    text = winnerfont.render(abc,1,"orange")
    screen.blit(text,(WIDTH/2 - text.get_width()/2,HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
def main():
    red=pygame.Rect(100,250,sw,sh)
    yellow=pygame.Rect(800,250,sw,sh)
    redbullets=[]
    yellowbullets=[]
    yellowhealth=10
    redhealth=10
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and len(redbullets) < maxbullets:
                    bullet = pygame.Rect(red.x,red.y + red.height/2,10,5)
                    redbullets.append(bullet)
                if event.key == pygame.K_l and len(yellowbullets) < maxbullets:
                    bullet = pygame.Rect(yellow.x,yellow.y + yellow.height/2,10,5)
                    yellowbullets.append(bullet)
            if event.type == redhit:
                redhealth -= 1
            if event.type == yellowhit:
                yellowhealth -= 1
        winnertext=""
        if redhealth <= 0:
            winnertext="Yellow wins!"
        if yellowhealth <= 0:
            winnertext="Red wins!"
        if winnertext != "":
            drawwinner(winnertext)
            break
        keys_pressed=pygame.key.get_pressed()
        yellowmovement(keys_pressed,yellow)
        redmovement(keys_pressed,red)
        movebullets(yellowbullets,redbullets,red,yellow)
        draw(red,yellow,yellowhealth,redhealth,redbullets,yellowbullets)
        pygame.display.update()
if __name__=="__main__":
    main()
