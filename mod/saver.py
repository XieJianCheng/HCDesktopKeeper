# coding:utf-8


import pygame
from random import randint as r

window = width_window, height_window = 1980, 1080
width_point = height_point = 50

screen = pygame.display.set_mode(window)  # 显示窗口

# 初始化
pygame.init()
print("Game is running!")

color_bg = (0, 0, 0)  # 设置颜色

# 设置移动的距离和方向
speed_point_black = [r(6, 12) + 3, r(4, 8) + 3]
speed_point_blue = [r(5, 10) + 1, r(8, 17) + 1]
speed_point_green = [r(12, 25) + 3, r(1, 4) + 3]
speed_point_red = [r(7, 15) + 3, r(2, 4) + 3]
speed_all = 160

point_black_x = point_black_y = 0
point_blue_x = point_blue_y = 0
point_green_x = point_green_y = 0
point_red_x = point_red_y = 0

# 暂停
move_state = True
# 变速
change_times = 0
# 设置时钟
clock = pygame.time.Clock()
while True:
    clock.tick(speed_all)  # 每秒执行……次
    l, m, r = pygame.mouse.get_pressed(3)
    if l or m or r:
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_f:
                if move_state is True:
                    move_state = False
                else:
                    move_state = True
            if event.key == pygame.K_s:
                change_times += 1
                if change_times % 2 == 1:
                    speed_point_black[0] = int(speed_point_black[0]/2)
                    speed_point_black[1] = int(speed_point_black[1]/2)

                    speed_point_blue[0] = int(speed_point_blue[0] / 2)
                    speed_point_blue[1] = int(speed_point_blue[1] / 2)

                    speed_point_green[0] = int(speed_point_green[0] / 2)
                    speed_point_green[1] = int(speed_point_green[1] / 2)

                    speed_point_red[0] = int(speed_point_red[0] / 2)
                    speed_point_red[1] = int(speed_point_red[1] / 2)
                else:
                    speed_point_black[0] = int(speed_point_black[0] * 2)
                    speed_point_black[1] = int(speed_point_black[1] * 2)

                    speed_point_blue[0] = int(speed_point_blue[0] * 2)
                    speed_point_blue[1] = int(speed_point_blue[1] * 2)

                    speed_point_green[0] = int(speed_point_green[0] * 2)
                    speed_point_green[1] = int(speed_point_green[1] * 2)

                    speed_point_red[0] = int(speed_point_red[0] * 2)
                    speed_point_red[1] = int(speed_point_red[1] * 2)

    screen.fill(color_bg)

    # 白色点
    point_black = pygame.draw.rect(screen, (255, 255, 255), (point_black_x, point_black_y, width_point, height_point),
                                   0)
    if point_black.x + width_point < 0 or point_black.x + width_point > width_window:
        speed_point_black[0] = -speed_point_black[0]
    if point_black.y + height_point < 0 or point_black.y + height_point > height_window:
        speed_point_black[1] = -speed_point_black[1]

    # 蓝色点
    point_blue = pygame.draw.rect(screen, (0, 162, 232), (point_blue_x, point_blue_y, width_point, height_point),
                                  0)
    if point_blue.x + width_point < 0 or point_blue.x + width_point > width_window:
        speed_point_blue[0] = -speed_point_blue[0]
    if point_blue.y + height_point < 0 or point_blue.y + height_point > height_window:
        speed_point_blue[1] = -speed_point_blue[1]

    # 绿色点
    point_green = pygame.draw.rect(screen, (34, 177, 76), (point_green_x, point_green_y, width_point, height_point),
                                   0)
    if point_green.x + width_point < 0 or point_green.x + width_point > width_window:
        speed_point_green[0] = -speed_point_green[0]
    if point_green.y + height_point < 0 or point_green.y + height_point > height_window:
        speed_point_green[1] = -speed_point_green[1]

    # 红色点
    point_red = pygame.draw.rect(screen, (237, 28, 36), (point_red_x, point_red_y, width_point, height_point),
                                 0)
    if point_red.x + width_point < 0 or point_red.x + width_point > width_window:
        speed_point_red[0] = -speed_point_red[0]
    if point_red.y + height_point < 0 or point_red.y + height_point > height_window:
        speed_point_red[1] = -speed_point_red[1]

    if move_state is True:
        point_black_x += speed_point_black[0]
        point_black_y += speed_point_black[1]

        point_blue_x += speed_point_blue[0]
        point_blue_y += speed_point_blue[1]

        point_green_x += speed_point_green[0]
        point_green_y += speed_point_green[1]

        point_red_x += speed_point_red[0]
        point_red_y += speed_point_red[1]

    # 更新全部显示
    pygame.display.update()
