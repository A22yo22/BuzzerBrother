from gpiozero import Button
from time import sleep, time

# GPIO-Pins definieren
button1 = Button(19, pull_up=False)  # Spieler 1 Taster
button2 = Button(6, pull_up=False)   # Spieler 2 Taster

# Spielparameter
rounds = 6  # Anzahl der Runden
player1_time = 0
player2_time = 0

def startup():
    print("Buzzer Brother")
    print("==============")
    print("\nDruecke den Knopf, um das Spiel zu starten...")
    button1.wait_for_press()
    print("\nSpiel startet in 3 Sekunden...")
    sleep(3)
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


def play_round(player, button):
    print(f"   >>> Spieler {player}, bereite dich vor...")
    sleep(2)  # Kurze Pause vor dem Start
    print("   >>> Druecke jetzt den Knopf!")
    start_time = time()
    button.wait_for_press()
    reaction_time = time() - start_time
    print(f"   >>> Spieler {player} Reaktionszeit: {reaction_time:.2f} Sekunden")
    return reaction_time

startup()

for r in range(rounds):
    print("\n" + "=" * 40)
    print(f"        Runde {r + 1} von {rounds}")
    print("=" * 40 + "\n")

    # Abwechselnd Spieler 1 und Spieler 2
    if r % 2 == 0:
        player1_time += play_round(1, button1)
    else:
        player2_time += play_round(2, button2)

    sleep(1)  # Kurze Pause zwischen den Runden

# Am Ende die Ergebnisse ausgeben
print("\n" + "=" * 40)
print(f"Spieler 1 Gesamtzeit: {player1_time:.2f} Sekunden")
print(f"Spieler 2 Gesamtzeit: {player2_time:.2f} Sekunden")
print("=" * 40 + "\n")

# Sieger ermitteln
if player1_time < player2_time:
    print("Spieler 1 gewinnt!")
elif player2_time < player1_time:
    print("Spieler 2 gewinnt!")
else:
    print("Unentschieden!")


