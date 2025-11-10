
class Book:
    def __init__(self,title,author,finished_date,stars,notes):
        self.title=title
        self.author=author
        self.finished_date=finished_date
        self.stars=stars
        self.notes=notes

    def update_title(self,title):
        self.title=title

    def update_author(self,author):
        self.author=author

    def update_finished_date(self,finished_date):
        self.finished_date=finished_date

    def update_stars(self,stars):
        self.stars=stars 

    def update_notes(self,notes):
        self.notes=notes

    def get_book_info(self):
        print("Book Information")
        print("----------------")
        print(f"Title         : {self.title}")
        print(f"Author        : {self.author}")
        print(f"Finished Date : {self.finished_date}")
        print(f"Rating        : {self.stars}")
        print(f"Notes         : {self.notes}")

