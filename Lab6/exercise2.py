import circular_queue
capacity = 3
normal_line = circular_queue.CircularQueue(capacity)
VIP_line = circular_queue.CircularQueue(capacity)
user_choice = input("Add, Serve, or Exit: ").lower()
while user_choice != "exit":
    if user_choice == "add":
        name = input("Enter the name of the person to add: ")
        status = input('Is the customer VIP?')
        if status == 'False':
            if normal_line.isFull():
                print("Error: Normal customers queue is full")
            else:
                normal_line.enqueue(name)
                print('add '+ name+' to the line.')
        elif status == 'true':
            if VIP_line.isFull():
                print("Error: VIP customers queue is full")
            else:
                VIP_line.enqueue(name)
                print('add '+ name+' to VIP line.')
    elif user_choice == "serve":
        if VIP_line.isEmpty() and normal_line.isEmpty():
            print("Error: Queues are empty.")
        elif VIP_line.isEmpty():
            print(noraml_line.dequeue(), "has been served.")
        else:
            print(VIP_line.dequeue(), "has been served.")
    print('people in the line:', normal_line)
    print('VIP customers queue:', VIP_line)
    user_choice = input("Add, Serve, or Exit: ")
print('Quitting')