from .antoine import AntoineComponent

R = 8.314  # Ideal gas constant [J/(mol*K)]
G = 9.81  # gravitational acceleration on earth [m/s^2]

COMPONENTS = {
    "H2": AntoineComponent("Hydrogen", 13.6333, 164.9, 3.19, "mmHg", "ln"),
    "CO": AntoineComponent("CO", 14.3686, 530.22, -13.15, "mmHg", "ln"),
    "CO2": AntoineComponent("Carbon-Dioxide", 22.5898, 3103.39, -0.16, "mmHg", "ln"),
    "CH4": AntoineComponent("Mehtane", 15.2243, 897.84, -7.16, "mmHg", "ln"),
    "MeOH": AntoineComponent("Methanol", 18.5875, 3626.55, -34.29, "mmHg", "ln"),
    "H20": AntoineComponent("Water", 18.3036, 3816.44, -46.13, "mmHg", "ln"),
}
