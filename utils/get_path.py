import os


def get_path():
    path = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
    return path
