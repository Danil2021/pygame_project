import pygame
import random

class MrSvin:
    def __init__(self, surf: pygame.surface.Surface):
        self.mr_svin_head_images = [
            pygame.image.load("recources/sprites/mr_svin/heads/head1.png"),
            pygame.image.load("recources/sprites/mr_svin/heads/head2.png"),
            pygame.image.load("recources/sprites/mr_svin/heads/head3.png"),
            pygame.image.load("recources/sprites/mr_svin/heads/head4.png")
        ]
        self.mr_svin_left_arm_images = [
            pygame.image.load("recources/sprites/mr_svin/arms/left_default.png")
        ]
        self.mr_svin_right_arm_images = [
            pygame.image.load("recources/sprites/mr_svin/arms/right_default.png"),
            pygame.image.load("recources/sprites/mr_svin/arms/right_get1.png"),
            pygame.image.load("recources/sprites/mr_svin/arms/right_get2.png"),
            pygame.image.load("recources/sprites/mr_svin/arms/right_get3.png"),
            pygame.image.load("recources/sprites/mr_svin/arms/right_get4.png"),
            pygame.image.load("recources/sprites/mr_svin/arms/right_get5.png")
        ]
        self.surf = surf
        self.emotion = None

    def angry(self):
        self.surf.blit(self.mr_svin_head_images[0], (280, 550))

    def default(self):
        self.surf.blit(self.mr_svin_head_images[1], (280, 550))

    def happy(self):
        self.surf.blit(self.mr_svin_head_images[2], (280, 515))

    def speak(self):
        self.surf.blit(self.mr_svin_head_images[3], (280, 515))

    def get_emotion(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.angry()
            self.emotion = self.angry()
        elif keys[pygame.K_2]:
            self.happy()
            self.emotion = self.happy()
        elif keys[pygame.K_3]:
            self.speak()
            self.emotion = self.speak()
        else:
            self.emotion = self.default()
        return self.emotion

    def default_speaking_animation(self, frame: int):
        anim_list = [False, True, True, True, True, False, False, True, True, False, True, True, True, True, False,
                     False, False, False, False, True, False, True, False, True, True, True, False, True, True, False,
                     False, True, True, True, False, False, False, True, True, True, False, True, False, False, False,
                     False, True, False, True, True, False, True, False, True, False, True, True, True, True, False]
        self.surf.blit(self.mr_svin_left_arm_images[0], (205, 660))
        self.surf.blit(self.mr_svin_right_arm_images[0], (600, 660))
        if anim_list[frame//5]:
            self.speak()
        else:
            self.default()

    def get_card(self, frame):
        self.angry()
        self.surf.blit(self.mr_svin_left_arm_images[0], (205, 660))
        if 0 < frame < 12:
            self.surf.blit(self.mr_svin_right_arm_images[1], (600, 660))
        elif 13 < frame < 24:
            self.surf.blit(self.mr_svin_right_arm_images[2], (600, 660))
        elif 26 < frame < 36:
            self.surf.blit(self.mr_svin_right_arm_images[3], (500, 660))
        elif 37 < frame < 48:
            self.surf.blit(self.mr_svin_right_arm_images[4], (450, 660))
        elif 49 < frame < 59:
            self.surf.blit(self.mr_svin_right_arm_images[5], (600, 660))




