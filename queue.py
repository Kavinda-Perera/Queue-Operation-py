MAX_SIZE = 100
queue = [-1] * MAX_SIZE
front = -1
rear = -1

def enqueue(value):
    global front, rear
    if rear == MAX_SIZE - 1:
        print("Error: Queue is full")
        return
    if front == -1:
        front = 0
    rear += 1
    queue[rear] = value

def dequeue():
    global front, rear
    if front == -1:
        print("Error: Queue is empty")
        return
    front += 1
    if front > rear:
        front = rear = -1

def front_value():
    if front == -1:
        print("Error: Queue is empty")
        return -1
    return queue[front]

def rear_value():
    if rear == -1:
        print("Error: Queue is empty")
        return -1
    return queue[rear]

def display():
    if front == -1:
        print("Queue is empty")
        return
    print("Queue elements: ", end="")
    for i in range(front, rear + 1):
        print(queue[i], end=" ")
    print()

while True:
    print("\n-- Queue Operations --")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front value")
    print("4. Rear value")
    print("5. Display queue")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter the value to be enqueued: "))
        enqueue(value)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        print("Front value:", front_value())
    elif choice == 4:
        print("Rear value:", rear_value())
    elif choice == 5:
        display()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
