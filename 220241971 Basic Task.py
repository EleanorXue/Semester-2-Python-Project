#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def move_robot(k, p, x_0, y_0):
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
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

    return x, y



def main():
    k = int(input("Here enters a integer："))
    p = float(input("Here enters the possibility（0 < p < 1）："))
    x_0, y_0 = 0, 0
    runs = int(input("Here enters the how many times of running："))
    locations = {}

    for _ in range(runs):
        x, y = move_robot(k, p, x_0, y_0)
        location = (x, y)
        locations[location] = locations.get(location, 0) + 1

    print("the probability of the robot different locations：")
    for location, count in locations.items():
        print(f"{location}: {count / runs * 100:.2f}%")

if __name__ == "__main__":
    main()


# ##### 
