def edit_book(books):
    num=1 #counter for listing books
    print()
    #list all books with numbers
    for b in books:
        print(f"{num}. {b.title}")
        num+=1
    print()

    choice=input("select book to edit:")
    #validate choice
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(books):
        print("Invalid choice!")
        return
    #get selected book
    book = books[int(choice) - 1] #choice=1 -> movies[0]
    while True:
        #display edit menu with current book info
        print("\nEdit Book")
        print("-------------")
        print("1. Title         : {book.title}")
        print("2. Author        : {book.author}")
        print("3. Finished Date : {book.finished_date}")
        print("4. Rating        : {book.stars}")
        print("5. Notes         : {book.notes}")
        print("6. Back to Previous Menu")

        edit_book_choice = input(f"\nSelect field to edit: ")
        #handle user's edit choice
        match edit_book_choice:
            case "1":
                #update title
                book.update_title(input("New title: "))
                print("Updated!")
            case "2":
                #update author
                book.update_author(input("New author: "))
                print("Updated!")
            case "3":
                #update finished date
                book.update_finished_date(input("New date (YYYY-MM-DD): "))
                print("Updated!")
            case "4":
                #update stars/rating
                book.update_stars(input("New rating (1-10): "))
                print("Updated!")
            case "5":
                #update notes
                book.update_notes(input("New notes: "))
                print("Updated!")
            case "6":
                #go back to previous menu
                print("Returning to previous menu...")
                return
            case _: #invalid choice
                print("Invalid choice.")

def edit_movie(movies):
    num=1 #counter for listing movies
    print()
    #list all movies with numbers
    for m in movies:
        print(f"{num}. {m.title}")
        num+=1
    print()

    choice=input("select movie to edit:")
    #validate choice
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(movies):
        print("Invalid choice!")
        return
    #get selected movie
    movie = movies[int(choice) - 1] #choice=1 -> movies[0]
    while True:
        #display edit menu with current movie info
        print("\nEdit Movie")
        print("-------------")
        print(f"1. Title        : {movie.title}")
        print(f"2. Director     : {movie.director}")
        print(f"3. Genre        : {movie.genre}")
        print(f"4. Language     : {movie.language}")
        print(f"5. Watched Date : {movie.watched_date}")
        print(f"6. Rating       : {movie.stars}")
        print(f"7. Notes        : {movie.notes}")
        print(f"8. Back to Previous Menu")


        edit_movie_choice= input(f"\nSelect field to Edit: ")

        match edit_movie_choice:
            case "1":
                #update title
                movie.update_title(input("New Title: "))
                print("Updated!")
            case "2":
                #update director
                movie.update_director(input("New Director: "))
                print("Updated!")
            case "3":
                #update genre
                movie.update_genre(input("New Genre: "))
                print("Updated!")
            case "4":
                #update language
                movie.update_language(input("New Language: "))
                print("Updated!")
            case "5":
                #update watched date
                movie.update_watched_date(input("New Watched Date: "))
                print("Updated!")
            case "6":
                #update stars/rating
                movie.update_stars(input("New Rating: "))
                print("Updated!")
            case "7":
                #update notes
                movie.update_notes(input("New Note: "))
                print("Updated!")
            case "8":
                #go back to previous menu
                print("returning to previous menu...")
                return
            case _:
                #invalid choice
                print("invalid choice.")

#display main menu
def get_main_menu(): 
    print("===================================")
    print("    Welcome to Your Media Tracker  ")
    print("===================================\n")
    print("              Main Menu")
    print("-----------------------------------")
    print("1. Books")
    print("2. Movies")
    print("3. Exit")

#display movies menu
def get_movies_menu():
    print("\n\n===================================")
    print("        Welcome to Movies Menu  ")
    print("===================================\n")
    print("1. Add New Movie")
    print("2. View All Movies")
    print("3. Update Movie")
    print("4. Back to Main Menu")

#display books menu
def get_books_menu():
        print("\n\n===================================")
        print("        Welcome to Books Menu  ")
        print("===================================\n")
        print("1. Add New Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Back to Main Menu")

