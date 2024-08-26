import colorgram

rgb_colors = []
number_of_colors = 20
colors = colorgram.extract('Hirstspotpainting.jpg',number_of_colors)

for _ in range(0, number_of_colors):
    #print(colors[_].rgb)
    r = colors[_].rgb.r
    g = colors[_].rgb.g
    b = colors[_].rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
