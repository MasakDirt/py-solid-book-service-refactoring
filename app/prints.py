from abc import ABC, abstractmethod


class Print(ABC):
    @staticmethod
    @abstractmethod
    def print_content(title: str, content: str) -> None:
        pass


class ConsolePrint(Print):
    @staticmethod
    def print_content(title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrint(Print):
    @staticmethod
    def print_content(title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class UpperCasePrint(Print):
    @staticmethod
    def print_content(title: str, content: str) -> None:
        print(f"Printing the book in upper case: {title}...")
        print(content.upper())


class LowerCasePrint(Print):
    @staticmethod
    def print_content(title: str, content: str) -> None:
        print(f"Printing the book in lower case: {title}...")
        print(content.lower())


class NoSpacesPrint(Print):
    @staticmethod
    def print_content(title: str, content: str) -> None:
        print(f"Printing the book in lower case: {title}...")
        print("".join(char for char in content.split()))


class PrintMixin:
    __PRINT_TYPES = {
        "console": ConsolePrint,
        "reverse": ReversePrint,
        "upper": UpperCasePrint,
        "lower": LowerCasePrint,
        "no_space": NoSpacesPrint,
    }

    def print_book(self, print_type: str) -> None:
        printer = self.__PRINT_TYPES.get(print_type)
        if printer:
            printer.print_content(self.title, self.content)
        else:
            raise ValueError(f"Unknown print type: {print_type}")
