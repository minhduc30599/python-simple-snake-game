from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_score_board()

    def update_score_board(self):
        self.write(f'Your score: {self.score}', align='center', font=('Arial', 24, 'italic'))

    def get_point(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def end_game(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 24, 'italic'))
