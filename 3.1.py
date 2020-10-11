class Movie:
    name="Valera"
    duration="2h"
    releaseDate="11.10.20"
    rating="10.0"
    def method(self, name, duration, releaseDate, rating):
        self.show_info=name, duration, releaseDate, rating
a=Movie
a.method
print(a)    
