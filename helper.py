import datetime 
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
        print(f"1. Title         : {book.title}")
        print(f"2. Author        : {book.author}")
        print(f"3. Finished Date : {book.finished_date}")
        print(f"4. Rating        : {book.stars}")
        print(f"5. Notes         : {book.notes}")
        print("6. Back to Previous Menu")

        edit_book_choice = input(f"\nSelect field to edit: ")
        #handle user's edit choice
        match edit_book_choice:
            case "1":
                #update title
                while True:
                    new_title = input("New Title: ")
                    try:
                        non_empty_string_validation(new_title)
                        book.update_title(new_title)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Title cannot be empty.")
            case "2":
                #update author
                while True:
                    new_author = input("New Author: ")
                    try:
                        non_empty_string_validation(new_author)
                        book.update_author(new_author)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Author name cannot be empty.")
            case "3":
                #update finished date
                while True:
                    new_date = input("New date (YYYY-MM-DD): ")
                    if date_validation(new_date):
                        book.update_finished_date(new_date)
                        print("Updated!")
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")
            case "4":
                #update stars/rating
                while True:
                    stars =input("New rating (1-10): ")
                    try:
                        rating_validation(stars)
                        book.update_stars(stars)
                        print("Updated!")
                        break
                    except ValueError:  
                        print("Invalid rating. Please enter a number between 1 and 10.")
            case "5":
                #update notes
                while True:
                    note=input("New Note: ")
                    try:
                        non_empty_string_validation(note)
                        book.update_notes(note)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Notes cannot be empty.")
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
                while True:
                    new_title = input("New Title: ")
                    try:
                        non_empty_string_validation(new_title)
                        movie.update_title(new_title)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Title cannot be empty.")
            case "2":
                #update director
                while True:
                    new_director = input("New Director: ")
                    try:
                        non_empty_string_validation(new_director)
                        movie.update_director(new_director)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Director name cannot be empty.")
            case "3":
                #update genre
                while True:
                    new_genre = input("New Genre: ")
                    try:
                        non_empty_string_validation(new_genre)
                        movie.update_genre(new_genre)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Genre cannot be empty.")
            case "4":
                #update language
                while True:
                    new_lang = input("New Language: ")
                    try:
                        language_validation(new_lang)
                        movie.update_language(new_lang)
                        print("Updated!")
                        break
                    except ValueError as e:
                        print(str(e))
            case "5":
                #update watched date
                while True:
                    new_date = input("New date (YYYY-MM-DD): ")
                    if date_validation(new_date):
                        movie.update_watched_date(new_date)
                        print("Updated!")
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")
            case "6":
                #update stars/rating
                while True:
                    rating =input("New rating (1-10): ")
                    try:
                        rating_validation(rating)
                        movie.update_stars(rating)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Invalid rating. Please enter a number between 1 and 10.")
            case "7":
                #update notes
                while True:
                    note=input("New Note: ")

                    try:
                        non_empty_string_validation(note)
                        movie.update_notes(note)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Notes cannot be empty.")
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
    print("    Welcome to Your Media Logger  ")
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

#date validation function
def date_validation(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
#rating validation function
def rating_validation(rating_text):
    if not rating_text.isdigit() or not(1 <= int(rating_text) <= 10):
        raise ValueError("Invalid rating. Please enter a number between 1 and 10.")
    return True
    
#string non-empty validation function
def non_empty_string_validation(input_text):
    if not input_text.strip():
        raise ValueError("Input cannot be empty.")
    return True

#language validation function
def language_validation(language_text):
    new_lang= language_text.strip()
    if not new_lang:
        raise ValueError("Language cannot be empty.")
    elif not new_lang.isalpha():
        raise ValueError("Language must contain only letters.")
    elif len(new_lang) < 2 or len(new_lang) > 30:
        raise ValueError("Language length must be between 2 and 30 characters.")
    return True
