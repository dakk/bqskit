"""This module implements the ConstantGate base class."""
from __future__ import annotations

from typing import Sequence

import numpy as np

from bqskit.ir.gate import Gate
from bqskit.qis.unitary.differentiable import DifferentiableUnitary
from bqskit.qis.unitary.optimizable import LocallyOptimizableUnitary
from bqskit.qis.unitary.unitarymatrix import UnitaryMatrix
from bqskit.utils.cachedclass import CachedClass


class ConstantGate(
    Gate,
    DifferentiableUnitary,
    LocallyOptimizableUnitary,
    CachedClass,
):
    """A gate that does not change during circuit instantiation."""

    _num_params = 0
    _utry: UnitaryMatrix

    def get_unitary(self, params: Sequence[float] = []) -> UnitaryMatrix:
        """Return the unitary for this gate, see :class:`Unitary` for more."""
        self.check_parameters(params)
        return getattr(self, '_utry')

    def get_grad(self, params: Sequence[float] = []) -> np.ndarray:
        """
        Return the gradient for this gate.

        See :class:`DifferentiableUnitary` for more info.
        """
        self.check_parameters(params)
        return np.array([])

    def get_unitary_and_grad(
        self,
        params: Sequence[float] = [],
    ) -> tuple[UnitaryMatrix, np.ndarray]:
        """
        Return the unitary and gradient for this gate.

        See :class:`DifferentiableUnitary` for more info.
        """
        self.check_parameters(params)
        return getattr(self, '_utry'), np.array([])

    def optimize(self, env_matrix: np.ndarray) -> list[float]:
        """
        Return the optimal parameters with respect to an environment matrix.

        See :class:`LocallyOptimizableUnitary` for more info.
        """
        return []
