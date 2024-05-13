import pygame
import random
from buttons import button
from pakudex import Pakudex
from battle_dynamics import BattleDynamics
from animation import Animation

class Screens():

    def __init__(self, width, height):
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

        self.WINDOW_HEIGHT = height
        self.WINDOW_WIDTH = width
        self.pakudexList = Pakudex()

        self.displayedPakuriMoves = [None] * 4


        self.whoWon = "No One"
        self.displayedPakuriParty = [" "] * 5

        self.battle = BattleDynamics()
        self.animate = Animation()

        self.moveChosen = None

        # initializes screen dimensions based on pixels
        self.screen = pygame.display.set_mode((width, height))
        # window name
        pygame.display.set_caption('Pakuri Showdwon Ver1.0')
        # font text will be written in
        self.titleFont = pygame.font.Font('freesansbold.ttf', 64)
        self.buttonFont = pygame.font.Font('freesansbold.ttf', 16)
        self.informationFont = pygame.font.Font('freesansbold.ttf', 15)
        self.dialogueFont = pygame.font.Font('freesansbold.ttf', 18)
        self.playerOptionsFont = pygame.font.Font('freesansbold.ttf', 24)

        self.button1 = button(100, 600, 100, 50, "Battle", (255, 255, 255))
        self.button2 = button(300, 600, 100, 50, "Pakuri", (255, 255, 255))
        self.button3 = button(500, 600, 100, 50, "Instructions", (255, 255, 255))
        self.button4 = button(700, 600, 100, 50, "Credits", (255, 255, 255))

        self.fightButton = button(600, 650, 120, 100, "FIGHT", self.RED)
        self.pakuriButton = button(720, 650, 120, 100, "PAKURI", self.BLUE)
        self.forfeitButton = button(600, 750, 120, 100, "FORFEIT", self.GREEN)
        self.exitButton = button(720, 750, 120, 100, "EXIT", self.WHITE)

        self.confirmOptionButton = button(600, 650, 240, 100, "CONFIRM", self.RED)
        self.switchButton = button(600, 650, 240, 100, "SWITCH", self.RED)
        self.backButton = button(600, 750, 240, 100, "BACK", self.BLUE)
        self.sureButton = button(600, 650, 240, 100, "SURE?", self.GREEN)
    def welcomeScreen(self):
        self.text = self.titleFont.render('Pakuri Showdown', False, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)
        # image and scaling apprpriate to window size
        self.image_path = "pictures/pakuri_arena.jpg"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0)), self.screen.blit(self.text, self.textRect)

        self.button1.draw(self.screen, self.buttonFont)
        self.button2.draw(self.screen, self.buttonFont)
        self.button3.draw(self.screen, self.buttonFont)
        self.button4.draw(self.screen, self.buttonFont)

    def pakuriSelectionOne(self):
        self.pakuriSelection = [0] * 20

        self.image_path = "pictures/pakuri_selection_background.png"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0))

        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.text = self.font.render('PLAYER 1 CHOOSE YOUR PAKURI', False, self.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)

        self.screen.blit(self.text, self.textRect)

        for i in range(len(self.pakudexList.pakudex)):
            self.pakuriName = self.pakudexList.getName(i)
            self.pakuriSelection[i] = (button(50, (150 + (30*i)), 100, 30, self.pakuriName, (255, 255, 255)))
            self.pakuriSelection[i].draw(self.screen, self.buttonFont)

        self.selectButton = button(580, 700, 100, 50, "SELECT", (255, 255, 255))
        self.selectButton.draw(self.screen, self.buttonFont)

    def pakuriSelectionTwo(self):
        self.pakuriSelection = [0] * 20

        self.image_path = "pictures/pakuri_selection_background.png"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0))

        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.text = self.font.render('PLAYER 2 CHOOSE YOUR PAKURI', False, self.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)

        self.screen.blit(self.text, self.textRect)

        for i in range(len(self.pakudexList.pakudex)):
            self.pakuriName = self.pakudexList.getName(i)
            self.pakuriSelection[i] = (button(50, (150 + (30 * i)), 100, 30, self.pakuriName, (255, 255, 255)))
            self.pakuriSelection[i].draw(self.screen, self.buttonFont)

        self.selectButton = button(580, 700, 100, 50, "SELECT", (255, 255, 255))
        self.selectButton.draw(self.screen, self.buttonFont)

    #Needs to be fixed
    def pakuriInfo(self):
        self.pakuriSelection = [0] * 20

        self.image_path = "pictures/pakuri_selection_background.png"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0))

        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.text = self.font.render('PAKURI DATABASE', False, self.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)

        self.screen.blit(self.text, self.textRect)

        for i in range(len(self.pakudexList.pakudex)):
            self.pakuriName = self.pakudexList.getName(i)
            self.pakuriSelection[i] = (button(50, (150 + (30 * i)), 100, 30, self.pakuriName, (255, 255, 255)))
            self.pakuriSelection[i].draw(self.screen, self.buttonFont)

        self.backButton = button(580, 700, 100, 50, "BACK", (255, 255, 255))
        self.backButton.draw(self.screen, self.buttonFont)

    def Instructions(self):
        self.image_path = "pictures/pakuri_selection_background.png"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0))

        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.text = self.font.render('INSTRUCTIONS', False, self.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)
        self.screen.blit(self.text, self.textRect)

        self.description_text = [
            "Pakuri Showdown is a dynamic 2-player game where players assemble teams of up to 5 powerful",  "Pakuris to battle head-to-head. ",
            "Each Pakuri comes with its unique moveset, adding strategic depth to the gameplay.", "Players can opt to switch between Pakuris in ",
            "their team or unleash devastating attacks to outwit their opponent.", "The game offers flexibility with a forfeit option, allowing ",
            "players to make tactical decisions throughout the intense showdown.",  "It's a thrilling battle of strategy, skill, and quick ",
            "thinking in the world of Pakuris!"
        ]

        for i in range(len(self.description_text)):
            self.font = pygame.font.Font('freesansbold.ttf', 18)
            self.text = self.font.render(self.description_text[i], False, self.BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (900 // 2, 400+ 18*i)
            self.screen.blit(self.text, self.textRect)


        self.backButton = button(580, 700, 100, 50, "BACK", (255, 255, 255))
        self.backButton.draw(self.screen, self.buttonFont)

    def credits(self):
        self.image_path = "pictures/pakuri_selection_background.png"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0))

        self.font = pygame.font.Font('freesansbold.ttf', 48)
        self.text = self.font.render('Credits', False, self.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)
        self.screen.blit(self.text, self.textRect)

        self.description_text = [
            "Made by Murali Krishna Lingamsetty",
            "Attending the University of Florida", " Currently pursuing a Bachelors in Computer Engineering"
            "Version 1.0 completed on 5/13/2024 at 7:29 a.m.",
            "Images and Sprites were AI generated",
        ]

        for i in range(len(self.description_text)):
            self.font = pygame.font.Font('freesansbold.ttf', 20)
            self.text = self.font.render(self.description_text[i], False, self.BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (200, 400+ 24*i)
            self.screen.blit(self.text, self.textRect)


        self.backButton = button(580, 700, 100, 50, "BACK", (255, 255, 255))
        self.backButton.draw(self.screen, self.buttonFont)

    def getImage(self, name, dimension, startX, startY, flipped=False):

        if name == "Flamix":
            if flipped == True:
                self.displayPakuriImagePath = "pictures/Flamix.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Flamix.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Aquoray":
            if flipped == True:
                self.displayPakuriImagePath = "pictures/Aquoray.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Aquoray.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Terrasaur":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Terrasaur.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Terrasaur.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Electrixie":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Electrixie.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Electrixie.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Windora":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Windora.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Windora.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Glaciorb":
            if flipped == True:
                self.displayPakuriImagePath = "pictures/Glaciorb.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Glaciorb.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Pyrotusk":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Pyrotusk.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Pyrotusk.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Leaflynx":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Leaflynx.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Leaflynx.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Magmawisp":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Magmawisp.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Magmawisp.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Thundragon":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Thundragon.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Thundragon.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Frostbite":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Frostbite.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Frostbite.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Rockscale":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Rockscale.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Rockscale.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Volcanix":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Volcanix.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Volcanix.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Aquaflare":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Aquaflare.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Aquaflare.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Zephyria":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Zephyria.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Zephyria.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Leafstorm":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Leafstorm.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Leafstorm.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Thunderclaw":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Thunderclaw.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Thunderclaw.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Endorphine":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Endorphine.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Endorphine.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Frocity":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Frocity.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Frocity.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

        elif name == "Georift":

            if flipped == True:
                self.displayPakuriImagePath = "pictures/Georift.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.mirrored_image = pygame.transform.flip(self.scaledDisplayPakuriImage, True, False)
                self.screen.blit(self.mirrored_image, (startX, startY))
            else:
                self.displayPakuriImagePath = "pictures/Georift.PNG"
                self.displayPakuriImage = pygame.image.load(self.displayPakuriImagePath)
                self.scaledDisplayPakuriImage = pygame.transform.scale(self.displayPakuriImage, (dimension, dimension))
                self.screen.blit(self.scaledDisplayPakuriImage, (startX, startY))

    #Character Selection Pakuri Information
    def pakuriImage(self, name):

        self.maxHealth = 150
        self.maxSpeed = 100
        self.maxAttack = 100
        self.maxDefense = 100

        self.pakuriDisplayName = name
        self.displayHealth = None
        self.displaySpeed = None
        self.displayAttack = None
        self.displayDefense = None
        self.displayMoveset = None

        self.displayPakuriImagePath = None
        self.displayPakuriImage = None
        self.scaledDisplayPakuriImage = None
        self.displayType = None


        for i in range(len(Pakudex().pakudex)):
            if Pakudex().pakudex[i].get_species() == self.pakuriDisplayName:
                self.displayType = Pakudex().pakudex[i].get_type()
                self.displayHealth = Pakudex().pakudex[i].get_health()
                self.displaySpeed = Pakudex().pakudex[i].get_speed()
                self.displayAttack = Pakudex().pakudex[i].get_attack()
                self.displayDefense = Pakudex().pakudex[i].get_defense()
                self.displayMoveset = Pakudex().pakudex[i].get_moveset()

                self.healthRatio = self.displayHealth/self.maxHealth
                self.speedRatio = self.displaySpeed / self.maxSpeed
                self.attackRatio = self.displayAttack / self.maxAttack
                self.defenseRatio = self.displayDefense / self.maxDefense

                break

        self.displayStats()
        self.getImage(self.pakuriDisplayName, 300, 500, 200)
        
    def displayStats(self):

        self.nameText = self.informationFont.render(self.pakuriDisplayName, False, (255, 255, 255))
        self.nameTextRect = self.nameText.get_rect()
        self.nameTextRect.center = (650, 150)

        self.displayCover = "pictures/black.PNG"
        self.displayCoverImage = pygame.image.load(self.displayCover)
        self.scaledDisplayCoverImage = pygame.transform.scale(self.displayCoverImage, (500, 560))  # 500, 560
        self.screen.blit(self.scaledDisplayCoverImage, (400, 130))
        self.screen.blit(self.nameText, self.nameTextRect)

        pygame.draw.rect(self.screen, self.GREY, (400, 130, 500, 45), 5)
        pygame.draw.rect(self.screen, self.GREY, (400, 175, 500, 330), 5)
        pygame.draw.rect(self.screen, self.GREY, (400, 175+330, 500, 185), 5)

        for i in range(len(self.displayType)):
            if(len(self.displayType) == 1):
                self.text = self.informationFont.render(self.displayType[i], False, (255, 255, 255))
                self.textRect = self.text.get_rect()
                self.textRect.center = (650 + (50 * i), 520)
            else:
                self.text = self.informationFont.render(self.displayType[i], False, (255, 255, 255))
                self.textRect = self.text.get_rect()
                self.textRect.center = (630 + (70 * i), 520)

            self.screen.blit(self.text, self.textRect)

        self.healthText = self.informationFont.render("Health: " + str(self.displayHealth), False, (255, 255, 255))
        self.healthTextRect = self.text.get_rect()
        self.healthTextRect.center = (500, 540)
        pygame.draw.rect(self.screen, (255, 255, 255), (580, 535, 300 * self.healthRatio, 10))

        self.speedText = self.informationFont.render("Speed: " + str(self.displaySpeed), False, (255, 255, 255))
        self.speedTextRect = self.text.get_rect()
        self.speedTextRect.center = (500, 560)
        pygame.draw.rect(self.screen, (255, 255, 255), (580, 555, 300 * self.speedRatio, 10))

        self.attackText = self.informationFont.render("Attack: " + str(self.displayAttack), False, (255, 255, 255))
        self.attackTextRect = self.text.get_rect()
        self.attackTextRect.center = (500, 580)
        pygame.draw.rect(self.screen, (255, 255, 255), (580, 575, 300 * self.attackRatio, 10))

        self.defenseText = self.informationFont.render("Defense: " + str(self.displayDefense), False, (255, 255, 255))
        self.defenseTextRect = self.text.get_rect()
        self.defenseTextRect.center = (500, 600)
        pygame.draw.rect(self.screen, (255, 255, 255), (580, 595, 300 * self.defenseRatio, 10))

        self.movesetText = self.informationFont.render("Moveset", False, (255, 255, 255))
        self.movesetTextRect = self.movesetText.get_rect()
        self.movesetTextRect.center = (650, 625)

        (self.screen.blit(self.healthText, self.healthTextRect),
         self.screen.blit(self.speedText, self.speedTextRect),
         self.screen.blit(self.attackText, self.attackTextRect),
         self.screen.blit(self.defenseText, self.defenseTextRect),
         self.screen.blit(self.movesetText, self.movesetTextRect))

        for i in range(4):
            self.moveText = self.informationFont.render(self.displayMoveset[i], False, (255, 255, 255))
            self.moveTextRect = self.moveText.get_rect()
            self.moveTextRect.center = (480 + 100*i, 660)
            self.screen.blit(self.moveText, self.moveTextRect)

    def updatePakuriCounter(self, counter):

        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(str(counter) + " Pakuri left to choose", False, self.BLACK, self.GREY)
        self.textRect = self.text.get_rect()
        self.textRect.center = (280, 300)
        self.screen.blit(self.text, self.textRect)

    def confirmationScreen(self, playerOneTeam, playerTwoTeam):

        self.playerOneTeam = playerOneTeam
        self.playerTwoTeam = playerTwoTeam

        self.displayCover = "pictures/download.png"
        self.displayCoverImage = pygame.image.load(self.displayCover)
        self.scaledDisplayCoverImage = pygame.transform.scale(self.displayCoverImage, (250, 560))  # 500, 560

        self.text = self.titleFont.render('PLAYER TEAMS', False, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (900 // 2, 100)
        # image and scaling apprpriate to window size
        self.image_path = "pictures/pokemon player teams.png"
        self.image = pygame.image.load(self.image_path)
        self.scaled_image = pygame.transform.scale(self.image, (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.screen.blit(self.scaled_image, (0, 0)), self.screen.blit(self.text, self.textRect)

        #player One:
        self.teamText = self.informationFont.render('Player One Team', False, (255, 255, 255))
        self.teamRect = self.teamText.get_rect()
        self.teamRect.center = (225, 155)

        self.screen.blit(self.scaledDisplayCoverImage, (100, 135))
        self.screen.blit(self.teamText, self.teamRect)

        pygame.draw.rect(self.screen, self.RED, (100, 135, 250, 45), 5)
        pygame.draw.rect(self.screen, self.RED, (100, 180, 250, 330+185), 5)

        for i in range(len(playerOneTeam)):
            if playerOneTeam[i].get_species() != "Player One":
                self.teamText = self.informationFont.render(playerOneTeam[i].get_species(), False, self.BLACK)
                self.teamRect = self.teamText.get_rect()
                self.teamRect.center = (225, 205 + 95*i)
                self.getImage(playerOneTeam[i].get_species(), 80, 180, (215 + 95*i))
                self.screen.blit(self.teamText, self.teamRect)

        #player Two:
        self.teamText = self.informationFont.render('Player Two Team', False, (255, 255, 255))
        self.teamRect = self.teamText.get_rect()
        self.teamRect.center = (550+125, 155)

        self.screen.blit(self.scaledDisplayCoverImage, (550, 135))
        self.screen.blit(self.teamText, self.teamRect)

        pygame.draw.rect(self.screen, self.BLUE, (550, 135, 250, 45), 5)
        pygame.draw.rect(self.screen, self.BLUE, (550, 180, 250, 330 + 185), 5)

        for i in range(len(playerOneTeam)):
            if playerTwoTeam[i].get_species() != "Player Two":
                self.teamText = self.informationFont.render(playerTwoTeam[i].get_species(), False, self.BLACK)
                self.teamRect = self.teamText.get_rect()
                self.teamRect.center = (550+125, 205 + 95*i)
                self.getImage(playerTwoTeam[i].get_species(), 80, (510+125), (215 + 95*i))
                self.screen.blit(self.teamText, self.teamRect)


        self.confirmButton = button(400, 700, 100, 50, "Confirm", (255, 255, 255))
        self.p1ReselectButton = button(150, 700, 150, 50, "P1 Reselect Pakuri", (255, 255, 255))
        self.p2ReselectButton = button(600, 700, 150, 50, "P2 Reselect Pakuri", (255, 255, 255))

        self.confirmButton.draw(self.screen, self.buttonFont)
        self.p1ReselectButton.draw(self.screen, self.buttonFont)
        self.p2ReselectButton.draw(self.screen, self.buttonFont)

    def battleScreen(self):

        self.p1PakuriDisplayed = self.playerOneTeam[0]
        self.p2PakuriDisplayed = self.playerTwoTeam[0]

        self.screen.fill(self.BLACK)
        self.backgroundNum = random.randint(1,100)

        if self.backgroundNum <= 33:
            self.battleBackground_path = "pictures/Battle_Background_One.png"
            self.battleBackground = pygame.image.load(self.battleBackground_path)
            self.scaledBattleBackground = pygame.transform.scale(self.battleBackground,
                                                                 (self.WINDOW_WIDTH, self.WINDOW_HEIGHT-300))
            self.screen.blit(self.scaledBattleBackground, (0, 0))
        elif 33 < self.backgroundNum and self.backgroundNum <= 66:
            self.battleBackground_path = "pictures/Battle_Background_Two.png"
            self.battleBackground = pygame.image.load(self.battleBackground_path)
            self.scaledBattleBackground = pygame.transform.scale(self.battleBackground,
                                                                 (self.WINDOW_WIDTH, self.WINDOW_HEIGHT - 300))
            self.screen.blit(self.scaledBattleBackground, (0, 0))
        else:
            self.battleBackground_path = "pictures/Battle_Backgroud_Three.png"
            self.battleBackground = pygame.image.load(self.battleBackground_path)
            self.scaledBattleBackground = pygame.transform.scale(self.battleBackground,
                                                                 (self.WINDOW_WIDTH, self.WINDOW_HEIGHT - 300))
            self.screen.blit(self.scaledBattleBackground, (0, 0))

        #user interface
        pygame.draw.rect(self.screen, self.GREY, (0, 600, 900, 300))
        pygame.draw.rect(self.screen, self.BROWN, (0, 600, 900, 300), 9)

        #Dialogue Box
        pygame.draw.rect(self.screen, self.WHITE, (40, 650, 550, 200))
        pygame.draw.rect(self.screen, self.BLACK, (40, 650, 550, 200), 9)

        self.text = self.playerOptionsFont.render("PLAYER ONE'S TURN", False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (215, 700)
        self.screen.blit(self.text, self.textRect)

        self.text = self.playerOptionsFont.render("What will " + self.playerOneTeam[0].get_species() + " do?", False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (230, 750)
        self.screen.blit(self.text, self.textRect)

        self.displayPakuri()

        self.fightButton.draw(self.screen, self.playerOptionsFont)
        self.pakuriButton.draw(self.screen, self.playerOptionsFont)
        self.forfeitButton.draw(self.screen, self.playerOptionsFont)
        self.exitButton.draw(self.screen, self.playerOptionsFont)

        self.getImage(self.playerTwoTeam[0].get_species(), 190, 550, 180)

    def displayPakuri(self):

        self.battleBackground = pygame.image.load(self.battleBackground_path)
        self.scaledBattleBackground = pygame.transform.scale(self.battleBackground,
                                                             (self.WINDOW_WIDTH, self.WINDOW_HEIGHT - 300))
        self.screen.blit(self.scaledBattleBackground, (0, 0))

        # player 1 pakuri details
        self.p1HealthRatio = self.p1PakuriDisplayed.get_currentHealth() / self.p1PakuriDisplayed.get_health()

        pygame.draw.rect(self.screen, self.WHITE, (470, 400, 400, 150))
        pygame.draw.rect(self.screen, self.BLACK, (470, 400, 400, 150), 5)

        self.text = self.playerOptionsFont.render("P1: " + self.p1PakuriDisplayed.get_species(), False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (670, 420)
        self.screen.blit(self.text, self.textRect)

        self.text = self.playerOptionsFont.render("HP: ", False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (510, 455)
        self.screen.blit(self.text, self.textRect)

        pygame.draw.rect(self.screen, self.RED, (540, 435, 300, 40))
        pygame.draw.rect(self.screen, self.GREEN, (540, 435, (300 * self.p1HealthRatio), 40))

        self.text = self.playerOptionsFont.render(
            (str(self.p1PakuriDisplayed.get_currentHealth()) + "/" + str(self.p1PakuriDisplayed.get_health())),
            False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (800, 495)
        self.screen.blit(self.text, self.textRect)
        self.getImage(self.p1PakuriDisplayed.get_species(), 190, 200, 350, True)



        # player 2 pakuri details
        self.p2HealthRatio = self.p2PakuriDisplayed.get_currentHealth() / self.p2PakuriDisplayed.get_health()

        pygame.draw.rect(self.screen, self.WHITE, (30, 40, 400, 150))
        pygame.draw.rect(self.screen, self.BLACK, (30, 40, 400, 150), 5)

        self.text = self.playerOptionsFont.render("P2: " + self.p2PakuriDisplayed.get_species(), False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (215, 60)
        self.screen.blit(self.text, self.textRect)

        self.text = self.playerOptionsFont.render("HP: ", False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (70, 95)
        self.screen.blit(self.text, self.textRect)

        pygame.draw.rect(self.screen, self.RED, (100, 75, 300, 40))
        pygame.draw.rect(self.screen, self.GREEN, (100, 75, (300 * self.p2HealthRatio), 40))

        self.text = self.playerOptionsFont.render(
            (str(self.p2PakuriDisplayed.get_currentHealth()) + "/" + str(self.p2PakuriDisplayed.get_health())),
            False, self.BLACK)
        self.textRect = self.text.get_rect()
        self.textRect.center = (360, 140)
        self.screen.blit(self.text, self.textRect)
        self.getImage(self.p2PakuriDisplayed.get_species(), 190, 550, 180)

    def selectedButton(self, button, font = None):
        if font == None:
            font = self.playerOptionsFont
        button.specialDraw(self.screen, font)

    def unselectButton(self, button, font = None):
        if font == None:
            font = self.playerOptionsFont
        button.draw(self.screen, font)

    def updateDialogue(self, player=1, isAlive = None):

        pygame.draw.rect(self.screen, self.WHITE, (40, 650, 550, 200))
        pygame.draw.rect(self.screen, self.BLACK, (40, 650, 550, 200), 9)

        if player %2 != 0:

            self.text = self.playerOptionsFont.render("PLAYER ONE'S TURN", False, self.BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (215, 700)
            #self.animate.print(self.screen, ('PLAYER ONE TURN'), self.playerOptionsFont, self.textRect)
            self.screen.blit(self.text, self.textRect)

            self.text = self.playerOptionsFont.render("What will " + self.p1PakuriDisplayed.get_species() + " do?", False,
                                                      self.BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (230, 750)
            self.screen.blit(self.text, self.textRect)
        else:
            self.text = self.playerOptionsFont.render("PLAYER TWO TURN", False, self.BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (215, 700)
            self.screen.blit(self.text, self.textRect)

            self.text = self.playerOptionsFont.render("What will " + self.p2PakuriDisplayed.get_species() + " do?",
                                                      False,
                                                      self.BLACK)
            self.textRect = self.text.get_rect()
            self.textRect.center = (230, 750)
            self.screen.blit(self.text, self.textRect)

    def getUpdatedDialogue(self, player, state):
        self.textRectDialogue = self.text.get_rect(topleft=(75, 700))
        if state == "Move is Ineffective...":
            return ([state,
                     ""], self.textRectDialogue, self.dialogueFont)
        elif state == "Not Very Effective...":
            return ([state,
                     ""], self.textRectDialogue, self.dialogueFont)
        elif state == "Super Effective!":
            return ([state,
                     ""], self.textRectDialogue, self.dialogueFont)
        elif state == "Player 1":
            return ([state + " has Won!",
                     ""], self.textRectDialogue, self.dialogueFont)
        elif state == "Player 2":
            return ([state + " has Won!",
                     ""], self.textRectDialogue, self.dialogueFont)
        elif state == "Forfeit":
                return (["Player 1" + " has Won!",""], self.textRectDialogue, self.dialogueFont) if player%2 == 0 \
                    else (["Player 2" + " has Won!", ""], self.textRectDialogue, self.dialogueFont)


        if player % 2 != 0:
            if state == "BACK" or state == "BATTLE":
                return (["Player One, What will " + self.p1PakuriDisplayed.get_species() + " do?",
                         ""], self.textRectDialogue, self.dialogueFont)
            elif state == "CONFIRM":
                return (["Player One's Pakuri " + self.p1PakuriDisplayed.get_species() + " used " + self.moveChosen,
                         ""], self.textRectDialogue, self.dialogueFont)
            elif state == "DEAD":
                return (["Player One's Pakuri " + self.p1FaintedPakuri.get_species() + " has fainted",
                         ""], self.textRectDialogue, self.dialogueFont)
        else:
            if state == "BACK" or state == "BATTLE":
                return (["Player Two, What will " + self.p2PakuriDisplayed.get_species() + " do?",
                        ""], self.textRectDialogue, self.dialogueFont)

            elif state == "CONFIRM":
                return (["Player Two's Pakuri " + self.p2PakuriDisplayed.get_species() + " used " + self.moveChosen,
                         ""], self.textRectDialogue, self.dialogueFont)
            elif state == "DEAD":
                return (["Player Two's Pakuri " + self.p2FaintedPakuri.get_species() + " has fainted",
                         ""], self.textRectDialogue, self.dialogueFont)

    def getDisplayedPakuri(self):
        return self.p1PakuriDisplayed, self.p2PakuriDisplayed

    def aquireMoveName(self, name):
        self.moveChosen = name

    def isDisplayPakuriAlive(self):
        return self.p1PakuriDisplayed.is_alive(), self.p2PakuriDisplayed.is_alive()

    def getPakuriDisplayedTeam(self, player):
        self.displayedParty = []
        self.increment = 1
        for self.i in range(len(self.playerOneTeam) - 1):
            if player % 2 != 0:
                if self.p1PakuriDisplayed.get_species() != self.playerOneTeam[self.i].get_species() and self.p1PakuriDisplayed.get_species() != "Player Two":
                    if self.playerOneTeam[self.i].get_currentHealth() != 0:
                        self.displayedParty.append(button(100, (620 + (45 * self.increment)), 120, 40, self.playerOneTeam[self.i].get_species(),
                                   self.WHITE))
                        self.getImage(self.playerOneTeam[self.i].get_species(), 50, 50, 620 + 40 * self.increment)
                        self.increment = (self.increment + 1)
            else:
                if self.p2PakuriDisplayed.get_species() != self.playerTwoTeam[self.i].get_species() and self.p1PakuriDisplayed.get_species() != "Player One":
                    if self.playerTwoTeam[self.i].get_currentHealth() != 0:
                        self.displayedParty.append(button(100, (620 + (45 * self.increment)), 120, 40,
                                                              self.playerTwoTeam[self.i].get_species(),
                                                              self.WHITE))
                        self.getImage(self.playerTwoTeam[self.i].get_species(), 50, 50, 620 + 40 * self.increment)
                        self.increment += 1
        self.i = 0
        for k in range(len(self.displayedParty)):
            for l in range(len(self.playerOneTeam)):
                if player % 2 != 0:
                    if (self.playerOneTeam[l].get_species() != "Player One"):
                        if(self.displayedParty[k].buttonName() == self.playerOneTeam[l].get_species()):
                            if(self.playerOneTeam[l].is_alive):
                                self.displayedParty[k].draw(self.screen, self.buttonFont, self.BLACK)
                            else:
                                self.displayedParty[k].draw(self.screen, self.buttonFont, self.RED)
                else:
                    if((self.playerTwoTeam[l].get_species() != "Player Two")):
                        if(self.displayedParty[k].buttonName() == self.playerTwoTeam[l].get_species()):
                            if(self.playerTwoTeam[l].is_alive):
                                self.displayedParty[k].draw(self.screen, self.buttonFont, self.BLACK)
                            else:
                                self.displayedParty[k].draw(self.screen, self.buttonFont, self.RED)
        return self.displayedParty

    def updateBattleScreen(self, buttonName, player = 1, pakuriSwitch = None):

        pygame.draw.rect(self.screen, self.GREY, (0, 600, 900, 300))
        pygame.draw.rect(self.screen, self.BROWN, (0, 600, 900, 300), 9)

        pygame.draw.rect(self.screen, self.WHITE, (40, 650, 550, 200))
        pygame.draw.rect(self.screen, self.BLACK, (40, 650, 550, 200), 9)

        if buttonName == "FIGHT":

            self.confirmOptionButton.draw(self.screen, self.playerOptionsFont)
            self.backButton.draw(self.screen, self.playerOptionsFont)
            pygame.draw.rect(self.screen, self.WHITE, (40, 650, 550, 200))
            pygame.draw.rect(self.screen, self.BLACK, (40, 650, 550, 200), 9)
            for i in range(4):
                if player % 2 != 0:
                    self.pakuriMoves = self.p1PakuriDisplayed.get_moveset()
                    self.displayedPakuriMoves[i] = button(100, (660 + (45 * i)), 120, 45, self.pakuriMoves[i], (255, 255, 255))
                    self.displayedPakuriMoves[i].draw(self.screen, self.playerOptionsFont)
                else:
                    self.pakuriMoves = self.p2PakuriDisplayed.get_moveset()
                    self.displayedPakuriMoves[i] = (button(100, (660 + (45 * i)), 120, 45, self.pakuriMoves[i], (255, 255, 255)))
                    self.displayedPakuriMoves[i].draw(self.screen, self.playerOptionsFont)

        elif buttonName == "PAKURI":

            self.switchButton.draw(self.screen, self.playerOptionsFont)
            self.backButton.draw(self.screen, self.playerOptionsFont)

            pygame.draw.rect(self.screen, self.WHITE, (40, 650, 550, 200))
            pygame.draw.rect(self.screen, self.BLACK, (40, 650, 550, 200), 9)

            self.pakuriParty = self.getPakuriDisplayedTeam(player)


        elif buttonName == "FORFEIT":
            self.sureButton.draw(self.screen, self.playerOptionsFont)
            self.backButton.draw(self.screen, self.playerOptionsFont)

        elif buttonName == "EXIT":
            self.sureButton.draw(self.screen, self.playerOptionsFont)
            self.backButton.draw(self.screen, self.playerOptionsFont)

        elif buttonName == "BACK":
            self.fightButton.draw(self.screen, self.playerOptionsFont)
            self.pakuriButton.draw(self.screen, self.playerOptionsFont)
            self.forfeitButton.draw(self.screen, self.playerOptionsFont)
            self.exitButton.draw(self.screen, self.playerOptionsFont)

            #self.updateDialogue(player)

        elif buttonName == "CONFIRM":
            self.isP1TeamAlive = False
            self.isP2TeamAlive = False
            self.speech = "I entered Confirm in update Battle Screen"
            #self.battle.moveSelected(str(self.moveChosen), player, self.p1PakuriDisplayed, self.p2PakuriDisplayed)
            self.displayPakuri()
            self.updateDialogue(player)

            self.fightButton.draw(self.screen, self.playerOptionsFont)
            self.pakuriButton.draw(self.screen, self.playerOptionsFont)
            self.forfeitButton.draw(self.screen, self.playerOptionsFont)
            self.exitButton.draw(self.screen, self.playerOptionsFont)

            if self.p1PakuriDisplayed.is_alive() is not True:
                self.speech = "I entered p1 pakuri died"
                self.p1FaintedPakuri = self.p1PakuriDisplayed
                for i in range(len(self.playerOneTeam)):
                    if self.playerOneTeam[i].is_alive() and (self.playerOneTeam[i].get_species() != "Player One"):
                        self.p1PakuriDisplayed = self.playerOneTeam[i]
                        self.speech = "I entered p1 pakuri died, new p1 pakuri is: " + self.p1PakuriDisplayed.get_species()
                        self.isP1TeamAlive = True

                if self.isP1TeamAlive != True: self.whoWon = "Player 2"
                self.displayPakuri()

            elif self.p2PakuriDisplayed.is_alive() is not True:
                self.p2FaintedPakuri = self.p2PakuriDisplayed
                for i in range(len(self.playerTwoTeam)):
                    self.speech = "I entered p1 pakuri died"
                    if self.playerTwoTeam[i].is_alive() and (self.playerTwoTeam[i].get_species() != "Player Two"):
                        self.p2PakuriDisplayed = self.playerTwoTeam[i]
                        self.speech = "I entered p2 pakuri died, new p2 pakuri is: " + self.p2PakuriDisplayed.get_species()
                        self.isP2TeamAlive = True

                if self.isP2TeamAlive != True: self.whoWon = "Player 1"
                self.displayPakuri()

        elif buttonName == "SWITCH":
            if player % 2 != 0:
                for i in range(len(self.playerOneTeam)):
                    if pakuriSwitch == self.playerOneTeam[i].get_species():
                        if(self.playerOneTeam[i].is_alive() is True):
                            self.p1PakuriDisplayed = self.playerOneTeam[i]
                            break
            else:
                for i in range(len(self.playerTwoTeam)):
                    if pakuriSwitch == self.playerTwoTeam[i].get_species():
                        if (self.playerTwoTeam[i].is_alive() is True):
                            self.p2PakuriDisplayed = self.playerTwoTeam[i]
                            break

            self.displayPakuri()


        elif buttonName == "SURE?":
            if pakuriSwitch == "FORFEIT":
                self.whoWon = "Player 1" if player%2 == 0 else "Player 2"

        elif buttonName == "BATTLE":
            if player %2 != 0:
                self.text = self.playerOptionsFont.render("PLAYER ONE'S TURN", False, self.BLACK)
                self.textRect = self.text.get_rect()
                self.textRect.center = (215, 700)
                self.screen.blit(self.text, self.textRect)

                self.text = self.playerOptionsFont.render("What will " + self.p1PakuriDisplayed.get_species() + " do?",
                                                          False, self.BLACK)
                self.textRect = self.text.get_rect()
                self.textRect.center = (230, 750)
                self.screen.blit(self.text, self.textRect)
            else:
                self.text = self.playerOptionsFont.render("PLAYER TWO'S TURN", False, self.BLACK)
                self.textRect = self.text.get_rect()
                self.textRect.center = (215, 700)
                self.screen.blit(self.text, self.textRect)

                self.text = self.playerOptionsFont.render("What will " + self.p2PakuriDisplayed.get_species() + " do?",
                                                          False, self.BLACK)
                self.textRect = self.text.get_rect()
                self.textRect.center = (230, 750)
                self.screen.blit(self.text, self.textRect)

            self.fightButton.draw(self.screen, self.playerOptionsFont)
            self.pakuriButton.draw(self.screen, self.playerOptionsFont)
            self.forfeitButton.draw(self.screen, self.playerOptionsFont)
            self.exitButton.draw(self.screen, self.playerOptionsFont)

    def whoWins(self):
        return self.whoWon

    def speechPrint(self):
        return self.speech