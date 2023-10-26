class Filmer:
    
    def __init__(self, title: str, year: int, score: float) -> None:
        self.title = title
        self.year = year
        self.score = score
        
        
    def print_movie(self):
        print(f"{self.title} was released in {self.year} and currently has a score of {self.score}")
        
        

inception = Filmer("Inception", 2010, 8.8)
the_martian = Filmer("The Martian", 2015, 8.0)
joker = Filmer("Joker", 2019, 8.4)

inception.print_movie()
the_martian.print_movie()
joker.print_movie() 