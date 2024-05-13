import pygame

class button:
    def __init__(self, x, y, width, height, text, color):

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BROWN = (210, 180, 140)
        self.PURPLE = (128, 0, 128)
        self.PINK = (255, 192, 203)
        self.YELLOW = (184, 134, 11)
        self.DARKBLUE = (106, 90, 205)

        self.startX = x
        self.startY = y
        self.width = width
        self.height = height

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.fontColor = None
        self.font = None

    def draw(self, screen, font, fontColor = None):
        self.text_surface = font.render("           ", True, self.WHITE)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, self.text_rect)
        self.font = font
        if fontColor == None:

            fontColor = self.BLACK

        self.fontColor = fontColor

        pygame.draw.rect(screen, self.color, self.rect)
        self.text_surface = font.render(self.text, True, self.fontColor)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, self.text_rect)

    def specialDraw(self, screen, font, fontColor = None):
        if fontColor == None:
            fontColor = self.GREEN

        self.fontColor = fontColor
        #pygame.draw.rect(screen, self.fontColor, self.rect, 4)
        self.text_surface = font.render(self.text, True, self.fontColor)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def get_font(self):
        return self.font
    def buttonName(self):
        return self.text

    def get_dimensions(self):
        return self.startX, self.startY, self.width, self.height