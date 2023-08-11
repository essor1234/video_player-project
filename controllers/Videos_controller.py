from models.model_video_lists import VideoList
from models.model_videos import Videos
import threading
import pandas as pd




class VideosController:

    videos = Videos.main()
    lists = VideoList.main()
    """update data for list"""

    def start_update_thread_list(self, file_path):
        # Start the update_data function in a separate thread
        update_thread = threading.Thread(target=self.update_data_list, args=(file_path,))
        # Use try-except block to catch and handle any exceptions or errors in the thread
        try:
            update_thread.start()
        except Exception as e:
            print(f"Error in thread {update_thread.name}: {e}")

    def update_data_list(self, file_path):
        # Read the csv file and update the videos list every 2 seconds
        while True:
            df = pd.read_csv(file_path)
            self.lists = VideoList.main()
            self.list_list()
            timer = threading.Timer(2.0, self.update_data_list, args=(file_path,))
            timer.start()
            break

    """update data for video"""
    def start_update_thread_videos(self, file_path):
        # Start the update_data function in a separate thread
        update_thread = threading.Thread(target=self.update_data_videos, args=(file_path,))
        try:
            update_thread.start()
        except Exception as e:
            print(f"Error in thread {update_thread.name}: {e}")

    def update_data_videos(self, file_path):
        # Read the csv file and update the videos list every 2 seconds
        while True:
            df = pd.read_csv(file_path)
            self.videos = Videos.main()
            self.list_videos()
            timer = threading.Timer(2.0, self.update_data_videos, args=(file_path,))
            timer.start()
            break

    """method to list out video"""
    def list_videos(self):
        # read the csv file again
        # call the update_data function and get the updated data
        all_video = self.videos
        # list to store id, title, video, duration
        list_data = []
        # loop through the list of VideoList objects
        for video in all_video:
            # get the attributes from each object
            id = video.id
            title = video.title
            director = video.director
            rate = video.rate
            plays = video.plays
            # append the attributes to the list
            list_data.append([id, title, director, rate, plays])
        # return the list
        return list_data

    """list out list  """
    def list_list(self):
        # call the update_data function and get the updated data
        all_list = self.lists
        # list to store id, title, video, duration
        list_data = []
        # loop through the list of VideoList objects
        for item in all_list:
            # get the attributes from each object
            id = item.id
            title = item.title
            video = item.video
            duration = item.duration
            # append the attributes to the list
            list_data.append([id, title, video, duration])
        # return the list
        return list_data

    """get video data"""
    def get_video_rate(self, video_id):
        # Check if the video ID is valid
        for video in self.videos:
            if video_id == video.id:
                # Return the video rate from the self.videos dictionary
                return video.rate
        return None

    def get_video_director(self, video_id):
        # Check if the video ID is valid
        for video in self.videos:
            if video_id == video.id:
                # Return the video rate from the self.videos dictionary
                return video.director
        return None

    def get_video_title(self, video_id):
        # Check if the video ID is valid
        for video in self.videos:
            if video_id == video.id:
                # Return the video rate from the self.videos dictionary
                return video.title
        return None

    def get_video_play(self, video_id):
        # Check if the video ID is valid
        for video in self.videos:
            if video_id == video.id:
                # Return the video rate from the self.videos dictionary
                return video.plays
        return None



    """Searching functions"""

    def find_videos_by_id(self, video_id):
        video_list = []
        # Try to convert the input to an integer[^1^][1]
        for video in self.videos:
            if video_id == video.id:
                video_list.append([video.id, video.title, video.director, video.rate])
        # If no videos match the input, return an error message
        if not video_list:
            return "This is invalid number"
        # Otherwise, return the list of videos
        else:
            return video_list


    def find_videos_by_title(self, video_title):
        video_list = []
        # run through data
        for video in self.videos:
            if video_title.lower().replace(" ","") in video.title.lower().replace(" ",""):
                video_list.append([video.id, video.title, video.director, video.rate])

        if not video_list:
            return None

        return video_list

    def find_videos_by_director(self, director_name):
        video_list = []
        for video in self.videos:
            if director_name.lower().replace(" ", "") in video.director.lower().replace(" ", ""):
                video_list.append([video.id, video.title, video.director, video.rate])
        if not video_list:
            return None
        return video_list


    def find_videos_by_rate(self, video_rate):
        video_list = []
        # Try to convert the input to an integer[^1^][1]
        for video in self.videos:
            if video_rate == video.rate:
                video_list.append([video.id, video.title, video.director, video.rate])

        # If no videos match the input, return an error message
        if not video_list:
            return None
        # Otherwise, return the list of videos
        else:
            return video_list

    def find_list_by_id(self, list_id):
        list_list = []
        for list in self.lists:
            if list_id == list.id:
                list_list.append([list.id, list.title, list.duration])
        # If no videos match the input, return an error message
        if not list_list:
            return None
        # Otherwise, return the list of videos
        else:
            return list_list

    def find_list_by_title(self, list_title):
        list_list = []
        for list in self.lists:
            if list_title.lower().replace(" ","") in list.title.lower().replace(" ",""):
                list_list.append([list.id, list.title, list.duration])

        if not list_list:
            return None
        return list_list

    """Check videos"""
    def check_video(self, order):
        for video in self.videos:
            if order == video.id:
                return video.title, video.director, video.rate, video.plays

                # if the video doesn't exist, return None
        return None



    """get videos from list """

    def display_videos_in_list(self, list_id):
        video_list = []
        for info in self.lists:
            if int(list_id) == info.id:
                # split the info.video string by comma and convert each element to an integer
                try:
                    video_ids = [int(id) for id in str(info.video).split(",")]
                    for video_id in video_ids:
                        for vid in self.videos:
                            if video_id == int(vid.id):
                                video_list.append([vid.id, vid.title, vid.director, vid.rate])
                except AttributeError:
                    return None
                except ValueError:
                    return None

        return video_list







controller = VideosController()


controller.start_update_thread_videos("models/videos.csv")
controller.start_update_thread_list("models/video_lists.csv")
