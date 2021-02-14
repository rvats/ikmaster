from random import randint
import pygame
black_color = (10, 10, 10)
white_color = (250, 250, 250)
red_color = (200, 0, 0)
blue_red_color = (240, 0, 0)
green_color = (0, 200, 0)
blue_green_color = (0, 230, 0)
blue_color = (0, 0, 200)
grey_color = (50, 50, 50)
yellow_color = (150, 150, 0)
purple_color = (43, 3, 132)
blue_purple_color = (60, 0, 190)
snakeAndLaddersBoard = [
     0,
      1,  2,  3,  4,  5,  6,  7,  8,  9,  10,
     11, 12, 13, 14, 15, 16, 17, 18, 19,  20,
     21, 22, 23, 24, 25, 26, 27, 28, 29,  30,
     31, 32, 33, 34, 35, 36, 37, 38, 39,  40,
     41, 42, 43, 44, 45, 46, 47, 48, 49,  50,
     51, 52, 53, 54, 55, 56, 57, 58, 59,  60,
     61, 62, 63, 64, 65, 66, 67, 68, 69,  70,
     71, 72, 73, 74, 75, 76, 77, 78, 79,  80,
     81, 82, 83, 84, 85, 86, 87, 88, 89,  90,
     91, 92, 93, 94, 95, 96, 97, 98, 99, 100,
     ]
def ladders(x):
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 9:
        return 31
    elif x == 28:
        return 84
    elif x == 21:
        return 42
    elif x == 51:
        return 67
    elif x == 80:
        return 99
    elif x == 72:
        return 91
    else:
        return x
def snakes(x):
    if x == 17:
        return 7
    elif x == 54:
        return 34
    elif x == 62:
        return 19
    elif x == 64:
        return 60
    elif x == 87:
        return 36
    elif x == 93:
        return 73
    elif x == 95:
        return 75
    elif x == 98:
        return 79
    else:
        return x
print(snakeAndLaddersBoard)