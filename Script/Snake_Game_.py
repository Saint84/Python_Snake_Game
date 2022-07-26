import pygame
import random


class SnakeGame:
    pygame.init()
    pygame.mixer.init()

    def __init__(self):
        self.Display_Size = (800, 600)
        self.Display_Title = "Snake Game Version 1.0"
        self.Colors = {"White": (255, 255, 255),
                       "Red": (215, 50, 80),
                       "Green": (0, 255, 0),
                       "Blue": (50, 155, 215),
                       "Black": (0, 0, 0)}

        self.Background_path = "../Source/Background_A.png"
        self.Sound_path = "../Source/Title.mp3"

        self.Display = pygame.display.set_mode(self.Display_Size)
        self.Background = pygame.image.load(self.Background_path)
        self.Background_Scale = pygame.transform.scale(self.Background, self.Display_Size)

        self.Text_Font_Style = pygame.font.SysFont("bahnschrift", 25)
        self.Score_Font_Style = pygame.font.SysFont("comicsansms", 25)

        self.Clock_Time = pygame.time.Clock()

        self.Snake_Position_x = self.Display_Size[0] / 2
        self.Snake_Position_y = self.Display_Size[0] / 2

        self.Snake_Move_x = 0
        self.Snake_Move_y = 0

        self.Snake_Size_x = 10
        self.Snake_Size_y = 10

        self.Food_Position_x = 0
        self.Food_Position_y = 0

        self.Food_Position_x = round(random.randint(2, (800 - 15)) / 10) * 10
        self.Food_Position_y = round(random.randint(2, (600 - 15)) / 10) * 10

        self.Food_Size_x = 10
        self.Food_Size_x = 10

        self.Snake_Length = 1
        self.Snake_list = []

        self.Score = 0
        self.Game_Speed = 15
        self.Game_Status = False
        return

    def music(self):
        pygame.mixer.music.load(self.Sound_path)
        pygame.mixer.music.play()
        return

    def screen(self):
        self.Display.blit(self.Background_Scale, (0, 0))
        pygame.display.set_caption(self.Display_Title)
        return

    def snake_pixels(self):
        snake_head = []
        snake_head.append(self.Snake_Position_x)
        snake_head.append(self.Snake_Position_y)
        self.Snake_list.append(snake_head)

        for p in self.Snake_list:
            pygame.draw.rect(self.Display, self.Colors["Blue"],
                             [p[0], p[1], self.Snake_Size_x, self.Snake_Size_y])

        pygame.draw.rect(self.Display, self.Colors["Red"],
                         [self.Food_Position_x, self.Food_Position_y, self.Food_Size_x, self.Food_Size_x])

        if len(self.Snake_list) > self.Snake_Length:
            del self.Snake_list[0]

        pygame.display.update()
        return

    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                self.Game_Status = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.Snake_Move_x = -10
                    self.Snake_Move_y = 0
                elif event.key == pygame.K_RIGHT:
                    self.Snake_Move_x = +10
                    self.Snake_Move_y = 0
                elif event.key == pygame.K_UP:
                    self.Snake_Move_x = 0
                    self.Snake_Move_y = -10
                elif event.key == pygame.K_DOWN:
                    self.Snake_Move_x = 0
                    self.Snake_Move_y = +10

        self.Snake_Position_x += self.Snake_Move_x
        self.Snake_Position_y += self.Snake_Move_y
        pygame.display.update()
        return

    def score_msg(self):
        sc = self.Score_Font_Style.render(f"Score: {self.Score}", True, self.Colors["White"])
        self.Display.blit(sc, [0, 0])
        return

    def continue_msg(self):
        cg = self.Text_Font_Style.render(f"Continue? (Y/N)", True, self.Colors["White"])
        self.Display.blit(cg, [335, 300])
        return

    def game_conditions(self):
        if self.Snake_Position_x >= 800 or self.Snake_Position_x <= 0 or \
                self.Snake_Position_y >= 600 or self.Snake_Position_y <= 0:
            self.Game_Status = True

            while self.Game_Status:
                self.continue_msg()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.WINDOWCLOSE:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            pygame.quit()
                            quit()
                        elif event.key == pygame.K_y:
                            SnakeGame().update()
        return

    def snake_points(self):
        if (self.Snake_Position_x == self.Food_Position_x) and (self.Snake_Position_y == self.Food_Position_y):
            self.Food_Position_x = round(random.randint(2, (800 - 15)) / 10) * 10
            self.Food_Position_y = round(random.randint(2, (600 - 15)) / 10) * 10
            self.Score += 1
            self.Game_Speed += 1
            self.Snake_Length += 1
        return

    def update(self):
        self.music()

        while not self.Game_Status:
            self.score_msg()
            self.control()
            self.snake_pixels()
            self.screen()
            self.snake_points()
            self.game_conditions()
            self.Clock_Time.tick(self.Game_Speed)
        return


if __name__ == '__main__':
    SnakeGame().update()
