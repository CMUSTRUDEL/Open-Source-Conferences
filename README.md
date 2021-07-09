# Open-Source-Conferences
A dataset of transcripts and descriptions from most OSS conferences after 2013.

## Method
1. Searched for list of conferences through previous knowledge, [Wikipedia](https://en.wikipedia.org/wiki/List_of_free-software_events), and several calendars tracking FOSS events(like [this](https://calendify.com/@blinkenweb/foss-events) and [this](https://lwn.net/Calendar/Monthly/cfp/)).
2. Searched for each conference from [this list](https://docs.google.com/spreadsheets/d/1Yd5ssM62rCE3pZKQndBB6DrwdZDCovpHeSN7pCeVtvs/edit?usp=sharing) on YouTube and found their channels.
3. Collected the channel IDs from their links if labeled as a channel. Else, used any video on the channel and used the function get_channel_id() in parse_through_playlists.py to find the channel ID.
4. Plugged in the list of channel IDs to the Python script parse_through_playlists.py which creates a directory for every channel and its playlists, then writes each video to its own file with title, publication date, playlist title, description, captions, and YouTube URL. (This can also be done with singular playlists or videos).

