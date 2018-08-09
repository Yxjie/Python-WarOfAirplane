import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 850))

# 绘制背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()
# 游戏循环
while True:
    pass

pygame.quit()
