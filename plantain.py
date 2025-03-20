import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
from random import randint
s=""
red = (255,0,0)
orange = (252,186,3)
yellow = (252,255,69)
green = (0,255,0)
blue = (0,0,255)
purple = (225,56,255)
brown = (191,112,0)
black = (0,0,0)
white = (235, 235, 235)
gray = (30,30,30)
icy = (56,213,245)
grass = (150,255,166)
colors = [red,orange,yellow,green,blue,purple,brown,black,white,gray,icy,grass]
font = pygame.font.Font('freesansbold.ttf', 10)
color= gray
screen.fill(color)
squares = []
def drawOptions():
  pygame.draw.rect(screen,white,[50,300,150,49])
  rect = pygame.Rect(50,300,150,49)
  squares.append(rect)
  text = font.render("bananas", True, colors[randint(2)])
  screen.blit(text, (75,300))
drawOptions()
while True:
  # Detects clicking
  m1, m2 = pygame.mouse.get_pos()
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.display.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            damage = randint(0,1000)
            text = font.render(f"{damage}", True, colors[randint(0,11)])
            screen.blit(text, (m1,m2))
  pygame.display.flip()
