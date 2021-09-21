def jumpingOnClouds(c):
    x, y = 0, 0
    while x < len(c) - 2:
        x = x + 1 if c[x + 2] else x + 2
        y += 1
    if x < len(c) - 1:
        y += 1
    return y

print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))