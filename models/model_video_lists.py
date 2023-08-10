import os
import pandas as pd

class VideoList:
    script_path = os.path.abspath(__file__)
    # Get the absolute path of the parent directory
    parent_path = os.path.dirname(script_path)
    # Get the absolute path of the CSV file
    file_path_videos = os.path.join(parent_path, "videos.csv")
    file_path_list = os.path.join(parent_path, "video_lists.csv")
    def __init__(self, id, duration,  title=None, video=None):
        self.title = title
        self.video = video
        self.duration = duration
        self.id = id


    def get_id(self):
        return self.id

    @classmethod
    def main(self):
        # read the csv file into a data frame
        df = pd.read_csv(self.file_path_list)
        # create an empty list to store the VideoList objects
        all_list = []
        # loop through the rows of the data frame
        for index, row in df.iterrows():
            # get the values from each row
            id = row['id']
            title = row['title']
            video = row['video_ids']
            duration = row['duration']
            # check if there is video in list or not
            if pd.isna(video):
                duration=0
            # create a VideoList object with the values
            list = VideoList(id=id, title=title, video=video, duration=duration)
            # append the object to the list
            all_list.append(list)
        # return the list of objects
        return all_list

    @classmethod
    def update_list(self, list_id, new_title, new_video_ids):
        df = pd.read_csv(self.file_path_list, header=0)
        # get the index of the row that matches the list_id
        index = df.index[df.id == list_id][0]
        # update the title and video_ids columns with the new values
        df.loc[index, "title"] = new_title
        df.loc[index, "video_ids"] = new_video_ids
        # update the duration column by counting the number of video ids
        df.loc[index, "duration"] = len(new_video_ids.split(", "))
        try:
            df.to_csv(self.file_path_list, index=False)  # save the updated dataframe to the file
            return True
        except:
            return False

    @classmethod
    def delete_list(self, list_id):
        df = pd.read_csv(self.file_path_list, header=0)
        # keeping only the rows that have a different id from video_id
        df = df[df.id != list_id]
        try:
            df.to_csv(self.file_path_list, index=False)
            return True
        except:
            return False

    @classmethod
    def create_list(self, title, video_ids):
        df = pd.read_csv(self.file_path_list, header=0)
        #get duration
        duration = len(video_ids.split(", "))
        new_id = df.id.max() + 1  # generate a new id by incrementing the maximum id in the file
        new_row = [new_id, title, video_ids, duration]  # create a new row with the given parameters
        df.loc[len(df)] = new_row  # append the new row to the end of the dataframe
        try:
            df.to_csv(self.file_path_list, index=False)  # save the updated dataframe to the file
            return True
        except:
            return False

