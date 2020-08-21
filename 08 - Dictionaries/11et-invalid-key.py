# One way to avoid keyError is to first check if the key exists in the dictionary:

# key_to_check = "Landmark 81"
# if key_to_check in dictionary:
#   do some things with key

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601,
                    "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights["Landmark 81"])
