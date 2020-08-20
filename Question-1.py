import sys



class Bracket:
    def __init__(self, type, position):
        self.type = type
        self.position = position

    def Match(self, c):
        if self.type == '(' and c == ')':
            return True
        if self.type == '[' and c == ']':
            return True
        if self.type == '{' and c == '}':
            return True
        return False


if __name__ == '__main__':
    entered_text = input()
    Main_stack = []

    for i, next in enumerate(entered_text):
        if next == '(' or next == '[' or next == '{':
            Main_stack.append(Bracket(next, i))
        if next == ')' or next == ']' or next == '}':
            if len(Main_stack) <= 0:
                print(i + 1)
                sys.exit()
            item = Main_stack.pop()
            if not item.Match(next):
                print(i + 1)
                sys.exit()

    if len(Main_stack) == 0:
        print("Success")
    else:
        print(Main_stack.pop().position + 1)