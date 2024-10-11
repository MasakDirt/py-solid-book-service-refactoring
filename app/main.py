from app.displays import DisplayMixin
from app.prints import PrintMixin
from app.serializers import SerializeMixin


class Book(SerializeMixin, PrintMixin, DisplayMixin):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("print", "no_space"),
                ("serialize", "xml")
            ]
        )
    )
