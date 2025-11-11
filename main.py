from books import Book
from movies import Movie
import yaml
import logging
from pythonjsonlogger import jsonlogger
import datetime

#initialize lists and loop control variable
books = []
movies = []
loop_continue = True

#constants for file names
BOOK_FILE = "books.yaml" #save books data
MOVIE_FILE = "movies.yaml" #save movies data
LOG_FILE = "media_tracker.json" #log file

#configure logging
logger = logging.getLogger(LOG_FILE)

# Clear any existing handlers to prevent duplicates
if logger.hasHandlers():
    logger.handlers.clear()

loghandler = logging.FileHandler(LOG_FILE)
formatter = jsonlogger.JsonFormatter()
loghandler.setFormatter(formatter)
logger.addHandler(loghandler)
logger.setLevel(logging.INFO)

# Prevent propagation to root logger
logger.propagate = False

#get current timestamp
def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Log application start BEFORE loading data
logger.info("Application started", extra={"timestamp": get_current_timestamp()})

try:
    with open(BOOK_FILE, 'r') as b_file:
        data = yaml.safe_load(b_file)
        logger.info("Books data loaded", extra={"book_count": len(data["books"])})
        for b_data in data["books"]:
            book = Book(
                title=b_data["title"],
                author=b_data["author"],
                finished_date=b_data.get("finished_date", ""),
                stars=b_data.get("stars", 0),
                notes=b_data.get("notes", "")
            )
            books.append(book)
except FileNotFoundError:
    logger.warning("Books file not found, starting with empty books list")

#opening movies.yaml file and loading data into movies list
try:
    with open(MOVIE_FILE, 'r') as m_file:
        data = yaml.safe_load(m_file)
        logger.info("Movies data loaded", extra={"movie_count": len(data["movies"])})
        for m_data in data["movies"]:
            movie = Movie(
                title=m_data["title"],
                director=m_data["director"],
                genre=m_data.get("genre", ""),
                language=m_data.get("language", ""),
                watched_date=m_data.get("watched_date", ""),
                stars=m_data.get("stars", 0),
                notes=m_data.get("notes", "")
            )
            movies.append(movie)
except FileNotFoundError:
    logger.warning("Movies file not found, starting with empty movies list")



#functions

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
                        logger.info("Book title updated", extra={"book": book.title, "new_value": new_title})
                        book.update_title(new_title)  # then updates title
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
                        logger.info( "Book author updated",extra={"extra_data": {"action": "update_book", "field": "author", "book": book.title, "new_value": new_author}})
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
                        logger.info( "Book finished date updated",extra={"extra_data": {"action": "update_book", "field": "finished_date", "book": book.title, "new_value": new_date}})
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
                        logger.info( "Book rating updated",extra={"extra_data": {"action": "update_book", "field": "rating", "book": book.title, "new_value": stars}})
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
                        logger.info( "Book notes updated",extra={"extra_data": {"action": "update_book", "field": "notes", "book": book.title, "new_value": note}})
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
                        logger.info("Movie title updated", extra={"movie": movie.title, "new_value": new_title})
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
                        logger.info( "Movie director updated",extra={"extra_data": {"action": "update_movie", "field": "director", "movie": movie.title, "new_value": new_director}})
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
                        logger.info( "Movie genre updated",extra={"extra_data": {"action": "update_movie", "field": "genre", "movie": movie.title, "new_value": new_genre}})
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
                        logger.info( "Movie language updated",extra={"extra_data": {"action": "update_movie", "field": "language", "movie": movie.title, "new_value": new_lang}})
                        break
                    except ValueError as e:
                        print(str(e))
                        logger.warning("Attempted to set invalid movie language",extra={"movie": movie.title, "error": str(e)})
            case "5":
                #update watched date
                while True:
                    new_date = input("New date (YYYY-MM-DD): ")
                    if date_validation(new_date):
                        movie.update_watched_date(new_date)
                        print("Updated!")
                        logger.info( "Movie watched date updated",extra={"extra_data": {"action": "update_movie", "field": "watched_date", "movie": movie.title, "new_value": new_date}})
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
                        logger.info( "Movie rating updated",extra={"extra_data": {"action": "update_movie", "field": "rating", "movie": movie.title, "new_value": rating}})
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
                        logger.info( "Movie notes updated",extra={"extra_data": {"action": "update_movie", "field": "notes", "movie": movie.title, "new_value": note}})
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


while loop_continue:
    # Main Menu
    get_main_menu()
    user_input = input("\nSelect an option: ")

    # Exit
    if user_input == "3":
        loop_continue = False
        print("\ngoodbye !")
        logger.info("Application exited", extra={"timestamp": get_current_timestamp()})
        break

    # Books Menu
    elif user_input == "1":
        get_books_menu()
        book_choice = input("\nSelect an option: ")

        if book_choice == "1":  #add new book
            #get book details from user
            #title input, validation
            while True:
                title = input("Title: ")
                try:
                    non_empty_string_validation(title)
                    break
                except ValueError:
                    print("Title cannot be empty.")
            
            #author input, validation
            while True:
                author = input("Author: ")
                try:
                    non_empty_string_validation(author)
                    break
                except ValueError:
                    print("Author cannot be empty.")
            
            #date input, validation
            while True:
                date = input("Finished date (YYYY-MM-DD): ")
                if date_validation(date):
                    break
                print("Invalid date format. Please use YYYY-MM-DD.")
            
            #stars input, validation
            while True:
                stars = input("Rating (1-10): ")
                try:
                    rating_validation(stars)
                    break
                except ValueError:
                    print("Invalid rating. Please enter a number between 1 and 10.")

            #notes input
            while True:
                notes = input("Notes: ")
                try:
                    non_empty_string_validation(notes)
                    break
                except ValueError:
                    print("Notes cannot be empty.")

            #create and add new book
            new_book = Book(title, author, date, stars, notes) #create new Book object
            books.append(new_book) #add new book to books list

            print("\nBook added successfully!\n")
            logger.info("New book added", extra={"title": title, "author": author})
            input()

        elif book_choice == "2": #view all books
            if not books: #if books list is empty
                print("\nNo books recorded yet.\n")
                input()

            else:
                for b in books: #print info of each book from the list
                    print("\n")
                    b.get_book_info()   #call get_book_info method from Book class
                input()
        elif book_choice=="3": #edit book
            edit_book(books) #call edit_book function
        else:
            continue

    # Movies Menu
    elif user_input == "2":
        get_movies_menu()
        movie_choice = input("\nSelect an option: ")

        if movie_choice == "1": #add new movie
            #movie title input and validation
            while True:
                title = input("Title: ")
                try:
                    non_empty_string_validation(title)
                    break
                except ValueError:
                    print("Title cannot be empty.")
            
            #director input and validation
            while True:
                director = input("Director: ")
                try:
                    non_empty_string_validation(director)
                    break
                except ValueError:
                    print("Director cannot be empty.")
            
            #genre input and validation
            while True:
                genre = input("Genre: ")
                try:
                    non_empty_string_validation(genre)
                    break
                except ValueError:
                    print("Genre cannot be empty.")
            
            #language input and validation
            while True:
                language = input("Language: ")
                try:
                    language_validation(language)
                    break
                except ValueError as e:
                    print(str(e))
            
            #watched date input and validation
            while True:
                date = input("Watched date (YYYY-MM-DD): ")
                if date_validation(date):
                    break
                print("Invalid date format. Please use YYYY-MM-DD.")
            
            #stars input and validation
            while True:
                stars = input("Rating (1-10): ")
                try:
                    rating_validation(stars)
                    break
                except ValueError:
                    print("Invalid rating. Please enter a number between 1 and 10.")
            
            #notes input and validation
            while True: 
                notes = input("Notes: ")
                try:
                    non_empty_string_validation(notes)
                    break
                except ValueError:
                    print("Notes cannot be empty.")
            
            new_movie = Movie(title, director, genre, language, date, stars, notes)    #create new Movie object
            movies.append(new_movie) #add new movie to movies list
            print("\nMovie added successfully!\n")
            logger.info("New movie added", extra={"title": title, "director": director})
            input()

        elif movie_choice == "2": #view all movie
            if not movies: #if movies list is empty
                print("\nNo movies recorded yet.\n")
            else:
                for m in movies:
                    m.get_movie_info() #call get_movie_info method from Movie class
            input()        
        elif movie_choice=="3": #edit movie
            edit_movie(movies) #call edit_movie function
        
        else:
            continue

#save updated data to yaml files    
# Movies    
with open(MOVIE_FILE, 'w') as m_file:
    yaml.safe_dump({"movies" : [m.__dict__ for m in movies]}, m_file)
logger.info("Movies data saved", extra={"movie_count": len(movies)})

# Books
with open(BOOK_FILE, "w") as b_file:
    yaml.safe_dump({"books" : [b.__dict__ for b in books]}, b_file)
logger.info("Books data saved", extra={"book_count": len(books)})

