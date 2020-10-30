import pygame
from config import *

class Body(object):
	def __init__(self, position, mass, velocity, density=None, radius=None, effect=None, color=(0, 0, 0)):
		self.mass = mass
		if density:
			self.density = density
			self.effect = effect
			self.radius = (self.mass / self.density)**(1 / 3)
		else:
			if radius:
				self.radius = radius
			else:
				raise Exception('Body creation error: not enough or wrong parameters')
		self.position = position
		self.velocity = velocity
		self.color = color
		self.force = [0, 0]
		self.cache()
		self.potential_energy = 0

	
	def move(self, dx, dy):
		self.position[0] += dx
		self.position[1] += dy
		

	def _update_forces(self, bodies):
		self.force = [0, 0]
		self.potential_energy = 0
		for body in bodies:
			if self == body:
				continue
			dx = body.cached_position[0] - self.cached_position[0]
			dy = body.cached_position[1] - self.cached_position[1]
			
			raw_F = G * self.mass * body.mass / (dx**2 + dy**2)**1.5
			Fx = raw_F * dx
			Fy = raw_F * dy

			self.potential_energy -= 0.5 * G * self.mass * body.mass / (dx**2 + dy**2)**0.5

			self.force[0] += Fx
			self.force[1] += Fy


	def update_position(self, layer, bodies=None):
		if bodies == None:
			pygame.draw.circle(layer, self.color, (self.position[0], 800 - self.position[1]), self.radius)
			return None

		self._update_forces(bodies)
		self.velocity[0] += self.force[0] * TICK / self.mass
		self.velocity[1] += self.force[1] * TICK / self.mass

		self.position[0] += self.velocity[0] * TICK
		self.position[1] += self.velocity[1] * TICK
		pygame.draw.circle(layer, self.color, (int(self.position[0]), 800 - int(self.position[1])), self.radius)


	def check_borders(self, bodies):
		pass


	def cache(self):
		self.cached_position = self.position[:]