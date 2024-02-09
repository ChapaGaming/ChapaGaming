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
        self.black = black
        self.look = look
    def cord(self):
        return [self.x,self.y]
    def delete(self,board):
        """Заменяет предмет на ' ' """
        board[self.x][self.y] = ' '
class Peshka(Thather):
    def __init__(self,look,black,x,y,first = True):
        """look -> str, black -> bool, x,y -> int"""
        super().__init__(look,black,x,y)
        self.first = first
    def move(self,board):
        """Возвращает нужные координаты для перестановки"""
        self.places1 = []
        if self.can_go(board) != -1:
            self.places1 = self.can_go(board)
        self.places2 = self.can_front(board)
        if self.places2 != -1:
            for pl in self.places2:
                if pl != -1:
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

        if board[self.y + self.go][self.x] == ' ':
            self.rett = [[self.x,self.y + self.go]]
            if self.first:
                if board[self.y + 2*self.go][self.x] == ' ':
                    self.rett.append([self.x,self.y + 2*self.go])
                    return self.rett
            else:
                return self.rett
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
        if board[self.y + self.go][self.x + 1] != ' ':
            self.ret = [self.x + 1,self.y + self.go]
        if board[self.y + self.go][self.x - 1] != ' ':

            return [[self.x - 1,self.y + self.go],self.ret]
        else:
            return [self.ret]
        return -1

            
    
