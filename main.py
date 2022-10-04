from game import sudoku_back

def play():

    game = sudoku_back()
    game_running = True

    while game_running == True:
        game.show_board()

        set_number = False
        
        while not set_number:
            new_number = input(f'Introduzca el nuevo número: ')
            row = input(f'Introduzca la fila en donde irá: ')
            col = input(f'Introduzca la columna en donde irá: ')

            try:
                set_number = game.put_number(int(row), int(col), int(new_number))
            except:
                print(f'Todos los números deben ser entre 1 y 9.')
        
        game_running = game.rep(int(row), int(col))
    
        if game_running != True:
            game.show_board()
            print(game.rep(int(row), int(col)))

if __name__ == '__main__':
    play()
