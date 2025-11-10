#learn git - ssh - pub key
#git commit (save) git add, git push (push to the remote)
#learn git branching strategy - features/(jira/trello ticket name)
#create a pull req
#constants
#automated test cases
#mise - python ve
#virtual env wrapper
#mk virtual enviroment book
#comments
#data structure should be coming from a diff file
#inputs should come from a yaml file
#logging - info and debug (json)
#instrumenting metrics - how much memory it uses (performance)
#prometheus metrics
#w metrics -> can create audit logs
#create a excel to log time IN OUT


from books import Book
from movies import Movie
import helper as h

books = []
movies = []
loop_continue = True

# Books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "2024-01-15", 8, "Classic novel about the American Dream")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "2024-02-20", 9, "Powerful story of racial injustice")
book3 = Book("1984", "George Orwell", "2024-03-10", 8, "Dystopian masterpiece about totalitarianism")

# Movies
movie1 = Movie("Inception", "Christopher Nolan", "Sci-Fi", "English", "2024-01-08", 9, "Mind-bending thriller about dreams")
movie2 = Movie("The Shawshank Redemption", "Frank Darabont", "Drama", "English", "2024-02-14", 10, "Best prison escape movie ever made")
movie3 = Movie("Spirited Away", "Hayao Miyazaki", "Animation", "Japanese", "2024-03-05", 10, "Gorgeous Studio Ghibli masterpiece")
books = [book1, book2, book3]
movies = [movie1, movie2, movie3]

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