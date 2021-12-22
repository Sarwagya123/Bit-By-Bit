import pygame 
import random #to randomize the pipes
pygame.init() #initialize all the modules

#now to have a screen to play the game lets make a screen
w,h=300,500
screen=pygame.display.set_mode((w,h)) #o set the screen size
pygame.display.set_caption("Jumping Santa")
icon=pygame.image.load("images/SANTA.png")
pygame.display.set_icon(icon)
#when we run the above code it jus appears for 1 sec and then closes

bg=pygame.image.load("images/snowfall.png")
bg=pygame.transform.scale(bg,(w,h))#resizes the background image to the size of the screen to fit it in the game window

base=pygame.image.load("images/base.png")

die_sound=pygame.mixer.Sound("sounds/die.wav")
point_sound=pygame.mixer.Sound("sounds/point.wav")
wing_sound=pygame.mixer.Sound("sounds/wing.wav")





class Santa:

    def __init__(self, pos):
        self.image=pygame.image.load("images/SANTA.png")
        self.image=pygame.transform.scale(self.image,(34,34))
        self.rect=self.image.get_rect() #it makes the topleft corner of the rectange (0,0)
        self.rect.x,self.rect.y=pos
        self.vel=5
        self.jump=False #whether my santa iis in jump state or not
        self.score=0

    def draw(self,screen):
        screen.blit(self.image,self.rect)

    def move(self):
        if self.jump:
            self.rect.y-=self.vel
        else:
            self.rect.y+=self.vel
        if self.rect.bottom>400:
            self.rect.bottom=400
        if self.rect.top<0:
            self.rect.top=0

    def collide(self,pipes):
        return self.rect.colliderect(pipes.trect) or self.rect.colliderect(pipes.brect)

            

class Pipes:
    def __init__(self,pos):
        self.top_pipe = pygame.image.load("images/pipe-up.png")
        self.bottom_pipe=pygame.image.load("images/pipe-down.png")
        self.trect=self.top_pipe.get_rect()
        self.brect=self.bottom_pipe.get_rect()
        self.trect.x,self.trect.y=pos
        self.brect.x,self.brect.y=self.trect.x, self.trect.bottom+110
        self.vel=5

    def draw(self,screen):
        screen.blit(self.top_pipe,self.trect)
        screen.blit(self.bottom_pipe,self.brect)

    def move(self,santa):
        self.trect.x-=self.vel
        self.brect.x-=self.vel

        if self.trect.right<0:
            self.trect.x=300
            self.brect.x=300
            self.trect.y=random.randint(-150, -50)#to change the gap between the pipes
            self.brect.y=self.trect.bottom+110 #random.choice([50,70]) incase of random gaps jus use this
            santa.score+=1
            point_sound.play()




FPS=50
clock=pygame.time.Clock()

font=pygame.font.SysFont("Arial",32,True)

def display_score(screen,score):
    text_surface=font.render(f"Score: {score}",True,(0,0,0))
    screen.blit(text_surface,(10,10))


gameover_png=pygame.image.load("images/gameover.png")
def gameover(screen, s):
    run=True
    while run:

    
        screen.blit(bg,(0,0))#to bring something onto ur screen we use blit here background image
        
        screen.blit(gameover_png,(60,100))
        clock.tick(FPS)#to control the no. of times the loop executes in 1 sec
        #we blitted the base after bg becoz we want base above bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when the user presses cross it will get quit
                run=False

        display_score(screen,s.score)
        pygame.display.update()




def gamestart(screen):

    s=Santa([100,250])

    pipe_pos=[200,-100]
    p=Pipes(pipe_pos)   

    run=True
    while run:

        

    
        screen.blit(bg,(0,0))#to bring something onto ur screen we use blit here background image
        
        clock.tick(FPS)#to control the no. of times the loop executes in 1 sec
        #we blitted the base after bg becoz we want base above bg

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #whe the user presses cross it will get quit
                run=False

            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                s.jump=True
                wing_sound.play()
                

            if event.type==pygame.KEYUP and event.key==pygame.K_SPACE:#key up means the key is released and here its space as specified by the second condition
                s.jump=False
                           

        s.move()
        p.move(s)

        if s.collide(p):
            die_sound.play()
            gameover(screen,s)
            run=False

        p.draw(screen)
        s.draw(screen)
        display_score(screen,s.score)
        screen.blit(base,(0,400))#to bring the base of the game on to the screen 
        pygame.display.update()#to update the display everytime

intro = pygame.image.load("images/intro.png")
sky_blue=(63,164,193)

#therefore now we will write code to hold that screen for infinite time until the user quits it
run=True
while run:

    screen.fill(sky_blue)
    screen.blit(intro,(50,100))#to bring something onto ur screen we use blit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #whe the user presses cross it will get quit
            print("QUIT")
            run=False

        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:#1 represents left click
            gamestart(screen)
        
    pygame.display.update()#to update the display everytime