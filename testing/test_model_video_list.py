from models.model_video_lists import VideoList
import pytest


@pytest.fixture
def sample():
    return VideoList(
        1,
        2,
        "My Favourite",
        "1, 3"
    )

def test_get_id():
    vl = VideoList(id=1, duration=10)
    assert vl.get_id() == 1

def test_video_list_attribute(capsys, sample):
    assert sample.id == 1
    assert sample.duration == 2
    assert sample.title == "My Favourite"
    assert sample.video == "1, 3"

def test_main(capsys, sample):
    lists = VideoList.main()
    for list in lists:
        assert list.id == list.id
        assert list.title == list.title
        assert list.duration == list.duration
        assert list.video == list.video


def test_delete_list(tmpdir):
    p = tmpdir.mkdir("sub").join("video_lists.csv")
    p.write("id,title,video_ids,duration\n1,test,1,2\n2,test2,2,3")
    VideoList.file_path_list = str(p)
    assert VideoList.delete_list(1) == True
    assert p.read() == "id,title,video_ids,duration\n2,test2,2,3\n"

def test_create_list(tmpdir):
    p = tmpdir.mkdir("sub").join("video_lists.csv")
    p.write("id,title,video_ids,duration\n1,test,1,2\n2,test2,2,3")
    VideoList.file_path_list = str(p)
    assert VideoList.create_list("test3", "3") == True
    assert p.read() == "id,title,video_ids,duration\n1,test,1,2\n2,test2,2,3\n3,test3,3,1\n"

def test_update_list(tmpdir):
    p = tmpdir.mkdir("sub").join("video_lists.csv")
    p.write("id,title,video_ids,duration\n1,test,1,2\n2,test2,2,3")
    VideoList.file_path_list = str(p)
    assert VideoList.update_list(1, "new_title", "4") == True
    assert p.read() == "id,title,video_ids,duration\n1,new_title,4,1\n2,test2,2,3\n"