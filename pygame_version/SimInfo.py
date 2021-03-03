import pygame_gui
import pygame as pg
from pygame_version import parametri


class SimInfo:
    def __init__(self):
        self.manager = pygame_gui.UIManager((parametri.SIRINA + parametri.SIRINA_MENIJA,
                                             parametri.VISINA))

        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 50), (200, 50)),
            text='Pokreni simulaciju',
            manager=self.manager)

        self.lab = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 2 * 50), (200, 50)),
            text='Vreme simulacije[ms]: ',
            manager=self.manager)

        self.sat = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 220, 2 * 50), (100, 50)),
            text=' ',
            manager=self.manager)

        # Prethodna pozicija robota
        self.lab_pret_x = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 3 * 50), (70, 50)),
            text='pret X: ',
            manager=self.manager)

        self.pret_x = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 90, 3 * 50), (50, 50)),
            text='0.0',
            manager=self.manager)
        self.lab_pret_y = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 140, 3 * 50), (70, 50)),
            text='pret Y: ',
            manager=self.manager)

        self.pret_y = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 210, 3 * 50), (50, 50)),
            text='0.0',
            manager=self.manager)
        self.lab_pret_t = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 270, 3 * 50), (70, 50)),
            text='theta: ',
            manager=self.manager)

        self.pret_theta = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 320, 3 * 50), (50, 50)),
            text='0.0',
            manager=self.manager)
        self.lab_sim_time = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 4 * 50), (200, 50)),
            text='sim time[sec]: ',
            manager=self.manager)

        self.sim_time = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((
            parametri.SIRINA + 220, 4 * 50), (50, 50)),
            manager=self.manager)
        self.sim_time.set_text("1.0")


        # Vr i Vl
        self.lab_vr = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 5 * 50), (70, 50)),
            text='Vr: ',
            manager=self.manager)

        self.vr = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((
            parametri.SIRINA + 90, 5 * 50), (50, 50)),
            manager=self.manager)
        self.vr.set_text("1.0")
        self.lab_vl = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 140, 5 * 50), (70, 50)),
            text='Vl: ',
            manager=self.manager)

        self.vl = pygame_gui.elements.UITextEntryLine(relative_rect=pg.Rect((
            parametri.SIRINA + 210, 5 * 50), (50, 50)),
            manager=self.manager)
        self.vl.set_text("1.0")

        # Prethodna pozicija robota
        self.lab_x = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 7 * 50), (70, 50)),
            text='X: ',
            manager=self.manager)

        self.x = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 90, 7 * 50), (50, 50)),
            text='0.0',
            manager=self.manager)
        self.lab_y = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 140, 7 * 50), (70, 50)),
            text='Y: ',
            manager=self.manager)

        self.y = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 210, 7 * 50), (50, 50)),
            text='0.0',
            manager=self.manager)
        self.lab_t = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 260, 7 * 50), (50, 50)),
            text='theta: ',
            manager=self.manager)
        self.theta = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 310, 7 * 50), (50, 50)),
            text='0.0',
            manager=self.manager)

        self.lab_pomeraj = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 20, 8 * 50), (80, 50)),
            text='Pomeraj: ',
            manager=self.manager)
        self.pomeraj = pygame_gui.elements.UILabel(relative_rect=pg.Rect((
            parametri.SIRINA + 100, 8 * 50), (250, 50)),
            text='x:, y:, th: ',
            manager=self.manager)

    def update_prev_position(self, x, y, theta):
        self.pret_x.set_text(f"{x:.1f}")
        self.pret_y.set_text(f"{y:.1f}")
        self.pret_theta.set_text(f"{theta:.1f}")

    def update_position(self, x, y, theta):
        self.x.set_text(f"{x:.1f}")
        self.y.set_text(f"{y:.1f}")
        self.theta.set_text(f"{theta:.1f}")

    def update_pos_diff(self, prev_pos, curr_pos):
        self.pomeraj.set_text("x: " + f"{curr_pos[0]-prev_pos[0]:.1f}" +
                              "  y: " + f"{curr_pos[1]-prev_pos[1]:.1f}" +
                              "  t: " + f"{curr_pos[2]-prev_pos[2]:.1f}"
                              )
