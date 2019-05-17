from luma.emulator.device import pygame as emulator
from luma.core.render import canvas
import time

device = emulator(128, 128, 0, 'RGB', 'none', 6)
while True:
    with canvas(device) as draw:
        draw.arc((0, 0, 128, 128), start=0, end=180, fill='white')
    time.sleep(0.1)
