import pygame  
from time import *
from random import *
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill((255,215,0))
clock=pygame.time.Clock()
'''o=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(xbul,ybul,5,5))'''
x=338
y=400





move_a=False
move_d=False
move_s=False
move_w=False

tttt=0

ygo=0
xgo=0
xbul=-8
ybul=-8

tb=0
tbos=time()
x_bos=338
y_bos=15
time_bos=3
rand_bos=0

xdb=-30
ydb=-30
xsb=-30
ysb=-30
xab=-30
yab=-30
xwb=-30
ywb=-30
xdsb=-30
ydsb=-30
xasb=-30
yasb=-30
xwab=-30
ywab=-30
xwdb=-30
ywdb=-30

xdb_go=0
ydb_go=0
xsb_go=0
ysb_go=0
xab_go=0
yab_go=0
xwb_go=0
ywb_go=0
xdsb_go=0
ydsb_go=0
xasb_go=0
yasb_go=0
xwab_go=0
ywab_go=0
xwdb_go=0
ywdb_go=0

bx1=-8000
bx2=-8000
bx3=-8000
bx4=-8000
bx5=-8000
bx6=-8000
bx7=-8000
bx8=-8000
bx9=-8000
bx10=-8000
bx11=-8000
bx12=-8000
bx13=-8000
bx14=-8000
bx15=-8000
bx16=-8000
bx17=-8000
bx18=-8000
bx19=-8000
bx20=-8000

by1=-8000
by2=-8000
by3=-8000
by4=-8000
by5=-8000
by6=-8000
by7=-8000
by8=-8000
by9=-8000
by10=-8000
by11=-8000
by12=-8000
by13=-8000
by14=-8000
by15=-8000
by16=-8000
by17=-8000
by18=-8000
by19=-8000
by20=-8000


ex1=-8000
ex2=-8000
ex3=-8000
ex4=-8000

ey1=-8000
ey2=-8000
ey3=-8000
ey4=-8000

ex1_go=0
ex2_go=0
ex3_go=0
ex4_go=0

ey1_go=0
ey2_go=0
ey3_go=0
ey4_go=0

bos_hp=100
tim2=pygame.font.SysFont('Arial', 20).render(str(bos_hp),True,(0,0,0)) 



while tttt< 3:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            ttb=time()
            tttb=ttb-tb
            if tttb>=0.5:                
                xb,yb=event.pos
                xll=x+12.5
                yll=y+25
                if xll<xb and yll <yb:               
                    tt1=xll-xb
                    tt2=yll-yb
                    tt3=tt1/tt2
                    ygo=20/(tt3+1)
                    xgo=20-ygo
                    xbul=xll
                    ybul=yll
                    
                    
                elif xll>xb and yll >yb:               
                    tt1=xll-xb
                    tt2=yll-yb
                    tt3=tt1/tt2
                    ygo=20/(tt3+1)
                    xgo=20-ygo
                    xgo=xgo*-1
                    ygo=ygo*-1
                    xbul=xll
                    ybul=yll
                    
                elif xll<xb and yll >yb:               
                    tt1=xb-xll
                    tt2=yll-yb
                    tt3=tt1/tt2
                    ygo=20/(tt3+1)
                    xgo=20-ygo
                    ygo=ygo*-1
                    xbul=xll
                    ybul=yll
                elif xll>xb and yll <yb:               
                    tt1=xll-xb
                    tt2=yb-yll
                    tt3=tt1/tt2
                    ygo=20/(tt3+1)
                    xgo=20-ygo
                    xgo=xgo*-1
                    xbul=xll
                    ybul=yll
                tb=time()
            
                
        
        if event.type == pygame.KEYDOWN: 
            if event.key==pygame.K_a:
                move_a=True
            if event.key==pygame.K_d:
                move_d=True
            if event.key==pygame.K_w:
                move_w=True
            if event.key==pygame.K_s:
                move_s=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_a:
                move_a=False
            if event.key==pygame.K_d:
                move_d=False
            if event.key==pygame.K_w:
                move_w=False
            if event.key==pygame.K_s:

                move_s=False
    screen.fill((255,215,0))

    if move_a==True and x>0:
        x-=2
    if move_d==True and x<475:
        x+=2
    if move_s==True and y<450:
        y+=2
    if move_w==True and y >0:
        y-=2
    
    xbul+=xgo
    ybul+=ygo

    ttbos=time()
    tttbos=ttbos-tbos
    if tttbos>=2.5:
        x_bos=randint(0,425)
        y_bos=randint(0,450)
        tbos=time()
        time_bos+=1


    if time_bos==4:
        xdb=-8000
        ydb=-8000
        xsb=-8000
        ysb=-8000
        xab=-8000
        yab=-8000
        xwb=-8000
        ywb=-8000
        xdsb=-8000
        ydsb=-8000
        xasb=-8000
        yasb=-8000
        xwab=-8000
        ywab=-8000
        xwdb=-8000
        ywdb=-8000

        ex1=-8000
        ex2=-8000
        ex3=-8000
        ex4=-8000

        ey1=-8000
        ey2=-8000
        ey3=-8000
        ey4=-8000
    
    rand_bos=randint(1,3)
    if time_bos==4:        
        time_bos=0
        if rand_bos==1:
            rand_bos=randint(1,3)

            xdb_go=3
            ydb_go=3
            xsb_go=3
            ysb_go=3
            xab_go=3
            yab_go=3
            xwb_go=3
            ywb_go=3
            xdsb_go=1.5
            ydsb_go=1.5
            xasb_go=1.5
            yasb_go=1.5
            xwab_go=1.5
            ywab_go=1.5
            xwdb_go=1.5
            ywdb_go=1.5


            xdb=x_bos
            ydb=y_bos
            xsb=x_bos
            ysb=y_bos
            xab=x_bos
            yab=y_bos
            xwb=x_bos
            ywb=y_bos
            xdsb=x_bos
            ydsb=y_bos
            xasb=x_bos
            yasb=y_bos
            xwab=x_bos
            ywab=y_bos
            xwdb=x_bos
            ywdb=y_bos
        elif rand_bos==2:
            x_bos=0
            y_bos=0

            bx1=x_bos
            bx2=x_bos
            bx3=x_bos
            bx4=x_bos
            bx5=x_bos
            bx6=x_bos
            bx7=x_bos
            bx8=x_bos
            bx9=x_bos
            bx10=x_bos
            bx11=x_bos
            bx12=x_bos
            bx13=x_bos
            bx14=x_bos
            bx15=x_bos
            bx16=x_bos
            bx17=x_bos
            bx18=x_bos
            bx19=x_bos
            bx20=x_bos


            by1=y_bos
            by2=y_bos
            by3=y_bos
            by4=y_bos
            by5=y_bos
            by6=y_bos
            by7=y_bos
            by8=y_bos
            by9=y_bos
            by10=y_bos
            by11=y_bos
            by12=y_bos
            by13=y_bos
            by14=y_bos
            by15=y_bos
            by16=y_bos
            by17=y_bos
            by18=y_bos
            by19=y_bos
            by20=y_bos
        elif rand_bos==3:
            x_bos=225
            y_bos=200

            ex1=100
            ey1=75

            ex2=100
            ey2=325

            ex3=350
            ey3=75

            ex4=350
            ey4=325



    bx1+=0.1
    bx2+=0.2
    bx3+=0.3
    bx4+=0.4
    bx5+=0.5
    bx6+=0.6
    bx7+=0.7
    bx8+=0.8
    bx9+=0.9
    bx10+=1
    bx11+=1.1
    bx12+=1.2
    bx13+=1.3
    bx14+=1.4
    bx15+=1.5
    bx16+=1.6
    bx17+=1.7
    bx18+=1.8
    bx19+=1.9
    bx20+=2

    by1+=2
    by2+=1.9
    by3+=1.8
    by4+=1.7
    by5+=1.6
    by6+=1.5
    by7+=1.4
    by8+=1.3
    by9+=1.2
    by10+=1.1
    by11+=1
    by12+=0.9
    by13+=0.8
    by14+=0.7
    by15+=0.6
    by16+=0.5
    by17+=0.4
    by18+=0.3
    by19+=0.2
    by20+=0.1


    



    xdb+=xdb_go
    ysb+=ysb_go
    xab-=xab_go
    ywb-=ywb_go
    xdsb+=xdsb_go
    ydsb+=ydsb_go
    xasb-=xasb_go
    yasb+=yasb_go
    xwab-=xwab_go
    ywab-=ywab_go
    xwdb+=xwdb_go
    ywdb-=ywdb_go

    if xdb>=475 or xdb<=0:
        xdb_go*=-1
    if xsb>=475 or xsb<=0:
        xsb_go*=-1   
    if xab>=475 or xab<=0:
        xab_go*=-1       
    if xwb>=475 or xwb<=0:
        xwb_go*=-1  
    if ydb>=475 or ydb<=0:
        ydb_go*=-1
    if ysb>=475 or ysb<=0:
        ysb_go*=-1
    if yab>=475 or yab<=0:
        yab_go*=-1
    if ywb>=475 or ywb<=0:
        ywb_go*=-1
    if xdsb>=475 or xdsb<=0:
        xdsb_go*=-1
    if xasb>=475 or xasb<=0:
        xasb_go*=-1
    if xwdb>=475 or xwdb<=0:
        xwdb_go*=-1
    if xwab>=475 or xwab<=0:
        xwab_go*=-1
    if ydsb>=475 or ydsb<=0:
        ydsb_go*=-1
    if yasb>=475 or yasb<=0:
        yasb_go*=-1
    if ywdb>=475 or ywdb<=0:
        ywdb_go*=-1
    if ywab>=475 or ywab<=0:
        ywab_go*=-1



    xll=x+12.5
    yll=y+25

    if ex1<xll and ey1 <yll:               
        tt1=ex1-xll
        tt2=ey1-yll
        tt3=tt1/tt2
        ey1_go=1/(tt3+1)
        ex1_go=1-ey1_go
                    
    elif ex1>xll and ey1 >yll:               
        tt1=ex1-xll
        tt2=ey1-yll
        tt3=tt1/tt2
        ey1_go=1/(tt3+1)
        ex1_go=1-ey1_go
        ex1_go*=-1
        ey1_go=ey1_go*-1

    elif ex1<xll and ey1 >yll:               
        tt1=xll-ex1
        tt2=ey1-yll
        tt3=tt1/tt2
        ey1_go=1/(tt3+1)
        ex1_go=1-ey1_go
        ey1_go=ey1_go*-1

    elif ex1>xll and ey1 <yll:               
        tt1=ex1-xll
        tt2=yll-ey1
        tt3=tt1/tt2
        ey1_go=1/(tt3+1)
        ex1_go=1-ey1_go
        ex1_go=ex1_go*-1



    if ex2<xll and ey2 <yll:               
        tt1=ex2-xll
        tt2=ey2-yll
        tt3=tt1/tt2
        ey2_go=1/(tt3+1)
        ex2_go=1-ey2_go
                    
    elif ex2>xll and ey2 >yll:               
        tt1=ex2-xll
        tt2=ey2-yll
        tt3=tt1/tt2
        ey2_go=1/(tt3+1)
        ex2_go=1-ey2_go
        ex2_go*=-1
        ey2_go=ey2_go*-1

    elif ex2<xll and ey2 >yll:               
        tt1=xll-ex2
        tt2=ey2-yll
        tt3=tt1/tt2
        ey2_go=1/(tt3+1)
        ex2_go=1-ey2_go
        ey2_go=ey2_go*-1

    elif ex2>xll and ey2 <yll:               
        tt1=ex2-xll
        tt2=yll-ey2
        tt3=tt1/tt2
        ey2_go=1/(tt3+1)
        ex2_go=1-ey2_go
        ex2_go=ex2_go*-1




    if ex3<xll and ey3 <yll:               
        tt1=ex3-xll
        tt2=ey3-yll
        tt3=tt1/tt2
        ey3_go=1/(tt3+1)
        ex3_go=1-ey3_go
                    
    elif ex3>xll and ey3 >yll:               
        tt1=ex3-xll
        tt2=ey3-yll
        tt3=tt1/tt2
        ey3_go=1/(tt3+1)
        ex3_go=1-ey3_go
        ex3_go*=-1
        ey3_go=ey3_go*-1

    elif ex3<xll and ey3 >yll:               
        tt1=xll-ex3
        tt2=ey3-yll
        tt3=tt1/tt2
        ey3_go=1/(tt3+1)
        ex3_go=1-ey3_go
        ey3_go=ey3_go*-1

    elif ex3>xll and ey3 <yll:               
        tt1=ex3-xll
        tt2=yll-ey3
        tt3=tt1/tt2
        ey3_go=1/(tt3+1)
        ex3_go=1-ey3_go
        ex3_go=ex3_go*-1

    if ex4<xll and ey4 <yll:               
        tt1=ex4-xll
        tt2=ey4-yll
        tt3=tt1/tt2
        ey4_go=1/(tt3+1)
        ex4_go=1-ey4_go
                    
    elif ex4>xll and ey4 >yll:               
        tt1=ex4-xll
        tt2=ey4-yll
        tt3=tt1/tt2
        ey4_go=1/(tt3+1)
        ex4_go=1-ey4_go
        ex4_go*=-1
        ey4_go=ey4_go*-1

    elif ex4<xll and ey4 >yll:               
        tt1=xll-ex4
        tt2=ey4-yll
        tt3=tt1/tt2
        ey4_go=1/(tt3+1)
        ex4_go=1-ey4_go
        ey4_go=ey4_go*-1

    elif ex4>xll and ey4 <yll:               
        tt1=ex4-xll
        tt2=yll-ey4
        tt3=tt1/tt2
        ey4_go=1/(tt3+1)
        ex4_go=1-ey4_go
        ex4_go=ex4_go*-1






        

    ex1+=ex1_go
    ey1+=ey1_go

    ex2+=ex2_go
    ey2+=ey2_go

    ex3+=ex3_go
    ey3+=ey3_go

    ex4+=ex4_go
    ey4+=ey4_go

    hero=pygame.draw.rect(screen,((63,72,204)),pygame.Rect(x,y,25,50))
    bulet=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(xbul,ybul,5,5))
    bos=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(x_bos,y_bos,25,50))
    

    db=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xdb,ydb,25,25))
    sb=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xsb,ysb,25,25))
    ab=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xab,yab,25,25))
    wb=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xwb,ywb,25,25))
    dsb=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xdsb,ydsb,25,25))
    asb=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xasb,yasb,25,25))
    wab=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xwab,ywab,25,25))
    wdb=pygame.draw.rect(screen,((0,70,0)),pygame.Rect(xwdb,ywdb,25,25))


    bulet_bos1=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx1,by1,5,5))
    bulet_bos2=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx2,by2,5,5))
    bulet_bos3=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx3,by3,5,5))
    bulet_bos4=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx4,by4,5,5))
    bulet_bos5=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx5,by5,5,5))
    bulet_bos6=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx6,by6,5,5))
    bulet_bos7=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx7,by7,5,5))
    bulet_bos8=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx8,by8,5,5))
    bulet_bos9=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx9,by9,5,5))
    bulet_bos10=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx10,by10,5,5))
    bulet_bos11=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx11,by11,5,5))
    bulet_bos12=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx12,by12,5,5))
    bulet_bos13=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx13,by13,5,5))
    bulet_bos14=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx14,by14,5,5))
    bulet_bos15=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx15,by15,5,5))
    bulet_bos16=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx16,by16,5,5))
    bulet_bos17=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx17,by17,5,5))
    bulet_bos18=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx18,by18,5,5))
    bulet_bos19=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx19,by19,5,5))
    bulet_bos20=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(bx20,by20,5,5))

    mana1=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(ex1,ey1,20,20))
    mana2=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(ex2,ey2,20,20))
    mana3=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(ex3,ey3,20,20))
    mana4=pygame.draw.rect(screen,((80,0,0)),pygame.Rect(ex4,ey4,20,20))

    if bulet.colliderect(bos):
        bos_hp-=1
        xbul=-8000
        ybul=-8000
    if bos_hp<=0:
        tttt=5

    pppp=bos_hp/100
    hp_hp=pygame.draw.rect(screen,((10,70,30)),pygame.Rect(50,5,pppp*400,10))

    if mana1.colliderect(hero):
        tttt=5
    if mana2.colliderect(hero):
        tttt=5
    if mana3.colliderect(hero):
        tttt=5
    if mana4.colliderect(hero):
        tttt=5
    if db.colliderect(hero):
        tttt=5
    if sb.colliderect(hero):
        tttt=5
    if ab.colliderect(hero):
        tttt=5
    if wb.colliderect(hero):
        tttt=5
    if dsb.colliderect(hero):
        tttt=5
    if asb.colliderect(hero):
        tttt=5
    if wab.colliderect(hero):
        tttt=5
    if wdb.colliderect(hero):
        tttt=5

    if bulet_bos1.colliderect(hero):
        tttt=5
    if bulet_bos2.colliderect(hero):
        tttt=5
    if bulet_bos3.colliderect(hero):
        tttt=5
    if bulet_bos4.colliderect(hero):
        tttt=5
    if bulet_bos5.colliderect(hero):
        tttt=5
    if bulet_bos6.colliderect(hero):
        tttt=5
    if bulet_bos7.colliderect(hero):
        tttt=5
    if bulet_bos8.colliderect(hero):
        tttt=5
    if bulet_bos9.colliderect(hero):
        tttt=5
    if bulet_bos10.colliderect(hero):
        tttt=5
    if bulet_bos11.colliderect(hero):
        tttt=5
    if bulet_bos12.colliderect(hero):
        tttt=5
    if bulet_bos13.colliderect(hero):
        tttt=5
    if bulet_bos14.colliderect(hero):
        tttt=5
    if bulet_bos15.colliderect(hero):
        tttt=5
    if bulet_bos16.colliderect(hero):
        tttt=5
    if bulet_bos17.colliderect(hero):
        tttt=5
    if bulet_bos18.colliderect(hero):
        tttt=5
    if bulet_bos19.colliderect(hero):
        tttt=5
    if bulet_bos20.colliderect(hero):
        tttt=5



    pygame.display.update()
    clock.tick(60)


if bos_hp<=0:
    tim3=pygame.font.SysFont('Arial', 80).render('Win',True,(0,0,0))
    ppppp=(255,215,0)
    
elif bos_hp>0:
    tim3=pygame.font.SysFont('Arial', 80).render('Lose',True,(50,0,0))
    ppppp=(0,0,0)

screen.fill((ppppp))
screen.blit(tim3,(200,250))
pygame.display.update()