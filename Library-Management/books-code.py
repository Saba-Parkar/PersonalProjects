import time

library = [
    ["novel", [["ANNE WITH AN E", ["Available", 1975]], ["Mobydick", ["Not available", 2001]],
               ["The catcher", ["Not available", 2009]], ["Little Women", ["Available", 1987]]]],
    ["comic", [["Archies", ["Available", 2000]], ["Tinkle", ["Available", 2008]],
               ["TTG", ["Available", 2001]], ["Tintin", ["Not available", 1980]],
               ["Ben 10", ["Available", 2002]], ["Peanuts", ["Not available", 1999]]]],
    ["fiction", [["Harry Potter", ["Not available", 1975]], ["Divergent", ["Not available", 2003]],
                 ["Silent Patient", ["Available", 2006]], ["Big Foot", ["Available", 2005]],
                 ["Gone Series", ["Available", 2010]], ["Arcane Series", ["Not available", 2020]]]],
    ["education", [["Aurora", ["Available", 1965]], ["Snapshots", ["Not available", 2003]],
                   ["RD Sharma", ["Not available", 1989]], ["Oswal", ["Not available", 2000]],
                   ["Exam Idea", ["Not available", 1999]]]]
]

history = []

while True:
    print("\n", "Welcome to the Advanced Scholar Domain Library!\n", sep="")
    print("Options: ADMIN | MEMBER | VIEWER | DONATE\n", sep="")
    choice = input("Select an option: ").strip().upper()

    if choice == "ADMIN":
        password = input("Enter admin password: ")
        if password == "password":
            print("\nWelcome, Admin!\n", sep="")
            print("Options: MAIN LIBRARY | USER HISTORY\n", sep="")
            ch = input("Select an option: ").strip().upper()

            if ch == "MAIN LIBRARY":
                print("Available Genres: NOVEL | COMIC | FICTION | EDUCATION\n", sep="")
                genre = input("Select a genre: ").strip().lower()
                for i in library:
                    if i[0] == genre:
                        print("\nBook Name", "Availability", "Year\n", sep="\t\t")
                        for k in i[1]:
                            print(k[0], k[1][0], k[1][1], sep="\t\t")
                        break
                else:
                    print("Invalid genre.\n", sep="")

            elif ch == "USER HISTORY":
                print("\nUser Name", "Book Borrowed", "Days Left\n", sep="\t\t")
                for a in history:
                    name = a[0]
                    borrowedtime = a[1]["borrow_time"]
                    duration = 15 - int((time.time() - borrowedtime) // (24 * 3600))
                    
                    if duration <= 0:
                        status = "Delayed"
                    else:
                        status = str(duration) + "days left"
                    
                    print(name, a[1]['book'], status, sep="\t\t")


            else:
                print("Incorrect password.\n", sep="")

    elif choice == "VIEWER":
        print("Available Genres: NOVEL | COMIC | FICTION | EDUCATION\n", sep="")
        genre = input("Select a genre: ").strip().lower()
        for i in library:
            if i[0] == genre:
                print("\nBook Name", "Availability", "Year\n", sep="\t\t\t")
                for k in i[1]:
                    print(k[0], k[1][0], k[1][1], sep="\t\t\t")
                break
        else:
            print("Invalid genre.\n", sep="")

    elif choice == "DONATE":
        print("Available Genres: NOVEL | COMIC | FICTION | EDUCATION\n", sep="")
        genre = input("Enter the genre of your book: ").strip().lower()
        for i in library:
            if i[0] == genre:
                book = input("Enter the book title: ")
                year = int(input("Enter the year of publication: "))
                i[1].append([book, ["Available", year]])
                print("Thank you for your donation! Updated list:\n")
                for k in i[1]:
                    print(k[0], k[1][0], k[1][1], sep="\t")
                break
        else:
            print("Invalid genre.\n", sep="")

    elif choice == "MEMBER":
        print("Options: SIGN UP | LOGIN\n", sep="")
        option = input("Choose an option: ").strip().lower()
        if option == "sign up":
            name = input("Enter your name: ")
            print("Your password is: member123\n", sep="")

        elif option == "login":
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            if password == "member123":
                print("\nWelcome,", name, "!\n", sep="")
                print("Available Genres: NOVEL | COMIC | FICTION | EDUCATION\n", sep="")
                genre = input("Select a genre: ").strip().lower()
                for i in library:
                    if i[0] == genre:
                        print("\nBook Name", "Availability", "Year\n", sep="\t")
                        for k in i[1]:
                            print(k[0], k[1][0], k[1][1], sep="\t")
                        break
                else:
                    print("Invalid genre.\n", sep="")

                print("\nOptions: BORROW | RETURN\n", sep="")
                option = input("Enter your option: ").strip().lower()
                if option == "borrow":
                    book = input("Enter the book you want to borrow: ")
                    for i in library:
                        if i[0] == genre:
                            for k in i[1]:
                                if k[0].lower() == book.lower():
                                    if k[1][0] == "Available":
                                        k[1][0] = "Not available"
                                        history.append([name, {"book": book, "borrow_time": time.time()}])
                                        print("Successfully borrowed:", book, "\n", sep="")
                                    else:
                                        print("Book is already borrowed.\n", sep="")
                                    break
                            else:
                                print("Book not found in", genre, "\n", sep="")
                            break

                elif option == "return":
                    book = input("Enter the book you want to return: ")
                    
                    for i in library:
                        if i[0] == genre:
                            for k in i[1]:
                                if k[0].lower() == book.lower():
                                    k[1][0] = "Available"
                                    print("Returned:", book, "\n", sep="")
                                    break
                            else:
                                print("Book not found in", genre, "\n", sep="")
                            break
                    
                    for a in history:
                        if a[0] == name and a[1]['book'].lower() == book.lower():
                            history.remove(a)
                            break


            else:
                print("Incorrect password.\n", sep="")

    else:
        print("Invalid option.\n", sep="")
