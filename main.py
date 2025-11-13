from books import Book
from movies import Movie
import yaml
import logging
from pythonjsonlogger.json import JsonFormatter
from prometheus_client import Counter, Histogram, start_http_server
import datetime

# Initialize lists and loop control variable
books = []
movies = []

# Constants for file names
BOOK_FILE = "books.yaml"
MOVIE_FILE = "movies.yaml"
LOG_FILE = "media_tracker.json"

# Counters for prometheus metrics
BOOKS_ADDED = Counter('books_added', 'Number of books added')
MOVIES_ADDED = Counter('movies_added', 'Number of movies added')

# Histograms for prometheus metrics
BOOK_EDIT_TIME = Histogram('book_edit_time_seconds', 'Time taken to edit a book')
MOVIE_EDIT_TIME = Histogram('movie_edit_time_seconds', 'Time taken to edit a movie')

# Configure logging
logger = logging.getLogger(LOG_FILE)

if logger.hasHandlers():
    logger.handlers.clear()

loghandler = logging.FileHandler(LOG_FILE)
formatter = JsonFormatter()
loghandler.setFormatter(formatter)
logger.addHandler(loghandler)
logger.setLevel(logging.INFO)
logger.propagate = False

# ============================================================================
# VALIDATION FUNCTIONS
# ============================================================================

def get_current_timestamp():
    """Get current timestamp in formatted string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def date_validation(date_text):
    """Validate date format YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def rating_validation(rating_text):
    """Validate rating is between 1-10."""
    if not rating_text.isdigit() or not(1 <= int(rating_text) <= 10):
        raise ValueError("Invalid rating. Please enter a number between 1 and 10.")
    return True


def non_empty_string_validation(input_text):
    """Validate string is not empty."""
    if not input_text.strip():
        raise ValueError("Input cannot be empty.")
    return True


def language_validation(language_text):
    """Validate language input."""
    new_lang = language_text.strip()
    if not new_lang:
        raise ValueError("Language cannot be empty.")
    elif not new_lang.isalpha():
        raise ValueError("Language must contain only letters.")
    elif len(new_lang) < 2 or len(new_lang) > 30:
        raise ValueError("Language length must be between 2 and 30 characters.")
    return True


# ============================================================================
# MENU DISPLAY FUNCTIONS
# ============================================================================

def get_main_menu(): 
    """Display main menu."""
    print("===================================")
    print("    Welcome to Your Media Logger  ")
    print("===================================\n")
    print("              Main Menu")
    print("-----------------------------------")
    print("1. Books")
    print("2. Movies")
    print("3. Exit")


def get_movies_menu():
    """Display movies menu."""
    print("\n\n===================================")
    print("        Welcome to Movies Menu  ")
    print("===================================\n")
    print("1. Add New Movie")
    print("2. View All Movies")
    print("3. Update Movie")
    print("4. Back to Main Menu")


def get_books_menu():
    """Display books menu."""
    print("\n\n===================================")
    print("        Welcome to Books Menu  ")
    print("===================================\n")
    print("1. Add New Book")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Back to Main Menu")


# ============================================================================
# BOOK AND MOVIE EDIT FUNCTIONS
# ============================================================================

@BOOK_EDIT_TIME.time()
def edit_book(books):
    """Edit an existing book."""
    num = 1
    print()
    for b in books:
        print(f"{num}. {b.title}")
        num += 1
    print()

    choice = input("select book to edit:")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(books):
        print("Invalid choice!")
        return
    
    book = books[int(choice) - 1]
    
    while True:
        print("\nEdit Book")
        print("-------------")
        print(f"1. Title         : {book.title}")
        print(f"2. Author        : {book.author}")
        print(f"3. Finished Date : {book.finished_date}")
        print(f"4. Rating        : {book.stars}")
        print(f"5. Notes         : {book.notes}")
        print("6. Back to Previous Menu")

        edit_book_choice = input(f"\nSelect field to edit: ")
        
        match edit_book_choice:
            case "1":
                while True:
                    new_title = input("New Title: ")
                    try:
                        non_empty_string_validation(new_title)
                        logger.info("Book title updated", extra={"book": book.title, "new_value": new_title})
                        book.update_title(new_title)
                        print("Updated!")
                        break
                    except ValueError:
                        print("Title cannot be empty.")
            case "2":
                while True:
                    new_author = input("New Author: ")
                    try:
                        non_empty_string_validation(new_author)
                        book.update_author(new_author)
                        print("Updated!")
                        logger.info("Book author updated", extra={"extra_data": {"action": "update_book", "field": "author", "book": book.title, "new_value": new_author}})
                        break
                    except ValueError:
                        print("Author name cannot be empty.")
            case "3":
                while True:
                    new_date = input("New date (YYYY-MM-DD): ")
                    if date_validation(new_date):
                        book.update_finished_date(new_date)
                        print("Updated!")
                        logger.info("Book finished date updated", extra={"extra_data": {"action": "update_book", "field": "finished_date", "book": book.title, "new_value": new_date}})
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")
            case "4":
                while True:
                    stars = input("New rating (1-10): ")
                    try:
                        rating_validation(stars)
                        book.update_stars(stars)
                        print("Updated!")
                        logger.info("Book rating updated", extra={"extra_data": {"action": "update_book", "field": "rating", "book": book.title, "new_value": stars}})
                        break
                    except ValueError:  
                        print("Invalid rating. Please enter a number between 1 and 10.")
            case "5":
                while True:
                    note = input("New Note: ")
                    try:
                        non_empty_string_validation(note)
                        book.update_notes(note)
                        print("Updated!")
                        logger.info("Book notes updated", extra={"extra_data": {"action": "update_book", "field": "notes", "book": book.title, "new_value": note}})
                        break
                    except ValueError:
                        print("Notes cannot be empty.")
            case "6":
                print("Returning to previous menu...")
                return
            case _:
                print("Invalid choice.")


@MOVIE_EDIT_TIME.time()
def edit_movie(movies):
    num = 1 # display movie list
    print()
    for m in movies:
        print(f"{num}. {m.title}")
        num += 1
    print()

    choice = input("select movie to edit:")
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(movies):
        print("Invalid choice!")
        return
    
    movie = movies[int(choice) - 1]
    
    while True:
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

        edit_movie_choice = input(f"\nSelect field to Edit: ")

        match edit_movie_choice:
            case "1":
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
                while True:
                    new_director = input("New Director: ")
                    try:
                        non_empty_string_validation(new_director)
                        movie.update_director(new_director)
                        print("Updated!")
                        logger.info("Movie director updated", extra={"extra_data": {"action": "update_movie", "field": "director", "movie": movie.title, "new_value": new_director}})
                        break
                    except ValueError:
                        print("Director name cannot be empty.")
            case "3":
                while True:
                    new_genre = input("New Genre: ")
                    try:
                        non_empty_string_validation(new_genre)
                        movie.update_genre(new_genre)
                        print("Updated!")
                        logger.info("Movie genre updated", extra={"extra_data": {"action": "update_movie", "field": "genre", "movie": movie.title, "new_value": new_genre}})
                        break
                    except ValueError:
                        print("Genre cannot be empty.")
            case "4":
                while True:
                    new_lang = input("New Language: ")
                    try:
                        language_validation(new_lang)
                        movie.update_language(new_lang)
                        print("Updated!")
                        logger.info("Movie language updated", extra={"extra_data": {"action": "update_movie", "field": "language", "movie": movie.title, "new_value": new_lang}})
                        break
                    except ValueError as e:
                        print(str(e))
                        logger.warning("Attempted to set invalid movie language", extra={"movie": movie.title, "error": str(e)})
            case "5":
                while True:
                    new_date = input("New date (YYYY-MM-DD): ")
                    if date_validation(new_date):
                        movie.update_watched_date(new_date)
                        print("Updated!")
                        logger.info("Movie watched date updated", extra={"extra_data": {"action": "update_movie", "field": "watched_date", "movie": movie.title, "new_value": new_date}})
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")
            case "6":
                while True:
                    rating = input("New rating (1-10): ")
                    try:
                        rating_validation(rating)
                        movie.update_stars(rating)
                        print("Updated!")
                        logger.info("Movie rating updated", extra={"extra_data": {"action": "update_movie", "field": "rating", "movie": movie.title, "new_value": rating}})
                        break
                    except ValueError:
                        print("Invalid rating. Please enter a number between 1 and 10.")
            case "7":
                while True:
                    note = input("New Note: ")
                    try:
                        non_empty_string_validation(note)
                        movie.update_notes(note)
                        print("Updated!")
                        logger.info("Movie notes updated", extra={"extra_data": {"action": "update_movie", "field": "notes", "movie": movie.title, "new_value": note}})
                        break
                    except ValueError:
                        print("Notes cannot be empty.")
            case "8" :
                print("returning to previous menu...")
                return
            case _:
                print("invalid choice.")

# ============================================================================
# EXISTING DATA LOADING FUNCTION
# ============================================================================

def load_data():
    global books, movies
    
    # Load books
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

    # Load movies
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


# ============================================================================
# SAVE DATA FUNCTION
# ============================================================================

def save_data():
    # Save movies
    with open(MOVIE_FILE, 'w') as m_file:
        yaml.safe_dump({"movies": [m.__dict__ for m in movies]}, m_file)
    logger.info("Movies data saved", extra={"movie_count": len(movies)})

    # Save books
    with open(BOOK_FILE, "w") as b_file:
        yaml.safe_dump({"books": [b.__dict__ for b in books]}, b_file)
    logger.info("Books data saved", extra={"book_count": len(books)})


# ============================================================================
# MAIN APPLICATION LOOP
# ============================================================================

def main():
    global books, movies
    
    # Log application start
    logger.info("Application started", extra={"timestamp": get_current_timestamp()})
    
    start_http_server(8000) # Prometheus metrics server
    
    load_data()  # Load existing data

    loop_continue = True
    
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
            
            if book_choice == "1":  # Add new book
                while True:
                    title = input("Title: ")
                    try:
                        non_empty_string_validation(title)
                        break
                    except ValueError:
                        print("Title cannot be empty.")
                
                while True:
                    author = input("Author: ")
                    try:
                        non_empty_string_validation(author)
                        break
                    except ValueError:
                        print("Author cannot be empty.")
                
                while True:
                    date = input("Finished date (YYYY-MM-DD): ")
                    if date_validation(date):
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")
                
                while True:
                    stars = input("Rating (1-10): ")
                    try:
                        rating_validation(stars)
                        break
                    except ValueError:
                        print("Invalid rating. Please enter a number between 1 and 10.")

                while True:
                    notes = input("Notes: ")
                    try:
                        non_empty_string_validation(notes)
                        break
                    except ValueError:
                        print("Notes cannot be empty.")

                new_book = Book(title, author, date, stars, notes)
                books.append(new_book)

                print("\nBook added successfully!\n")
                logger.info("New book added", extra={"title": title, "author": author})
                BOOKS_ADDED.inc()
                input()

            elif book_choice == "2":  # View all books
                if not books:
                    print("\nNo books recorded yet.\n")
                    input()
                else:
                    for b in books:
                        print("\n")
                        b.get_book_info()
                    input()
                    
            elif book_choice == "3":  # Edit book
                edit_book(books)
            else:
                continue

        # Movies Menu
        elif user_input == "2":
            get_movies_menu()
            movie_choice = input("\nSelect an option: ")

            if movie_choice == "1":  # Add new movie
                while True:
                    title = input("Title: ")
                    try:
                        non_empty_string_validation(title)
                        break
                    except ValueError:
                        print("Title cannot be empty.")
                
                while True:
                    director = input("Director: ")
                    try:
                        non_empty_string_validation(director)
                        break
                    except ValueError:
                        print("Director cannot be empty.")
                
                while True:
                    genre = input("Genre: ")
                    try:
                        non_empty_string_validation(genre)
                        break
                    except ValueError:
                        print("Genre cannot be empty.")
                
                while True:
                    language = input("Language: ")
                    try:
                        language_validation(language)
                        break
                    except ValueError as e:
                        print(str(e))
                
                while True:
                    date = input("Watched date (YYYY-MM-DD): ")
                    if date_validation(date):
                        break
                    print("Invalid date format. Please use YYYY-MM-DD.")
                
                while True:
                    stars = input("Rating (1-10): ")
                    try:
                        rating_validation(stars)
                        break
                    except ValueError:
                        print("Invalid rating. Please enter a number between 1 and 10.")
                
                while True: 
                    notes = input("Notes: ")
                    try:
                        non_empty_string_validation(notes)
                        break
                    except ValueError:
                        print("Notes cannot be empty.")
                
                new_movie = Movie(title, director, genre, language, date, stars, notes)
                movies.append(new_movie)
                print("\nMovie added successfully!\n")
                logger.info("New movie added", extra={"title": title, "director": director})
                MOVIES_ADDED.inc()
                input()

            elif movie_choice == "2":  # View all movies
                if not movies:
                    print("\nNo movies recorded yet.\n")
                else:
                    for m in movies:
                        m.get_movie_info()
                input()
                
            elif movie_choice == "3":  # Edit movie
                edit_movie(movies)
            
            else:
                continue
    
    # Save data before exiting
    save_data()

# ============================================================================
# SCRIPT ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()