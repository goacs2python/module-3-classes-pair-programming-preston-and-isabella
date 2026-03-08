import pgzrun
import random
import os

score = 0
high_score = 0
timer = 20
game_over = False
WIDTH = 1000
HEIGHT = 800
playerX = WIDTH // 2
playerY = HEIGHT - 50

class Bullet:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def update(self):
        self.y =self.y- 10

class Target:
    def __init__(self):
        self.x = random.randint(50, 950)
        self.y = random.randint(50, 400)
    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 20, "red")

bullets = []
targets = [Target() for _ in range(5)]

def load_high_score():
    global high_score
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read().strip())
    except:
        high_score = 0

def save_high_score():
    if score > high_score:
        with open("highscore.txt", "w") as f:
            f.write(str(score))

load_high_score()

def countdown():
    global timer, game_over
    if timer > 0:
        timer = timer-1
        clock.schedule(countdown, 1.0)
    else:
        game_over = True
        save_high_score()

clock.schedule(countdown, 1.0)

def on_mouse_move(pos):
    global playerX
    if not game_over:
        playerX = pos[0]

def on_mouse_down(button):
    if button == mouse.LEFT and not game_over:
        bullets.append(Bullet(playerX, playerY - 10))

def update():
    global score
    
    if game_over:
        return
    
    for b in bullets[:]:
        b.update()
        if b.y < -20:
            bullets.remove(b)
            continue
        for t in targets[:]:
            if ((b.x - t.x)**2 + (b.y - t.y)**2)**0.5 < 30:
                targets.remove(t)
                bullets.remove(b)
                score = score+1
                targets.append(Target())
                break

def draw():
    screen.clear()
    screen.draw.filled_circle((playerX, playerY), 20, "green")
    
    for b in bullets:
        screen.draw.filled_circle((b.x, b.y), 10, "white")
    
    for t in targets:
        t.draw()
    
    screen.draw.text(f"Score: {score}", (10, 10), color="white")
    screen.draw.text(f"High Score: {high_score}", (10, 30), color="yellow")
    screen.draw.text(f"Time: {timer}", (10, 50), color="red")
    
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH//2, HEIGHT//2), fontsize=60, color="red")

pgzrun.go()