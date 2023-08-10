from controllers.Videos_controller import controller






def test_list_videos():
    # Check if the list_videos method returns a list of lists with the correct attributes for each video
    expected_list = [[1, ' Jurassic Park ', 'Steven Spielberg', 5, 0],
                     [2, ' Titanic ', 'James Cameron', 4, 3],
                     [3, ' Inception', 'Christopher Nolan', 5, 0],
                     [4, ' Pulp Fiction', 'Quentin Tarantino', 3, 3],
                     [5, ' Goodfellas', 'Martin Scorsese', 5, 0],
                     [6, 'Spirited Away ', 'Hayao Miyazaki', 5, 0],
                     [7, 'Your Name', ' Makoto Shinkai', 5, 0],
                     [8, 'A Whisker Away', ' Junichi Sato and Tomotaka Shibayama', 5, 0]]
 # A sample list of videos for testing
    actual_list = controller.list_videos()
    assert len(actual_list) == len(expected_list) # Check if the length of the lists are equal
    for i in range(len(actual_list)):
        assert actual_list[i] == expected_list[i] # Check if each element of the lists are equal

def test_list_list():
    # Check if the list_list method returns a list of lists with the correct attributes for each list
    expected_list = [[1, ' My Favourite', '1, 3', 2],
                     [2, ' My Least favourite', ' 4, 7', 2],
                     ]

    # A sample list of lists for testing
    actual_list = controller.list_list()
    assert len(actual_list) == len(expected_list) # Check if the length of the lists are equal
    for i in range(len(actual_list)):
        assert actual_list[i] == expected_list[i] # Check if each element of the lists are equal

def test_get_video_rate():
    expected_rate = 5 # A sample rate for testing
    actual_rate = controller.get_video_rate(1) # A sample video ID for testing
    assert actual_rate == expected_rate # Check if the actual rate matches the expected rate

def test_get_video_director():
    expected_director = 'Steven Spielberg' # A sample director for testing
    actual_director = controller.get_video_director(1) # A sample video ID for testing
    assert actual_director == expected_director #

def test_get_video_title():
    expected_title = "Jurassic Park" # sample for testing
    actual_title = controller.get_video_title(1)
    assert actual_title == expected_title

def test_get_video_play():
    expected_play = 0
    actual_play = controller.get_video_play(1)
    assert actual_play == expected_play

def test_find_videos_by_id():
    # Test with a valid input
    assert controller.find_videos_by_id(1) == [[1, 'Jurassic Park', 'Steven Spielberg', 5]]
    # Test with an invalid input
    assert controller.find_videos_by_id(10) == "This is invalid number"

def test_find_videos_by_title():
    # Test with a valid input
    assert controller.find_videos_by_title('Jurassic Park') == [[1, 'Jurassic Park', 'Steven Spielberg', 5]]

def test_find_videos_by_director():
    # Test with a valid input
    assert controller.find_videos_by_director('Steven Spielberg') == [[1, 'Jurassic Park', 'Steven Spielberg', 5]]

def test_find_videos_by_rate():
    # Test with a valid input
    assert controller.find_videos_by_rate(5) == [[1, 'Jurassic Park', 'Steven Spielberg', 5],
 [3, 'Inception', 'Christopher Nolan', 5],
 [5, 'Goodfellas', 'Martin Scorsese', 5],
 [6, 'Spirited Away', 'Hayao Miyazaki', 5],
 [7, 'Your Name', ' Makoto Shinkai', 5],
 [8, 'A Whisker Away', ' Junichi Sato and Tomotaka Shibayama', 5]] != [[1, 'Jurassic Park', 'Steven Spielberg', 5]]

    # Test with an invalid input
    assert controller.find_videos_by_id(10) == "This is invalid number"

def test_find_list_by_id():
    assert controller.find_list_by_id(1)== [[1, ' My Favourite',2]]
    assert controller.find_list_by_id(3) == "This is invalid number"

def test_find_lsit_by_title():
    assert controller.find_list_by_title(' My Favourite')== [[1, ' My Favourite',2]]

def test_check_video():
    assert controller.check_video(1) == ('Jurassic Park', 'Steven Spielberg', 2, 0)
    assert controller.check_video(100) == None

def test_display_video_in_list():
    expected = [[1, 'Jurassic Park', 'Steven Spielberg', 2],
                [3, 'Inception', 'Christopher Nolan', 5]]
    assert controller.display_videos_in_list(1) == expected


