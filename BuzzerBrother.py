from gpiozero import Button, LED
from time import sleep, time
import random

# GPIO-Pins definieren
button1 = Button(19, pull_up=False)  # Spieler 1 Taster
button2 = Button(6, pull_up=False)   # Spieler 2 Taster

led_player1 = LED(12)
led_player2 = LED(21)
led_reakt = LED(16)

# Spielparameter
rounds = 6  # Anzahl der Runden
player1_points = 0
player2_points = 0

def startup():
    print("Buzzer Brother")
    print("==============")
    print("\nWillkommen zu Buzzer Brother!")
    print("   ____                      ____  _               _             ")
    print("  | __ )  ___  _ __   __ _  | __ )| | __ _ _   _  | | ___   __ _ ")
    print("  |  _ \ / _ \| '_ \ / _` | |  _ \| |/ _` | | | | | |/ _ \ / _` |")
    print("  | |_) | (_) | | | | (_| | | |_) | | (_| | |_| | | | (_) | (_| |")
    print("  |____/ \___/|_| |_|\__, | |____/|_|\__,_|\__, | |_|\___/ \__, |")
    print("                     |___/                |___/            |___/ ")
    print("\nSpieler 1, bist du bereit? Druecke den Knopf!")
    button1.wait_for_press()
    print("Spieler 1 ist bereit!")
    sleep(1)
    print("\nSpieler 2, bist du bereit? Druecke den Knopf!")
    button2.wait_for_press()
    print("Spieler 2 ist bereit!")
    sleep(1)

def play_round():
    print(f"   >>> Spieler bereite euch vor...")

    sleep(random.randint(1,5))

    print("   >>> Druecke jetzt den Knopf!")
    led_reakt.on()

    gameOn = True

    player_1_pressed = False
    
    start_time = time()

    while(gameOn):
        if button1.is_pressed:
            gameOn = False
            led_reakt.off()
            led_player1.on()
            player_1_pressed = True


        elif button2.is_pressed:
            led_reakt.off()
            led_player2.on()
            gameOn = False

    reaction_time = time() - start_time

    if(player_1_pressed): print(f"   >>> Game Over Spieler 1 Gewinnt mit: {reaction_time:.2f} Sekunden")
    else: print(f"   >>> Game Over Spieler 2 Gewinnt mit: {reaction_time:.2f} Sekunden")

    return player_1_pressed

startup()

for r in range(rounds):
    print("\n" + "=" * 40)
    print(f"        Runde {r + 1} von {rounds}")
    print("=" * 40 + "\n")

    if play_round():
        player1_points += 1
    else:
        player2_points += 1

    sleep(1)  # Kurze Pause zwischen den Runden
    led_player1.off()
    led_player2.off()
# Am Ende die Ergebnisse ausgeben
# print("\n" + "=" * 40)
# print(f"Spieler 1 Gesamtzeit: {player1_time:.2f} Sekunden")
# print(f"Spieler 2 Gesamtzeit: {player2_time:.2f} Sekunden")
# print("=" * 40 + "\n")

# Sieger ermitteln
if player1_points < player2_points:
    print("Spieler 1 gewinnt!")
    led_player1.blink()
    led_reakt.blink()
    sleep(5)
    led_player1.off()
    led_reakt.off()
elif player1_points < player2_points:
    print("Spieler 2 gewinnt!")
    led_player2.blink()
    led_reakt.blink()
    sleep(5)
    led_player2.off()
    led_reakt.off()
else:
    print("Unentschieden!")


