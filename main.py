class Particula:
    _x: float
    _y: float
    _vx: float
    _vy: float

    def __init__(self):
        try:
            self._x = float(input("Escriba la coordenada x: "))
        except ValueError:
            self._x = float(0)
        try:
            self._y = float(input("Escriba la coordenada y: "))
        except ValueError:
            self._y = float(0)
        try:
            self._vx = float(input("Escriba la velocidad en el eje x: "))
        except ValueError:
            self._vx = float(1)
        try:
            self._vy = float(input("Escriba la velocidad en el eje y: "))
        except ValueError:
            self._vy = float(1)

    def dt(self):
        # Coordenadas
        cx = self._x
        cy = self._y
        # Desplazamiento
        dpx = self._x + self._vx
        dpy = self._y + self._vy
        return cx, cy, dpx, dpy

    def _mover(self, tupler):
        returns = tupler

        cx = returns[0]
        cy = returns[1]
        desX = returns[2]
        desY = returns[3]

        print(f"Partícula en posición ({cx}, {cy}) y velocidad ({desX}, {desY})")


ptc = Particula

ptc.__init__(ptc)
ptc._mover(ptc, ptc.dt(ptc))
