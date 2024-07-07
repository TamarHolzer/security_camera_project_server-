import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the coordinates of the polygon
polygon_coords = [(20,5),(25,8),(21,10),(18, 7)]

# Define the point
point_coords = (18.0, 7.0)

# Create the plot
fig, ax = plt.subplots()

# Add the polygon to the plot
polygon = patches.Polygon(polygon_coords, closed=True, fill=None, edgecolor='r')
ax.add_patch(polygon)

# Add the point to the plot
ax.plot(point_coords[0], point_coords[1], 'bo')  # 'bo' means blue color, circle marker

# Set the limits of the plot
ax.set_xlim(-1, 30)
ax.set_ylim(-1, 30)

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Polygon with a Point')

# Show the plot
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
