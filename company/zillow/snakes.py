class SnakeGame:

    def __init__(self, width: int, height: int, food):
        self.height = height
        self.width = width
        self.food = food
        self.status = bool[width][height]

    def is_valid(self, direction, x, y):
        d = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}

        x_delta, y_delta = d[direction]
        x = x + x_delta
        y = x + y_delta
        return x >= 0 and y >= 0 and x < self.height and y < self.width

        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)