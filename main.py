import pygame

from body import Body
from config import TICK

pygame.init()
window = pygame.display.set_mode((800, 800))


planet_1 = Body([400, 400], 1000, [0, 0], radius = 30)
planet_2 = Body([600, 400], 20, [0, -3], radius = 15, color=(225, 0, 0))
planet_3 = Body([200, 400], 20, [0, 3], radius = 15, color=(0, 225, 0))
planet_4 = Body([400, 600], 20, [3, 0], radius = 15, color=(0, 0, 255))
planet_5 = Body([400, 200], 20, [-3, 0], radius = 15, color=(0, 127, 127))
	

bodies = [planet_2, planet_1, planet_3, planet_4, planet_5]

run_flag = True
cache_flag = True

while run_flag:
# for _ in range(2):
	pygame.time.delay(int(1))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run_flag = False
	window.fill((255, 255, 255))

	for body in bodies:
		body.update_position(window, bodies=bodies)

	kinetic_energy = sum([0.5 * body.mass * (body.velocity[0]**2 + body.velocity[1]**2) for body in bodies])
	potential_energy = sum([body.potential_energy for body in bodies])
	if cache_flag:
		total_energy = kinetic_energy + potential_energy
		cache_flag = False


	print(total_energy - kinetic_energy - potential_energy)
	for body in bodies:
		body.cache()
	pygame.display.update()
	
	

	
