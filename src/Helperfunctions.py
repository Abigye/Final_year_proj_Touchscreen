# from Touchscreen_version3 import resource_path
import os,sys

# writes to textfile
def write_to_text_file(**kwargs):
    with open('EventRecords.txt', 'a') as f:
        for key, value in kwargs.items():
            print(key, ":", value)
            f.write(key + ": " + value+"\n")
        f.write("\n")


videos = ['/Users/s1871633/Desktop/kivy_venv/touchscreen_v3/Templates/videos/climbing_clip.mp4',
          '/Users/s1871633/Desktop/kivy_venv/touchscreen_v3/Templates/videos/discrepancy.mp4',
          '/Users/s1871633/Desktop/kivy_venv/touchscreen_v3/Templates/videos/fvb.mp4',
          '/Users/s1871633/Desktop/kivy_venv/touchscreen_v3/Templates/videos/edited_1.mp4']


# function to view file
def file_to_view():
    result = []
    with open("EventRecords.txt",'r') as f:
        content = f.readlines()

        if content:
            index_of_whitespace = [0]
            index_of_whitespace.extend([i for i in range(len(content)) if content[i]== '\n'])

            result = [content[index_of_whitespace[i]+1:index_of_whitespace[i+1]]
                    for i in range(len(index_of_whitespace)-1)]
        else: 
            result = []

    return result
    





