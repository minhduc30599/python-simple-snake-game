from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_score_board()

    def update_score_board(self):
        self.write(f'Your score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 24, 'italic'))

    def get_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.clear()
        self.score = 0
        self.update_score_board()

    def get_point(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def end_game(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 24, 'italic'))
