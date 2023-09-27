# her importeres datetime funktionen fra datetime sammen med pygame og math
import pygame
import math
from datetime import datetime as dt

# her defineres vinduets bredde og højde
screen_width, screen_height = 1200, 800

# her startes pygame
pygame.init() 
# her sættes vinduets navn til 'Analog ur'
pygame.display.set_caption('Analog ur')
# her sættes vinduets dimensioner til 1200 x 800
screen = pygame.display.set_mode((screen_width, screen_height))
# her oprettes clock til senere brug
clock = pygame.time.Clock()

# her sørger jeg for at koden altid kører indtil vinduet lukkes
while True:
    # her henter pygame en liste med alle events
    for event in pygame.event.get():
        # her tjekker pygame om event typen er 'pygame.QUIT' og hvis den er, så lukker den python ned
        if event.type == pygame.QUIT:
            exit()

    # her fyldes skærmen med sort for ikke at gøre at folk får ondt i øjnene 
    # og for at de forældede visere ikke kan ses
    screen.fill((0, 0, 0))

    # her tegnes en cirkel som repræsenterer urskiven
    pygame.draw.circle(screen, (255, 255, 255), (0.5 * screen_width, 0.5 * screen_height), 300, 2)

    # her defineres centrum af skærmen ved at tage henholdsvis halvdelen af vinduets bredde og højde
    center_x, center_y = 0.5 * screen_width, 0.5 * screen_height

    # dette for-loop køres 12 gange for at lave de 12 time visere
    for i in range(12):
        # først defineres angle i radianer hvor i ganges med 30 da 12 * 30 giver 360
        angle = math.radians(i * 30)
        
        # her defineres startpunktet for x og y med en radius på 300 så det rammer urskiven
        # og cosinus og sinus bruges til at dreje startpunktet
        start_x = center_x + 299 * math.cos(angle)
        start_y = center_y + 299 * math.sin(angle)
        
        # her defineres slutpunktet for x og y med en radius på 270 for tydeligt at indikere de 12 timer
        # og cosinus og sinus bruges til at dreje slutpunktet
        end_x = center_x + 270 * math.cos(angle)
        end_y = center_y + 270 * math.sin(angle)
        
        # her tegnes linjen med start- og slutpunktet med hvid for at den kan ses på den sorte baggrund
        pygame.draw.line(screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 2)

    # Visere
    # først bruges datetime til at finde ud af hvilket sekund der er på computerens lokale tid
    second = dt.now().strftime("%S")
    # herefter sættes vinklen i radianer til at være sekunder gange med 6 - 90 da 60 * 6 er 360 
    # og der trækkes 90 fra for at den ikke er forskudt og at den ved minut-skiftet står lodret opad
    second_hand_angle = math.radians(int(second) * 6 - 90)
    # herefter defineres slutpunkterne for x og y ved at starte i centrum af vinduet 
    # og derefter lægge 299 som sammen med cosinus og sinus repræsenterer radius af viseren
    second_hand_end_x = center_x + 299 * math.cos(second_hand_angle)
    second_hand_end_y = center_y + 299 * math.sin(second_hand_angle)
    # til sidst tegnes linjen som repræsenterer sekundviseren
    pygame.draw.line(screen, (0, 255, 0), (center_x, center_y), (second_hand_end_x, second_hand_end_y), 2)

    # her findes minuttet for computeren først
    minute = dt.now().strftime("%M")
    # herefter defineres vinklen af minut viseren som er afhængig af det nuværende minut 
    # og sekund for at opdatere den hvert sekund i stedet for at den rykker sig en gang hvert minut
    minute_hand_angle = math.radians(90 - ((int(minute) * 6) + (int(second) * 0.1)))
    # her defineres slutpunkterne for x og y med radius på 250
    # Jeg ved ikke hvorfor det var nødvendigt at trække fra ved y punktet som det eneste
    minute_hand_end_x = center_x + 250 * math.cos(minute_hand_angle)
    minute_hand_end_y = center_y - 250 * math.sin(minute_hand_angle)
    # til sidste tegnes minutviseren
    pygame.draw.line(screen, (255, 255, 255), (center_x, center_y), (minute_hand_end_x, minute_hand_end_y), 2)

    # først defineres timen ved at tage computerens lokale time
    hour = dt.now().strftime("%H")
    # her defineres time viserens vinkel baseret på hvilken time og hvilket minut computeren 
    # har for løbende at opdatere den i stedet for at den hopper en gang i timen
    hour_hand_angle = math.radians((((int(hour) % 12) * 30) + (int(minute) * 0.5)) - 90)
    # her beregnes slutpunktet for timeviseren med cosinus og sinus 
    # baseret på centrum af vinduet og radius af viseren 
    hour_hand_end_x = center_x + 200 * math.cos(hour_hand_angle)
    hour_hand_end_y = center_y + 200 * math.sin(hour_hand_angle)
    # til sidst tegnes timeviseren fra centrum med en radius på 200
    pygame.draw.line(screen, (255, 255, 255), (center_x, center_y), (hour_hand_end_x, hour_hand_end_y), 3)

    # her opdateres vinduet så baggrunden bliver sort og det nye ur med det opdaterede visere ses i stedet
    pygame.display.flip()

    # her brgrænses koden til at køre 10 gange per sekund for at undgå at spilde resourcer 
    clock.tick(10)

# hvis while løkken skulle stoppe så vil pygame lukke ned
pygame.quit()
