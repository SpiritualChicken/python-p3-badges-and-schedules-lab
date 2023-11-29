def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    list_of_names = []
    for name in names:
        list_of_names.append(badge_maker(name))
    return list_of_names
    

def assign_rooms(names):
    welcome_messages = []
    room = 1 
    for name in names: 
        welcome_messages.append(f"Hello, {name}! You'll be assigned to room {room}!")
        room += 1
    return(welcome_messages) 

def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)

    for badge in badges:
        print(badge)

    for room in rooms:
        print(room)


print(printer(["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]))