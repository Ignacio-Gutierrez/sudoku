class sudoku_back:
    
    def __init__(self):
        self.board = [[' ' for _ in range(9)] for _ in range(9)]

    def show_board(self):
        # Un espacio
        print('\n')

        # Fila que lista las columnas
        for col in range(10):                
            print(f' ({col})', end = '')
        print('\n')                                
        
        # Matriz del tablero de juego, ordenada estéticamente
        row_valor = 0 
        for row in range(9):   
            row_valor += 1            
            print(f'({row_valor})', '|', end = '')
            for col in range(9):                                   
                print(f' {self.board[row][col]} |', end = '')
            print('\n')

    # Repetidos
    def rep(self, row, col):
        row = row-1
        col = col-1

        if not any(' ' in _ for _ in self.board):
            return('Ganaste')

        if self.board[row][col] != ' ':
    # Revisar Horizontales  
            repr = 0
            for c in range(9):
                if self.board[row][col] == self.board[row][c]:
                    repr += 1   

    # Revisar Verticales
            repc = 0
            for r in range(9):
                if self.board[row][col] == self.board[r][col]:
                    repc += 1

	# Revisar Matriz 3x3
            x = (row//3)
            y = (col//3)
            repm = 0
            for r in range(3*x, 3*(x+1)):
                for c in range(3*y, 3*(y+1)):
                    if self.board[row][col] == self.board[r][c]:
                        repm += 1

            if repr > 1 or repc > 1 or repm > 1:
                return False
            if repr == 1 or repc == 1 or repm == 1:
                return True
    
    # Pone números
    def put_number(self, row, col, new_number):

        row = row-1
        col = col-1

        if 0 < new_number < 10 and -1 < row < 9 and -1 < col < 9:

            if self.board[row][col] == ' ' or self.board[row][col] != ' ':
                self.board[row][col] = str(new_number)
    
                if self.rep(row+1,col+1) == False:
                    self.board[row][col] = ' '
                    print(f'{new_number} se repite, cambie el número o la posición')
                else:
                    return True
        else:
            print(f'Todos los números deben ser entre 1 y 9.')   