def handle(troublemaker):

    # nothing being returned from this fn

    try:

        if troublemaker == 0:
            10 / 0

        if troublemaker == 1:
            my_tasks = ["cook"]
            my_tasks[1]

        if troublemaker == 2:
            my_dict = {}
            my_dict["not a key in dict"]

        if troublemaker == 3:
            int("not a number!")

    except ZeroDivisionError:
        print("Zero Division Error: Try a number other than 0")
    except IndexError as ie:
        print(ie)
        print("Index Error: Tried to access value in a list that DNE")
    except KeyError as ke:
        print(ke)
        print("Key Error: Key not in dict")
    except ValueError:
        print("Value Error: Cannot convrt this value / incorrect value entered")

handle(3)

print("Application finished")
