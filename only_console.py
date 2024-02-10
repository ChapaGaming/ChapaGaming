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

        self.pawns = []
        self.rooks = []
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
        self.create_pawns()
        self.create_rooks()
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

    def create_pawns(self):
        x = 1
        for x in range(9):# Чёрные пешки
            if x == 0: x = 1
            self.p = h.Pawn('♟',True,x-1,6)
            self.board[self.p.y][self.p.x] = self.p.look
            self.pawns.append(self.p)
        y = 1
        for y in range(8):# Белые пешки
            self.p = h.Pawn('♙',False,y-1,1)
            self.board[self.p.y][self.p.x] = self.p.look
            self.pawns.append(self.p)
    def create_rooks(self):
        rookCord = [[0,0],[7,0],[7,7],[0,7]]
        for i in [0,1]:#белые ладьи
            self.rooks.append(h.Rook("♖",False,rookCord[i][0],rookCord[i][1]))
        for i in [2,3]:#чёрные ладьи
            self.rooks.append(h.Rook("♜",True,rookCord[i][0],rookCord[i][1]))
    def update(self):
        for p in self.pawns:
            cord = p.cord()
            self.board[cord[1]][cord[0]] = p.look
        for r in self.rooks:
            cord = r.cord()
            self.board[cord[1]][cord[0]] = r.look
def who(look,x,y):
    if look in['♟','♙']:
        for p in board.pawns:
            if p.x == x:
                if p.y == x:
                    return p
    elif look in['♗','♝']:
        return "bishop"
    elif look in['♜','♖']:
        for p in board.rooks:
            if p.x == x:
                if p.y == x:
                    return p
    elif look in['♘','♞']:
        return "knight"
    elif look in['♛','♕']:
        return "queen"
    elif look in['♔','♚']:
        return "king"
        
board = ChessBoard()
alph = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    }

black_go = False

while True:
    board.update()
    board.show()
    ans_good = False
    while not ans_good:
        try:
            of = input("Фигура для ходьбы: ")
            fy = int(of[0]) - 1
            fx = alph[of[1]]
            s = board.board[fy][fx]
            board.board[fy][fx] = Back.GREEN + s + Style.RESET_ALL
            if len(of) > 2:
                print(Fore.RED + Style.BRIGHT+"нужно ввести 2 символа"+Style.RESET_ALL)
            else:
                ans_good = True
            #simvol = who(board.board[fy][fx],fx,fy)
            #kcan = simvol.move(board.board)
            #for c in can:
            #    board.board[c[1]][c[0]] = ""
        except ValueError:
            print(Fore.RED + Style.BRIGHT+"первый символ должен быть ЦИФРОЙ"+Style.RESET_ALL)
        except KeyError:
            print(Fore.RED + Style.BRIGHT+"недопустимая БУКВА (a, b, c, d, e, f, g, h)"+Style.RESET_ALL)
        except IndexError:
            print(Fore.RED + Style.BRIGHT+"нужно ввести 2 символа"+Style.RESET_ALL)

    to = input("Куда поставить: ")
    if to == 'stop':
        break

