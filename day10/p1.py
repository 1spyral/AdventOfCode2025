# AOC 2025 Day 10 Problem 1

with open("input.txt", "r") as f:
    data = f.read()

lines = data.split("\n")

ans = 0

for line in lines:
    segments = line.split()
    desired = segments[0][1:-1]
    buttons = [list(map(int, segment[1:-1].split(","))) for segment in segments[1:-1]]

    lights = [0 for _ in range(len(desired))]

    val = float("inf")

    def check():
        for i in range(len(desired)):
            if desired[i] == "." and lights[i] % 2 == 1 or desired[i] == "#" and lights[i] % 2 == 0:
                return False
        return True

    def traverse(index = 0, pressed = 0):
        if index == len(buttons):
            return
        # Not pressed
        traverse(index + 1, pressed)
        # Pressed
        for light in buttons[index]:
            lights[light] += 1
        if check():
            global val
            val = min(val, pressed + 1)
        traverse(index + 1, pressed + 1)
        for light in buttons[index]:
            lights[light] -= 1
    
    traverse()

    ans += val

print(ans)
