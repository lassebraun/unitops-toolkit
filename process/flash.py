from typing import Iterable
from ..common.antoine import AntoineComponent


def calculate_flash(
    p_target_pa, components, ref_n, xi_n, epsilon=0.1, initial_T=298.15
):
    """
    Approximates the temperature of a p-xi Flash by iteration
    """
    T_kelvin = initial_T
    T_prev = T_kelvin + 1.0
    error_prev = None

    for iteration in range(100):
        p0 = {}
        alpha_k_n = {}
        xi_k = {}
        x5_k = {}

        for name, comp in components.items():
            p0[name] = comp.get_psat_pa(T_kelvin)

        for name in components:
            alpha_k_n[name] = p0[name] / p0[ref_n]

        for name in components:
            numerator = alpha_k_n[name] * xi_n
            denominator = 1 + (alpha_k_n[name] - 1) * xi_n
            xi_k[name] = numerator / denominator
            x5_k[name] = xi_k[name]

        alpha_bar = sum(x5_k[name] * alpha_k_n[name] for name in components)

        p_calc = alpha_bar * p0[ref_n]
        error = abs(p_target_pa - p_calc)

        if error <= epsilon:
            print(f"Converged after {iteration} iterations.")
            print(
                f"Calculated Temperature: {T_kelvin:.2f} K ({T_kelvin - 273.15:.2f} °C)"
            )
            return T_kelvin, x5_k

        if error_prev is not None:
            derivative = (error - error_prev) / (T_kelvin - T_prev)
            if derivative != 0:
                T_next = T_kelvin - error / derivative
            else:
                T_next = T_kelvin * 1.01
        else:
            T_next = T_kelvin * 1.01

        T_prev = T_kelvin
        error_prev = error
        T_kelvin = T_next

    raise ValueError("Did not converge in 100 steps.")
