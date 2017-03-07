import pygame
from random import randint
import math

class Polygon:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.points = [(x + randint(-50,50), y + randint(-50,50)),
                        (x + randint(-50,50), y + randint(-50,50)),
                        (x + randint(-50,50), y + randint(-50,50)),
                        (x + randint(-50,50), y + randint(-50,50)),
                        (x + randint(-50,50), y + randint(-50,50)),
                        (x + randint(-50,50), y + randint(-50,50))]
        x_points = []
        y_points = []
        for x, y in self.points:
            x_points.append(x)
            y_points.append(y)
        self.top = min(y_points)
        self.bottom = max(y_points)
        self.left = min(x_points)
        self.right = max(x_points)
        print(self.top, self.bottom, self.left, self.right)


        self.dx = randint(-20, 20)
        self.dy = randint(-20, 20)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.screen_width = width
        self.screen_height = height

    def paint(self, surface):
        pygame.draw.polygon(surface, self.color, self.points )

    def move_logic(self):

        if self.right >= self.screen_width:
            self.dx *= -1
        if self.left <= 0:
            self.dx *= -1
        if self.bottom >= self.screen_height:
            self.dy *= -1
        if self.top <= 0:
            self.dy *= -1


        self.top += self.dy
        self.bottom += self.dy
        self.left += self.dx
        self.right += self.dx
        points = []
        for x, y in self.points:
            points.append((x + self.dx, y + self.dy))
        self.points = points
    def collision_logic_c(self, shape):
        self_x1, self_y1 = self.points[len(self.points)-1]
        for self_x2, self_y2 in self.points:
            if self_x1 - self_x2 == 0:
                if (shape.x - self_x1)**2 <= shape.radius**2:
                    temp_points = {}
                    temp_y1 = shape.y - math.sqrt(shape.radius**2 - (shape.x - self_x1)**2)
                    temp_y2 = shape.y + math.sqrt(shape.radius**2 - (shape.x - self_x1)**2)
                    if temp_y1 < max(self_y1, self_y2) and temp_y1 > min(self_y1, self_y2):
                        temp_points["y1"] = temp_y1
                    if temp_y2 < max(self_y1, self_y2) and temp_y2 > min(self_y1, self_y2):
                        temp_points["y2"] = temp_y2
                    if len(temp_points) > 0:
                        return True

            elif self_y1 - self_y2 == 0:
                if (shape.y - self_y1)**2 <= shape.radius**2:
                    temp_points = {}
                    temp_x1 = shape.y - math.sqrt(shape.radius**2 - (shape.y - self_y1)**2)
                    temp_x2 = shape.y + math.sqrt(shape.radius**2 - (shape.y - self_y1)**2)
                    if temp_x1 < max(self_x1, self_x2) and temp_x1 > min(self_x1, self_x2):
                        temp_points["x1"] = temp_x1
                    if temp_x2 < max(self_x1, self_x2) and temp_x2 > min(self_x1, self_x2):
                        temp_points["x2"] = temp_x2
                    if len(temp_points) > 0:
                        return True
            else:
                px = self_x2-self_x1
                py = self_y2-self_y1
                temp = px*px + py*py
                u =  ((shape.x - self_x1) * px + (shape.y - self_y1) * py) / float(temp)
                if u > 1:
                    u = 1
                elif u < 0:
                    u = 0
                x = self_x1 + u * px
                y = self_y1 + u * py
                dx = x - shape.x
                dy = y - shape.y
                dist = math.sqrt(dx*dx + dy*dy)
                if dist <= shape.radius:
                    return True
            self_x1, self_y1 = self_x2, self_y2
        return False

    def collision_logic_p(self, shape):
        self_x1, self_y1 = self.points[len(self.points)-1]
        for self_x2, self_y2 in self.points:
            
            x1, y1 = shape.points[len(shape.points)-1]
            for x2, y2 in shape.points:

                x1, y1 = x2 , y2
            self_x1, self_y1 = self_x2, self_y2
