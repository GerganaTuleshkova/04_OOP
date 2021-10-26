def print_rhombus():

    n = int(input())

    def print_line(spaces_count, stars_count):
        print(" " * spaces_count, end="")
        print(' '.join("*" * stars_count))

    for i in range(1, n + 1):
        spaces_count = n - i
        stars_count = i
        print_line(spaces_count, stars_count)
    for i in range(n - 1, -1, -1):
        spaces_count = n - i
        stars_count = i
        print_line(spaces_count, stars_count)


print_rhombus()