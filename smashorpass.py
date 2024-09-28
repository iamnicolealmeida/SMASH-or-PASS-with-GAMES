import random
import os
import time
from colorama import Fore, Style, init
import pyfiglet  


init(autoreset=True)


games = [
    "The Witcher 3",
    "Cyberpunk 2077",
    "Red Dead Redemption 2",
    "Dark Souls 3",
    "Sekiro: Shadows Die Twice",
    "Hollow Knight",
    "Celeste",
    "Hades",
    "God of War",
    "Elden Ring",
    "The Walking Dead"
    "The Legend of Zelda: Breath of the Wild",
    "Grand Theft Auto V",
    "Assassin's Creed Valhalla",
    "Resident Evil Village",
    "Ghost of Tsushima",
    "Final Fantasy VII Remake",
    "Spider-Man: Miles Morales",
    "Death Stranding",
    "Doom Eternal",
    "Control",
    "Monster Hunter: World",
    "Overwatch",
    "Apex Legends",
    "The Last of Us Part II",
    "Bloodborne",
    "Persona 5",
    "Ori and the Will of the Wisps",
    "Star Wars Jedi: Fallen Order",
    "Far Cry 5",
    "Divinity: Original Sin 2"
]

library = []

def already_in_library(game):
    return game in library

def show_games():
    if not games:
        print(Fore.RED + "There are no games to choose!")
        return None

    game = random.choice(games)
    games.remove(game)

    return game

def show_library():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.YELLOW + "Opening your library...")
    time.sleep(1)  
    if not library:
        print(Fore.RED + "Your library is empty!")
    else:
        os.system('cls')
        print(Fore.GREEN + "\nSaved games in your library:")
        for game in library:
            print(Fore.CYAN + "- " + game)

    time.sleep(2)

def play():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Exibe o título com fonte estilizada
    title = pyfiglet.figlet_format("Smash or Pass", font="slant")
    print(Fore.MAGENTA + title)
    time.sleep(1)

    print(Fore.MAGENTA + "Welcome to 'Smash or Pass' Game!\n")
    time.sleep(1)

    while True:
        game = show_games()
        if game is None:
            break
        game_font = pyfiglet.figlet_format(game, font="slant")
        print(Fore.YELLOW + "\nYou've received the game: " + Fore.LIGHTBLUE_EX + game_font + "\n")
        
        print(Fore.GREEN + "[S] - SMASH (save to library)")
        print(Fore.RED + "[P] - PASS")
        print(Fore.CYAN + "[B] - OPEN LIBRARY")

        choice = input(Fore.LIGHTMAGENTA_EX + '=» ').strip().lower()

        if choice == "s":
            os.system('cls' if os.name == 'nt' else 'clear')
            if not already_in_library(game):
                library.append(game)
                print(Fore.GREEN + game + " added to your library!\n")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + game + " already in your library!\n")
        elif choice == "p":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + game + " was rejected.\n")
        elif choice == "b":
            show_library()
        else:
            print(Fore.RED + "INVALID INPUT!\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    final_font = pyfiglet.figlet_format("Game Over", font="slant")
    print(Fore.MAGENTA + final_font)
    
    print(Fore.MAGENTA + "\nThere are no more games left.\nYour final library:")
    show_library()



if __name__ == "__main__":
    play()
