# Hotel Booking System

rooms = {
    101: {"type": "Single", "price": 1500, "status": "Available"},
    102: {"type": "Single", "price": 1500, "status": "Available"},
    201: {"type": "Double", "price": 2500, "status": "Available"},
    202: {"type": "Double", "price": 2500, "status": "Available"},
    301: {"type": "Deluxe", "price": 4000, "status": "Available"}
}

bookings = {}


def view_rooms():
    print("\n===== AVAILABLE ROOMS =====")

    for room_no, room in rooms.items():
        print(
            "Room:", room_no,
            "| Type:", room["type"],
            "| Price: Rs.", room["price"],
            "| Status:", room["status"]
        )


def book_room():
    print("\n===== BOOK A ROOM =====")

    try:
        room_no = int(input("Enter room number: "))

        if room_no not in rooms:
            print("Invalid room number.")
            return

        if rooms[room_no]["status"] == "Booked":
            print("Sorry, this room is already booked.")
            return

        name = input("Enter guest name: ")
        age = int(input("Enter guest age: "))
        phone = input("Enter phone number: ")
        nights = int(input("Enter number of nights: "))

        if nights <= 0:
            print("Number of nights must be greater than 0.")
            return

        total = rooms[room_no]["price"] * nights

        bookings[room_no] = {
            "name": name,
            "age": age,
            "phone": phone,
            "nights": nights,
            "total": total
        }

        rooms[room_no]["status"] = "Booked"

        print("\n===== BOOKING SUCCESSFUL =====")
        print("Guest Name:", name)
        print("Room Number:", room_no)
        print("Room Type:", rooms[room_no]["type"])
        print("Number of Nights:", nights)
        print("Total Amount: Rs.", total)

    except ValueError:
        print("Please enter valid information.")


def cancel_booking():
    print("\n===== CANCEL BOOKING =====")

    try:
        room_no = int(input("Enter room number: "))

        if room_no not in rooms:
            print("Invalid room number.")
            return

        if room_no not in bookings:
            print("No booking found for this room.")
            return

        guest = bookings[room_no]

        print("Guest Name:", guest["name"])

        confirm = input("Do you want to cancel this booking? (yes/no): ")

        if confirm.lower() == "yes":
            del bookings[room_no]
            rooms[room_no]["status"] = "Available"
            print("Booking cancelled successfully.")
        else:
            print("Booking was not cancelled.")

    except ValueError:
        print("Please enter a valid room number.")


def view_bookings():
    print("\n===== ALL BOOKINGS =====")

    if len(bookings) == 0:
        print("No bookings available.")
        return

    for room_no, guest in bookings.items():
        print("\nRoom Number:", room_no)
        print("Guest Name:", guest["name"])
        print("Age:", guest["age"])
        print("Phone:", guest["phone"])
        print("Nights:", guest["nights"])
        print("Total Amount: Rs.", guest["total"])


def checkout():
    print("\n===== CHECKOUT =====")

    try:
        room_no = int(input("Enter room number: "))

        if room_no not in bookings:
            print("No active booking found.")
            return

        guest = bookings[room_no]

        print("\nGuest Name:", guest["name"])
        print("Room Number:", room_no)
        print("Total Bill: Rs.", guest["total"])

        confirm = input("Confirm checkout? (yes/no): ")

        if confirm.lower() == "yes":
            del bookings[room_no]
            rooms[room_no]["status"] = "Available"
            print("Checkout completed successfully.")
        else:
            print("Checkout cancelled.")

    except ValueError:
        print("Please enter a valid room number.")


def main():
    while True:

        print("\n================================")
        print("       HOTEL BOOKING SYSTEM")
        print("================================")
        print("1. View Rooms")
        print("2. Book a Room")
        print("3. Cancel Booking")
        print("4. View Bookings")
        print("5. Checkout")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_rooms()

        elif choice == "2":
            book_room()

        elif choice == "3":
            cancel_booking()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("\nThank you for using the Hotel Booking System!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
