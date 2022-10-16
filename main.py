
class MaxFinder:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.greatest_of_three()

    def got_helper(self) -> str:
        """
        Helper function to greatest of three, checks which number is the greatest, assuming none are equal
        """
        if self.a < self.b:
            # b max so far
            if self.c < self.b:
                # b is max
                return "b"
            else:
                return "c"
        else:
            if self.c < self.a:
                return "a"
            else:
                return "c"

    def greatest_of_three(self) -> None:
        """
        Checks for equal numbers and calls got_helper for getting the biggest one
        If multiple are the biggest, handles communicating that to user
        """
        if self.a == self.b == self.c:
            print("a, b i c są największe, więc żadna liczba nie jest największa")
        else:
            if self.a == self.b:
                if self.got_helper() == "c":
                    print("c jest największe")
                else:
                    print("a i b są największe")
            else:
                if self.a == self.c:
                    if self.got_helper() == "b":
                        print("b jest największe")
                    else:
                        print("a i c są największe")
                else:
                    if self.c == self.b:
                        if self.got_helper() == "a":
                            print("a jest największe")
                        else:
                            print("b i c są największe")
                    else:
                        # All numbers are not equal, call got_helper to determine which is the greatest
                        print(f'{self.got_helper()} jest największe')


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


def the_checker(*args: int):
    """
    Finds the greatest number of all given (or multiple, if applicable)
    :param args: how many numbers you want in int (if too many, will probably break because ASCII)
    :return: str, self-explanatory
    """
    arr = list(args)
    mx = max(arr)
    indices = []
    for index, element in enumerate(arr):
        if element == mx:
            # To print out all NUMBERS of numbers, ex. 1,2,3,4,4 will return "4, 5", as fourth number is the biggest
            #indices.append(str(index + 1))
    # return f"Największe liczby to te o numerach {', '.join(indices)} (z kolejności wpisywania)"
            # Prints out characters with regard to alphabet in ASCII using chr() (inverse of ord())
            # 96 is there, as 97 is a in ASCII and + 1 is left to remain similar to solution with numbers
            indices.append(chr(index + 1 + 96))
    return f"Największe liczby to te o literach {', '.join(indices)} (z kolejności wpisywania)"


if __name__ == '__main__':
    # print(the_checker(1,3,2,4,2,4,6,-3,4,5,3,64,8,43,7,4,8,4,73,5,8,35,7,3,57,86))
    # raise SystemExit
    print("Program znajduje największą liczbę spośród 3 podanych, obsługuje jedynie liczby całkowite w systemie "
          "dziesiętnym")
    try:
        a = int(input("Podaj liczbę a: "))
        b = int(input("Podaj liczbę b: "))
        c = int(input("Podaj liczbę c: "))
    except ValueError as e:
        print(f"Jedna z podanych liczb nie jest liczbą lub nie została zamieniona w typ int,\nerr: {e}")
        raise SystemExit(1)
    # greatest_of_three(a, b, c)
    MaxFinder(a, b, c)
