import pygame
import sys
from pygame.locals import *
import math
import string
from largeType import LargeType

class InputWindow(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((320,240))
		word = self.ask(self.screen)
		pygame.display.quit()
		self.lt = LargeType(word)
		self.lt.render_text_on_screen()

	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def display_box(self, screen, message):
		"Print a message in a box in the middle of the screen"
		fontobject = pygame.font.Font(None,18)
		pygame.draw.rect(screen, (0,0,0), ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10, 200,20), 0)
		pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
		if len(message) != 0:
			screen.blit(fontobject.render(message, 1, (255,255,255)),((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))

		pygame.display.flip()

	def ask(self, screen):
		"ask(screen, question) -> answer"
		pygame.font.init()
		current_string = []
		self.display_box(screen, string.join(current_string,""))
		while 1:
			inkey = self.get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
			elif inkey == K_RETURN:
				break
			elif inkey == K_MINUS:
				current_string.append("_")
			elif inkey <= 127:
				current_string.append(chr(inkey))
			
			self.display_box(screen, string.join(current_string,""))
		return string.join(current_string,"")

			# self.lt = LargeType(word)


if __name__ == '__main__':
	w = InputWindow()