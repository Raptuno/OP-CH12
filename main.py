try:
    x = float(input("Escriba el valor de x: "))
except ValueError:
    x = float(0)

try:
    y = float(input("Escriba el valor de y: "))
except ValueError:
    y = float(0)

try:
    vx = float(input("Escriba la velocidad de x: "))
except ValueError:
    vx = float(1)

try:
    vy = float(input("Escriba la velocidad de y: "))
except ValueError:
    vy = float(1)


class Particula:
    _x: float
    _y: float
    _vx: float
    _vy: float

    def __init__(self):
        self._x = x
        self._y = y
        self._vx = vx
        self._vy = vy

    #def dt(self):
     #   return
    # def _mover(dt):


ptc = Particula

ptc.__init__(ptc)
