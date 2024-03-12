import pygame, sys
from button import Button

import mediapipe as mp
import cv2

pygame.init()
pygame.mixer.init()

#WIDTH = 890
#HEIGHT = 750
#size = (WIDTH,HEIGHT)
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
FPS = 60
SCREEN = pygame.display.set_mode((1280, 720))

BG = pygame.image.load("C:/Users/Asus/Desktop/10° semestre FIUADY/VCPy/menutest/assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("C:/Users/Asus/Desktop/10° semestre FIUADY/VCPy/menutest/assets/font.ttf", size)

#game 
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
#game tutorial    
def options(): # I think you can erase this funtion 
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#menu
def main_menu():
    pygame.display.set_caption("Menu")

    SCREEN.blit(BG, (0, 0))

    #MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
    #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    # inicializamos la clase Hands y almacenarla en una variable
    handsMp = mp.solutions.hands
    # cargamos componente con las herramientas que nos permitira dibujar mas adelante
    drawingMp = mp.solutions.drawing_utils
    # cargamos los estilos en la variable mp_drawing_styles
    mp_drawing_styles = mp.solutions.drawing_styles
    # iniciamos una captura de video en la camara 1
    cap = cv2.VideoCapture(0)
    hands= handsMp.Hands(static_image_mode=False,
                         max_num_hands=2,
                         min_detection_confidence=0.5,
                         min_tracking_confidence=0.5)
    with hands:
        while cap.isOpened():
            success, image = cap.read()
            #print("camara prendida")

        while True:
            SCREEN.blit(BG, (0, 0))
            print("menu")
            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            success, image = cap.read()
            #height, width, _ = image.shape
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_hand_landmarks is not None:
                for hand_landmarks in results.multi_hand_landmarks:
                    drawingMp.draw_landmarks(image,
                                             hand_landmarks,
                                             handsMp.HAND_CONNECTIONS,
                                             mp_drawing_styles.get_default_hand_landmarks_style(),
                                             mp_drawing_styles.get_default_hand_connections_style())

            #MENU_MOUSE_POS = pygame.mouse.get_pos()
                    #SCREEN.blit(BG, (0, 0))
                    #MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
                    #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

                    PLAY_BUTTON = Button(image=pygame.image.load("C:/Users/Asus/Desktop/10° semestre FIUADY/VCPy/menutest/assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                    OPTIONS_BUTTON = Button(image=pygame.image.load("C:/Users/Asus/Desktop/10° semestre FIUADY/VCPy/menutest/assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                    QUIT_BUTTON = Button(image=pygame.image.load("C:/Users/Asus/Desktop/10° semestre FIUADY/VCPy/menutest/assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

                    SCREEN.blit(MENU_TEXT, MENU_RECT)

                    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                        #button.changeColor(MENU_MOUSE_POS)
                        button.update(SCREEN)
        
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y):
                                #play()
                                print("1")
                            if (hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y):
                                #options()
                                print("2")
                            if (hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y):
                                pygame.quit()
                                sys.exit()

                    pygame.display.update()

main_menu()