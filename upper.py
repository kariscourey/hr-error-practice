def uppercase_items(lst):

    output = []


    for item in lst:
        try:
            upper = item.upper()
            output.append(upper)

        except AttributeError:
            print("You entered a non-string value!")
            output.append(item)

    return output

print(uppercase_items(["i", 7]))
print('code end')
