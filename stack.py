# Stack implementation in python

def create_stack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    print(f"Pushed {item} onto stack. Current stack: {stack}")

def check_empty(stack):
    is_empty = len(stack) == 0
    if(is_empty) :
        print(f"Stack is empty: {is_empty}")
    return is_empty

def pop(stack):
    if check_empty(stack):
        print("Stack is empty. Cannot pop.")
        return None
    item = stack.pop()
    print(f"Popped {item} from stack. Current stack: {stack}")
    return item

stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))