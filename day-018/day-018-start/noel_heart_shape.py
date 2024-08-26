import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_dog(ax, x, y, size):
    # Draw the body
    body = patches.Ellipse((x, y), width=size * 2, height=size, edgecolor='black', facecolor='brown')
    ax.add_patch(body)

    # Draw the head
    head = patches.Circle((x + size, y + size * 0.75), radius=size * 0.5, edgecolor='black', facecolor='brown')
    ax.add_patch(head)

    # Draw the ears
    ear1 = patches.Ellipse((x + size * 1.3, y + size * 1.2), width=size * 0.3, height=size * 0.6, angle=45,
                           edgecolor='black', facecolor='brown')
    ear2 = patches.Ellipse((x + size * 0.7, y + size * 1.2), width=size * 0.3, height=size * 0.6, angle=-45,
                           edgecolor='black', facecolor='brown')
    ax.add_patch(ear1)
    ax.add_patch(ear2)

    # Draw the legs
    leg1 = patches.Rectangle((x - size * 0.5, y - size * 0.75), width=size * 0.2, height=size * 0.75, edgecolor='black',
                             facecolor='brown')
    leg2 = patches.Rectangle((x + size * 0.3, y - size * 0.75), width=size * 0.2, height=size * 0.75, edgecolor='black',
                             facecolor='brown')
    ax.add_patch(leg1)
    ax.add_patch(leg2)

    # Draw the tail
    tail = patches.FancyArrow(x - size, y, dx=-size * 0.5, dy=size * 0.5, width=size * 0.1, length_includes_head=True,
                              head_length=size * 0.5, head_width=size * 0.2, color='brown')
    ax.add_patch(tail)


# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_aspect('equal')

# Draw multiple dogs in a grid
grid_size = 5
for i in range(grid_size):
    for j in range(grid_size):
        draw_dog(ax, x=i * 15 - 30, y=j * 15 - 30, size=5)

# Show the plot
ax.set_axis_off()
plt.show()