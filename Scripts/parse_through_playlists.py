## Program: parse_through_playlists.py 
## Author: Kimberly Truong
## Date: July 1st, 2021
## Description: Parses through given channel ID's then finds and downloads captions for all the videos in all the playlists on that channel.
## Relevant functions:
    # get_channels(channels, youtube, save_to_csv)
        # Input: channels (list of channel IDs as strings), youtube (just the youtube variable), save_to_csv (bool)
        # Pre-Conditions: Videos of interest must be in playlists.
        # Outcome: Videos will be downloaded from all playlists on the channel (the user can choose which playlists are downloaded. Each playlist will be a seperate directory within the channel directory)
    # get_channel_id(videoID, youtube)
        # Input: videoID (string of only one video ID), youtube (just the youtube variable)
        # Outcome: Channel ID is returned.
    # get_playlists(playlists, titles, youtube, save_to_csv)
        # Input: playlists (list of playlist IDs as strings), titles (list of names for each playlist in the same order as the playlist IDs as strings), youtube (just the youtube variable), save_to_csv (bool)
        # Outcome: Videos will be saved from all given playlists and be saved to the directory with the given playlist titles.
    # get_video(videos, conference_name, youtube, save_to_csv)
        # Input: videos (list of video IDs as strings), conference_name (title of directory where the videos will be saved), youtube (just the youtube variable), save_to_csv (bool)
        # Outcome: All videos will be saved into the given directory name.

# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from linked_list import Linked_List, Video, YouTube
from csv import writer

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from six import print_


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
directory = '/Users/kimberlytruong/CMU REUSE' #insert your current directory here
video_files = 'OSS Video Files' #insert name of your video files directory here

#see https://developers.google.com/youtube/v3/docs for further information on API set-up

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json" #rename this with your client search file

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    get_channels(["UCWnPjmqvljcafA0z2U1fwKQ", "UC7c3Kb6jYCRj4JOHHZTxKsQ"], youtube, True)
    
    

def get_playlists(playlists, titles, youtube, save_to_csv: bool):

    if len(playlists) != len(titles):
        print("Error: Playlist ID's don't have matching number of titles.")
        return None

    urls = Linked_List()

    for playlistID, title in zip(playlists, titles):
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId= playlistID,
            maxResults = 50
        )
        response = request.execute()
        videos = response.get("items", [])

        try:
            os.mkdir(video_files + '/' + title) #make new directory here for playlist
        except:
            print("This directory already exists.")

        for video in videos:
            vid = Video(video["snippet"]["resourceId"]["videoId"], video["snippet"]["title"], video["snippet"]["publishedAt"], title, video["snippet"]["description"])
            vid.get_tags()
            write_to_file(vid, directory + '/' + video_files + '/' + title + '/')

            urls.append(vid)

    #writes to csv
    if save_to_csv:
        url = urls.head
        before = url

        print("Ready to write to file")

        while url != None:
            if len(url.tags) < 3:
                url = urls.delete(url, before)
            else:
                write_to_csv(url)
                if before == url:
                    url = url.next
                else:
                    before = before.next
                    url = url.next

        

def get_channels(channels, youtube, save_to_csv: bool):

    urls = Linked_List()

    for channel in channels: #get 100 video ids for each keyword, 50 4-20 mins and 50 20+ mins

        request = youtube.playlists().list(
            part = "snippet,contentDetails",
            channelId = channel,
            maxResults = 50
        )
        response = request.execute()

        playlists = response.get("items", [])

        try:
            os.mkdir(video_files + '/' + fix_title(playlists[0]["snippet"]["channelTitle"])) #make new directory here for channel
        except:
            print("This directory already exists.")
        
        for playlist in playlists:

            request = youtube.playlistItems().list(
                part="snippet",
                maxResults = 50,
                playlistId = playlist["id"] #playlist id to parse through all videos in that playlist
            )

            response = request.execute()
            videos = response.get("items", [])

            # Insures irrelevant playlists aren't downloaded. 
            # If you don't want to manually filter out playlists, comment out these two lines and the following if statement.
            print("Title of playlist: " + playlist["snippet"]["title"]) 
            choice = input("Parse through? 'y' or 'n' ")
            
            if choice == 'y':

                try:
                    os.mkdir(video_files + '/' + fix_title(playlists[0]["snippet"]["channelTitle"]) + '/' + fix_title(playlist["snippet"]["title"]))
                except:
                    print("This directory already exists.")

                for video in videos:
                    vid = Video(video["snippet"]["resourceId"]["videoId"], video["snippet"]["title"], video["snippet"]["publishedAt"], fix_title(playlist["snippet"]["title"]), video["snippet"]["description"])
                    vid.get_tags()
                    write_to_file(vid, directory + '/' + video_files + '/' + fix_title(playlists[0]["snippet"]["channelTitle"]) + '/' + fix_title(playlist["snippet"]["title"]) + '/')

                    urls.append(vid)
    
    #writes to csv
    if save_to_csv:
        url = urls.head
        before = url

        print("Ready to write to file")

        while url != None:
            if len(url.tags) < 3:
                url = urls.delete(url, before)
            else:
                write_to_csv(url)
                if before == url:
                    url = url.next
                else:
                    before = before.next
                    url = url.next

def get_video(videos, conference_name, youtube, save_to_csv:bool):

    try:
        os.mkdir(video_files + '/' + conference_name)
    except:
        print("This directory already exists.")

    for videoID in videos:

        request = youtube.videos().list(
            part = "snippet",
            id = videoID
        )
        response = request.execute()

        video = response.get("items", [])

        vid = Video(videoID, video[0]["snippet"]["title"], video[0]["snippet"]["publishedAt"], conference_name, video[0]["snippet"]["description"])
        vid.get_tags()
        write_to_file(vid, directory + '/' + video_files + '/' + conference_name + '/')
        if save_to_csv and len(vid.tags) >= 3:
            write_to_csv(vid)

def get_channel_id(videoID, youtube): #use any video from the channel

    request = youtube.videos().list(
        part = "snippet",
        id = videoID
    )
    response = request.execute()

    video = response.get("items", [])
    channelID = video[0]["snippet"]["channelId"]

    return channelID


def write_to_csv(url):
    # name of csv file 
    filename = "filtered_youtube_transcripts.csv"
        
    # writing to csv file 
    new_row = [url.title, url.pub_date, url.word_searched, [tag for tag in url.tags.keys()], url.captions, url.url]
    
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(filename, 'a') as f_object:
    
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
    
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(new_row)
    
        #Close the file object
        f_object.close()

def write_to_file(url, directory):
    f = open(directory + url.title + '.txt', "w")
    content = "Title: " + url.title + "\nPublication date: " + url.pub_date + "\nPlaylist: " + url.word_searched + "\nDescription: \n\t" + url.description
    content += "\nCaptions: \n\t" + url.captions + "\nYouTube URL: " + url.url + "\n\n\n"
    f.write(content)
    f.close() 
        
def fix_title(title):
    temp = ''
    for ch in title:
        if ch == '/':
            temp += ' '
        else:
            temp += ch
    return temp

if __name__ == "__main__":
    main()
