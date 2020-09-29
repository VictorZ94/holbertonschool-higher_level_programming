class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # YYYYMMDD
        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        last_name = name_pieces[-1]

user1 = User("Dave Bowman", "19900520")
print(user1.name)
print(user1.birthday)


