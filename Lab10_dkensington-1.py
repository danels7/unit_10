import pathlib, string

class WordAnalyzer:
    def __init__(self, filepath: str):
        self.__path: pathlib.Path = pathlib.Path(filepath)
        self.__words: dict[str, int] = dict()
    
    def process_file(self) -> bool:
        if self.__path.exists():
            try:
                file = self.__path.open()
            except FileNotFoundError:
                return False
        else:
            return False
        
        content = file.read()
        file.close()
        lines = content.splitlines()
        transtable = str.maketrans("", "", string.punctuation)
        for line in lines:
            formatted = line.translate(transtable).lower()
            words = formatted.split()
            for word in words:
                if word in self.__words.keys():
                    self.__words[word] += 1
                else:
                    self.__words[word] = 1

        return True