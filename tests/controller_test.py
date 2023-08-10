from controllers.Videos_controller import controller
from models.model_videos import Videos
def test_list_videos():
    videos={}
    videos["01"] = Videos("Jurassic Park", "Steven Spielberg", 5)
    result = controller.list_videos()
    expected = ["Jurassic Park", "Steven Spielberg", 5]
    assert result == expected

