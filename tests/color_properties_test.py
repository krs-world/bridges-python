from bridges.color import Color

my_color = Color()

my_color.red = 10
my_color.green = 100
my_color.blue = 255
my_color.alpha = 1.0

print(my_color.rgba)

other_color = Color()
other_color.rgba = 100, 0, 20, 0
print(my_color.rgba, other_color.rgba)

other_color.set_red(255)
other_color.set_green(255)
other_color.set_blue(255)
other_color.set_alpha(1.0)
print(other_color.rgba)

other_color.set_color(0, 0, 0, 0)
print(other_color.rgba)

try:
    my_color.rgba = 256, 0, 1, 1.0
except ValueError:
    try:
        my_color.rgba = 0, 256, 0, 1.0
    except ValueError:
        try:
            my_color.rgba = 0, 0, 256, 1.0
        except ValueError:
            try:
                my_color.rgba = 0, 0, 0, 1.1
            except ValueError:
                print("Setter passed for overflow on RGBA")

try:
    my_color.rgba = -1, 0, 255, 0.0
except ValueError:
    try:
        my_color.rgba = 0, -1, 0, 1.0
    except ValueError:
        try:
            my_color.rgba = 0, 0, -1, 1.0
        except ValueError:
            try:
                my_color.rgba = 0, 0, 0, -0.1
            except ValueError:
                print("Setter passed for underflow on RGBA")
