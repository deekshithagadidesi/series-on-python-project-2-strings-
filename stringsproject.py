Name = input("Enter your name: ")
branch = input("Enter your branch: ")
college = input("Enter your college: ")
favprog = input("Enter your favorite programming language: ")

print(Name.upper())
print(Name.lower())
print(len(Name))
print(Name[0])
print(Name[-1])
print(Name[::-1])

print(f"""Hello, My name is {Name}.
I am studying {branch} at {college}.
My favourite programming language is {favprog}.""")

if 'a' in Name.lower():
    print("contains : a")
else:
    print("doesn't contain : a")

print("Count of i:", Name.lower().count("i"))

print(Name.strip())
print(Name.split())

# Character count
print("Character count:", len(Name))

# Word count
print("Word count:", len(Name.split()))

# Replace 'college' with 'institution'
print(college.replace("college", "institution"))

vowels = (
    Name.lower().count("a")
    + Name.lower().count("e")
    + Name.lower().count("i")
    + Name.lower().count("o")
    + Name.lower().count("u")
)

print("Number of vowels:", vowels)