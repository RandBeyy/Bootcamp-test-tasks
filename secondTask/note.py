class Note():

    def __init__(self, film_name: str, note: str, rating: int):
        assert rating > 1 or rating < 5, "Rating must be a number in range 1 - 5"
        self.film_name = film_name
        self.note = note
        self.rating = rating

    """def __repr__(self):
        return {
            'film_name': self.film_name,
            'note': self.note,
            'rating': self.rating
        }"""