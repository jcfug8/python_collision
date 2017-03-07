#
# You should not need to edit this file.
#
import pygame
import pygame.locals

class Game:
    def __init__(self, name, width, height, frames_per_second):
        self.width = width
        self.height = height
        self.frames_per_second = frames_per_second
        self.on = True

        self.screen = pygame.display.set_mode(
                # set the size
                (width, height),

                # use double-buffering for smooth animation
                pygame.locals.DOUBLEBUF |

                # apply alpha blending
                pygame.locals.SRCALPHA)

        # set the title of the window
        pygame.display.set_caption(name)
        
        # set time tracking
        self.clock = pygame.time.Clock()
        self.this_frame_time = pygame.time.get_ticks() / 1000.
        self.last_frame_time = self.this_frame_time
        return

    def get_frame_time(self):
        return self.this_frame_time
        
    def get_delta_time(self):
        return self.delta_time
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        raise NotImplementedError()
        return

    def paint(self, surface):
        raise NotImplementedError()
        return

    def main_loop(self):
        keys = set()
        buttons = set()
        mouse_position = (1,1)
        self.last_frame_time = pygame.time.get_ticks() / 1000.

        while True:
            self.clock.tick(self.frames_per_second)

            newkeys = set()
            newbuttons = set()
            for e in pygame.event.get():
                # did the user try to close the window?
                if e.type == pygame.QUIT:
                    pygame.quit()
                    return

                # did the user just press the escape key?
                if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

                # track which mouse buttons are currently pressed
                if e.type == pygame.MOUSEBUTTONDOWN:
                    buttons.add(e.button)
                    newbuttons.add(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEBUTTONUP:
                    buttons.discard(e.button)
                    mouse_position = e.pos

                if e.type == pygame.MOUSEMOTION:
                    mouse_position = e.pos
                
                # track which keys are currently set
                if e.type == pygame.KEYDOWN:
                    keys.add(e.key)
                    newkeys.add(e.key)
                if e.type == pygame.KEYUP:
                    keys.discard(e.key)

            self.this_frame_time = pygame.time.get_ticks() / 1000.
            self.delta_time = (self.this_frame_time - self.last_frame_time)
            self.last_frame_time = self.this_frame_time
            if self.on:
                self.game_logic(keys, newkeys, buttons, newbuttons, mouse_position)
                self.paint(self.screen)

            pygame.display.flip()
        return

