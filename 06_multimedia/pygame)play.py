import pygame
pygame.init()

pygame.mixer.music.load('sample.mp3')

while:
    cmd = input("play:p, pause:pp, unpause:up, stop:s, quit:q >")
    if cmd == 'p':
        pygame.mixer.music.play()
    elif cmd == 'pp':
        pygame.mixer.music.pause()
    elif cmd == 'up':
        pygame.mixer.music.unpause()
    elif cmd == 's':
        pygame.mixer.music.stop()
    elif cmd == 'q':
        break
    else:
        print('incorrect cmd')
pygame.mixer.music.unload()