import pygame
import random
 # 初始化Pygame
pygame.init()
 # 设置游戏窗口的大小
width = 500
height = 500
win = pygame.display.set_mode((width, height))
 # 设置游戏标题
pygame.display.set_caption("Dodge the Obstacles")
 # 定义游戏对象的类
class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
 # 定义球的类
class Ball(GameObject):
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
         # 碰到边缘时反弹
        if self.x < 0 or self.x + self.width > width:
            dx = -dx
        if self.y < 0 or self.y + self.height > height:
            dy = -dy
        return dx, dy
 # 定义障碍物的类
class Obstacle(GameObject):
    def move(self, speed):
        self.x -= speed
 # 定义游戏循环
def game_loop():
    # 创建球和障碍物
    ball = Ball(50, 50, 20, 20, (255, 0, 0))
    obstacles = []
     # 游戏循环标志
    running = True
     # 游戏分数
    score = 0
     # 设置游戏时钟
    clock = pygame.time.Clock()
     # 游戏循环
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         # 生成障碍物
        if random.randint(0, 50) == 0:
            obstacle = Obstacle(width, random.randint(0, height), 20, 20, (0, 0, 255))
            obstacles.append(obstacle)
         # 移动球和障碍物
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        if keys[pygame.K_UP]:
            dy = -5
        if keys[pygame.K_DOWN]:
            dy = 5
        dx, dy = ball.move(dx, dy)
        for obstacle in obstacles:
            obstacle.move(5)
         # 检测碰撞
        for obstacle in obstacles:
            if ball.x < obstacle.x + obstacle.width and ball.x + ball.width > obstacle.x and ball.y < obstacle.y + obstacle.height and ball.y + ball.height > obstacle.y:
                running = False
         # 绘制游戏对象
        win.fill((255, 255, 255))
        ball.draw(win)
        for obstacle in obstacles:
            obstacle.draw(win)
         # 更新分数
        score += 1
        font = pygame.font.SysFont("comicsans", 30)
        score_text = font.render("Score: " + str(score), 1, (0, 0, 0))
        win.blit(score_text, (10, 10))
         # 刷新屏幕
        pygame.display.update()
         # 设置游戏帧率
        clock.tick(60)
     # 游戏结束
    font = pygame.font.SysFont("comicsans", 50)
    game_over_text = font.render("Game Over", 1, (255, 0, 0))
    win.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)
 # 运行游戏循环
game_loop()
 # 退出Pygame
#pygame.quit()
