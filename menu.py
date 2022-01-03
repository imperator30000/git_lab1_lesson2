# import pygame
# import random
# from settings import *
#
#
# def anim(arr, sk, counter=0, name=0, x=0, y=0):
#     if counter > len(arr) ** 2 - len(arr):
#         counter = 0
#     if name:
#         sk.blit(arr[counter // len(arr)], (x - int(arr[counter // len(arr)].get_rect()[2]), y))
#     else:
#         sk.blit(arr[counter // len(arr)], (x, y))
#     counter += 7
#     return counter
#
#
# anim__ = [pygame.transform.scale(pygame.image.load(f'images/анимация/{i}.png'), (WIDTH, HEIGHT)) for i in range(21)]
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()
# c = 0
# # Цикл игры
# running = True
# while running:
#     # Держим цикл на правильной скорости
#     clock.tick(FPS)
#     # Ввод процесса (события)
#     for event in pygame.event.get():
#         # check for closing window
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     c = anim(anim__, screen, c)
#     # После отрисовки всего, переворачиваем экран
#
#     pygame.display.flip()
#
# pygame.quit()


from PIL import Image


def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=w, height=h))

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise RuntimeError('Width or height required!')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print('The scaled image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))


for i in range(21):
    scale_image(f'images/анимация/{i}.png', f'images/111/{i}.png', 600, 400)
