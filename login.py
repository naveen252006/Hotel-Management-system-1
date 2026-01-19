def login(username, password):
    if username == "admin" and password == "admin123":
        print("Login successful!")
    else:
        print("Invalid credentials.")
# Example usage
if __name__ == "__main__":
    login("admin", "admin123")