# If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# In one line of code, add two new users to the user_ids dictionary:
# theLooper, with an id of 138475
# stringQueen, with an id of 85739

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)
