from models.model_videos import Videos
import pytest
@pytest.fixture
def sample():
    return Videos(
        1,
        0,
        "Jurassic Park",
        "Steven Spielberg",
        2,

    )


def test_video_attribute(capsys, sample):
    assert sample.id == 1
    assert sample.title == "Jurassic Park"
    assert sample.director == "Steven Spielberg"
    assert sample.rate == 2
    assert sample.plays == 0


def test_main(capsys, sample):
    # get the list of Videos objects from the main method
    videos = Videos.main()
    # loop through the videos list
    for video in videos:
        # assert that each object has the same attributes as the sample object
        assert video.id == sample.id
        assert video.title == sample.title
        assert video.director == sample.director
        assert video.rate == sample.rate
        assert video.plays == sample.plays




def test_plays_count(tmpdir):
    # call the plays_count method with list_id=1
    df_video = Videos.plays_count(1)
    # assert that the plays value for video ids 1 and 2 have been incremented by 1
    assert df_video.loc[df_video.id == 1, 'plays'].values[0] == 8
    assert df_video.loc[df_video.id == 3, 'plays'].values[0] == 11
    # assert that the plays value for video ids 3 and 4 have not been changed
    assert df_video.loc[df_video.id == 6, 'plays'].values[0] == 0
    assert df_video.loc[df_video.id == 8, 'plays'].values[0] == 0



def test_delete_video(tmpdir):
    p = tmpdir.mkdir("sub").join("videos.csv")
    p.write("id,title,director,rate,plays\n1,test,test,5,0\n2,test2,test2,4,0")
    Videos.file_path_videos = str(p)
    assert Videos.delete_video(1) == True
    assert p.read() == "id,title,director,rate,plays\n2,test2,test2,4,0\n"

def test_update_video(tmpdir):
    p = tmpdir.mkdir("sub").join("videos.csv")
    p.write("id,title,director,rate,plays\n1,test,test,5,0\n2,test2,test2,4,0")
    Videos.file_path_videos = str(p)
    assert Videos.update_video("new_title", "new_director", 3.5, 10, 1) == True
    assert p.read() == "id,title,director,rate,plays\n1,new_title,new_director,3.5,10\n2,test2,test2,4.0,0\n"