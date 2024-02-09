class Thather():
    """
        Главный класс
            1.передача координат
            2.__init__
    """
    def __init__(self,look,black,x,y):
        """look -> str, black -> bool, x,y -> int"""
        self.x = x
        self.y = y
        self.look = look
        self.black = black
    def cord(self):
        return [self.x,self.y]
    def delete(self,board):
        """Заменяет предмет на ' ' """
        board[self.x][self.y] = ' '
class Peshka(Thather):
    def __init__(self,look,black,x,y):
        """look -> str, black -> bool, x,y -> int"""
        super().__init__(look,black,x,y)
    def move(self,board):
        """Возвращает нужные координаты для перестановки"""
        self.places1 = [self.can_go(board)]
        self.places2 = self.can_front(board)
        if self.places2 != -1:
            for pl in self.places2:
                self.places1.append(pl)
        return self.places1
    def can_go(self,board):
        """Возвращает передние координаты
                        если нет фигур
                    да                   нет
            вернуть координаты       вернуть -1
        """
    
        if self.black:
            self.go = -1
        else:
            self.go = +1

        if board[self.x][self.y + self.go] == ' ':

            return self.y + self.go

        else:

            return -1
    def can_front(self,board):
        """Проверяет:
             ___пешка___
            /           \
          cюда         сюда
          если         если
          есть         есть
        """

        if self.black:
            self.go = -1
        else:
            self.go = +1
        self.ret = -1
        if board[self.x + 1][self.y + self.go] != ' ':
            self.ret = [self.x + 1,self.y + self.go]
        if board[self.x - 1][self.y + self.go] != ' ':

            return [[self.x - 1,self.y + self.go],self.ret]
        else:
            return [self.ret]
        return -1

            
    
