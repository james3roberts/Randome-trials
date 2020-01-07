##This project is using pygame so that it shows up as a interactive page instead of a normal basic script. 


import time
import pygame





#started working on the pygame on line 5-9
pygame.font.init()
screen = pygame.display.set_mode((1200,1200))
background = (0,0,0)
screen.fill((background))
myfont = pygame.font.Font(None,50)

text=myfont.render('Hello and welcome to House wrap 101', True,(255,0,0))
screen.blit(text, (100,100))
pygame.display.update()
time.sleep(2.0)
screen.fill((background))
pygame.display.update()
print('Hello and welcome to House wrap 101')
time.sleep(1.0)
text=myfont.render('We are going to be learning how to paper a house quickly and correctly', True,(255,0,0))
screen.blit(text, (75,75))
pygame.display.update()
print('We are going to be learning how to paper a house quickly and correctly.')
time.sleep(3.0)
#Question 1
answer = input('Have you ever papered before? y/n ')
if answer=='n':
  print('Thats okay I will cover everything that you need to know.')
  time.sleep(2.0)
  #Question 2
  answer1= input('Do you know all of the basic tools that are required? y/n ')
  if answer1 =='n':
    print('Thats alright, I will go over everything that you will need to know.')
    time.sleep(2.0)
    print('First you will need to know which style of fastners you must use.')
    # Question 3
    answer2= input('Are you supposed to use button caps?y/n ')
    if answer2 =='n':
      print('Hammer Tackers are really simple to use.')
      time.sleep(1.5)
      print('Just drop the staples in the bottom of the handel and you are ready to go.')
      time.sleep(1.5)
      print('You will also be needing a utility knife.')
      time.sleep(1.5)
      #Question 4
      answer3 = input('Do you know the difference between grace tape and tyvek tape? y/n ')
      if answer3 =='n':
        print('Grace tape is a rubber tape that goes around windows, usually black and super sticky and normaly 6 inches wide.')
        time.sleep(5.0)
        print('Tyvek tape is generally clear or white and about 2 inches wide. ')
        time.sleep(5.0)
        print('Now that you know what is needed lets install the paper.')
    else:
      print('Button caps are great and they keep the paper on much better if it needs to sit for a periord of time.')
      time.sleep(1.0)
      print('You will also be needing a utility knife.')
      time.sleep(1.0)
      answer3 = input('Do you know the difference between grace tape and tyvek tape? y/n ')
      if answer3 =='n':
        print('Grace tape is a rubber tape that goes around windows, usually black and super sticky and normaly 6 inches wide')
        time.sleep(5.0)
        print('Tyvek tape is generally clear or white and about 2 inches wide. ')
        time.sleep(5.0)
        print('Now that you know what is needed lets install the paper.')
        
    
else:
  print('Great we can get straight to getting it done fast and right!')
time.sleep(2.0)
print('Start by rolling the paper out the length of the wall.')
time.sleep(3.0)
print('Make sure that you have about 18 inches extra on each end.')
time.sleep(3.0)
print('Cut the paper now unless it is windy then just prop up the roll of paper.')
time.sleep(5.0)
print('Start at one corner and at the bottom.')
time.sleep(3.0)
print('line up the bottom of the paper with the bottom of the mud sill.')
time.sleep(3.0)
print('tack the paper to the bottom all of the way across the wall.')
time.sleep(3.0)
print('make sure that you keep pulling the paper tight as you go across.')
time.sleep(2.0)
# Question 5
answer4 = input('Is the entire bottom attached and flush? y/n?')
if answer4 =='n':
  print('For this to work quickly and efficiently the entire bottome has to be set inplace before going any futher.')
  exit()
else:
  print('Now starting near the center push the straight up and tack it off as high as you can reach.')
  time.sleep(2.0)
print('Now working away from the center just keep pushing the paper up and tacking it off.')
time.sleep(2.0)
print('')
