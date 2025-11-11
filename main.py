from books import Book
from movies import Movie
import helper as h
import yaml

books = []
movies = []
loop_continue = True

BOOK_FILE = "books.yaml" #constant
MOVIE_FILE = "movies.yaml"
LOG_FILE = "media_tracker.log" #not yet used

# opening books yaml file and loading data into books list
with open(BOOK_FILE, 'r') as b_file:
    data = yaml.safe_load(b_file)
    for b_data in data["books"]:
        book = Book(
            title=b_data["title"],
            author=b_data["author"],
            finished_date=b_data.get("finished_date", ""),
            stars=b_data.get("stars", 0),
            notes=b_data.get("notes", "")
        )
        books.append(book)

# opening movies yaml file and loading data into movies list
with open(MOVIE_FILE, 'r') as m_file:
    data = yaml.safe_load(m_file)
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

while loop_continue:
    # Main Menu
    h.get_main_menu()
    user_input = input("\nSelect an option: ")

    # Exit
    if user_input == "3":
        loop_continue = False
        print("\ngoodbye !")
        break

    # Books Menu
    elif user_input == "1":
        h.get_books_menu()
        book_choice = input("\nSelect an option: ")

        if book_choice == "1":  #add new book
            title = input("Title: ")
            author = input("Author: ")
            date = input("Finished date: ")
            stars = input("Rating (1-10): ")
            notes = input("Notes: ")
            new_book = Book(title, author, date, stars, notes) #create new Book object
            books.append(new_book) #add new book to books list
            print("\nBook added successfully!\n")
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
            h.edit_book(books) #call edit_book function from helper.py
        else:
            continue

    # Movies Menu
    elif user_input == "2":
        h.get_movies_menu()
        movie_choice = input("\nSelect an option: ")

        if movie_choice == "1": #add new movie
            title = input("Title: ")
            director = input("Director: ")
            genre = input("Genre: ")
            language = input("Language: ")
            date = input("Watched date: ")
            stars = input("Rating (1-10): ")
            notes = input("Notes: ")
            new_movie = Movie(title, director, genre, language, date, stars, notes)    #create new Movie object
            movies.append(new_movie) #add new movie to movies list
            print("\nMovie added successfully!\n")
            input()

        elif movie_choice == "2": #view all movie
            if not movies: #if movies list is empty
                print("\nNo movies recorded yet.\n")
            else:
                for m in movies:
                    m.get_movie_info() #call get_movie_info method from Movie class
            input()        
        elif movie_choice=="3": #edit movie
            h.edit_movie(movies) #call edit_movie function from helper.py
        
        else:
            continue

#save updated data to yaml files    
# Movies    
with open(MOVIE_FILE, 'w') as m_file:
    yaml.safe_dump({"movies" : [m.__dict__ for m in movies]}, m_file)

# Books
with open(BOOK_FILE, "w") as b_file:
    yaml.safe_dump({"books" : [b.__dict__ for b in books]}, b_file)