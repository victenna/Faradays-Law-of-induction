import pygame,sys

pygame.init()
screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()
BLACK=(255,255,255)
font = pygame.font.SysFont("Ubuntu Condensed", 35)
text = font.render('Open switch' , True , (255,255,255))
text1 = font.render('Close switch' , True , (255,255,255))

Q=6
images=['img0.png','img1.png','img2.png','img3.png','img4.png','img5.png']
x,y=[500,510,391,850,850,850],[450,305,601,300,300,300]
img=[0]*Q
rect=[0]*Q
a,angle,i=0,0,0
X,Y=800,700# start_stop button position
a1=0
def button():
    global a
    global a1
    mouse=pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
        if abs(mouse[0] - (X+100))<50 and abs(mouse[1] - (Y+10)) <50:
            a=a+1
            a1=a%2
def position(m):
    base(1,850,450,0)
    base(2,50,70,0)
    base(m,200,200,0)
    base(0,470,470,0)

def base(i,scalex,scaley,angle):
    img[i]=pygame.image.load(images[i])
    img[i]=pygame.transform.scale(img[i],(scalex,scaley))
    img[i]=pygame.transform.rotate(img[i],angle)
    rect[i]=img[i].get_rect(center=(x[i],y[i]))
    screen.blit(img[i],rect[i])
j=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        button()
    screen.fill('grey')
    base(0,470,470,0)
    pygame.draw.rect(screen,(183,168,249), (X, Y,200,50))

    if a1==0 :
        screen.blit(text,(X+20,Y+10))
        position(4)
        x[2],y[2]=391,601 # swith is closed
        
    if a1==1:
        j=0
        screen.blit(text1,(X+20,Y+10))
        i=i+1
        i1=i
        if i1<5:
            x[2],y[2]=391,615 #switch is open
            x[1],y[1]=510,305 #field
            position(3)
        if i1>4 :
            position(5)
            x[2],y[2]=391,615 #switch is open
            x[1]=3000 #no field
    print('a1=',a1)    
    if a1==0:
        i=0
        j=j+1
        if j<5:
            x[2],y[2]=391,601 #switch is closed
            x[1],y[1]=510,305 #field
            position(3)
        if j>4 :
            position(4)
            x[2],y[2]=391,601 #switch is closed
    clock.tick(300)
    pygame.display.update()


