# Open-Source-Conferences
A dataset of descriptions from most Open-Source Software conferences from January 2011 to June 2021. This dataset contains:
- Name of the video
- Publication date
- Playlist (often the conference edition)
- Description
- YouTube URL

Due to the YouTube license, we cannot show the video transcripts. Run the given scripts to get the full dataset (with transcripts).

## Get Transcripts
1. Access the [Google APIs Client Library](https://developers.google.com/youtube/v3/getting-started#before-you-start).
2. Make an API Key on the site.
3. Download the ```client_secrets.json``` file connected to you API Key. Put this in the 'Scripts' directory.
4. Install pytube.
5. In the 'Scripts' directory, run ```python3 parse_through_playlists.py [channel_ids: list] [saved directory: string]```

Where for channel_ids, you can type ```'all'``` (to get videos from all conferences in the list) or enter a list of conference ids in the following format: ```[id1, id2, id3, ..., idn]```

## Method
1. Searched for list of conferences through previous knowledge and [other sources](#sources).
2. Searched for each conference from [this list](https://docs.google.com/spreadsheets/d/1Yd5ssM62rCE3pZKQndBB6DrwdZDCovpHeSN7pCeVtvs/edit?usp=sharing) on YouTube and found their channels.
3. Collected the channel IDs from their links if labeled as a channel. Else, used any video on the channel and used the function get_channel_id() in [parse_through_playlists.py](https://github.com/xKymberlite/Open-Source-Conferences/blob/main/Scripts/parse_through_playlists.py) to find the channel ID.
4. Plugged in the list of channel IDs to the Python script parse_through_playlists.py which creates a directory for every channel and its playlists, then writes each video to its own file with title, publication date, playlist title, description, captions, and YouTube URL. (This can also be done with singular playlists or videos).

## Updates
**Last updated:** July 2021

This dataset can updated by third-parties by using the provided scripts and submitting a pull request. If there is a conference missing from the conference list, please use the suggestion feature in [Google Sheets](https://docs.google.com/spreadsheets/d/1Yd5ssM62rCE3pZKQndBB6DrwdZDCovpHeSN7pCeVtvs/edit?usp=sharing) or submit an issue on this repository.

## Sources

- [Software events Wikipedia](https://en.wikipedia.org/wiki/List_of_free-software_events)
- [FOSS events calendar](https://calendify.com/@blinkenweb/foss-events)
- [Call for proposals calendar](https://lwn.net/Calendar/Monthly/cfp/)
- [Linux Foundation events](https://events.linuxfoundation.org)
- [Mozilla speakers caldendar](https://calendar.google.com/calendar/u/0/embed?src=mozilla.com_pn0rt7a2nop8tokpcsb25jnbj8@group.calendar.google.com&ctz=America/Los_Angeles)
- [Open Source Initiative events](https://opensource.org/events)
- [OpenSource.com archived events](https://web.archive.org/web/20190321192158/https://opensource.com/resources/conferences-and-events-monthly#event-node-50461)

