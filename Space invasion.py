import pygame,sys
pygame.init()
WIDTH,HEIGHT=900,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space invasion")
screen.fill("white")
spaceimg=pygame.image.load("starsbg.png")
space=pygame.transform.scale(spaceimg,(WIDTH,HEIGHT))
yellowhealth=10
redhealth=10
healthfont=pygame.font.SysFont('comicsans',40)
winnerfont=pygame.font.SysFont('comicsans',100)
border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
redspaceship=pygame.image.load("spaceship1.png")
sw,sh=55,40
redship=pygame.transform.scale(redspaceship,(sw,sh))
redship1=pygame.transform.rotate(redship,90)
yellowspaceship=pygame.image.load("spaceship2.png")
yellowship=pygame.transform.scale(yellowspaceship,(sw,sh))
yellowship1=pygame.transform.rotate(yellowship,270)
pygame.display.update()
def draw(red,yellow):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",border)
    yellowhealthtext=healthfont.render('Health:'+str(yellowhealth),1,'yellow')
    redhealthtext=healthfont.render('Health:'+str(redhealth),1,'red')
    screen.blit(yellowhealthtext,(WIDTH-yellowhealthtext.get_width()-250,10))
    screen.blit(redhealthtext,(10,10))
    screen.blit(redship1,(red.x,red.y))
    screen.blit(yellowship1,(yellow.x,yellow.y))
    pygame.display.update()
VEL=5
def yellowmovement(keys_pressed,yellow):
    if keys_pressed[pygame.K_UP]:
        yellow.y-=VEL
    if keys_pressed[pygame.K_DOWN]:
        yellow.y+=VEL
    if keys_pressed[pygame.K_LEFT]:
        yellow.x-=VEL
    if keys_pressed[pygame.K_RIGHT]:
        yellow.x+=VEL
def yellowmovement(keys_pressed,yellow):
    if keys_pressed[pygame.K_UP]:
        yellow.y-=VEL
    if keys_pressed[pygame.K_DOWN]:
        yellow.y+=VEL
    if keys_pressed[pygame.K_LEFT]:
        yellow.x-=VEL
    if keys_pressed[pygame.K_RIGHT]:
        yellow.x+=VEL
def main():
    red=pygame.Rect(100,250,sw,sh)
    yellow=pygame.Rect(800,250,sw,sh)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        keys_pressed=pygame.key.get_pressed()
        yellowmovement(keys_pressed,yellow)
        draw(red,yellow)
        pygame.display.update()
if __name__=="__main__":
    main()
