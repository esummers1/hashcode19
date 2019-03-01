from guac.controller import Controller
from guac.strategies import DumbStrategy


if __name__ == "__main__":

    # List of input files to take - modify if desired
    files = [
        "a_example",
        "b_lovely_landscapes",
        "c_memorable_moments",
        "d_pet_pictures",
        "e_shiny_selfies"
    ]

    # List of Strategies to run - modify if desired
    strategies = [
        DumbStrategy()
    ]

    controller = Controller(files, strategies)
    controller.run()
