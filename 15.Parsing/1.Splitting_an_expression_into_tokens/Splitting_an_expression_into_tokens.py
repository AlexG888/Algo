DIGITS = "0123456789"
OPERATORS = "+-*()"
LAST_SYMBOL = "."
ALL_SYMBOLS = DIGITS + OPERATORS + LAST_SYMBOL


class Lexer:
    def __init__(self, string):
        self.string = string
        self.iter = 0
        self.ended = False

    def next_token(self):
        token = ""
        element = self.string[self.iter]
        if element in OPERATORS:
            token = element
        elif element == LAST_SYMBOL:
            self.ended = True
        else:
            while element in DIGITS:
                token += element
                self.iter += 1
                element = self.string[self.iter]
            self.iter -= 1
        self.iter += 1
        return token


if __name__ == "__main__":
    s = input()
    lexer = Lexer(s)
    while not lexer.ended:
        print(lexer.next_token())


# 1+(2*2-3).
#
# 1
# +
# (
# 2
# *
# 2
# -
# 3
# )