from typing import List, Tuple


def format_date(day: int, month: int, year: int) -> str:
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    if month < 1 or month > 12:
        raise Exception(f"The given date: {day}, {month}, {year} is invalid")
    days_in_month = [31, 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month - 1]:
        raise Exception(f"The given date: {day}, {month}, {year} is invalid")
    
    return f"{str(day).zfill(2)} {months[month - 1]}, {year}"


def check_palindrome_tuples(tups: List[Tuple[str, str]]) -> bool:
    if not isinstance(tups, list) or not all(isinstance(t, tuple) and len(t) == 2 for t in tups):
        raise Exception("Invalid Input")
    for word1, word2 in tups:
        if not isinstance(word1, str) or not isinstance(word2, str) or len(word1) <= 1 or len(word2) <= 1:
            raise Exception("Invalid Input")
        if word1 != word2[::-1]:
            return False
    
    return True


def join_by_delimiter(substrings: List[str], delimiter: str) -> str:
    if not isinstance(substrings, list) or not all(isinstance(s, str) for s in substrings):
        raise Exception("Invalid Input")
    if not isinstance(delimiter, str):
        raise Exception("Invalid Input")
    if len(substrings) == 0:
        return ""
    
    return delimiter.join(substrings)
