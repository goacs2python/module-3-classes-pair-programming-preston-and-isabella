import pgzrun
import random
import os

WIDTH = 800
HEIGHT = 600

score = 0
highScore = 0
timer = 60
gameOver = False
gameStarted = False

def loadHighScore():
    global highScore