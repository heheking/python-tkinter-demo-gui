from moviepy.editor import *
import pygame

pygame.display.set_mode((800, 600))
clip = VideoFileClip('355_x264.mp4')
clip.preview()

pygame.quit()


