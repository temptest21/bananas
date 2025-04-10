import pygame

pygame.init()
screen = pygame.display.set_mode((600, 650))
from random import randint
s=""
clicked = 0
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
darkGrass = (2,186,5)
darkBlue = (14,22,171)
colors = [red,orange,yellow,green,blue,purple,brown,black,white,gray,icy,grass]
font = pygame.font.Font('freesansbold.ttf', 50)
bg= darkBlue
screen.fill(bg)
fruits = []
fruitColors = []
score = 0
frameCount = 0
def fruitLoop():
  horizontal = randint(15,555)
  color = colors[randint(0,len(colors)-1)]
  pygame.draw.rect(screen,color,[horizontal,30,50,50])
  fruit = pygame.Rect(horizontal,30,50,50)
  fruits.append(fruit)
  fruitColors.append(color)
fruitLoop()
while True:
  # Detects clicking
  m1, m2 = pygame.mouse.get_pos()
  pygame.draw.rect(screen,icy,[0,545,600,20])
  barrier = pygame.Rect(0,575,600,20)
  for index, fallingFruit in enumerate(fruits): 
    if frameCount % 50 <= 1:
      pygame.draw.rect(screen,bg,fallingFruit)
      fallingFruit.y += 1
      pygame.draw.rect(screen,fruitColors[index],fallingFruit)
      fruits[index] = fallingFruit
      if fallingFruit.colliderect(barrier):
        score -= 100
        text = font.render("-100...",True,fruitColors[index])
        screen.blit(text, (m1-75,m2-25))
        pygame.draw.rect(screen,bg,fallingFruit)
        fruits.remove(fallingFruit)
        fruitColors.remove(fruitColors[index])
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.display.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if clicked == 1:
          pass
        clicked = 1
        if event.button == 1:
          for index, fallingFruit in enumerate(fruits):
            if fallingFruit.collidepoint(m1,m2):
              score += 100
              text = font.render("+100!",True,fruitColors[index])
              pygame.draw.rect(screen,bg,fallingFruit)
              screen.blit(text, (m1-75,m2-25))
              fruits.remove(fallingFruit)
              fruitColors.remove(fruitColors[index])
      elif event.type == pygame.MOUSEBUTTONUP:
        clicked = 0
  if frameCount < 200000:
    spawnChance = 3000
  else:
    spawnChance = 2000
  if randint(0,spawnChance) == 0:
    fruitLoop()
  frameCount += 1
  if score > 0:
    scoreColor = icy
  elif score == 0:
    scoreColor = gray
  else:
    scoreColor = orange
  text = font.render(f"Score: {score}",True,scoreColor)
  pygame.draw.rect(screen,bg,[0,575,600,125])
  screen.blit(text, (0,575))
  pygame.display.flip()
