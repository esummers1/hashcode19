import os


class Writer:

    @staticmethod
    def write(file_name, slides):
        """
        Write a solution (i.e. the contents of a Slideshow) to a file.

        :param file_name: the filename, including path
        :param slides: the slides to be written
        """

        # Create output directory, if it does not exist
        directory = os.path.dirname(file_name)
        if not os.path.exists(directory):
            os.mkdir(directory)
        else:
            # If a file with the target name exists, delete it
            Writer.delete(file_name)

        # Create output file
        output_file = open(file_name, "x")

        # Write number of slides
        output_file.write(str(len(slides)) + "\n")

        # Write out slides by Photo Id
        for slide in slides:
            output_file.write((" ".join([str(photo.photo_id) for photo in slide.photos])) + "\n")


    @staticmethod
    def delete(file_name):
        """
        Check if a file exists, and delete it if so.

        :param file_name: the filename, including path
        """

        if os.path.exists(file_name):
            os.remove(file_name)
