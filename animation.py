import pygame

class Animation():


    def __init__(self):
        pygame.init()
        self.text = " "
        self.moveName = " "

        self.textRect = None
        self.screen = None
        self.font = None

        self.speed = 5
        self.counter = 0
        self.timer = pygame.time.Clock()

    def print(self, screen, text, font, textRect):
        self.timer.tick(60)
        self.isItDone = False
        self.screen = screen
        self.text = text
        self.font = font
        self.textRect = textRect

        while self.isItDone != True:
            if self.counter < self.speed * len(self.text):
                self.counter += 1
            elif self.counter >= self.speed * len(self.text):
                self.isItDone = True

            self.snip = self.font.render(self.text[0:(self.counter // (self.speed))], True, 'black')
            self.screen.blit(self.snip, self.textRect)


    def attackingMove(self, attackingMove):
        pass