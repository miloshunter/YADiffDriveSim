# Osnovni Pygame file za prikaz simulacije

import pygame as pg
import pygame_gui
import sys
import random
from pygame_version import parametri
from pygame_version.Lavirint import Lavirint
from pygame_version.Robot import Robot
from pygame_version.SimInfo import SimInfo
from copy import copy
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
        self.poc_pozicija = None
        self.nova_simulacija()
        self.trail_set = []
        self.old_trail_set = []

    def nova_simulacija(self):
        self.svi_sprajtovi = pg.sprite.Group()
        self.lavirint_sprajtovi = pg.sprite.Group()
        self.lavirint = Lavirint(self)

        self.robot = Robot(self, *parametri.cm_to_px(40, 40, 90))

        self.update_start_position()
        self.robot.update()

    def glavna_petlja(self):
        # Simulira dok se self.simuliraj ne postavi na False
        self.crtaj()

        self.sim_ticks = 0

        while True:
            # dt -> broj milisekundi izmedju 2 poziva .tick funkcije
            self.clock.tick(parametri.FPS)
            self.dt = 10 #ms

            self.dogadjaji()
            self.sim_info.manager.update(self.dt)

            self.crtaj()

            if self.simuliraj:
                self.sim_ticks += self.dt
                trajanje = self.sim_ticks - self.pocetak_simulacije

                self.azuriraj()

                self.sim_info.sat.set_text(str(trajanje))
                self.sim_info.update_pos_diff(self.poc_pozicija, self.robot.get_cm_pos())

                self.trail_set.append(copy(self.robot.pos))

                if trajanje >= (self.sim_time * 1000):
                    self.simuliraj = False
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
        self.pocetak_simulacije = self.sim_ticks
        self.update_start_position()
        self.robot.vr = float(self.sim_info.vr.get_text())/self.robot.reduction
        self.robot.vl = float(self.sim_info.vl.get_text())/self.robot.reduction

        self.robot.set_wheel_power(self.robot.vr, self.robot.vl)

        self.sim_time = float(self.sim_info.sim_time.get_text())

        self.old_trail_set += copy(self.trail_set)
        self.trail_set.clear()



    def update_start_position(self):
        self.poc_pozicija = self.robot.get_cm_pos()
        self.sim_info.update_prev_position(*self.poc_pozicija)

    def update_position(self):
        self.sim_info.update_position(*self.robot.get_cm_pos())

    def azuriraj(self):
        self.svi_sprajtovi.update()
        self.update_position()

    def draw_trail(self):
        for i in range(0, len(self.old_trail_set) - 1):
            pg.draw.line(self.ekran, parametri.ZUTA,
                         (self.old_trail_set[i][0], self.old_trail_set[i][1]),
                         (self.old_trail_set[i+1][0], self.old_trail_set[i+1][1]))

        for i in range(0, len(self.trail_set) - 1):
            pg.draw.line(self.ekran, parametri.CRVENA,
                         (self.trail_set[i][0], self.trail_set[i][1]),
                         (self.trail_set[i + 1][0], self.trail_set[i + 1][1]))

        if self.trail_set.__sizeof__() > 2000:
            self.trail_set.pop(0)

    def crtaj(self):
        # Iscrtavanje sa dvostrukim baferovanjem
        self.ekran.fill(parametri.BOJA_POZADINE)
        self.ekran.blit(self.background_image, (0, 0))

        for sprajt in self.svi_sprajtovi:
            self.ekran.blit(sprajt.image, sprajt.rect)

        self.draw_trail()

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





