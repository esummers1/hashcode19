class Slideshow:
    def __init__(self, slides, score, strategy):
        self.slides = slides
        self.score = score
        self.strategy = strategy


class Slide:
    def __init__(self, photos, tags):
        self.photos = photos
        self.tags = tags

    @staticmethod
    def create_horizontal(photo):
        return Slide([photo], photo.tags)

    @staticmethod
    def create_vertical(photo1, photo2):
        tags = [tag for tag in photo1.tags] + [tag for tag in photo2.tags]
        return Slide([photo1, photo2], tags)


class Photo:
    def __init__(self, photo_id, orientation, tags):
        self.photo_id = photo_id
        self.orientation = orientation
        self.tags = tags
