from abc import ABC, abstractmethod
from guac.models import Slide


class Strategy(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def identify(self):
        pass

    @abstractmethod
    def solve(self, photos):
        pass


class DumbStrategy(Strategy):

    def __init__(self):
        super().__init__()
        self.name = "Dumb Strategy"

    def identify(self):
        return self.name

    def solve(self, photos):
        """
        Compose slides of all horizontal photos, followed by pairs of all vertical
        photos, in the order they were received.

        :param photos: the photos to arrange
        :return: a list of slides
        """

        horizontal_photos = [photo for photo in photos if photo.orientation == "H"]
        vertical_photos = [photo for photo in photos if photo.orientation == "V"]

        slides = []

        # Compose horizontal slides in order
        for photo in horizontal_photos:
            slides.append(Slide.create_horizontal(photo))

        # Compose vertical slides of pairs in order
        for i in range(0, len(vertical_photos), 2):
            slides.append(
                Slide.create_vertical(vertical_photos[i], vertical_photos[i + 1]))

        return slides
