# Open-Source-Conferences
Transcripts and descriptions from most OSS conferences.

**Method**
1. Searched for list of conferences through previous knowledge, Wikipedia (https://en.wikipedia.org/wiki/List_of_free-software_events), and several calendars tracking FOSS events (https://calendify.com/@blinkenweb/foss-events and https://lwn.net/Calendar/Monthly/cfp/).
2. Searched for each conference on YouTube and found their channels.
3. Collected the channel IDs from their links if labeled as a channel. Else, used one of the playlists and my Python script to find the channel ID.
4. Plugged in the list of channel IDs to the Python script parse_through_playlists.py which creates a directory for every channel and its playlists, then writes each video to its own file with title, publication date, playlist title, description, captions, and YouTube URL.
