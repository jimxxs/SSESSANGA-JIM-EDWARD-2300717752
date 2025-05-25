print("Ssessanga Jim Edward\n")
print("2300717752\n")
print("23/U/17752/EVE\n")
print("Python Individual Assignment One\n") 
#

####################################
# Exercise 1: Lists
####################################

print("EXERCISE 1: LISTS\n")

# 1. Create a list with 5 items (names of people) and output the 2nd item
names = ["John", "Mary", "David", "Sarah", "Michael"]
print("1. Second item in the list:", names[1])

# 2. Change the value of the first item to a new value
names[0] = "James"
print("2. List after changing first item:", names)

# 3. Add a sixth item to the list
names.append("Emma")
print("3. List after adding sixth item:", names)

# 4. Add "Bathel" as the 3rd item in your list
names.insert(2, "Bathel")
print("4. List after adding Bathel as 3rd item:", names)

# 5. Remove the 4th item from the list
names.pop(3)
print("5. List after removing 4th item:", names)

# 6. Use negative indexing to print the last item in your list
print("6. Last item using negative indexing:", names[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th, and 5th items
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("7. 3rd, 4th, and 5th items:", days[2:5])

# 8. Write a list of countries and make a copy of it
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = countries.copy()
print("8. Original countries:", countries)
print("   Copied countries:", countries_copy)

# 9. Write a python program to loop through the list of countries
print("9. Looping through countries:")
for country in countries:
    print("   -", country)

# 10. Write a list of animal names and sort them in both descending and ascending order
animals = ["Lion", "Elephant", "Zebra", "Giraffe", "Monkey"]
animals_asc = sorted(animals)
animals_desc = sorted(animals, reverse=True)
print("10. Animals sorted ascending:", animals_asc)
print("    Animals sorted descending:", animals_desc)

# 11. Using the list above, output only animal names with the letter 'a' in them
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("11. Animals with 'a' in their name:", animals_with_a)

# 12. Write two lists, one containing your first names and the other your second names. Join the two lists
first_names = ["John", "Mary", "Robert"]
last_names = ["Doe", "Smith", "Johnson"]
full_names = first_names + last_names
print("12. Joined name lists:", full_names)

####################################
# Exercise 2: Tuples
####################################

print("\nEXERCISE 2: TUPLES\n")

# 1. Consider the tuple below and output your favorite phone brand
x = ("samsung", "iphone", "tecno", "redmi")
print("1. My favorite phone brand:", x[1])  # Assuming iPhone is the favorite

# 2. Use negative indexing to print the 2nd last item in your tuple
print("2. Second last item:", x[-2])

# 3. Update "iphone" to "itel" (convert to list first since tuples are immutable)
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("3. Updated tuple:", x)

# 4. Add "Huawei" to your tuple
x = x + ("Huawei",)
print("4. Tuple after adding Huawei:", x)

# 5. Loop through the tuple
print("5. Looping through the tuple:")
for phone in x:
    print("   -", phone)

# 6. Remove/delete the first item in the tuple
x = x[1:]
print("6. Tuple after removing first item:", x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("7. Cities in Uganda:", cities)

# 8. Unpack the tuple
city1, city2, city3, city4, city5 = cities
print("8. Unpacked cities:", city1, city2, city3, city4, city5)

# 9. Use a range of indexes to print the 2nd, 3rd, and 4th cities
print("9. 2nd, 3rd, and 4th cities:", cities[1:4])

# 10. Join two tuples of first names and second names
first_names_tuple = ("John", "Mary", "Robert")
last_names_tuple = ("Doe", "Smith", "Johnson")
full_names_tuple = first_names_tuple + last_names_tuple
print("10. Joined name tuples:", full_names_tuple)

# 11. Create a tuple of colors and multiply it by 3
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print("11. Colors multiplied by 3:", colors_multiplied)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_8 = thistuple.count(8)
print("12. Number of times 8 appears:", count_of_8)

####################################
# Exercise 3: Sets
####################################

print("\nEXERCISE 3: SETS\n")

# 1. Use the set() constructor to create a set of your favorite beverages
beverages = set(["coffee", "tea", "juice"])
print("1. Favorite beverages:", beverages)

# 2. Add 2 more items to the beverages set
beverages.add("water")
beverages.add("soda")
print("2. Updated beverages set:", beverages)

# 3. Check if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_present = "microwave" in mySet
print("3. Is microwave present in the set?", is_present)

# 4. Remove "kettle" from the set
mySet.remove("kettle")
print("4. Set after removing kettle:", mySet)

# 5. Loop through the set
print("5. Looping through the set:")
for item in mySet:
    print("   -", item)

# 6. Add elements in a list to elements in a set
mySet2 = {"apple", "banana", "cherry", "date"}
myList = ["elderberry", "fig"]
mySet2.update(myList)
print("6. Set after adding list elements:", mySet2)

# 7. Join two sets of ages and first names
ages = {25, 30, 35, 40}
names_set = {"John", "Mary", "David"}
combined_set = ages.union(names_set)
print("7. Joined sets:", combined_set)

####################################
# Exercise 4: Strings
####################################

print("\nEXERCISE 4: STRINGS\n")

# 1. Concatenate an integer and a string
num = 10
text = "years old"
result = str(num) + " " + text
print("1. Concatenated result:", result)

# 2. Remove spaces from the beginning, middle, and end
txt = "      Hello,       Uganda!       "
clean_txt = " ".join(txt.split())
print("2. Text without extra spaces:", clean_txt)

# 3. Convert to uppercase
upper_txt = txt.upper()
print("3. Uppercase text:", upper_txt)

# 4. Replace character 'U' with 'V'
replaced_txt = txt.replace("U", "V")
print("4. Text with U replaced by V:", replaced_txt)

# 5. Return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
char_range = y[1:4]
print("5. Characters in 2nd, 3rd, and 4th position:", char_range)

# 6. Fix the string with quotes
x = "All \"Data Scientists\" are cool!"
print("6. Corrected string:", x)

####################################
# Exercise 5: Dictionaries
####################################

print("\nEXERCISE 5: DICTIONARIES\n")

# Add the provided dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of the shoe size
print("1. Shoe size:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("2. Updated dictionary:", Shoes)

# 3. Add key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("3. Dictionary after adding type:", Shoes)

# 4. Return a list of all keys
keys_list = list(Shoes.keys())
print("4. List of keys:", keys_list)

# 5. Return a list of all values
values_list = list(Shoes.values())
print("5. List of values:", values_list)

# 6. Check if the key "size" exists
key_exists = "size" in Shoes
print("6. Does 'size' key exist?", key_exists)

# 7. Loop through the dictionary
print("7. Looping through dictionary:")
for key, value in Shoes.items():
    print(f"   - {key}: {value}")

# 8. Remove "color" from the dictionary
Shoes.pop("color")
print("8. Dictionary after removing color:", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("9. Dictionary after clearing:", Shoes)

# 10. Create a new dictionary and make a copy
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
car_copy = car.copy()
print("10. Original dictionary:", car)
print("    Copied dictionary:", car_copy)

# 11. Show nested dictionaries
student = {
    "name": "John",
    "age": 20,
    "courses": {
        "math": {
            "grade": "A",
            "credits": 4
        },
        "science": {
            "grade": "B",
            "credits": 3
        }
    }
}
print("11. Nested dictionary example:", student)
print("    Math grade:", student["courses"]["math"]["grade"])