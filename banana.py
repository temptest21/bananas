import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
from random import randint
g = ["a","b","c","d","e","f","g","h","i","j"]
refgrid = []
s=""
checked = []
researched = []
researchcache = []
flagged = []
def squareText(square,isItBomb,number,operation):
  if operation == "flag":
    if square not in researched:
      if square not in flagged:
        flagged.append(square)
        text = font.render("P", True, colors[2])
        screen.blit(text, (squares[square].x+7,squares[square].y-1))
      else:
        flagged.remove(square)
        pygame.draw.rect(screen,white,[squares[square].x,squares[square].y,49,49])
  if number == "stop":
    return
  if operation == "dig":
    if isItBomb == "*":
      text = font.render("*", True, colors[7])
      screen.blit(text, (squares[square].x+13,squares[square].y+10))
      print("dead btw")
      return
    text = font.render(f"{isItBomb}", True, colors[number-1])
    screen.blit(text, (squares[square].x+7,squares[square].y-1))
def checkAdjacents(pointpoint,operation):
    #i dont know why but this function just kinda hates working bruh
    if pointpoint in flagged:
        return
    if pointpoint in researched:
        return 
    researched.append(pointpoint)
    if grid[pointpoint] == " x " or grid[pointpoint] == " x \n":
      squareText(pointpoint,"*",8,operation)
      return
    pointback = pointpoint-1
    pointfront = pointpoint+1
    adjacents = [pointback,pointpoint,pointfront]
    for i in adjacents[:]:
      adjacents.append(i-10)
      adjacents.append(i+10)
    for i in adjacents[:]:
      if i > 99 or i < 0:
        adjacents.remove(i)
      elif len(str(i)) > 1 or len(str(pointpoint)) > 1:
        c1 = divmod(i,10)
        c2 = divmod(pointpoint,10)
        if abs(c1[0]-c2[0]) <= 1 and abs(c1[1]-c2[1]) <= 1:
          pass
        else:
          adjacents.remove(i)
      else:
        if abs(i-pointpoint) >1:
          adjacents.remove(i)
    digit = 0
    templist = list(adjacents)
    for i in templist:
        if grid[i] == " x " or grid[i] == " x \n":
            digit += 1
    if digit == 0:
        for i in templist:
            checkAdjacents(i,"dig")
    squareText(pointpoint,digit,digit,operation)
    return
for i in range(100):
    if (i+1) % 10 == 0:
        refgrid.append(" . \n")
    else:
        refgrid.append(" . ")
grid = list(refgrid)
w=0
already = []
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
colors = [red,orange,yellow,green,blue,purple,brown,black]
while w < 10 :
    w+=1
    check = randint(0,99)
    if check not in already:
        already.append(check)
        if (check+1) % 10 == 0:
            grid[check] = " x \n"
        else:
            grid[check] = " x "
    else:
        w -= 1
        continue
font = pygame.font.Font('freesansbold.ttf', 60)
iteration = 0   
color= gray
screen.fill(color)
squares = []
for mult in range(10):
  for i in range(10,590,59):
    pygame.draw.rect(screen,white,[i,10+(59*mult),49,49])
    rect = pygame.Rect(i, 10+(59*mult), 49, 49)
    squares.append(rect)
while True:
  m1, m2 = pygame.mouse.get_pos()
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.display.quit()
      if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
              whichoneisit=-1
              for square in squares:
                whichoneisit+=1
                if square.collidepoint(m1, m2):
                  checkAdjacents(whichoneisit,"dig")
          elif event.button == 3:
            whichoneisit=-1
            for square in squares:
              whichoneisit+=1
              if square.collidepoint(m1, m2):
                squareText(whichoneisit,0,0,"flag")
          elif event.button == 2:
            print(s.join(grid))
  pygame.display.flip()
