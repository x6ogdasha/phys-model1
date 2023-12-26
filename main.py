import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Новые размеры платформы
PLATFORM_WIDTH = SCREEN_WIDTH
PLATFORM_HEIGHT = 20

# Размеры стены
WALL_WIDTH = 20
WALL_HEIGHT = SCREEN_HEIGHT

# Массы и цвета кубов
MASS_CUBE1 = 1
MASS_CUBE2 = 1000000ц
CUBE1_COLOR = RED
CUBE2_COLOR = BLUE

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пример с платформой, стеной и кубами")

# Создание новой платформы
platform = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
platform.fill(WHITE)
platform_rect = platform.get_rect()
platform_rect.topleft = (0, SCREEN_HEIGHT - PLATFORM_HEIGHT)

# Создание стены
wall = pygame.Surface((WALL_WIDTH, WALL_HEIGHT))
wall.fill(WHITE)
wall_rect = wall.get_rect()
wall_rect.topleft = (0, 0)

# Создание первого куба
cube1_speed = 0
cube1_mass = MASS_CUBE1
cube1 = pygame.Surface((100, 100))
cube1.fill(CUBE1_COLOR)
cube1_rect = cube1.get_rect()
cube1_rect.topleft = (100, SCREEN_HEIGHT - PLATFORM_HEIGHT - cube1.get_height())

# Создание второго куба с начальной скоростью
cube2_speed = -0.01
cube2_mass = MASS_CUBE2
cube2 = pygame.Surface((30, 30))
cube2.fill(CUBE2_COLOR)
cube2_rect = cube2.get_rect()
cube2_rect.topleft = (200.0, SCREEN_HEIGHT - PLATFORM_HEIGHT - cube2.get_height())

count = 0
dx1 = 0.0
dx2 = 0.0
trueOrder = True

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Проверка столкновения кубов и изменение направления с учетом упругости столкновения
    if cube1_rect.colliderect(cube2_rect) and trueOrder:
        print(f"init speed1 {cube1_speed} speed2 {cube2_speed}")
        # Рассчитываем измененные скорости по нормали с учетом упругости столкновения
        tempSpeed1 = cube1_speed
        cube1_speed = (cube1_speed * (cube1_mass - cube2_mass) + 2 * cube2_mass * cube2_speed) / (
                    cube1_mass + cube2_mass)
        cube2_speed = (cube2_speed * (cube2_mass - cube1_mass) + 2 * cube1_mass * tempSpeed1) / (
                    cube1_mass + cube2_mass)
        print(f"after speed1 {cube1_speed} speed2 {cube2_speed}\n")

        trueOrder = not trueOrder
        count += 1
        print(count)

    # Проверка столкновения куба 1 со стеной и изменение направления
    if cube1_rect.left <= wall_rect.right and not trueOrder and cube1_speed < 0:
        cube1_speed = -cube1_speed

        trueOrder = not trueOrder
        count += 1
        print(count)

    dx1 += cube1_speed
    dx2 += cube2_speed

    if dx1 > 1 or dx1 < -1:
        dx = int(dx1)
        cube1_rect.x += dx
        dx1 = dx1 - int(dx1)
        isChanged = True
        isReversed= True

    if dx2 > 1 or dx2 < -1:
        dx = int(dx2)
        cube2_rect.x += dx
        dx2 = dx2 - int(dx2)
        isChanged = True
        isReversed = True

    # Обновление экрана
    screen.fill(BLACK)
    screen.blit(platform, platform_rect)
    screen.blit(wall, wall_rect)
    screen.blit(cube1, cube1_rect)
    screen.blit(cube2, cube2_rect)

    # Отображение изменений
    pygame.display.flip()

    # Задержка для управления частотой обновления
    pygame.time.Clock().tick(60000)
