input_file =  open("./Input/Names/invited_names.txt")
names = input_file.readlines()
input_file.close()

names = list(map(lambda x: x[:-1], names))

for name in names:
    output_file = open(f"./Output/ReadyToSend/email_for_{name}.txt", "w")

    example_letter = open("./Input/Letters/starting_letter.txt")
    sample = example_letter.read()
    example_letter.close()

    new_letter = sample.replace("[name]", name)
    output_file.write(new_letter)
