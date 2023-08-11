# A representation of a chess board
from typing import Literal, List
from dataclasses import dataclass
from string import ascii_uppercase
#TODO: Fix

@dataclass
class ChessPiece:
    icon: Literal["♔","♕","♗","♘","♙","♖","♚","♛","♝","♞","♟","♜"]
    letter: Literal["K","Q","R","B","N",""]
    color: Literal["white", "black"]
    column:str
    row: int
    

    def __post_init__(self):
        # Valid Column
        self.column = self.column.upper()
        if not self.column in ascii_uppercase:
            raise ValueError("Invalid Column Provided")


    def column_to_number(self) -> int:
        """Converts a column to an integer representation

        Returns
        -------
        int
            The integer representation of the column letter
        """
        return ord(self.column)-65

def column_to_number(col) -> int:
    """Converts a column to an integer representation

    Returns
    -------
    int
        The integer representation of the column letter
    """
    return ord(col)-65

@dataclass
class ChessBoard:
    pieces: List[ChessPiece] = None
    board:List[List[str]] = None
    
    def __post_init__(self):
        # Setup pieces in default positions if not provided
        if not self.pieces:
            self.pieces = [
                ChessPiece("♔","K","white","E",7),
                ChessPiece("♕","Q","white","D",7),
                ChessPiece("♗","B","white","C",7),
                ChessPiece("♗","B","white","F",7),
                ChessPiece("♘","N","white","B",7),
                ChessPiece("♘","N","white","G",7),
                ChessPiece("♖","R","white","A",7),
                ChessPiece("♖","R","white","H",7),
                ChessPiece("♙","","white","A",6),
                ChessPiece("♙","","white","B",6),
                ChessPiece("♙","","white","C",6),
                ChessPiece("♙","","white","D",6),
                ChessPiece("♙","","white","E",6),
                ChessPiece("♙","","white","F",6),
                ChessPiece("♙","","white","G",6),
                ChessPiece("♙","","white","H",6),

                ChessPiece("♚","K","black","E",0),
                ChessPiece("♛","Q","black","D",0),
                ChessPiece("♝","B","black","C",0),
                ChessPiece("♝","B","black","F",0),
                ChessPiece("♞","N","black","B",0),
                ChessPiece("♞","N","black","G",0),
                ChessPiece("♜","R","black","A",0),
                ChessPiece("♜","R","black","H",0),
                ChessPiece("♟","","black","A",1),
                ChessPiece("♟","","black","B",1),
                ChessPiece("♟","","black","C",1),
                ChessPiece("♟","","black","D",1),
                ChessPiece("♟","","black","E",1),
                ChessPiece("♟","","black","F",1),
                ChessPiece("♟","","black","G",1),
                ChessPiece("♟","","black","H",1),
                ]
        
        # Setup board with provided pieces
        ## Start with blank board
        self.board = [
            ["◽","◾","◽","◾","◽","◾","◽","◾"],
            ["◾","◽","◾","◽","◾","◽","◾","◽"],
            ["◽","◾","◽","◾","◽","◾","◽","◾"],
            ["◾","◽","◾","◽","◾","◽","◾","◽"],
            ["◽","◾","◽","◾","◽","◾","◽","◾"],
            ["◾","◽","◾","◽","◾","◽","◾","◽"],
            ["◽","◾","◽","◾","◽","◾","◽","◾"],
            ["◾","◽","◾","◽","◾","◽","◾","◽"],
        ]
        
        ## replace squares with pieces
        for piece in self.pieces:
            self.board[piece.row][piece.column_to_number()] = piece.icon


    def printable_board(self) -> str:
        """Provides a printable representation of the board

        Returns
        -------
        str
            A printable representation of the board
        """
        result = "  A B C D E F G H\n"
        for index, row in enumerate(self.board):
            result += f"{index+1} "
            result += " ".join(row)
            result += "\n"
        result += "  A B C D E F G H"
        return result
    
    def make_move(self, move:str, piece:ChessPiece):
        
        # TODO: You would want to add logic for each piece to confirm it's legal
        if len(move) != 2:
            raise ValueError("Invalid move format")
        
        if piece.row-1%2 == 0 and piece.column_to_number()%2 ==0:
            self.board[piece.row-1][piece.column_to_number()] = "◽"
        elif piece.row-1%2 == 0 and piece.column_to_number()%2 !=0:
            self.board[piece.row-1][piece.column_to_number()] = "◾"
        elif piece.row-1%2 != 0 and piece.column_to_number()%2 ==0:
            self.board[piece.row-1][piece.column_to_number()] = "◾"
        else:
            self.board[piece.row-1][piece.column_to_number()] = "◽"
        
        new_column = column_to_number(move[0])
        new_row = int(move[1])
        
        self.board[new_row-1][new_column] = piece.icon
        
        
        # TODO: Need to add logic to confirm a piece isn't there already


if __name__ == "__main__":
    c = ChessBoard()
    print(c.printable_board())
    c.make_move("H3", c.pieces[-1])
    print(c.printable_board())
    