#!/usr/bin/env python
# coding: utf-8
# For this section, I choose "Additional instructions might include moving forward by more than one square, or moving backwards one square."for improvement.

# In[ ]:


import random

def move_robot(k, p, x_0, y_0, steps):
    x, y = x_0, y_0
    direction = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(k):
        r = random.random()
        if r < p:
            x += dx[direction]
            y += dy[direction]
        elif r < (1 + p) / 2:
            direction = (direction - steps) % 4
        else:
            direction = (direction + steps) % 4

    return x, y

def main():
    k = int(input("Here enters a integer："))
    p = float(input("Here enters the possibility（0 < p < 1）："))
    x_0, y_0 = 0, 0
    runs = int(input("Here enters the how many times of running："))
    steps = int(input("Here enters the unit length of the step(n is natural number )"))
    locations = {}

    for _ in range(runs):
        x, y = move_robot(k, p, x_0, y_0, steps)
        location = (x, y)
        locations[location] = locations.get(location, 0) + 1

    print("the location of the robot：")
    for location, count in locations.items():
        print(f"{location}: {count / runs * 100:.2f}%")

if __name__ == "__main__":
    main()


# In[ ]:




