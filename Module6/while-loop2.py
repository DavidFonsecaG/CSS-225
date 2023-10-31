# Initialize loop variable
count = 0
while count <= 10:
    print("This is x: ", count)
    if count == 5:
        count += 5  # increment x to control the condition
        continue
    count += 1  # increment x to control the condition