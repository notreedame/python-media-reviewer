def edit_book(books):
    num=1
    print()
    for b in books:
        print(f"{num}. {b.title}")
        num+=1
    print()

    choice=input("select book to edit:")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(books):
        print("Invalid choice!")
        return

    book = books[int(choice) - 1] #choice=1 -> movies[0]
    while True:
        print("\nEdit Book")
        print("-------------")
        print("1. Title")
        print("2. Author")
        print("3. Finished Date")
        print("4. Rating")
        print("5. Notes")
        print("6. Back")

        edit_book_choice = input("Select field to edit: ")

        match edit_book_choice:
            case "1":
                book.update_title(input("New title: "))
                print("Updated!")
            case "2":
                book.update_author(input("New author: "))
                print("Updated!")
            case "3":
                book.update_finished_date(input("New date (YYYY-MM-DD): "))
                print("Updated!")
            case "4":
                book.update_stars(input("New rating (1-10): "))
                print("Updated!")
            case "5":
                book.update_notes(input("New notes: "))
                print("Updated!")
            case "6":
                print("Returning to previous menu...")
                return
            case _:
                print("Invalid choice.")

def edit_movie(movies):
    num=1
    print()
    for m in movies:
        print(f"{num}. {m.title}")
        num+=1
    print()

    choice=input("select movie to edit:")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(movies):
        print("Invalid choice!")
        return

    movie = movies[int(choice) - 1] #choice=1 -> movies[0]
    while True:
        print("\nEdit Movie")
        print("-------------")
        print("1. Title")
        print("2. Director")
        print("3. Genre")
        print("4. Language")
        print("5. Watched Date")
        print("6. Rating")
        print("7. Notes")
        print("8. Back")


        edit_movie_choice= input("Select field to Edit: ")

        match edit_movie_choice:
            case "1":
                movie.update_title(input("New Title: "))
                print("Updated!")
            case "2":
                movie.update_director(input("New Director: "))
                print("Updated!")
            case "3":
                movie.update_genre(input("New Genre: "))
                print("Updated!")
            case "4":
                movie.update_language(input("New Language: "))
                print("Updated!")
            case "5":
                movie.update_watched_date(input("New Watched Date: "))
                print("Updated!")
            case "6":
                movie.update_stars(input("New Rating: "))
                print("Updated!")
            case "7":
                movie.update_notes(input("New Note: "))
                print("Updated!")
            case "8":
                print("returning to previous menu...")
                return
            case _:
                print("invalid choice.")

def get_main_menu():
    print("===================================")
    print("    Welcome to Your Media Tracker  ")
    print("===================================\n")
    print("              Main Menu")
    print("-----------------------------------")
    print("1. books")
    print("2. Movies")
    print("3. Exit")


def get_movies_menu():
    print("\n\n===================================")
    print("        Welcome to Movies Menu  ")
    print("===================================\n")
    print("1. Add New Movie")
    print("2. View All Movies")
    print("3. Update Movie")
    print("4. Back to Main Menu")


def get_books_menu():
        print("\n\n===================================")
        print("        Welcome to Books Menu  ")
        print("===================================\n")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Back to Main Menu")

