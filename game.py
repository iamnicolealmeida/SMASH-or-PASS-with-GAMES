import random, os, time, sys
global resposta, resposta2
games = ['The walking dead season 1', 'The walking dead game season 2', 'The walking dead a new frontier', 'The walking dead the final season']
         
def main_menu():
    os.system('cls')
    print('____ENGLISH\/M E N U____')
    print('[1] - SORT RANDOM GAME')
    print('[2] - VIEW SAVED GAMES')
    print('[3] - CHANGE LANGUAGE')
    print('[4] - RULES')
    print('[5] - exit')
    while True:
        resposta = int(input('VALID OPTION=» '))
        while resposta <=0 or resposta >5:
            os.system('cls')
            main_menu()
            print('INSERT A VALID NUMBER!')
            resposta = int(input('VALID OPTION=» '))
        if resposta == 1:
            sort_random_game()
        if resposta == 3:
            portuguese_language_menu()
        if resposta == 5:
            sys.exit()
    
def sort_random_game():
    os.system('cls')
    print('SORT RANDOM GAME')
    print(random.choice(games))
    time.sleep(3)
    main_menu()
    

def view_saved_games():
    print('view right')
    time.sleep(3)
    main_menu()
    
    
def rules_game():
    print('RULES')
    main_menu()

def portuguese_language_menu():
    os.system('cls')
    print('____PORTUGUESE\/M E N U____')
    print('[1] - SORTEAR JOGO ALEATÓRIO')
    print('[2] - VER JOGOS SALVOS')
    print('[3] - MUDAR IDIOMA')
    print('[4] - REGRAS')
    print('[5] - sair')
    while True:
        resposta2 = int(input('VALID OPTION=» '))
        while resposta2 <=0 or resposta2 >5:
            os.system('cls')
            portuguese_language_menu()
            print('INSERT A VALID NUMBER!')
            resposta2 = int(input('VALID OPTION=» '))
        if resposta2 == 1:
            sort_random_game()
        if resposta2 == 3:
            main_menu()
        if resposta2 == 5:
            sys.exit()
    

main_menu()