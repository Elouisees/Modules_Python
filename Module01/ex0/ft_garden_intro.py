
if __name__ == "__main__":
    name: str = "Rose"
    height: str = "28cm"
    age: str = "60 days"

    print("=== Welcome To My Garden ===")
    print("Plant: ", name)
    print("Height: ", height)
    print("Age: ", age)

    print("\n=== End of Program ===")


# Notes:

# The idiom is a conditonal statement that checks
# whether the value of the variable __name__ is equal to the string "__main__"

# Python sets the global __name__ of a module equal to "__main__"
# if the python interpreter runs your code in the top-level code environment.

# n the top-level code environment, the value of __name__ is "__main__".
# In an imported module, the value of the __name__ is the module's name
# as a string.

# You use this idiom when you want to create an
# additional entry point for your script.
