# Sadrzi klasu Lavirint i Zid
import pygame as pg
from pygame_version import parametri


class Lavirint():
    def __init__(self, simulacija):
        self.zidovi = []
        self.zidovi.append(Zid(simulacija, 0, 0,
                               parametri.SIRINA, 10))
        self.zidovi.append(Zid(simulacija, 0, parametri.VISINA-10,
                               parametri.SIRINA, 10))
        self.zidovi.append(Zid(simulacija, 0, 0,
                               10, parametri.VISINA))
        self.zidovi.append(Zid(simulacija, parametri.SIRINA-10, 0,
                               10, parametri.VISINA))


class Zid(pg.sprite.Sprite):
    def __init__(self, simulacija, x, y, width, height):
        self.grupe = simulacija.svi_sprajtovi, simulacija.lavirint_sprajtovi

        pg.sprite.Sprite.__init__(self, self.grupe)

        self.image = pg.Surface((width, height))
        self.image.fill(parametri.ZELENA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




