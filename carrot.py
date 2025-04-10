import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
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
bg= icy
screen.fill(bg)
score = 0
frameCount = 0
w, a, s, d = False, False, False, False
player = pygame.Rect(275,275,50,50)
pygame.draw.rect(screen,white,player)
while True:
  # Detects clicking
  screen.fill(bg)
  pygame.draw.rect(screen,white,player)
  m1, m2 = pygame.mouse.get_pos()
  if w:
    if frameCount % 50 <= 5:
      player.y -= 2
  if a:
    if frameCount % 50 <= 5:
      player.x -= 2
  if s:
    if frameCount % 50 <= 5:
      player.y += 2
  if d:
    if frameCount % 50 <= 5:
      player.x += 2
  if player.x > 550:
    player.x = 550
  if player.x < 0:
    player.x = 0
  if player.y > 550:
    player.y = 550
  if player.y < 0:
    player.y = 0
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.display.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          pass
      elif event.type == pygame.MOUSEBUTTONUP:
        pass
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
          pass
        if event.key == pygame.K_w:
          w = False
        if event.key == pygame.K_a:
          a = False
        if event.key == pygame.K_s:
          s = False
        if event.key == pygame.K_d:
          d = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          pass
        if event.key == pygame.K_w:
          w = True
        if event.key == pygame.K_a:
          a = True
        if event.key == pygame.K_s:
          s = True
        if event.key == pygame.K_d:
          d = True
  frameCount += 1
  pygame.display.flip()
