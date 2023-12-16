import os
import os


t = 0

#function to convert all words to numbers
def convert_to_numbers(line):

    converted_numbers = line
    # Define a dictionary to map number names to digits
    number_names = {
        "zero": "z0ero",
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine"
    }
    #convert all words to numbers
    key_found = False
    # print a = line the length of the terminal
    print(f"="*os.get_terminal_size().columns)
    for key in number_names:
        if key in line:
            key_found = True
            print(f"key: {key}, value: {number_names[key]}")
            print(f"line: {line}")
            converted_numbers = converted_numbers.replace(key, number_names[key])
            print(f"converted_numbers: {converted_numbers}")
    if key_found:
        return converted_numbers
    #if no words are found, return the original line
    return line

digits = []

output_file = open("answer.txt", "w")
for x in open("input.txt"):
    # strip the newline character
    x = x.strip()
    # convert all words to numbers
    x = convert_to_numbers(x)
    # find all digits in the line
    digits = [d for d in x if d.isdigit()]
    output_file.write(f"line: {x}, digits: [{','.join(digits)}], {digits[0]+digits[-1]}\n")
    t += int(digits[0] + digits[-1])
output_file.close()
print(t)
