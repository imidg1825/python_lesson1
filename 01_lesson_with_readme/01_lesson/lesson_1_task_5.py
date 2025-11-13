"""Task 5: parameterized function; print 88005553535 using 11 calls."""

def print_piece(num: str) -> None:
    """Печатает переданный фрагмент без переноса строки."""
    print(num, end="")

if __name__ == "__main__":
    target = "88005553535"  # 11 символов
    for ch in target:
        print_piece(ch)
    print()  # финальный перевод строки
