import pathlib

class WordAnalyzer:
    def __init__(self, filepath: str):
        self.__path: pathlib.Path = pathlib.Path(filepath)
        self.__words: dict[str, int] = dict()