import heroes as h#собственный файл
from time import sleep
def delete(obj):
    """Заменяет предмет на ' ' """
    x = obj.x
    y = obj.y
    board.board[x][y] = ' '

class ChessBoard():
    """
        Это класс главного поля он делает:
        1.Вывод
        2.Установка символа на поле
    """
    def __init__(self,**kwargs):
        """
            поламетры в **kwargs:
                line_1= list() // восемь елементов(фигур)
                line_2= list() // восемь елементов(фигур)
                line_3= list() // восемь елементов(фигур)
                line_4= list() // восемь елементов(фигур)
                line_5= list() // восемь елементов(фигур)
                line_6= list() // восемь елементов(фигур)
                line_7= list() // восемь елементов(фигур)
                line_8= list() // восемь елементов(фигур)

        """
        #списки с типами фигур#

        self.peshki = []

        #списки с типами фигур#

        self.board = [
            ['♖','♘','♗','♕','♔','♗','♘','♖'],
            ['♙','♙','♙','♙','♙','♙','♙','♙'],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♟','♟','♟','♟','♟','♟','♟','♟'],
            ['♜','♞','♝','♛','♚','♝','♞','♜']  
            ]
        #Создаю поле(классы)
        self.create_peshki()
        #коректировка по **kwargs
        self.lines = kwargs
        if self. lines != {}:
            for line in self.lines:
                self.N = int(line.split('_')[1]) -1
                self.board[self.N] = self.lines[line]
    def show(self):
        """показывает список"""
        self.print = ''
        for line in self.board:
            for simvol in line:
                self.print += simvol
                self.print += ' '
            self.print += '\n'
        print(self.print)
    def create_peshki(self):
        x = 1
        for x in range(8):# Чёрные пешки
            if x == 0: x = 1
            self.p = h.Peshka('♟',True,x-1,7)
            print(self.p.y,self.p.x)
            self.board[self.p.y][self.p.x] = self.p.look
            self.peshki.append(self.p)
        y = 1
        for y in range(8):# Белые пешки
            self.p = h.Peshka('♙',False,y-1,1)
            self.board[self.p.y][self.p.x] = self.p.look
            self.peshki.append(self.p)
    def update(self):
        for p in self.peshki:
            cord = p.cord()
            self.board[cord[1]][cord[0]] = p.look

board = ChessBoard()

while True:
    of = input("Фигура для ходьбы: ")
    to = input("Куда поставить: ")
    print(board.peshki[1].move(board.board))
    board.update()
    board.show()
    if to == '':
        break
