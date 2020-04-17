import pygame, sys, pygame.locals
pygame.init()
janela=pygame.display.set_mode((1280, 720), 0, 32)
pygame.display.set_caption("Triangulo do kaller")
branco = (0, 0, 0)
vermelho = (255, 0, 0)

angulo = 0

triangle=pygame.Surface((200, 200))
triangle.fill((255, 255, 255))
pygame.draw.rect(triangle,vermelho,(200,150,20,50))
pygame.draw.polygon(triangle, vermelho, ((-100, -100), (0, 100), (100, -100)))
triangle.set_colorkey((0, 0, 0)) #mascarar o triangulo no quadrado kkk

movimento = triangle.get_rect()
while True:
    for event in pygame.event.get():
        if event.type==pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

    rect = movimento
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        movimento.top-=3
    if pressed[pygame.K_DOWN]: 
        movimento.top+=3               
    if pressed[pygame.K_LEFT]:
        movimento.left-=3                        
    if pressed[pygame.K_RIGHT]: 
        movimento.right+=3
    if pressed[pygame.K_x]:
        x = pygame.Surface.get_width(triangle)
        y = pygame.Surface.get_height(triangle)
        triangle = pygame.transform.scale(triangle, (x + 10, y + 10))
    if pressed[pygame.K_z]:
        x = pygame.Surface.get_width(triangle)
        y = pygame.Surface.get_height(triangle)
        triangle = pygame.transform.scale(triangle, (x - 10, y - 10))
    if pressed[pygame.K_q]:
        centro = movimento.center
        angulo = angulo + 1
        if angulo > 360:
            angulo = 0
        triangle =  pygame.transform.rotate(triangle, angulo)
        movimento = triangle.get_rect()
        movimento.center =  centro
    
    janela.fill(branco)
    janela.blit(triangle, movimento)
    pygame.time.Clock().tick(40)
    pygame.display.update()