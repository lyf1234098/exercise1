# Open the file to read
with open("file_to_read (2).txt", "r") as file:
    # Read the contents of the file
    content = file.read()

# Calculate the total times the word "terrible" appears
count = content.count("terrible")


new_content = ""
terrible_count = 0
for word in content.split():
    if word == "terrible":
        terrible_count += 1
        if terrible_count % 2 == 0:
            new_content += "pathetic "
        else:
            new_content += "marvellous "
    else:
        new_content += word + " "

# Write the new text to a new file called "result.txt"
with open("result.txt", "w") as file:
    file.write(new_content)

# Display the total times the word "terrible" appears
print(f"The word 'terrible' appears {count} times.")