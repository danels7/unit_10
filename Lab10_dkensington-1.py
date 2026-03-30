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
    
    def print_report(self) -> None:
        sorted_keys = sorted(self.__words.keys())
        longest = len(max(sorted_keys, key=len))
        for key in sorted_keys:
            print(f"{key:<{longest}}  :: {self.__words[key]}")


def print_menu() -> None:
    print("--- Word Analyzer ---")
    print("Choose a file to analyze:")
    print("1. Monte Cristo")
    print("2. Princess Mars")
    print("3. Tarzan")
    print("4. Treasure Island")


def get_input() -> int:
    inp = input("> ")
    while True:
        try:
            num = int(inp)
        except ValueError:
            print("Enter a number 1-5")
            continue
        if num < 1 or num > 5:
            print("Enter a number 1-5")
            continue
        return num


def main():
    paths = {
        1: "monte_cristo.txt",
        2: "princess_mars.txt",
        3: "Tarzan.txt",
        4: "treasure_island.txt"
    }

    inp = 0
    while inp != 5:
        print_menu()
        inp = get_input()
        path = paths[inp]

        print(f"Processing {path}...")

        analyzer = WordAnalyzer(path)
        analyzer.process_file()
        analyzer.print_report()

    print("Goodbye!")


if __name__ == "__main__":
    main()