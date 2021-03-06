class Movie:
    '''
    class to define movie objects    
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    all_reviews = []

    def __init__(self, movie_id, title, review):
        self.movie_id = movie_id
        self.title = title
        # self.imageurl = imageurl
        self.review  = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):
        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
