def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column."""
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from the water column height."""
    rho = 998.2  # Density of water (kg/m³)
    g = 9.80665  # Gravitational acceleration (m/s²)
    return (rho * g * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure loss from pipe friction."""
    rho = 998.2  # Density of water (kg/m³)
    return (-friction_factor * pipe_length * rho * fluid_velocity ** 2) / (2000 * pipe_diameter)
