from books import Book
from movies import Movie
import helper as h
import yaml

books = []
movies = []
loop_continue = True

book_file = "books.yaml" #constant
movie_file = "movies.yaml"
LOG_FILE = "media_tracker.log" #not yet used

# Books
with open(book_file, 'r') as b_file:
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


# Moves
with open(movie_file, 'r') as m_file:
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
    h.get_main_menu()
    user_input = input("\nSelect an option: ")

    if user_input == "3":
        loop_continue = False
        print("\ngoodbye !")
        break

    elif user_input == "1":
        h.get_books_menu()
        book_choice = input("\nSelect an option: ")

        if book_choice == "1":  #add new book
            title = input("Title: ")
            author = input("Author: ")
            date = input("Finished date: ")
            stars = input("Rating (1-10): ")
            notes = input("Notes: ")
            new_book = Book(title, author, date, stars, notes)
            books.append(new_book)
            print("\nBook added successfully!\n")
            input()

        elif book_choice == "2": #view all books
            if not books:
                print("\nNo books recorded yet.\n")
                input()

            else:
                for b in books:
                    print("\n")
                    b.get_book_info()
                input()
        elif book_choice=="3": #edit book
            h.edit_book(books)
        else:
            continue

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
            new_movie = Movie(title, director, genre, language, date, stars, notes)
            movies.append(new_movie)
            print("\nMovie added successfully!\n")
            input()

        elif movie_choice == "2": #view all movie
            if not movies:
                print("\nNo movies recorded yet.\n")
            else:
                for m in movies:
                    m.get_movie_info()
            input()        
        elif movie_choice=="3": #edit movie
            h.edit_movie(movies)
        
        else:
            continue