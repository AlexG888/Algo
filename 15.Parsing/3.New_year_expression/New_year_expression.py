from collections import deque
from enum import Enum
import operator


class Lexer:
    def __init__(self, string):
        self.string = string
        self.iter = 0
        self.last_pos = deque()

    def next_token(self):
        current_pos = self.iter
        self.last_pos.append(current_pos)
        if self.iter == len(self.string):
            raise ParseException()
        chars = []
        has_number, has_char = False, False
        while current_pos < len(self.string):
            current_char = self.string[current_pos]
            current_token = Token.parse(current_char)
            is_number = current_token.token_type == TokenType.NUMBER
            is_char = current_token.token_type == TokenType.STRING
            is_not_sym = not is_number and not is_char
            has_number = has_number or is_number
            has_char = has_char or is_char
            if is_not_sym and len(chars) == 0:
                self.iter = current_pos + 1
                return current_token
            elif (
                (is_char and has_number)
                or (is_number and has_char)
                or (is_not_sym and len(chars) > 0)
            ):
                self.iter = current_pos
                chars = "".join(chars)
                if chars in Token.CONST_DICT:
                    return Token(TokenType.NUMBER, Token.CONST_DICT[chars])
                elif chars in Token.FUNC_DICT:
                    return Token(TokenType.FUNCTIONS, chars, Token.FUNC_DICT[chars])
                try:
                    return Token(TokenType.NUMBER, int(chars))
                except:
                    raise ParseException()
            elif not is_not_sym:
                current_pos += 1
                chars.append(current_char)
            else:
                raise ParseException()
        self.iter = current_pos
        return Token.parse("".join(chars))


class ParseException(Exception):
    pass


class TokenType(Enum):
    NUMBER = 0
    OPERATOR = 1
    BRACKET = 2
    STRING = 3
    FUNCTIONS = 4
    END = 5


class Podarok:
    def __init__(self, name, op):
        self.name = name
        self.op = op

    def __call__(self, *args, **kwargs):
        return self.op(*args, **kwargs)


class Token:
    CONST_DICT = {"Ded Moroz": 2020, "Moroz": -30, "Snegurochka": 10}
    FUNC_DICT = {
        func.name: func
        for func in [Podarok("Podarok", lambda x: x + 5 if x > 0 else abs(x))]
    }
    OP_DICT = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    BRACKETS = {"(", ")"}
    LAST_SYMBOL = "."

    def __init__(self, token_type: TokenType, value, op=None):
        self.token_type = token_type
        self.value = value
        self.op = op

    def parse(value):
        if value == Token.LAST_SYMBOL:
            return Token(TokenType.END, value)
        elif value in Token.BRACKETS:
            return Token(TokenType.BRACKET, value)
        elif value in Token.OP_DICT:
            return Token(TokenType.OPERATOR, value, Token.OP_DICT[value])
        try:
            return Token(TokenType.NUMBER, int(value))
        except ValueError:
            return Token(TokenType.STRING, value)


class Parser:
    def __init__(self, string):
        self.lexer = Lexer(string)

    def parse(self):
        expr = self.addit()
        if self.lexer.next_token().token_type != TokenType.END:
            raise ParseException()
        return expr.__dict__["value"]

    def operand(self):
        token = self.lexer.next_token()
        if token.value == "(":
            result = self.addit()
            second_token = self.lexer.next_token()
            if second_token.value != ")":
                raise ParseException()
            return result
        elif token.token_type == TokenType.NUMBER:
            return Token(TokenType.NUMBER, token.value)
        elif token.token_type == TokenType.FUNCTIONS:
            return self.func(token)
        raise ParseException()

    def mult(self):
        first = self.operand()
        while self.lexer.iter != len(self.lexer.string):
            op = self.lexer.next_token()
            if op.value != "*":
                self.lexer.iter = self.lexer.last_pos.pop()
                break
            second = self.operand()
            first = Token(TokenType.NUMBER, op.op(first.value, second.value))
        return first

    def addit(self):
        first_operand = self.mult()
        while self.lexer.iter != len(self.lexer.string):
            op = self.lexer.next_token()
            if op.value not in {"+", "-"}:
                self.lexer.iter = self.lexer.last_pos.pop()
                break
            second_operand = self.mult()
            first_operand = Token(
                TokenType.NUMBER, op.op(first_operand.value, second_operand.value)
            )
        return first_operand

    def func(self, func_token):
        open_bracket = self.lexer.next_token()
        if open_bracket.value != "(":
            raise ParseException()
        arg = self.addit()
        close_bracket = self.lexer.next_token()
        if close_bracket.value != ")":
            raise ParseException()
        return Token(TokenType.NUMBER, func_token.op(arg.value))


if __name__ == "__main__":
    s = input()
    parser = Parser(s)
    try:
        print(parser.parse())
    except ParseException:
        print("WRONG")

# Podarok(Moroz-Ded Moroz)*2.
#
# 4100

# Snegurochka-30.
# 
# -20

