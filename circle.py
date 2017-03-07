import pygame
from random import randint
import math

class Circle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.radius = randint(10,50)
        self.top = y - self.radius
        self.bottom = y + self.radius
        self.left = x - self.radius
        self.right = x + self.radius
        self.dx = randint(-20, 20)
        self.dy = randint(-20, 20)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.screen_width = width
        self.screen_height = height
        self.area = self.get_area()

    def paint(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius )
    def get_area(self):
        return math.pi*self.radius**2
    def move_logic(self, x, y):

        if self.x + self.radius >= self.screen_width:
            self.dx *= -1
            self.x = self.screen_width - self.radius
        if self.x - self.radius <= 0:
            self.dx *= -1
            self.x = self.radius
        if self.y + self.radius >= self.screen_height:
            self.dy *= -1
            self.y = self.screen_height - self.radius
        if self.y - self.radius <= 0:
            self.dy *= -1
            self.y = self.radius

        self.x += self.dx
        self.y += self.dy
        # self.x = x
        # self.y = y

        self.top = self.y - self.radius
        self.bottom = self.y + self.radius
        self.left = self.x - self.radius
        self.right = self.x + self.radius
    def rebound(self, shape):
        temp_dx, temp_dy = self.dx, self.dy
        self.dx, self.dy = shape.dx, shape.dy
        shape.dx, shape.dy = temp_dx, temp_dy

    def collision_logic_c(self, shape):
        if math.sqrt((self.x - shape.x)**2 + (self.y - shape.y)**2) <= self.radius + shape.radius:
            # print("collision")
            self.rebound(shape)
            return True
        return False
    def collision_logic_p(self, shape):
        # print(shape.points)
        if self.left > shape.right or self.right < shape.left or self.top > shape.bottom or self.bottom < shape.top:
            return False

        x1, y1 = shape.points[len(shape.points)-1]
        for x2, y2 in shape.points:
            if x1 - x2 == 0:
                if (self.x - x1)**2 <= self.radius**2:
                    temp_points = {}
                    temp_y1 = self.y - math.sqrt(self.radius**2 - (self.x - x1)**2)
                    temp_y2 = self.y + math.sqrt(self.radius**2 - (self.x - x1)**2)
                    if temp_y1 < max(y1, y2) and temp_y1 > min(y1, y2):
                        temp_points["y1"] = temp_y1
                    if temp_y2 < max(y1, y2) and temp_y2 > min(y1, y2):
                        temp_points["y2"] = temp_y2
                    if len(temp_points) > 0:
                        self.rebound(shape)
                        return True

            elif y1 - y2 == 0:
                if (self.y - y1)**2 <= self.radius**2:
                    temp_points = {}
                    temp_x1 = self.y - math.sqrt(self.radius**2 - (self.y - y1)**2)
                    temp_x2 = self.y + math.sqrt(self.radius**2 - (self.y - y1)**2)
                    if temp_x1 < max(x1, x2) and temp_x1 > min(x1, x2):
                        temp_points["x1"] = temp_x1
                    if temp_x2 < max(x1, x2) and temp_x2 > min(x1, x2):
                        temp_points["x2"] = temp_x2
                    if len(temp_points) > 0:
                        self.rebound(shape)
                        return True
            else:
                px = x2-x1
                py = y2-y1
                temp = px*px + py*py
                u =  ((self.x - x1) * px + (self.y - y1) * py) / float(temp)
                if u > 1:
                    u = 1
                elif u < 0:
                    u = 0
                x = x1 + u * px
                y = y1 + u * py
                dx = x - self.x
                dy = y - self.y
                dist = math.sqrt(dx*dx + dy*dy)
                if dist <= self.radius:
                    self.rebound(shape)
                    return True

            x1, y1 = x2 , y2
        return False
