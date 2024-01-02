
# import important packages
import matplotlib.pyplot as plt
import numpy as np

def projectile_motion(angle, initial_height, initial_velocity, gravity=9.8, time_step=0.01):
    """
    Calculate the trajectory of the projectile for a given launch angle.

    Parameters:
    - angle (float): Launch angle of the projectile in degrees.
    - initial_height (float): Initial height of the projectile.
    - initial_velocity (float): Initial velocity of the projectile.
    - gravity (float): Acceleration due to gravity.
    - time_step (float): Time mesh for simulation.

    Returns:
    - tuple: x and y coordinates of the projectile at each time point.
    """
    # Convert angle to radians
    theta = np.radians(angle)

    # Initialize position and velocity
    x = 0
    y = initial_height
    vx = initial_velocity * np.cos(theta)
    vy = initial_velocity * np.sin(theta)

    # Lists to store trajectory points
    x_values = [x]
    y_values = [y]

    # Update position until the projectile hits the ground
    while y >= 0:
        x = x + (vx * time_step)
        y = y + (vy * time_step) - (0.5 * gravity * time_step**2)
        vy = vy - (gravity * time_step)

        # Append current position to the lists
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# Set general title for the entire figure
fig.suptitle('Projectile Motion of Ball at 3 Different Angles and Heights', fontsize=14)

def plot_projectiles(ax, initial_height, initial_velocity, angles):
    """
    Plot the projectile motion for multiple launch angles.

    Parameters:
    - ax (matplotlib.axes._subplots.AxesSubplot): Axes object for the subplot.
    - initial_height (float): Initial height of the projectile.
    - initial_velocity (float): Initial velocity of the projectile.
    - angles (list): List of launch angles in degrees.

    Returns:
    - None
    """
    
    colors = ['r', 'g', 'b'] # list of color palette
    for angle, color in zip(angles, colors):
        x_vals, y_vals = projectile_motion(angle, initial_height, initial_velocity) # store trajectectory in resp. cordinates
        ax.plot(x_vals, y_vals, label=f'Angle {angle}°', color=color)

    ax.set_xlabel('Range (m)')
    ax.set_ylabel('Altitude (m)')
    
    # Set x-axis and y-axis limits to start from 0
    ax.set_xlim(0)
    ax.set_ylim(bottom=0)

    # Add faded grid
    ax.grid(alpha=0.2)

    # Add legend with labels
    ax.legend()


# Common parameters for all balls (editable)
initial_height = [0, 30]
initial_velocity = 25

# List of launch angles (editable)
angles = [30, 45, 60]


# Plot projectile motion for initial height = 0
plot_projectiles(ax1, initial_height[0], initial_velocity, angles)
ax1.set_title(f'Initial Altitude = {initial_height[0]}m    Initial Velcity = {initial_velocity}m/s')

# Plot projectile motion for initial height = 20
plot_projectiles(ax2, initial_height[1], initial_velocity, angles)
ax2.set_title(f'Initial Altitude = {initial_height[1]}   Initial Velcity = {initial_velocity}m/s')



plt.show()