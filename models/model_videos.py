import os
import pandas as pd
from models.model_video_lists import VideoList


class Videos:
    script_path = os.path.abspath(__file__)
    # Get the absolute path of the parent directory
    parent_path = os.path.dirname(script_path)
    # Get the absolute path of the CSV file
    file_path_videos = os.path.join(parent_path, "videos.csv")
    file_path_list = os.path.join(parent_path, "video_lists.csv")

    def __init__(self, id, plays, title=None, director=None, rate=None ):
        self.director = director
        self.rate = rate
        self.id= id
        self.title = title
        self.plays = plays

        video_list = VideoList(id=1, duration=0)
        # call the get_id() method on the instance
        self.video_list_id = video_list.get_id()

    @classmethod
    def main(self):
        # read the csv file into a data frame using a relative path
        df = pd.read_csv(self.file_path_videos)
        # create an empty list to store the VideoList objects
        all_videos = []
        # loop through the rows of the data frame

        for index, row in df.iterrows():
            id = row['id']
            title = row['title']
            director = row['director']
            rate = row['rate']
            plays = row['plays']
            # create a Videos object with the values using the class name Videos
            video = Videos(id=id, title=title, director=director, rate=rate, plays=plays)
            # append the object to the list
            all_videos.append(video)
        # return the list of objects
        return all_videos




    @classmethod
    def plays_count(self, list_id):
        # read the video_lists.csv file into a data frame
        df_list = pd.read_csv(self.file_path_list)
        try:
            # get the video_ids value from the row that matches the list_id
            video_ids = df_list.loc[df_list.id == list_id, 'video_ids'].values[0] # [0] select only first element of the result array
            # split the video_ids by comma to get a list of video ids
            video_ids = video_ids.split(",")
            # convert each video id to an integer
            video_ids = [int(id) for id in video_ids]
            # read the videos.csv file into a data frame
            df_video = pd.read_csv(self.file_path_videos)
            # increment the plays value by 1 for the rows that match the video ids
            df_video.loc[df_video.id.isin(video_ids), 'plays'] += 1
            # save the updated data frame to the same file
            df_video.to_csv(self.file_path_videos, index=False)
            # return the updated data frame or videos list
            return df_video
        except AttributeError:
            return None


    @classmethod
    def delete_video(self, video_id):
        # read file and ignore first row
        df = pd.read_csv(self.file_path_videos, header=0)
        #keeping only the rows that have a different id from video_id
        df = df[df.id != video_id]
        try:
            df.to_csv(self.file_path_videos, index=False)
            return True
        except:
            return False

    @classmethod
    def update_video(self, video_title, video_director, video_rate, video_play, video_id):
        df = pd.read_csv(self.file_path_videos, header=0)
        # get index value of these rows, then return the first element of the resulting array
        index = df.index[df.id == video_id][0]
        # update parts
        df.loc[index, "title"] = video_title
        df.loc[index, "director"] = video_director
        df.loc[index, "rate"] = video_rate
        df.loc[index, "plays"]= video_play
        try:
            df.to_csv(self.file_path_videos, index=False)
            return True
        except:
            return False


