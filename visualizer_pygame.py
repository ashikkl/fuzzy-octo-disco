import pygame
import numpy as np
import pyaudio

# initialize Pygame and Pyaudio
pygame.init()
p = pyaudio.PyAudio()

# set up Pygame display
screen = pygame.display.set_mode((640, 480))

# set up Pyaudio stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# set up color variables
bg_color = (0, 0, 0)
line_color = (255, 255, 255)

# main loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            p.terminate()
            quit()

    # read audio input
    data = np.fromstring(stream.read(1024), dtype=np.int16)

    # calculate frequency spectrum using Fast Fourier Transform
    spectrum = np.fft.fft(data)
    spectrum = np.abs(spectrum[:len(spectrum)//2])

    # draw spectrum on Pygame screen
    screen.fill(bg_color)
    for i in range(len(spectrum)):
        pygame.draw.line(screen, line_color, (i*2, 480), (i*2, 480 - spectrum[i] // 200))

    # update Pygame display
    pygame.display.update()
