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
        # get the last modified time of the file
        # create an empty list to store the VideoList objects
        all_list = []
        # loop through the rows of the data frame
        for index, row in df.iterrows():
            # get the values from each row
            id = row['id']
            title = row['title']
            video = row['video_ids']
            duration = row['duration']
            # create a VideoList object with the values
            list = VideoList(id=id, title=title, video=video, duration=duration)
            # append the object to the list
            all_list.append(list)
        # return the list of objects and the last modified time
        return all_list

    def length(self):
        # read the csv file into a data frame
        df = pd.read_csv(self.file_path_list)
        # get the video_ids value from the object attribute
        video_ids = self.video
        # split the video_ids by comma to get a list of video ids
        video_ids = video_ids.split(",")
        # convert each video id to an integer
        video_ids = [int(id) for id in video_ids]
        # get the length of the list and store it as the duration value
        duration = len(video_ids)
        # update the duration attribute with the new value
        self.duration = duration
        # update the data frame with the new duration value for the matching id
        df.loc[df.id == self.id, 'duration'] = duration
        # save the updated data frame to the same file
        df.to_csv(self.file_path_list, index=False)

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


'''
#TODO: use this later on for create list
data = pd.read_csv("videos.csv")
# Loop through the rows in the DataFrame object
for index, row in data.iterrows():
    # Get the id value from the first column
    id_value = row["id"]
    # Do something with the id value, such as print it or store it in a variable

videos = []
for index, row in data.iterrows():
    # Create a video object with the attributes from the row
    video = Videos(row["title"], row["director"], row["rate"])
    # Assign the id value from the row as a string
    video.id = str(row["id"])
    # Add the video object to the list
    videos.append(video)

# Create a list of video list objects with random titles
video_lists = []
video_lists.append(VideoList("My Favorite Movies"))
video_lists.append(VideoList("Movies I Want to Watch"))

# Assign random ids to the video list objects
for i, video_list in enumerate(video_lists):
    video_list.id = i + 1

# Add random videos to each video list object and update the duration
for video_list in video_lists:
    # Choose a random number of videos to add, between 1 and 2
    num_videos = random.randint(1, 2)
    # Choose a random sample of videos from the videos list
    sample_videos = random.sample(videos, num_videos)
    # Add the sample videos to the video list object
    video_list.video.extend(sample_videos)
    # Update the duration of the video list object by counting the number of videos
    video_list.duration = len(video_list.video)

# Create a list of field names for the csv file
field_names = ["id", "title", "video_ids", "duration"]

# Open a new csv file with write mode
with open("../controllers/video_lists.csv", "w") as csv_file:
    # Create a csv writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
    # Write the header row
    csv_writer.writeheader()
    # Loop through the video list objects and write each one as a row
    for video_list in video_lists:
        # Create a dictionary with the video list attributes
        video_list_dict = {
            "id": video_list.id,
            "title": video_list.title,
            # Join the ids of the videos in the list with commas
            "video_ids": ",".join([video.id for video in video_list.video]),
            "duration": video_list.duration
        }
        # Write the video list dictionary as a row
        csv_writer.writerow(video_list_dict)'''
