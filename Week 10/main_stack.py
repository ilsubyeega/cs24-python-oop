from stack import Stack

stack = Stack()

for alphabet in range(6):
    stack.push(chr(97 + alphabet))

print(f'Pop: {stack.pop()}')
print(f'Peek: {stack.peek()}')
print(f'Size: {stack.get_size()}')

stack.show()
