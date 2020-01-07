#Ok to get this started you will need to have the pygame library installed
# call the librarys that will be used. 
import pygame
import time

#This is to set up the back ground
pygame.font.init()
screen = pygame.display.set_mode((800,600))
background = (0, 0, 0)
screen.fill((background))
myfont = pygame.font.Font(None, 90)
#This is where you choose your File
# I had to create a new file in notepad. when I saved it I made sure that the encoding was in utf-8. 
# If you use something else you will need to change the next line after encoding to what ever
#you encoded it as when you saved it. The other problem that I had was getting the full path 
#to the file. so to fix this find your file hold shift and right click. about 8 from the top is 
# an option to copy as path just copy and past below . 
# the random r in the next line turns the string into a raw input which allows the entire file name
# to be followed. I blocked out the line of code that I was using so you can have a visual aid. 
# and I started the the line for you just past you path in the first set of"" and add what you encoded it as
# in the "" after encoding. 
f = open(r"C:\Users\James\Documents\programUsage.txt",encoding = 'utf-8')
#f = open(r"",encoding="")
for line in f:
    for word in line.split():
        text = myfont.render(word,1,(0,255,0))
        screen.blit(text, (300,300))
        pygame.display.update()
        # time.sleep is the amount of time in between words. so this is where the math
        # part comes into play. At .2 sleep there will be just over 300 wpm
        time.sleep(0.2)
        screen.fill((background))
        pygame.display.update()
pygame.display.quit()
#So after getting all of this set up I decided to play with it. So what I did was copy text off of a website and
# then I pasted it in the same file that I was using. It still works. So I do not know how much of this is making sense
# and a get together or phone call may need to happen but the hardest part is line 22. if you get that one to work
# everything seems to fall in place.  