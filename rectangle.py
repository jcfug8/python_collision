import pygame
from random import randint

class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = randint(20,100)
        self.height = randint(20,100)

        self.top = y
        self.bottom = y + self.height
        self.left = x
        self.right = x + self.width

        self.points = [(x, y), (self.right, y), (self.right, self.bottom), (x, self.bottom)]

        self.dx = randint(-20, 20)
        self.dy = randint(-20, 20)
        self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.screen_width = width
        self.screen_height = height

    def paint(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height) )

    def move_logic(self):

        if self.x + self.width >= self.screen_width:
            self.dx *= -1
        if self.x <= 0:
            self.dx *= -1
        if self.y + self.height >= self.screen_height:
            self.dy *= -1
        if self.y <= 0:
            self.dy *= -1

        self.x += self. dx
        self.y += self. dy


        self.top = self.y
        self.bottom = self.y + self.height
        self.left = self.x
        self.right = self.x + self.width
        self.points = [(self.x, self.y), (self.right, self.y), (self.right, self.bottom), (self.x, self.bottom)]

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
