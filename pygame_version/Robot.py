# Klasa za robota koji ce ici po lavirintu i meriti
import pygame as pg
from pygame_version.Laser import Laser
import pygame_version.parametri as parametri
vec = pg.math.Vector2
import math


class Robot(pg.sprite.Sprite):
    def __init__(self, simulacija, x, y, theta):
        self.grupe = simulacija.svi_sprajtovi
        self.simulacija = simulacija

        pg.sprite.Sprite.__init__(self, self.grupe)

        self.original_image = pg.image.load("robot.png")
        self.original_image = pg.transform.scale(self.original_image, (
            parametri.DIMENZIJE_ROBOTA, parametri.DIMENZIJE_ROBOTA))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rot_speed = 0
        self.speed = 0
        self.vel = vec(0, 0)
        self.vr = 0
        self.vl = 0
        self.R = 9.8
        self.L = 35
        self.reduction = 1
        self.w_tocka = 5  # rad/s
        self.pos = vec(x, y)
        self.theta = theta
        self.orijentacija_za_90 = self.theta

    def get_keys(self):
        #self.rot_speed = 0
        #self.vel = vec(0, 0)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.rot_speed = 5
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.rot_speed = -5
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel = vec(2, 0).rotate(-self.theta)
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel = vec(-2 / 2, 0).rotate(-self.theta)

        # Provera udarca o ivicu
        new_sprite = pg.sprite.Sprite()
        new_rect = pg.Rect(self.rect)
        new_rect.x += self.vel[0]
        new_rect.y += self.vel[1]
        new_sprite.rect = new_rect
        if pg.sprite.spritecollide(new_sprite, self.simulacija.lavirint_sprajtovi, False):
            self.vel = vec(0, 0)
            self.set_wheel_power(0, 0)

    def update(self):
        self.get_keys()
        vx = self.speed * math.cos(math.radians(-self.theta))
        vy = self.speed * math.sin(math.radians(-self.theta))
        # Cm to Pixels
        self.vel[0] = vx * 5
        self.vel[1] = vy * 5

        self.theta += self.rot_speed
        if self.theta > 360:
            self.theta = self.theta - 360
        elif self.theta < -360:
            self.theta = self.theta + 360
        self.pos += self.vel
        self.image = pg.transform.rotate(self.original_image, self.theta)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def set_wheel_power(self, vr, vl):

        self.vr = self.w_tocka*self.R*vr
        self.vl = self.w_tocka*self.R*vl

        self.speed = 1/2*(self.vr+self.vl)/100  # Faktor 100 zbog diskretizacije po 10ms
        omega_rad = 1/self.L*(self.vr-self.vl)/100

        omega = 360/(2*3.14)*omega_rad

        self.vel = vec(self.speed, 0).rotate(-self.theta)

        self.rot_speed = omega

    def get_cm_pos(self):
        x_cm = self.pos[0]/5
        y_cm = (parametri.VISINA - (self.pos[1]))/5

        return x_cm, y_cm, self.theta


