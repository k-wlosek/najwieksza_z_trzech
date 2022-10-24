from typing import Tuple, List


class MaxFinder:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        # self.greatest_of_three()

    def got_helper(self) -> tuple[str, list[int]]:
        """
        Helper function to greatest of three, checks which number is the greatest, assuming none are equal
        """
        if self.a < self.b:
            # b max so far
            if self.c < self.b:
                # b is max
                return "b", [self.b]
            else:
                return "c", [self.c]
        else:
            if self.c < self.a:
                return "a", [self.a]
            else:
                return "c", [self.c]

    def greatest_of_three(self) -> tuple[str, list[int]]:
        """
        Checks for equal numbers and calls got_helper for getting the biggest one
        If multiple are the biggest, handles communicating that to user
        """
        if self.a == self.b == self.c:
            return "a, b i c", [self.a, self.b, self.c]
        else:
            if self.a == self.b:
                if self.got_helper()[0] == "c":
                    return "c", [self.c]
                else:
                    return "a i b", [self.a, self.b]
            else:
                if self.a == self.c:
                    if self.got_helper()[0] == "b":
                        return "b", [self.b]
                    else:
                        return "a i c", [self.a, self.c]
                else:
                    if self.c == self.b:
                        if self.got_helper()[0] == "a":
                            return "a", [self.a, self.c]
                        else:
                            return "b i c", [self.b, self.c]
                    else:
                        # All numbers are not equal, call got_helper to determine which is the greatest
                        return self.got_helper()


# def got_helper(a: int, b: int, c: int) -> str:
#     """
#     Helper function to greatest of three, checks which number is the greatest, assuming none are equal
#     """
#     if a < b:
#         # b max so far
#         if c < b:
#             # b is max
#             return "b"
#         else:
#             return "c"
#     else:
#         if c < a:
#             return "a"
#         else:
#             return "c"
#
#
# def greatest_of_three(a: int, b: int, c: int) -> None:
#     """
#     Checks for equal numbers and calls got_helper for getting the biggest one
#     If multiple are the biggest, handles communicating that to user
#     """
#     if a == b == c:
#         print("a, b i c są największe, więc żadna liczba nie jest największa")
#     else:
#         if a == b:
#             if got_helper(a, b, c) == "c":
#                 print("c jest największe")
#             else:
#                 print("a i b są największe")
#         else:
#             if a == c:
#                 if got_helper(a, b, c) == "b":
#                     print("b jest największe")
#                 else:
#                     print("a i c są największe")
#             else:
#                 if c == b:
#                     if got_helper(a, b, c) == "a":
#                         print("a jest największe")
#                     else:
#                         print("b i c są największe")
#                 else:
#                     # All numbers are not equal, call got_helper to determine which is the greatest
#                     print(f'{got_helper(a, b, c)} jest największe')


def the_checker(number_list: list[int]) -> tuple[str, str, int]:
    """
    Finds the greatest number of all given (or multiple, if applicable)
    :param number_list: how many numbers you want in int in a list (if too many, will probably break because ASCII)
    :return: tuple of a letter(s), number(s) and the biggest value
    """
    mx = max(number_list)
    indices_chr = []
    indices_no = []
    for index, element in enumerate(number_list):
        if element == mx:
            # To print out all NUMBERS of numbers, ex. 1,2,3,4,4 will return "4, 5", as fourth number is the biggest
            indices_no.append(str(index + 1))
            # Prints out characters with regard to alphabet in ASCII using chr() (inverse of ord())
            # 96 is there, as 97 is a in ASCII and + 1 is left to remain similar to solution with numbers
            indices_chr.append(chr(index + 1 + 96))
    return ', '.join(indices_chr), ', '.join(indices_no), mx


if __name__ == '__main__':
    # print(the_checker(1,3,2,4,2,4,6,-3,4,5,3,64,8,43,7,4,8,4,73,5,8,35,7,3,57,86))
    # raise SystemExit
    print("Program znajduje największą liczbę spośród 3 podanych, obsługuje jedynie liczby całkowite w systemie "
          "dziesiętnym")

    print("Czy chcesz podać więcej niż 3 liczby (ale dalej spełniające wymogi)?")
    answer = input("y/n\n")
    if answer == "n" or "\n":
        try:
            a = int(input("Podaj liczbę a: "))
            b = int(input("Podaj liczbę b: "))
            c = int(input("Podaj liczbę c: "))
        except ValueError as e:
            print(f"Jedna z podanych liczb nie jest liczbą lub nie została zamieniona w typ int,\nerr: {e}")
            raise SystemExit(1)
        # greatest_of_three(a, b, c)
        ob = MaxFinder(a, b, c)
        letter, values = ob.greatest_of_three()
        # print(letter, values[0])
        print(f"Największa wartość ma literę {letter}, jej wartość to {values[0]}" if len(values) == 1
              else f"Największe wartości mają litery {letter}, o wartościach równych {values[0]}")
    else:
        if answer != "y":
            print("Nieprawidłowa odpowiedź")
            raise SystemExit
        else:
            space_sep_no = input("Wprowadzaj liczby w formacie 'x y z'\nPrzykład: 1 2 3 4 5 12 54\n")
            no_list = [int(el) for el in list(space_sep_no.split(" "))]
            letter, index, val = the_checker(no_list)
            print(f"Największa wartość ma literę {letter}, jej numer porządkowy to {index}, jej wartość to {val}"
                  if "," not in letter else
                  f"Największe wartości mają litery {letter}, ich numery porządkowe to {index}, o wartościach równych {val}")
