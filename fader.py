import math
import time

class Fader:
    def __init__(self, period):
        self.period = period
        self.ended = True

        self.rStart = 0
        self.gStart = 0
        self.bStart = 0

        self.r0 = 0
        self.g0 = 0
        self.b0 = 0
        self.r1 = 0
        self.g1 = 0
        self.b1 = 0

        self.rEnd = 0
        self.gEnd = 0
        self.bEnd = 0

        self.dR = 0
        self.dG = 0
        self.dB = 0
        self.dMax = 0

        self.sR = 0
        self.sG = 0
        self.sB = 0

        self.steps = 0

        self.timeInterval = 0
        self.timeStart = 0

    def set_period(self, period):
        self.period = period
        self.calc_time_interval()

    def reset(self):
        self.set_fade(self.rStart, self.gStart, self.bStart, self.rEnd, self.gEnd, self.bEnd)

    def set_fade(self, r0, g0, b0, r1, g1, b1):
        self.r0 = r0
        self.g0 = g0
        self.b0 = b0
        self.r1 = r1
        self.g1 = g1
        self.b1 = b1

        self.rStart = r0
        self.gStart = g0
        self.bStart = b0

        self.rEnd = r1
        self.gEnd = g1
        self.bEnd = b1

        self.dR = self.uiabs(r1, r0)
        self.sR = 1 if r0 < r1 else -1

        self.dG = self.uiabs(g1, g0)
        self.sG = 1 if g0 < g1 else -1

        self.dB = self.uiabs(b1, b0)
        self.sB = 1 if b0 < b1 else -1

        self.dMax = self.max3(self.dR, self.dG, self.dB)
        self.steps = self.dMax

        self.calc_time_interval()
        self.timeStart = 0

        self.r1 = self.g1 = self.b1 = self.dMax / 2

        self.ended = False

    def calc_time_interval(self):
        if self.steps == 0:
            self.timeInterval = 1
            return

        self.timeInterval = self.period / self.steps
        
        if self.timeInterval == 0:
            self.timeInterval = 1

    def get_next(self):
        if time.time_ns() - self.timeStart < self.timeInterval:
            return (-1, -1, -1)

        self.timeStart = time.time_ns()

        r = self.r0
        g = self.g0
        b = self.b0

        self.ended = self.steps == 0

        if not self.ended:
            self.steps -= 1

            self.r1 -= self.dR
            if self.r1 < 0:
                self.r1 += self.dMax
                self.r0 += self.sR

            self.g1 -= self.dG
            if self.g1 < 0:
                self.g1 += self.dMax
                self.g0 += self.sG

            self.b1 -= self.dB
            if self.b1 < 0:
                self.b1 += self.dMax
                self.b0 += self.sB

        return (r, g, b)

    def max3(self, x, y, z):
        m = z

        if x > y:
            if x > z:
                m = x
        else:
            if y > z:
                m = y
        
        return m

    def uiabs(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a
