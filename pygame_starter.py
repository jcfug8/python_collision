import pygame
import math
import game_mouse
import circle
import rectangle
import polygon

# Starter code for PyGame applications

class PygameStarter(game_mouse.Game):

    def __init__(self, width, height, fps):

        game_mouse.Game.__init__(self, "Pygame Starter",
                                 width,
                                 height,
                                 fps)
        self.circles = []
        self.rectangles = []
        self.polygons = []
        return
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]

        if pygame.K_c in newkeys:
            self.circles.append(circle.Circle(x,y, self.width, self.height))
        if pygame.K_r in newkeys:
            self.rectangles.append(rectangle.Rectangle(x,y, self.width, self.height))
        if pygame.K_p in newkeys:
            self.polygons.append(polygon.Polygon(x,y, self.width, self.height))

        if 1 in newbuttons:
            print("button clicked")

        for c in self.circles:
            c.move_logic(x,y)
            for c2 in self.circles:
                if c2 is not c:
                    if c.collision_logic_c(c2):
                        print("boom-c")
            for r in self.rectangles:
                if c.collision_logic_p(r):
                    print("boom-c")
            for p in self.polygons:
                if c.collision_logic_p(p):
                    print("boom-c")
        for r in self.rectangles:
            r.move_logic()
        for p in self.polygons:
            p.move_logic()

        return

    def paint(self, surface):
        surface.fill((255,255,255))
        for c in self.circles:
            c.paint(surface)
        for r in self.rectangles:
            r.paint(surface)
        for p in self.polygons:
            p.paint(surface)
        return

def main():
    screen_width = 600
    screen_height = 500
    frames_per_second = 20
    game = PygameStarter(screen_width, screen_height, frames_per_second)
    game.main_loop()
    return

if __name__ == "__main__":
    main()
