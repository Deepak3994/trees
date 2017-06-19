# python3
import sys
import stack           

class Bracket:

    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read(10)

    s = stack.Stack()
    b = Bracket(0,0)

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            s.push(next)
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            a = s.pop(next)
            if a == next:
                print("Success!!!")
                pass
            else:
                #print("Error at index "+i".Found"+next"instead of"+s.pop(next)".")
                print("Error")

    # Printing answer, write your code here
