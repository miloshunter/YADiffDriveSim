import pygame as pg

# Boje
BELA = (255, 255, 255)
CRNA = (0, 0, 0)
TAMNO_SIVA = (40, 40, 40)
SVETLO_SIVA = (100, 100, 100)
ZELENA = (0, 255, 0)
CRVENA = (255, 0, 0)
ZUTA = (255, 255, 0)

# Prozor
SIRINA = 1200   # 16 * 64 or 32 * 32 or 64 * 16
VISINA = 1000  # 16 * 48 or 32 * 24 or 64 * 12
SIRINA_MENIJA = 400
FPS = 10
NASLOV = "Lavirint"
BOJA_POZADINE = TAMNO_SIVA

# Robot
DIMENZIJE_ROBOTA = 150
DOMET_LASERA = 250


def cm_to_px(x, y, theta):
    x_px = x * 5
    y_px = VISINA - (y * 5)
    theta_px = -theta + 90
    return x_px, y_px, theta_px

