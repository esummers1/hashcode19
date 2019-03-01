from guac.models import Slideshow
from guac.scorer import ScoreCalculator


class Solver:

    def __init__(self, photos, strategies):
        self.photos = photos
        self.strategies = strategies

    def solve(self):
        """
        Construct a Slideshow using the stored set of Photos by running every
        Strategy, and return whichever Slideshow has the highest score.

        :return: the Slideshow from the most suitable Strategy
        """

        best_score = 0
        results = {}

        for strategy in self.strategies:
            slides = strategy.solve(self.photos)
            score = ScoreCalculator.get_score(slides)

            if score >= best_score:
                best_score = score
                results[score] = Slideshow(slides, score, strategy)

        return results[best_score]
