# Function to validate user input with a specific type
def errores(prompt, type=str):
    valid = False
    while valid == False:
        try:
            # Convert input to the given type
            value = type(input(prompt))

            # If it's a string, allow only letters and spaces
            if type == str:
                if not value.replace(" ","").isalpha():
                    print("Please, only letters.")
                    continue
            
            # Input is valid
            valid = True

        except ValueError:
            # Handle invalid type conversion
            print("pelase only numbers")

    # Return validated value
    return value    