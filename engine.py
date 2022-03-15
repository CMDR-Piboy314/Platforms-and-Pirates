from os import walk
import pygame

class Colours:
    def __init__(self):
        self.WHITE         = (255, 255, 255)
        self.BLACK         = (0  ,   0,   0)
        self.RED           = (255,   0,   0)
        self.GREEN         = (0  , 255,   0)
        self.BLUE          = (0  ,   0, 255)
        self.LIGHTSKYBLUE  = (146, 244, 255)
        self.SKYBLUE       = (  0, 191, 255)
        self.PURPLE        = ( 50,  50, 130)
        self.GREY          = (140, 140, 140)
        self.BROWN         = (172,  90,   0)
        self.CYAN          = (  0, 255, 255)
        self.YELLOW        = (255, 255,   0)
        self.DARKGREEN     = (  7,  80,  75)
        self.MIDGREEN      = (  9,  91,  85)
        self.BRIGHTGREEN   = ( 14, 222, 150)

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in img_files:
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path).convert_alpha()
			surface_list.append(image_surf)

	return surface_list
