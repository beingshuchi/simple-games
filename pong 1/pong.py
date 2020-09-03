import pygame

#variables
WIDTH=1200
HEIGHT=600
BORDER=20
VELOCITY=15
FRAMERATE=35
fgColor=pygame.Color("black")
bgColor=pygame.Color("white")
ballColor=pygame.Color("red")
paddleColor=pygame.Color("grey")

#classes
class Ball:
    RADIUS=20
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    
    def show(self,color):
        global screen
        pygame.draw.circle(screen,color,(self.x,self.y),Ball.RADIUS)
    def update(self):
        global bgColor,ballColor
        
        newx=self.x+self.vx
        newy=self.y+self.vy

        if newx < BORDER+Ball.RADIUS:
            self.vx= -self.vx
        elif newy < BORDER+Ball.RADIUS or newy > HEIGHT-BORDER-Ball.RADIUS:
            self.vy= -self.vy
        elif newx+Ball.RADIUS > WIDTH-Paddle.WIDTH and abs(newy-paddle.y)<Paddle.HEIGHT//2:
            self.vx= -self.vx
        else:
            self.show(bgColor)
            self.x=newx
            self.y=newy
            self.show(ballColor)
class Paddle:
    HEIGHT=100
    WIDTH=20
    def __init__(self,y):
        self.y=y
    def show(self,color):
        global screen
        pygame.draw.rect(screen,color,pygame.Rect(WIDTH-self.WIDTH,self.y-self.HEIGHT/2,self.WIDTH,self.HEIGHT))
    def update(self):
        global bgColor,paddleColor
        self.show(bgColor)
        self.y=pygame.mouse.get_pos()[1]
        self.show(paddleColor)

#create objects
ball=Ball(WIDTH-Ball.RADIUS,HEIGHT//2,-VELOCITY,-VELOCITY)
paddle=Paddle(HEIGHT//2)
#draw the screen
pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(bgColor)
pygame.draw.rect(screen,fgColor,pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen,fgColor,pygame.Rect((0,0,BORDER,HEIGHT)))
pygame.draw.rect(screen,fgColor,pygame.Rect((0,HEIGHT-BORDER,WIDTH,BORDER)))
ball.show(fgColor)
paddle.show(fgColor)
clock=pygame.time.Clock()

while True:
    e=pygame.event.poll()
    if e.type==pygame.QUIT:
        break
    clock.tick(FRAMERATE)
    ball.update()
    paddle.update()
    pygame.display.flip()