import pygame
import mediapipe as mp
import cv2
pygame.init()
pygame.mixer.init()

WIDTH = 890
HEIGHT = 750
size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)

RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

score = 0
balls = 1
velocity = 4

paddle_width = 84
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#game variables 
game_pause = False

#define fouts 
fout = pygame.font.SysFont("arialblack",40)

#define color 
TEXT_COL = (255,255,255)




def main(score, ball):
    # inicializamos la clase Hands y almacenarla en una variable
    handsMp = mp.solutions.hands
    # cargamos componente con las herramientas que nos permitira dibujar mas adelante
    drawingMp = mp.solutions.drawing_utils
    # cargamos los estilos en la variable mp_drawing_styles
    mp_drawing_styles = mp.solutions.drawing_styles
    # iniciamos una captura de video en la camara 1
    cap = cv2.VideoCapture(0)

    hands = handsMp.Hands(static_image_mode=False, 
                      max_num_hands=2, 
                      min_detection_confidence=0.5, 
                      min_tracking_confidence=0.5)
    
    with hands: 
        while cap.isOpened():
            success, image = cap.read()
            step = 0
            run = True
            
            #game loop 
            while run:
                success, image = cap.read()
                height, width, _ = image.shape
                print("camara prendida sin manos")
                #draw_text("Press SPASE to pause", fout, TEXT_COL, 160, 250)

                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks is not None:
                    
                    draw_text("Press SPASE to pause", fout, TEXT_COL, 160, 250)
                    
                    print("Manos") #revisar

                    pass

                    # recorremos esos puntos multiples de referencia
                    for hand_landmarks in results.multi_hand_landmarks:
                        drawingMp.draw_landmarks(image,hand_landmarks,
                                                 handsMp.HAND_CONNECTIONS,
                                                 mp_drawing_styles.get_default_hand_landmarks_style(),
                                                 mp_drawing_styles.get_default_hand_connections_style())
                        
                        #event hander 
                        for event in pygame.event.get():
                            if event in pygame.event.get():
                                if (hand_landmarks.landmark[20].y < hand_landmarks.landmark[17].y):
                                #if event.key == pygame.K_SPACE:
                                #if event.type == pygame.QUIT:
                                    game_pause = True
                        if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y):
                            estado = "1"
                            game_pause = True
                            print(estado)
                        else:
                            run = False
                            estado = "0"
                            print(estado)
                        
                        pygame.display.update()

                        clock.tick(FPS)

            else:
                draw_text("Press SPASE to pause", fout, TEXT_COL, 160, 250)
                        




main(score, balls)