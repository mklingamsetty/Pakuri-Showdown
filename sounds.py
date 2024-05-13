import pygame
class Sounds:

    def stopMusic(self, sound):
        sound.stop()
    def welcomeScreenMusic(self):
        sound_file = "music/welcome_screen_music.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
        return sound

    def battleMusic(self):
        sound_file = "music/battle_music.mp3"
        sound = pygame.mixer.Sound(sound_file)
        sound.stop()

        sound.play()
        return sound
