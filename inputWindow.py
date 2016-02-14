import pygame
import sys
from pygame.locals import *
import math
import string
from largeType import LargeType

class InputWindow(object):
	def __init__(self):
		self.screen = pygame.display.set_mode((320,240))
		word = self.ask()
		pygame.display.quit()
		if len(word) > 1:
			self.lt = LargeType(word)
			self.lt.render_text_on_screen()


	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def display_box(self, message):
		"Print a message in a box in the middle of the screen"
		fontobject = pygame.font.Font(None,18)
		pygame.draw.rect(self.screen, (0,0,0), ((self.screen.get_width() / 2) - 100, (self.screen.get_height() / 2) - 10, 200,20), 0)
		pygame.draw.rect(self.screen, (255,255,255),
                   ((self.screen.get_width() / 2) - 102,
                    (self.screen.get_height() / 2) - 12,
                    204,24), 1)
		if len(message) != 0:
			self.screen.blit(fontobject.render(message, 1, (255,255,255)),((self.screen.get_width() / 2) - 100, (self.screen.get_height() / 2) - 10))

		pygame.display.flip()

	def ask(self):
		"ask(screen, question) -> answer"
		pygame.font.init()
		current_string = []
		self.display_box(string.join(current_string,""))
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
			
			self.display_box(string.join(current_string,""))
		return string.join(current_string,"")


if __name__ == '__main__':
	w = InputWindow()