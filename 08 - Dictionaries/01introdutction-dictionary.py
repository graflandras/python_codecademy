# A dictionary is an unordered set of key: value pairs.

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

# Dictionaries in Python rely on each key having a hash value, a specific identifier
# for the key. If the key can change, that hash value would not be reliable.
# So the keys must always be unchangeable, hashable data types, like numbers or strings.
