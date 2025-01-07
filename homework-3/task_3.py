def draw_christmas_tree(size):
    for i in range(size):
        spaces = ' ' * (size - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    trunk_width = 1
    trunk_height = 2
    trunk_spaces = ' ' * (size - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + '*' * trunk_width)
draw_christmas_tree(6)

