rooms = ["Deluxe", "Suite", "Standard", "Executive"]

def search_room(query):
    results = [room for room in rooms if query.lower() in room.lower()]
    if results:
        print("Available rooms:", results)
    else:
        print("No rooms found.")

# Example usage
if __name__ == "__main__":
    search_room("Suite")
