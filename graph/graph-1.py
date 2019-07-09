# -*- coding: utf-8 -*-
import math

step = 5
range = 50

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
    
    def get_adjacent(self, points:list):
        l = []
        for p in points:
            if math.sqrt(abs(self.x - p.x) * abs(self.x - p.x) + abs(self.y - p.y) * abs(self.y - p.y)) <= 10:
                l.append(p)
        
        return l
    
    def can_out(self):
        return abs(self.x) >= (range - step) or abs(self.y) >= (range -step)  

def dfs(p:Point, points:list):
    p.visited = True
    if p.can_out():
        return True
    else:
        r = False
        adjacent_points = p.get_adjacent(points)
        for ap in adjacent_points:
            if ap.visited == True:
                continue
            can_out = dfs(ap, points)
            if can_out:
                r = True
                break

        return r

if __name__ == "__main__":
    points = []
    points.append(Point(50,50))
    points.append(Point(5,5))
    points.append(Point(10,10))
    points.append(Point(15,15))
    points.append(Point(20,20))
    points.append(Point(25,25))
    points.append(Point(30,30))
    points.append(Point(35,35))
    points.append(Point(40,40))
    points.append(Point(45,45))
    result = dfs(Point(0,0), points)
    print(result)