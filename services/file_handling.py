import sys
import os
import re

BOOK_PATH = '../book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    temp = text[start:start + size].rstrip()
    try:
        if text[start + size - 1] in ',.!:;?' and text[start + size] in ',.!:;?':
            temp = text[start:start + size - 1].rstrip(',.!:;?')

        part = re.search(r'^.+[,.!:;?]', temp, re.DOTALL)
        return part.group(0), part.end()

    except (AttributeError, IndexError):
        return temp, len(temp)



def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        file_text = f.read()
        start, page_number = 0, 1

        while start < len(file_text):
            page, page_size = _get_part_text(file_text, start, PAGE_SIZE)
            start += page_size
            book[page_number] = page.strip()
            page_number += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))

