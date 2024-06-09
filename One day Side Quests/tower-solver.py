# Solves Tower of Hanoi


def play(h, curr, pivot, target):
    if h == 0:
        return
    play(h - 1, curr, target, pivot)
    print(f"Move {str(h)} to {target}")
    play(h - 1, pivot, curr, target)


TOWER_HEIGHT = 15


if __name__ == "__main__":
    play(TOWER_HEIGHT, "left", "middle", "right")