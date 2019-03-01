class ScoreCalculator:

    @staticmethod
    def get_score(slides):
        """
        Compute the total score of a solution (list of Slides).

        :param slideshow: the Slides to be scored
        :return: the score
        """

        score = 0

        for counter, value in enumerate(slides):
            if counter == len(slides) - 1:
                break

            score += ScoreCalculator.compare_slides(
                slides[counter], slides[counter + 1])

        return score

    @staticmethod
    def compare_slides(slide1, slide2):
        """
        Compare two Slides and evaluate the score of the pairing, according to
        the procedure defined in the problem statement:
            Factor 1 - number of tags the slides have in common
            Factor 2 - number of tags present in the first but not the second
            Factor 3 - number of tags present in the second but not the first
        Return the smallest of these factors.

        :param slide1: the first Slide
        :param slide2: the second Slide
        :return: the interest factor, i.e. score for the pairing
        """

        common_tags = len([tag for tag in slide1.tags if tag in slide2.tags])
        unique_left_tags = len([tag for tag in slide1.tags if tag not in slide2.tags])
        unique_right_tags = len([tag for tag in slide2.tags if tag not in slide1.tags])

        return min(common_tags, unique_left_tags, unique_right_tags)
