number_of_room = int(input("Enter the number of rooms: "))

room_number = 0
booked_room = 0
available_room = 0

standard = 0
deluxe = 0
suite = 0

rooms = []     

for i in range(1, number_of_room + 1):

    room_number = int(input("Enter the room number: "))
    room_type = input("Enter standard/deluxe/suite: ").upper()
    booking_status = input("Enter the room booked or available: ").upper()

    rooms.append([room_number, room_type, booking_status])  

    if booking_status == "BOOKED":
        booked_room += 1
    elif booking_status == "AVAILABLE":
        available_room += 1

    if room_type == "STANDARD":
        standard += 1
    elif room_type == "DELUXE":
        deluxe += 1
    elif room_type == "SUITE":
        suite += 1


if standard >= deluxe and standard >= suite:
    print("Most Booked Room Type: STANDARD")
elif deluxe >= standard and deluxe >= suite:
    print("Most Booked Room Type: DELUXE")
else:
    print("Most Booked Room Type: SUITE")


print("\n------------- HOTEL REPORT -------------")

for room in rooms:                 
    print("Room Number:", room[0])
    print("Room Type:", room[1])
    print("Status:", room[2])
    print()

print("----------------------------------------")
print("Total Rooms:", number_of_room)
print("Booked Rooms:", booked_room)
print("Available Rooms:", available_room)

print("Standard Room:", standard)
print("Deluxe Room:", deluxe)
print("Suite Room:", suite)