from guac.models import Photo


class Reader:

    @staticmethod
    def read(file_name):
        """
        Open the file with the supplied path, read its contents into an array of
        strings, and return them. Newline characters are discarded.

        :param file_name: the filename (including path) of the file to be read
        :return: a list of strings, one for each line of the file
        """

        file = open(file_name, "r")
        return [line[:-1] for line in file]

    @staticmethod
    def tabulate(lines):
        """
        Convert raw input (list of lines of a file) into Photo objects.

        :param lines: a list of strings representing the lines of an input file
        :return: a list of Photos
        """

        photos = []

        for counter, line in enumerate(lines[1:]):
            entries = line.split(" ")
            orientation = entries[0]
            tags = [entry for entry in entries[2:]]
            photos.append(Photo(counter, orientation, tags))

        return photos
