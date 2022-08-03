from typing import Iterable
from hybrid_routing.vectorfields.base import Vectorfield
import jax.numpy as jnp


class Circular(Vectorfield):
    """Circular vector field, implements Vectorfield class.
    Vectorfield defined by:
    W: (x, y) -> (u, v), u(x, y) = 0.05 * (y + 1), v(x, y) = 0.05 * (-x - 3)
    with:
        du/dx = 0,      du/dy = 0.05
        dv/dx = -0.05,  dv/dy = 0
    """

    def __init__(self):
        pass

    def dvdx(self, x: float, y: float) -> float:
        return -0.05

    def dvdy(self, x: float, y: float) -> float:
        return 0

    def dudx(self, x: float, y: float) -> float:
        return 0

    def dudy(self, x: float, y: float) -> float:
        return 0.05

    def get_current(self, x: float, y: float) -> jnp.array:
        return jnp.asarray([0.05 * (y + 1), 0.05 * (-x - 3)])
