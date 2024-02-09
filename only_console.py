import heroes as h#собственный файл
from time import sleep
from colorama import *
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
    def chet(self,x):
        if '.5' in str(x /2):
            return False
        return True
    def show(self):
        """показывает список"""
        #self.print = ' 1'
        i = 1
        print(" a b c d e f g h")
        for line in self.board:
            if self.chet(i):
                print(str(i) + Back.BLACK + " "+line[0] + Back.WHITE + " "+line[1] + Back.BLACK + " "+line[2] + Back.WHITE + " "+line[3] + Back.BLACK + " "+line[4] + Back.WHITE + " "+line[5] + Back.BLACK + " "+line[6] + Back.WHITE + " "+line[7]+ Style.RESET_ALL)
            else:
                print(str(i) + Back.WHITE + " "+line[0] + Back.BLACK + " "+line[1] + Back.WHITE + " "+line[2] + Back.BLACK + " "+line[3] + Back.WHITE + " "+line[4] + Back.BLACK + " "+line[5] + Back.WHITE + " "+line[6] + Back.BLACK + " "+line[7] + Style.RESET_ALL )
            i+=1
        """Другой алгоритм


        for line in self.board:
            for simvol in line:
                if self.chet(n_sim):
                    self.print += Fore.WHITE + simvol + ' ' + Style.RESET_ALL
                else:
                    self.print += Fore.BLACK + simvol + ' ' + Style.RESET_ALL
            if i != 9:
                self.print += '\n '+str(i)
                i += 1
            n_sim += 1
        print(self.print)
        """
    def create_peshki(self):
        x = 1
        for x in range(8):# Чёрные пешки
            if x == 0: x = 1
            self.p = h.Peshka('♟',True,x-1,6)
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
if 1 == 1:
#while True:
    #of = input("Фигура для ходьбы: ")
    #to = input("Куда поставить: ")
    el = board.peshki[12]
    el.look = Back.GREEN+ el.look

    liste = el.move(board.board)
    print(liste)
    for c in liste:

        board.board[c[1]][c[0]] = "✗"
    board.update()
    board.show()
    #if to == '':
    #    break
