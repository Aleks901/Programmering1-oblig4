class Filmer:
    
    def __init__(self, title: str, year: int, score: float) -> None:
        self.title = title
        self.year = year
        self.score = score
        
        
    def print_movie(self):
        print(f"{self.title} was released in {self.year} and currently has a score of {self.score}")
        
        
newmovie = Filmer("Lotr", 2001, 10.0)

newmovie.print_movie()