# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import pygame_gui
import sys
import random
from pygame_version import parametri
from pygame_version.Lavirint import Lavirint
from pygame_version.Robot import Robot
from pygame_version.SimInfo import SimInfo
import threading
import time


do_parallel = False

class Simulacija:
    def __init__(self):
        pg.init()
        self.ekran = pg.display.set_mode((parametri.SIRINA+parametri.SIRINA_MENIJA,
                                          parametri.VISINA))
        self.sim_info = SimInfo()
        self.background_image = pg.image.load("grid.png")
        pg.display.set_caption(parametri.NASLOV)
        self.clock = pg.time.Clock()
        self.simuliraj = False
        self.sim_time = 0
        self.pocetak_simulacije = 0
        self.nova_simulacija()

    def nova_simulacija(self):
        self.svi_sprajtovi = pg.sprite.Group()
        self.lavirint_sprajtovi = pg.sprite.Group()
        self.lavirint = Lavirint(self)

        self.robot = Robot(self, *parametri.cm_to_px(40, 40, 45))

        self.update_start_position()

    def glavna_petlja(self):
        # Simulira dok se self.simuliraj ne postavi na False
        self.crtaj()

        while True:
            # dt -> broj milisekundi izmedju 2 poziva .tick funkcije
            self.dt = self.clock.tick(parametri.FPS) / 1000.0

            self.dogadjaji()
            self.sim_info.manager.update(self.dt)

            self.crtaj()
            self.azuriraj()

            if self.simuliraj:
                self.robot.set_wheel_power(self.robot.vr, self.robot.vl)
                trajanje = pg.time.get_ticks() - self.pocetak_simulacije
                self.sim_info.sat.set_text(str(trajanje / 1000.0))

                if trajanje > (self.sim_time*1000):
                    self.simuliraj = False

            else:
                self.robot.set_wheel_power(0, 0)

    def izadji(self):
        self.tajmer_ispisa.cancel()
        pg.quit()
        sys.exit()

    def algoritam(self):

        start_time = time.time()

    def dogadjaji(self):
        for dogadjaj in pg.event.get():
            if dogadjaj.type == pg.QUIT:
                self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_ESCAPE:
                    self.izadji()
            if dogadjaj.type == pg.KEYDOWN:
                if dogadjaj.key == pg.K_SPACE:
                    self.algoritam()
            if dogadjaj.type == pg.USEREVENT:
                if dogadjaj.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if dogadjaj.ui_element == self.sim_info.hello_button:
                        self.start_sim()

            self.sim_info.manager.process_events(dogadjaj)

    def start_sim(self):
        self.simuliraj = True
        self.pocetak_simulacije = pg.time.get_ticks()
        self.robot.vr = float(self.sim_info.vr.get_text())
        self.robot.vl = float(self.sim_info.vl.get_text())

        self.sim_time = float(self.sim_info.sim_time.get_text())

        self.update_start_position()

    def update_start_position(self):
        poc_pozicija = self.robot.get_cm_pos()
        self.sim_info.update_prev_position(*poc_pozicija)

    def update_position(self):
        self.sim_info.update_position(*self.robot.get_cm_pos())

    def azuriraj(self):
        self.svi_sprajtovi.update()
        self.update_position()


    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(parametri.BOJA_POZADINE)
        self.ekran.blit(self.background_image, (0, 0))

        for sprajt in self.svi_sprajtovi:
            self.ekran.blit(sprajt.image, sprajt.rect)

        # Update simInfo

        self.sim_info.manager.draw_ui(self.ekran)
        pg.display.update()


simulacija = Simulacija()


def printit():
    tajmer_ispisa = threading.Timer(0.5, printit)
    simulacija.tajmer_ispisa = tajmer_ispisa
    tajmer_ispisa.setDaemon(False)
    tajmer_ispisa.start()


try:
  printit()
except (KeyboardInterrupt, SystemExit):
   sys.exit()


simulacija.glavna_petlja()





