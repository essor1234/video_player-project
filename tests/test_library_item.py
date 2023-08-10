from tests.library_item import LibraryItem
def test_init():
    movie = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5)
    assert movie.name == "The Shawshank Redemption"
    assert movie.director == "Frank Darabont"
    assert movie.rating == 5
    assert movie.play_count == 0

def test_info():
    movie = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5)
    assert movie.info() == "The Shawshank Redemption - Frank Darabont *****"

def test_stars():
    movie = LibraryItem("The Shawshank Redemption", "Frank Darabont", 5)
    assert movie.stars() == "*****"
