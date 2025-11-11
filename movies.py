class Movie:
    #Movie class constructor
    def __init__(self,title,director,genre,language,watched_date,stars,notes):
        self.title=title
        self.director=director
        self.genre=genre
        self.language=language
        self.watched_date=watched_date
        self.stars=stars
        self.notes=notes
    
    #update methods
    def update_title(self,title):
        self.title=title

    def update_director(self,director):
        self.director=director

    def update_genre(self,genre):
        self.genre=genre

    def update_language(self,language):
        self.genre=language

    def update_watched_date(self,watched_date):
        self.watched_date=watched_date

    def update_stars(self,stars):
        self.stars=stars 

    def update_notes(self,notes):
        self.notes=notes

    #display movie information
    def get_movie_info(self):
        print("Movie Information")
        print("----------------")
        print(f"Title         : {self.title}")
        print(f"Director      : {self.director}")
        print(f"Genre         : {self.genre}")
        print(f"Language      : {self.language}")
        print(f"Watched Date  : {self.watched_date}")
        print(f"Rating        : {self.stars}")
        print(f"Notes         : {self.notes}")
