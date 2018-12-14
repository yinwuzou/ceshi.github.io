import sys,pygame,random,time
from pygame.locals import *
red=pygame.Color(255,0,0)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)
def gameOver(playSurface):
    gameOverFont=pygame.font.Font('arial.ttf',72)
    gameOverSurf=gameOverFont.render('Game over',True,red)
    gameOverRect=gameOverSurf.get_rect()
    gameOverRect.midtop=(320,10)#????
    playSurface.blit(gameOverSurf,gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
def main():
    pygame.init()
    fpsClock=pygame.time.Clock()
    playSurface=pygame.display.set_mode((640,480))
    pygame.display.set_caption('mygame')
    snakePosition=[100,100]
    snakeSegments=[[100,100],[80,100],[60,100]]
    raspberryPosition=[300,300]
    raspberrySpawned=1
    direction='right'
    changDirection=direction
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT or event.key==ord('d'):
                    changDirection='right'
                if event.key==K_LEFT or event.key==ord('a'):
                    changDirection='left'
                if event.key==K_UP or event.key==ord('w'):
                    changDirection='up'
                if  event.key==K_DOWN or event.key==ord('s'):
                    changDirection='down'
                if event.key==K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if changDirection=='right'and not direction=='left':
                direction=changDirection
            if changDirection=='left'and not direction=='right':
                direction=changDirection
            if changDirection=='up' and not direction=='down':
                direction=changDirection
            if changDirection=='down' and not direction=='up':
                direction=changDirection
            if direction=='right':
                snakePosition[0]+=20
            if direction=='left':
                snakePosition[0]-=20
            if direction=='up':
                snakePosition[1]-=20
            if direction=='down':
                snakePosition[1]+=20
            snakeSegments.insert(0,list(snakePosition))#?????
            if snakePosition[0]==raspberryPosition[0] and snakePosition[1]==raspberryPosition[1]:
                raspberrySpawned=0
            else:
                snakeSegments.pop()#?????
            if raspberrySpawned==0:
                x=random.randrange(1,32)
                y=random.randrange(1,24)
                raspberryPosition=[int(x*20),int(y*20)]
                raspberrySpawned=1
            playSurface.fill(black)
            for position in snakeSegments:
                pygame.draw.rect(playSurface,white,Rect(position[0],position[1],20,20))
                pygame.draw.rect(playSurface,red,Rect(raspberryPosition[0],raspberryPosition[1],20,20))
            pygame.display.flip()
            if snakePosition[0]>620 or snakePosition[0]<0:
                gameOver(playSurface)
            if snakePosition[1]>460 or snakePosition[1]<0:
                for snakeBody in snakeSegments[1:]:
                    if snakePosition[0]==snakeBody[0] and snakePosition[1]==snakeBody[1]:
                        gameOver(playSurface)
            fpsClock.tick(5)
if __name__=="__main__":
    main()
