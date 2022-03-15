OPERATORS = "+-*()"
LAST_SYMBOL = "."
ALL_SYMBOLS = OPERATORS + LAST_SYMBOL


class Lexer:
    def __init__(self, string):
        self.string = string
        self.iter = 0
        self.ended = False

    def next_token(self):
        token = ""
        element = self.string[self.iter]
        if (element not in ALL_SYMBOLS) and (not element.isdigit()):
            raise ValueError()
        else:
            if element in OPERATORS:
                token = element
            elif element == LAST_SYMBOL:
                self.ended = True
            else:
                while element.isdigit():
                    token += element
                    self.iter += 1
                    element = self.string[self.iter]
                self.iter -= 1
            self.iter += 1
            return token


class Parser:
    def __init__(self, string):
        self.lexer = Lexer(string)
        self.iter = self.lexer.iter

    def get_tokens(self):
        all_tokens = []
        while not self.lexer.ended:
            all_tokens.append(self.lexer.next_token())
        return all_tokens

    def parse(self):
        self.tokens = self.get_tokens()
        self.size = len(self.tokens)
        expr = self.expr()
        if self.iter != self.size - 1:
            raise ValueError()
        return expr

    def expr(self):
        first_part = self.get_part()
        while self.iter < self.size:
            if self.tokens[self.iter] == "+":
                self.iter += 1
                second_part = self.get_part()
                first_part += second_part
            elif self.tokens[self.iter] == "-":
                self.iter += 1
                second_part = self.get_part()
                first_part -= second_part
            else:
                break
        return first_part

    def get_part(self):
        part = self.mult()
        while self.iter < self.size:
            if self.tokens[self.iter] == "*":
                self.iter += 1
                part *= self.mult()
            else:
                break
        return part

    def mult(self):
        next_token = self.tokens[self.iter]
        if next_token == "(":
            self.iter += 1
            result = self.expr()
            if self.iter < self.size:
                expected_bracket = self.tokens[self.iter]
            else:
                raise ValueError()
            if self.iter < self.size and expected_bracket == ")":
                self.iter += 1
                return result
            raise ValueError()
        self.iter += 1
        return int(next_token)


if __name__ == "__main__":
    s = input()
    parser = Parser(s)
    try:
        print(parser.parse())
    except ValueError:
        print("WRONG")


# 1+(2*2-3).
#
# 2

# 1+a+1.
#
# WRONG
