import pygame

pygame.init()
win = pygame.display.set_mode((1920, 1080))
win.fill((255, 255, 255))

run_flag = True

x = 100
y = 100
r = 20
speed = 1


while run_flag:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run_flag = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		x -= speed
	if keys[pygame.K_RIGHT]:
		x += speed
	if keys[pygame.K_UP]:
		y -= speed
	if keys[pygame.K_DOWN]:
		y += speed

	win.fill((255, 255, 255))
	pygame.draw.circle(win, (0, 0, 100), (x, y), r)
	pygame.display.update()