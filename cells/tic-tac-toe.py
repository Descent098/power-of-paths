from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, List

@dataclass
class Cell:
    row: Literal[1, 2, 3] # Can be either a 1, 2 or 3
    column: Literal["A", "B", "C"] # Can be either an "A", "B", or "C"
    player: Literal["X", "O", None] = None # Which player has the space, defaults to None

@dataclass
class Board:
    cells:List[Cell] # List of all the cells in the game
    winner:Literal["X","O", None] = None # Which player has won, defaults to None

    def player_move(self:Board, player: Literal["X", "O"], column:Literal["A", "B", "C"], row:Literal[1, 2, 3]):
        # Record a player's move
        for cell in self.cells:
            if cell.row == row and cell.column == column:
                cell.player = player
                return # Found cell
        raise ValueError(f"Could not find cell {column}{row}")
    
    def get_moves(self: Board) -> List[List[Cell],List[Cell]]:
        # Get a list of the moves made for each player
        x_moves = []
        o_moves = []
        for cell in self.cells:
            if cell.player is None:
                continue
            elif cell.player == "X":
                x_moves.append(cell)
            else:
                o_moves.append(cell)
        return [x_moves, o_moves]

def create_board() -> List[Cell]:
    # Setup cells for new game
    cells = []
    for column in ["A","B","C"]:
        for row in [1,2,3]:
            cells.append(Cell(row, column))
    return cells

if __name__ == "__main__":
    # Testing

    ## 1. Create new game
    game:Board = Board(create_board())

    ## 2. Register player moves
    game.player_move("X", "B", 2)
    game.player_move("O", "A", 3)
    game.player_move("X", "A", 1)
    game.player_move("O", "C", 2)
    game.player_move("X", "C", 3)

    ## 3. Register Winner
    game.winner = "X"

    moves = game.get_moves()

    # Convert each move to a readable format
    moves = [ 
        [f"{move.column}{move.row}" for move in moves[0]], 
        [f"{move.column}{move.row}" for move in moves[1]], 
    ]
    print(f"""\nGame over:

    Winner: {game.winner}
    X Moves: {' '.join(moves[0])}
    O Moves: {' '.join(moves[1])}\n"""
    )