from typing import List


class NQueenII:
    def __init__(self, size: int):
        """
        Initialize the NQueenII class.

        Parameters:
        - size (int): The size of the chessboard.
        """
        self.n: int = size
        self.chess_grid: List[List[bool]] = [[False for _ in range(size)] for _ in range(size)]
        self.solutions: List[List[List[bool]]] = []

    def __can_be_placed(self, row: int, col: int) -> bool:
        """
        Check if a queen can be placed at the given position.

        Parameters:
        - row (int): The row index.
        - col (int): The column index.

        Returns:
        - bool: True if the queen can be placed, False otherwise.
        """
        # Check for column
        for i in range(row):
            if self.chess_grid[i][col]:
                return False

        # Check main diagonal (top-left to bottom-right)
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.chess_grid[i][j]:
                return False

        # Check anti-diagonal (top-right to bottom-left)
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.chess_grid[i][j]:
                return False

        return True

    def solve(self, row=0):
        """
        Solve the N-Queens problem recursively.

        Parameters:
        - row (int): The current row to be processed.
        """
        if row >= self.n:
            # Append a deep copy of the current chess_grid to solutions
            self.solutions.append([row[:] for row in self.chess_grid])
            return

        for col in range(self.n):
            if self.__can_be_placed(row=row, col=col):
                self.chess_grid[row][col] = True
                self.solve(row=row + 1)
                self.chess_grid[row][col] = False

    @staticmethod
    def validate_input(number: str) -> bool:
        """
        Validate the input for the size of the chessboard.

        Parameters:
        - number (str): The input string.

        Returns:
        - bool: True if the input is valid, False otherwise.
        """
        try:
            number = int(number)
            if 1 <= number <= 9:
                return True
        except ValueError:
            pass
        return False


if __name__ == "__main__":
    # Example usage
    size_of_chessboard = input("Enter the size of chessboard (1-9): ")
    if NQueenII.validate_input(number=size_of_chessboard):
        n_queen = NQueenII(size=int(size_of_chessboard))
        n_queen.solve()
        print(f"Number of solutions for {n_queen.n}-Queens: {len(n_queen.solutions)}")
    else:
        print("Invalid input.")
