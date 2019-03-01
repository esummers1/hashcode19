import os
from guac.reader import Reader
from guac.solver import Solver
from guac.writer import Writer


class Controller:

    def __init__(self, files, strategies):
        self.files = files
        self.strategies = strategies
        self.input_path = os.path.dirname(os.path.dirname(__file__)) + "/files/"
        self.output_path = os.path.dirname(os.path.dirname(__file__)) + "/output/"

    def run(self):
        """
        For every file in our stored list:
            1. Read its contents
            2. Apply our algorithm
            3. Determine the score
            4. Print the score to the console
            5. Generate the output file
        """

        total_score = 0

        for file in self.files:
            lines = Reader.read(self.input_path + file + ".txt")
            photos = Reader.tabulate(lines)

            solver = Solver(photos, self.strategies)
            slideshow = solver.solve()

            print("Score for " + file + ": " + str(slideshow.score)
                  + " - " + slideshow.strategy.identify())
            Writer.write(self.output_path + file + ".output", slideshow.slides)

            total_score += slideshow.score

        print("\nTotal Score: " + str(total_score) + " - Holy Guacamole!!")
