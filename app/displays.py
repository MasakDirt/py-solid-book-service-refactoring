from abc import ABC, abstractmethod


class Display(ABC):
    @staticmethod
    @abstractmethod
    def display(content: str) -> None:
        pass


class ConsoleDisplay(Display):
    @staticmethod
    def display(content: str) -> None:
        print(content)


class ReverseDisplay(Display):
    @staticmethod
    def display(content: str) -> None:
        print(content[::-1])


class DisplayCMD:
    __DISPLAY_TPES = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }

    @classmethod
    def display(cls, display_type: str, book: object) -> None:
        display_cls = cls.__DISPLAY_TPES.get(display_type)
        if display_cls:
            return display_cls.display(book.content)
        else:
            raise ValueError(f"Unknown display type: {display_type}")
