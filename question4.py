import sys


class Stackoperations():
    def __init__(self):
        self.primarystack = []
        self.secondarystack = []

    def push(self, a):
        self.primarystack.append(a)
        if len(self.secondarystack) == 0:
            self.secondarystack.append(a)
        elif a >= self.filterfunc():
            self.secondarystack.append(a)

    def filterfunc(self):
        assert(len(self.primarystack))
        return self.secondarystack[-1]

    def pop(self):
        assert(len(self.primarystack))
        if self.primarystack.pop() == self.filterfunc():
            self.secondarystack.pop()
        
    def max(self):
        assert(len(self.primarystack))
        return self.filterfunc()


if __name__ == '__main__':
    stack = Stackoperations()

    num_queries = int(sys.stdin.readline())
    for i in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert 0