import tkinter as tk
from PIL import Image, ImageTk

class AbstractPiece(tk.Label):
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

        self.Brown_Pawn_Photo=ImageTk.PhotoImage(ChessApp.Brown_Pawn_Image)
        self.Brown_Horse_Photo=ImageTk.PhotoImage(ChessApp.Brown_Horse_Image)
        self.Brown_Knight_Photo=ImageTk.PhotoImage(ChessApp.Brown_Knight_Image)
        self.Brown_Tower_Photo=ImageTk.PhotoImage(ChessApp.Brown_Tower_Image)
        self.Brown_King_Photo=ImageTk.PhotoImage(ChessApp.Brown_King_Image)
        self.Brown_Queen_Photo=ImageTk.PhotoImage(ChessApp.Brown_Queen_Image)

        self.Gray_Pawn_Photo=ImageTk.PhotoImage(ChessApp.Gray_Pawn_Image)
        self.Gray_Horse_Photo=ImageTk.PhotoImage(ChessApp.Gray_Horse_Image)
        self.Gray_Knight_Photo=ImageTk.PhotoImage(ChessApp.Gray_Knight_Image)
        self.Gray_Tower_Photo=ImageTk.PhotoImage(ChessApp.Gray_Tower_Image)
        self.Gray_King_Photo=ImageTk.PhotoImage(ChessApp.Gray_King_Image)
        self.Gray_Queen_Photo=ImageTk.PhotoImage(ChessApp.Gray_Queen_Image)

        self.GrayPawns=[(6, i) for i in range(8)]
        self.GrayKnights=[(7, 2), (7, 5)]
        self.GrayTowers=[(7, 0), (7, 7)]
        self.GrayHorses=[(7, 1), (7, 6)]
        self.GrayKing=[7, 3]
        self.GrayQueen=[7, 4]

        self.GrayPiecesAlive=[self.GrayPawns, self.GrayKnights, self.GrayTowers, self.GrayHorses, self.GrayKing, self.GrayQueen]

        self.BrownPawns=[(1, i) for i in range(8)]
        self.BrownKnights=[(0, 2), (0, 5)]
        self.BrownTowers=[(0, 0), (0, 7)]
        self.BrownHorses=[(0, 1), (0, 6)]
        self.BrownKing=[0, 4]
        self.BrownQueen=[0, 3]

        self.BrownPiecesAlive=[self.BrownPawns, self.BrownKnights, self.BrownTowers, self.BrownHorses, self.BrownKing, self.BrownQueen]

        self.SquareLabels=[[AbstractPiece(self, y, x, image=self.PhotoPixel, width=99, height=87, compound="c") for x in range(8)] for y in range(8)]

        self.CreateBoard()

        self.CreatePieces()

    def CreatePieces(self):
        if self.BrownPawns:
            for item in self.BrownPawns:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Brown_Pawn_Photo, "Pawn", 1)

        if self.BrownHorses:
            for item in self.BrownHorses:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Brown_Horse_Photo, "Horse", 1)

        if self.BrownKnights:
            for item in self.BrownKnights:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Brown_Knight_Photo, "Knight", 1)

        if self.BrownTowers:
            for item in self.BrownTowers:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Brown_Tower_Photo, "Tower", 1)

        if self.BrownKing:
            self.RenderPiece(self.SquareLabels[self.BrownKing[0]][self.BrownKing[1]], self.Brown_King_Photo, "King", 1)

        if self.BrownQueen:
            self.RenderPiece(self.SquareLabels[self.BrownQueen[0]][self.BrownQueen[1]], self.Brown_Queen_Photo, "Queen", 1)

        if self.GrayPawns:
            for item in self.GrayPawns:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Gray_Pawn_Photo, "Pawn", 2)

        if self.GrayHorses:
            for item in self.GrayHorses:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Gray_Horse_Photo, "Horse", 2)

        if self.GrayKnights:
            for item in self.GrayKnights:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Gray_Knight_Photo, "Knight", 2)

        if self.GrayTowers:
            for item in self.GrayTowers:
                self.RenderPiece(self.SquareLabels[item[0]][item[1]], self.Gray_Tower_Photo, "Tower", 2)

        if self.GrayKing:
            self.RenderPiece(self.SquareLabels[self.GrayKing[0]][self.GrayKing[1]], self.Gray_King_Photo, "King", 2)

        if self.GrayQueen:
            self.RenderPiece(self.SquareLabels[self.GrayQueen[0]][self.GrayQueen[1]], self.Gray_Queen_Photo, "Queen", 2)

    def CreateBoard(self):
        for i, row in enumerate(self.SquareLabels):
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
        for row in self.SquareLabels:
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

    def PieceSelect(self, Square):
        def MovePiece(Square, piecename, piecearr):
            if self.selected_piece==piecename:
                for item in piecearr:
                    if item[0]==self.selected_square_tuple[0] and item[1]==self.selected_square_tuple[1]:
                        holder = list(item)
                        piecearr.remove(item)
                        holder[0]=Square.row
                        holder[1]=Square.column
                        piecearr.append(tuple(holder))
        def MovePieceTwo(Square, piecename, piecearr):
            if self.selected_piece==piecename:
                if piecearr[0]==self.selected_square_tuple[0] and piecearr[1]==self.selected_square_tuple[1]:
                    piecearr[0]=Square.row
                    piecearr[1]=Square.column
        if not Square.selected and not self.selected_square and Square.color==self.color_turn:
            Square.configure(bg="yellow")
            Square.selected=True
            self.selected_piece=Square.current_piece
            self.selected_square=True
            self.selected_square_tuple=(Square.row, Square.column)
            self.selected_square_moves=self.PieceMove(Square)
            print(self.selected_square_moves)
            try:
                for item in self.selected_square_moves:
                    self.SquareLabels[item[0]][item[1]].configure(bg="white")
                    self.SquareLabels[item[0]][item[1]].update()
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
            for item in self.selected_square_moves:
                if Square.row==item[0] and Square.column==item[1]:
                    if self.color_turn==1:
                        if self.selected_piece=="Pawn":
                            MovePiece(Square, "Pawn", self.BrownPawns)
                        elif self.selected_piece=="Tower":
                            MovePiece(Square, "Tower", self.BrownTowers)
                        elif self.selected_piece=="Horse":
                            MovePiece(Square, "Horse", self.BrownHorses)
                        elif self.selected_piece=="Knight":
                            MovePiece(Square, "Knight", self.BrownKnights)
                        elif self.selected_piece=="King":
                            MovePieceTwo(Square, "King", self.BrownKing)
                        elif self.selected_piece=="Queen":
                            MovePieceTwo(Square, "Queen", self.BrownQueen)

                    elif self.color_turn==2:
                        if self.selected_piece=="Pawn":
                            MovePiece(Square, "Pawn", self.GrayPawns)
                        elif self.selected_piece=="Tower":
                            MovePiece(Square, "Tower", self.GrayTowers)
                        elif self.selected_piece=="Horse":
                            MovePiece(Square, "Horse", self.GrayHorses)
                        elif self.selected_piece=="Knight":
                            MovePiece(Square, "Knight", self.GrayKnights)
                        elif self.selected_piece=="King":
                            MovePieceTwo(Square, "King", self.GrayKing)
                        elif self.selected_piece=="Queen":
                            MovePieceTwo(Square, "Queen", self.GrayQueen)

                    print(self.GrayPawns)
                    self.selected_square=False
                    self.selected_square_tuple=0
                    self.selected_square_moves=0
                    self.selected_piece=""
                    Square.used = True
                    if self.color_turn==1:
                        self.color_turn=2
                    elif self.color_turn==2:
                        self.color_turn=1
                    self.UpdateBoard()

        elif not Square.selected and self.selected_square and Square.color!=self.color_turn:
            print("Eat!")
            for item in self.selected_square_moves:
                if Square.row==item[0] and Square.column==item[1]:
                    self.eatpiece(Square)
                    if self.color_turn==1:
                        if self.selected_piece=="Pawn":
                            MovePiece(Square, "Pawn", self.BrownPawns)
                        elif self.selected_piece=="Tower":
                            MovePiece(Square, "Tower", self.BrownTowers)
                        elif self.selected_piece=="Horse":
                            MovePiece(Square, "Horse", self.BrownHorses)
                        elif self.selected_piece=="Knight":
                            MovePiece(Square, "Knight", self.BrownKnights)
                        elif self.selected_piece=="King":
                            MovePieceTwo(Square, "King", self.BrownKing)
                        elif self.selected_piece=="Queen":
                            MovePieceTwo(Square, "Queen", self.BrownQueen)

                    elif self.color_turn==2:
                        if self.selected_piece=="Pawn":
                            MovePiece(Square, "Pawn", self.GrayPawns)
                        elif self.selected_piece=="Tower":
                            MovePiece(Square, "Tower", self.GrayTowers)
                        elif self.selected_piece=="Horse":
                            MovePiece(Square, "Horse", self.GrayHorses)
                        elif self.selected_piece=="Knight":
                            MovePiece(Square, "Knight", self.GrayKnights)
                        elif self.selected_piece=="King":
                            MovePieceTwo(Square, "King", self.GrayKing)
                        elif self.selected_piece=="Queen":
                            MovePieceTwo(Square, "Queen", self.GrayQueen)

                    self.selected_square=False
                    self.selected_square_tuple=0
                    self.selected_square_moves=0
                    self.selected_piece=""
                    if self.color_turn==1:
                        self.color_turn=2
                    elif self.color_turn==2:
                        self.color_turn=1
                    self.UpdateBoard()
                else:
                    pass

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

    def eatpiece(self, Square):
        def eatsetup(piecename, piecearr):
            for item in piecearr:
                for move in self.selected_square_moves:
                    if item==move:
                        piecearr.remove(item)
        def eatsetuptwo(piecename, piecelist):
            for move in self.selected_square_moves:
                if (Square.row==piecelist[0] and Square.column==piecelist[1]) and (Square.row==move[0] and Square.column==move[1]):
                    piecelist.pop()
                    piecelist.pop()
        if Square.current_piece=="Pawn":
            eatsetup("Pawn", self.BrownPawns)
        elif Square.current_piece=="Horse":
            eatsetup("Horse", self.BrownHorses)
        elif Square.current_piece=="Tower":
            eatsetup("Tower", self.BrownTowers)
        elif Square.current_piece=="Knight":
            eatsetup("Knight", self.BrownKnights)
        elif Square.current_piece=="King":
            eatsetuptwo("King", self.BrownKing)
        elif Square.current_piece=="Queen":
            eatsetuptwo("Queen", self.BrownQueen)

        if Square.current_piece=="Pawn":
            eatsetup("Pawn", self.GrayPawns)
        elif Square.current_piece=="Horse":
            eatsetup("Horse", self.GrayHorses)
        elif Square.current_piece=="Tower":
            eatsetup("Tower", self.GrayTowers)
        elif Square.current_piece=="Knight":
            eatsetup("Knight", self.GrayKnights)
        elif Square.current_piece=="King":
            eatsetuptwo("King", self.GrayKing)
        elif Square.current_piece=="Queen":
            eatsetuptwo("Queen", self.GrayQueen)

    def PieceMove(self, Square):
        def minoftwo(a, b):
            if a>b:
                return b
            else:
                return a
        def itermove(a, b):
            if a<0 or b<0:
                return False
            elif self.SquareLabels[a][b].current_piece!="" and self.SquareLabels[a][b].color==Square.color:
                return False
            elif self.SquareLabels[a][b].current_piece!="" and self.SquareLabels[a][b].color!=Square.color:
                movelist.append((a, b))
                return False
            else:
                movelist.append((a, b))
                return True
        def normalmove(a, b):
            if self.SquareLabels[a][b].current_piece=="" or self.SquareLabels[a][b].color!=Square.color:
                movelist.append((a, b))
        def emptyspaceadd(a, b):
            if self.SquareLabels[a][b].current_piece=="":
                movelist.append((a, b))
        def possiblemove(a, b):
            if self.SquareLabels[a][b].current_piece!="" and self.SquareLabels[a][b].color!=Square.color:
                movelist.append((a, b))
        def horsemove(a, b):
            if self.SquareLabels[a][b].current_piece=="" or self.SquareLabels[a][b].color!=Square.color:
                movelist.append((a, b))
        movelist=[]
        posy = int(Square.row)
        posx = int(Square.column)
        if Square.current_piece=="Pawn":
            if Square.color==2:
                emptyspaceadd(posy-1, posx)
                if not Square.used:
                    emptyspaceadd(posy-2, posx)
                try:
                    possiblemove(posy-1, posx-1)
                    possiblemove(posy-1, posx+1)
                except IndexError:
                    pass
            elif Square.color==1:
                emptyspaceadd(posy+1, posx)
                if not Square.used:
                    emptyspaceadd(posy+2, posx)
                try:
                    possiblemove(posy+1, posx-1)
                    possiblemove(posy+1, posx+1)
                except IndexError:
                    pass
        elif Square.current_piece=="Horse":
            if posy+2<=7 and posx+1<=7:
                horsemove(posy+2, posx+1)
            if posy+2<=7 and posx-1>=0:
                horsemove(posy+2, posx-1)
            if posy-2>=0 and posx+1<=7:
                horsemove(posy-2, posx+1)
            if posy-2>=0 and posx-1>=0:
                horsemove(posy-2, posx-1)
            if posy-1>=0 and posx-2>=0:
                horsemove(posy-1, posx-2)
            if posy-1>=0 and posx+2<=7:
                horsemove(posy-1, posx+2)
            if posy+1<=7 and posx-2>=0:
                horsemove(posy+1, posx-2)
            if posy+1<=7 and posx+2<=7:
                horsemove(posy+1, posx+2)
        elif Square.current_piece=="Tower":
            for i in range(Square.row-1, -1, -1):
                if not itermove(i, posx):
                    break
            for i in range(Square.column-1, -1, -1):
                if not itermove(posy, i):
                    break
            for i in range(1, 8-Square.row):
                if not itermove(posy+i, posx):
                    break
            for i in range(1, 8-Square.column):
                if not itermove(posy, posx+i):
                    break
        elif Square.current_piece=="Knight":
            for i in range(1, minoftwo(Square.row, Square.column)+1):
                if not itermove(posy-i, posx-i):
                    break
            for i in range(1, minoftwo(Square.row, 7-Square.column)+1):
                if not itermove(posy-i, posx+i):
                    break
            for i in range(1, minoftwo(7-Square.row, Square.column)+1):
                if not itermove(posy+i, posx-i):
                    break
            for i in range(1, minoftwo(7-Square.row, 7-Square.column)+1):
                if not itermove(posy+i, posx+i):
                    break
        elif Square.current_piece=="King":
            try:
                if posy-1>=0:
                    normalmove(posy-1, posx)
                if posy+1<=7:
                    normalmove(posy+1, posx)
                if posx-1>=0:
                    normalmove(posy, posx-1)
                if posx+1<=7:
                    normalmove(posy, posx+1)
                if posy-1>=0 and posx-1>=0:
                    normalmove(posy-1, posx-1)
                if posy+1<=7 and posx-1>=0:
                    normalmove(posy+1, posx-1)
                if posy-1>=0 and posx+1<=7:
                    normalmove(posy-1, posx+1)
                if posy+1<=7 and posx+1<=7:
                    normalmove(posy+1, posx+1)
            except IndexError:
                pass
        elif Square.current_piece=="Queen":
            for i in range(Square.row-1, -1, -1):
                if not itermove(i, posx):
                    break
            for i in range(Square.column-1, -1, -1):
                if not itermove(posy, i):
                    break
            for i in range(1, 8-Square.row):
                if not itermove(posy+i, posx):
                    break
            for i in range(1, 8-Square.column):
                if not itermove(posy, posx+i):
                    break
            for i in range(1, minoftwo(Square.row, Square.column)+1):
                if not itermove(posy-i, posx-i):
                    break
            for i in range(1, minoftwo(Square.row, 7-Square.column)+1):
                if not itermove(posy-i, posx+i):
                    break
            for i in range(1, minoftwo(7-Square.row, Square.column)+1):
                if not itermove(posy+i, posx-i):
                    break
            for i in range(1, minoftwo(7-Square.row, 7-Square.column)+1):
                if not itermove(posy+i, posx+i):
                    break
        return movelist


def main():
    aa = tk.Tk()
    cc = ChessApp(aa)
    cc.mainloop()

if __name__ == "__main__":
    main()
