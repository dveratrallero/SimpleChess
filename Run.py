import tkinter as tk
from PIL import Image, ImageTk

class AbstractPiece(tk.Label):
    """docstring for Piece"""
    def __init__(self, root, row, column, *args, **kwargs):
        tk.Label.__init__(self, root, *args, **kwargs)
        self.current_piece=""
        self.row=row
        self.column=column
        self.color = 0
        self.defaultbg=""
        self.selected = False
        self.used = False

class ChessApp(tk.Frame):

    Brown_Pawn_Image =Image.open("ChessPieces/Brown_Pawn.png")
    Brown_Horse_Image = Image.open("ChessPieces/Brown_Horse.png")
    Brown_Knight_Image =Image.open("ChessPieces/Brown_Knight.png")
    Brown_Tower_Image = Image.open("ChessPieces/Brown_Tower.png")
    Brown_King_Image =Image.open("ChessPieces/Brown_King.png")
    Brown_Queen_Image = Image.open("ChessPieces/Brown_Queen.png")

    Gray_Pawn_Image =Image.open("ChessPieces/Gray_Pawn.png")
    Gray_Horse_Image = Image.open("ChessPieces/Gray_Horse.png")
    Gray_Knight_Image =Image.open("ChessPieces/Gray_Knight.png")
    Gray_Tower_Image = Image.open("ChessPieces/Gray_Tower.png")
    Gray_King_Image =Image.open("ChessPieces/Gray_King.png")
    Gray_Queen_Image = Image.open("ChessPieces/Gray_Queen.png")

    def __init__(self, chess_window):
        super().__init__(chess_window)
        chess_window.title("QUESS")
        self.place(width=800, height=800)
        chess_window.geometry("800x800")

        self.selected_square=False
        self.selected_square_tuple=0
        self.selected_square_moves=0
        self.selected_piece=""
        self.color_turn=2

        self.PhotoPixel=tk.PhotoImage(width=1, height=1)

        self.BrownPiecesPhotos={
        "Pawn":   ImageTk.PhotoImage(ChessApp.Brown_Pawn_Image),
        "Knight": ImageTk.PhotoImage(ChessApp.Brown_Horse_Image),
        "Tower":  ImageTk.PhotoImage(ChessApp.Brown_Knight_Image),
        "Horse":  ImageTk.PhotoImage(ChessApp.Brown_Tower_Image),
        "King":   ImageTk.PhotoImage(ChessApp.Brown_King_Image),
        "Queen":  ImageTk.PhotoImage(ChessApp.Brown_Queen_Image),
        }

        self.GrayPiecesPhotos={
        "Pawn":   ImageTk.PhotoImage(ChessApp.Gray_Pawn_Image),
        "Knight": ImageTk.PhotoImage(ChessApp.Gray_Horse_Image),
        "Tower":  ImageTk.PhotoImage(ChessApp.Gray_Knight_Image),
        "Horse":  ImageTk.PhotoImage(ChessApp.Gray_Tower_Image),
        "King":   ImageTk.PhotoImage(ChessApp.Gray_King_Image),
        "Queen":  ImageTk.PhotoImage(ChessApp.Gray_Queen_Image)
        }

        self.GrayPiecesAlive={
        "Pawn":   [(6, i) for i in range(8)],
        "Knight": [(7, 2), (7, 5)],
        "Tower":  [(7, 0), (7, 7)],
        "Horse":  [(7, 1), (7, 6)],
        "King":   [(7, 3)],
        "Queen":  [(7, 4)]
        }

        self.BrownPiecesAlive={
        "Pawn":   [(1, i) for i in range(8)],
        "Knight": [(0, 2), (0, 5)],
        "Tower":  [(0, 0), (0, 7)],
        "Horse":  [(0, 1), (0, 6)],
        "King":   [(0, 4)],
        "Queen":  [(0, 3)]
        }

        self.Board=[[AbstractPiece(self, y, x, image=self.PhotoPixel, width=99, height=87, compound="c") for x in range(8)] for y in range(8)]

        self.CreateBoard()

        self.CreatePieces()

    def CreatePieces(self):
        def IterRender(PieceAliveDict, PieceAlivePhoto, color):
            for a, b in PieceAliveDict.items():
                if b:
                    for item in b:
                        self.RenderPiece(self.Board[item[0]][item[1]], PieceAlivePhoto[a], a, color)
        IterRender(self.BrownPiecesAlive, self.BrownPiecesPhotos, 1)
        IterRender(self.GrayPiecesAlive, self.GrayPiecesPhotos, 2)

    def CreateBoard(self):
        for i, row in enumerate(self.Board):
            for h, square in enumerate(row):
                if (i+1)%2!=0:
                    if (h+1)%2!=0:
                        square.defaulbg="green"
                    elif (h+1)%2==0:
                        square.defaulbg="black"
                elif (i+1)%2==0:
                    if (h+1)%2!=0:
                        square.defaulbg="black"
                    elif (h+1)%2==0:
                        square.defaulbg="green"
                square.configure(bg=square.defaulbg)
                square.bind('<Button-1>', lambda event, Square=square: self.PieceSelect(Square))
                square.grid(row=i, column=h)

    def UpdateBoard(self):
        for row in self.Board:
            for square in row:
                square.configure(bg=square.defaulbg, image=self.PhotoPixel)
                square.image=self.PhotoPixel
                square.current_piece=""
                square.color=0
                square.selected=False
                square.update()
        self.CreatePieces()

    def RenderPiece(self, Square, img, name, color):
        Square.configure(image=img)
        Square.image=img
        Square.current_piece=name
        Square.color= color
        Square.update()

    def EndTurn(self):
        self.selected_square=False
        self.selected_square_tuple=0
        self.selected_square_moves=0
        self.selected_piece=""
        if self.color_turn==1:
            self.color_turn=2
        elif self.color_turn==2:
            self.color_turn=1

    def ExecuteMove(self, Square):
        def MovePiece(Square, piecename, piecearr):
            if self.selected_piece==piecename:
                for item in piecearr:
                    if item[0]==self.selected_square_tuple[0] and item[1]==self.selected_square_tuple[1]:
                        holder = list(item)
                        piecearr.remove(item)
                        holder[0]=Square.row
                        holder[1]=Square.column
                        piecearr.append(tuple(holder))
        for item in self.selected_square_moves:
            if Square.row==item[0] and Square.column==item[1]:
                if Square.current_piece!="":
                    self.EatPiece(Square)
                if self.color_turn==1:
                    MovePiece(Square, self.selected_piece, self.BrownPiecesAlive[self.selected_piece])
                elif self.color_turn==2:
                    MovePiece(Square, self.selected_piece, self.GrayPiecesAlive[self.selected_piece])

    def PieceSelect(self, Square):
        if not Square.selected and not self.selected_square and Square.color==self.color_turn:
            Square.configure(bg="yellow")
            Square.selected=True
            self.selected_piece=Square.current_piece
            self.selected_square=True
            self.selected_square_tuple=(Square.row, Square.column)
            self.selected_square_moves=self.PieceMove(Square)
            try:
                for item in self.selected_square_moves:
                    self.Board[item[0]][item[1]].configure(bg="white")
                    self.Board[item[0]][item[1]].update()
            except IndexError:
                pass

        elif not Square.selected and not self.selected_square and Square.color==0:
            print("Please select a Piece")

        elif not Square.selected and not self.selected_square and Square.color!=self.color_turn:
            print("Please wait until the other player moves")

        elif not Square.selected and self.selected_square and Square.color==self.color_turn:
            print("Another piece has been selected!")

        elif not Square.selected and self.selected_square and Square.color==0:
            print("Move!!")
            self.ExecuteMove(Square)
            Square.used = True
            self.EndTurn()
            self.UpdateBoard()

        elif not Square.selected and self.selected_square and Square.color!=self.color_turn:
            print("Eat!")
            self.ExecuteMove(Square)
            self.EndTurn()
            self.UpdateBoard()

        elif not Square.selected and self.selected_square and Square.color==self.color_turn:
            print("Hello World! You broke the game!")

        elif Square.selected and self.selected_square and Square.color==0:
            print("Yay! You broke the game!")

        elif Square.selected and self.selected_square and Square.color==self.color_turn:
            print("Rethink!")
            Square.selected=False
            self.selected_square=False
            self.selected_square_moves=0
            self.selected_square_tuple=0
            self.selected_piece=""
            self.UpdateBoard()

    def EatPiece(self, Square):
        def eatsetup(piecearr):
            for item in piecearr:
                if item[0]==Square.row and item[1]==Square.column:
                    piecearr.remove(item)
        if Square.color==1:
            eatsetup(self.BrownPiecesAlive[Square.current_piece])
        elif Square.color==2:
            eatsetup(self.GrayPiecesAlive[Square.current_piece])

    def PieceMove(self, Square):
        def MinOfTwo(a, b):
            if a>b:
                return b
            else:
                return a
        def IterMove(a, b):
            if a<0 or b<0:
                return False
            elif self.Board[a][b].current_piece!="" and self.Board[a][b].color==Square.color:
                return False
            elif self.Board[a][b].current_piece!="" and self.Board[a][b].color!=Square.color:
                movelist.append((a, b))
                return False
            else:
                movelist.append((a, b))
                return True
        def NormalMove(a, b):
            if self.Board[a][b].current_piece=="" or self.Board[a][b].color!=Square.color:
                movelist.append((a, b))
        def EmptySpaceAdd(a, b):
            if self.Board[a][b].current_piece=="":
                movelist.append((a, b))
        def PossibleMove(a, b):
            if self.Board[a][b].current_piece!="" and self.Board[a][b].color!=Square.color:
                movelist.append((a, b))
        def HorseMove(a, b):
            if self.Board[a][b].current_piece=="" or self.Board[a][b].color!=Square.color:
                movelist.append((a, b))
        movelist=[]
        if Square.current_piece=="Pawn":
            if Square.color==2:
                EmptySpaceAdd(Square.row-1, Square.column)
                if not Square.used:
                    EmptySpaceAdd(Square.row-2, Square.column)
                try:
                    PossibleMove(Square.row-1, Square.column-1)
                    PossibleMove(Square.row-1, Square.column+1)
                except IndexError:
                    pass
            elif Square.color==1:
                EmptySpaceAdd(Square.row+1, Square.column)
                if not Square.used:
                    EmptySpaceAdd(Square.row+2, Square.column)
                try:
                    PossibleMove(Square.row+1, Square.column-1)
                    PossibleMove(Square.row+1, Square.column+1)
                except IndexError:
                    pass
        elif Square.current_piece=="Horse":
            if Square.row+2<=7 and Square.column+1<=7:
                HorseMove(Square.row+2, Square.column+1)
            if Square.row+2<=7 and Square.column-1>=0:
                HorseMove(Square.row+2, Square.column-1)
            if Square.row-2>=0 and Square.column+1<=7:
                HorseMove(Square.row-2, Square.column+1)
            if Square.row-2>=0 and Square.column-1>=0:
                HorseMove(Square.row-2, Square.column-1)
            if Square.row-1>=0 and Square.column-2>=0:
                HorseMove(Square.row-1, Square.column-2)
            if Square.row-1>=0 and Square.column+2<=7:
                HorseMove(Square.row-1, Square.column+2)
            if Square.row+1<=7 and Square.column-2>=0:
                HorseMove(Square.row+1, Square.column-2)
            if Square.row+1<=7 and Square.column+2<=7:
                HorseMove(Square.row+1, Square.column+2)
        elif Square.current_piece=="Tower":
            for i in range(Square.row-1, -1, -1):
                if not IterMove(i, Square.column):
                    break
            for i in range(Square.column-1, -1, -1):
                if not IterMove(Square.row, i):
                    break
            for i in range(1, 8-Square.row):
                if not IterMove(Square.row+i, Square.column):
                    break
            for i in range(1, 8-Square.column):
                if not IterMove(Square.row, Square.column+i):
                    break
        elif Square.current_piece=="Knight":
            for i in range(1, MinOfTwo(Square.row, Square.column)+1):
                if not IterMove(Square.row-i, Square.column-i):
                    break
            for i in range(1, MinOfTwo(Square.row, 7-Square.column)+1):
                if not IterMove(Square.row-i, Square.column+i):
                    break
            for i in range(1, MinOfTwo(7-Square.row, Square.column)+1):
                if not IterMove(Square.row+i, Square.column-i):
                    break
            for i in range(1, MinOfTwo(7-Square.row, 7-Square.column)+1):
                if not IterMove(Square.row+i, Square.column+i):
                    break
        elif Square.current_piece=="King":
            try:
                if Square.row-1>=0:
                    NormalMove(Square.row-1, Square.column)
                if Square.row+1<=7:
                    NormalMove(Square.row+1, Square.column)
                if Square.column-1>=0:
                    NormalMove(Square.row, Square.column-1)
                if Square.column+1<=7:
                    NormalMove(Square.row, Square.column+1)
                if Square.row-1>=0 and Square.column-1>=0:
                    NormalMove(Square.row-1, Square.column-1)
                if Square.row+1<=7 and Square.column-1>=0:
                    NormalMove(Square.row+1, Square.column-1)
                if Square.row-1>=0 and Square.column+1<=7:
                    NormalMove(Square.row-1, Square.column+1)
                if Square.row+1<=7 and Square.column+1<=7:
                    NormalMove(Square.row+1, Square.column+1)
            except IndexError:
                pass
        elif Square.current_piece=="Queen":
            for i in range(Square.row-1, -1, -1):
                if not IterMove(i, Square.column):
                    break
            for i in range(Square.column-1, -1, -1):
                if not IterMove(Square.row, i):
                    break
            for i in range(1, 8-Square.row):
                if not IterMove(Square.row+i, Square.column):
                    break
            for i in range(1, 8-Square.column):
                if not IterMove(Square.row, Square.column+i):
                    break
            for i in range(1, MinOfTwo(Square.row, Square.column)+1):
                if not IterMove(Square.row-i, Square.column-i):
                    break
            for i in range(1, MinOfTwo(Square.row, 7-Square.column)+1):
                if not IterMove(Square.row-i, Square.column+i):
                    break
            for i in range(1, MinOfTwo(7-Square.row, Square.column)+1):
                if not IterMove(Square.row+i, Square.column-i):
                    break
            for i in range(1, MinOfTwo(7-Square.row, 7-Square.column)+1):
                if not IterMove(Square.row+i, Square.column+i):
                    break
        return movelist


def main():
    aa = tk.Tk()
    cc = ChessApp(aa)
    cc.mainloop()

if __name__ == "__main__":
    main()
