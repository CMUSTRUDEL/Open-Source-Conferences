# Open-Source-Conferences
A dataset of transcripts and descriptions from most OSS conferences after 2013.

## Method
1. Searched for list of conferences through previous knowledge and [other sources](#sources).
2. Searched for each conference from [this list](https://docs.google.com/spreadsheets/d/1Yd5ssM62rCE3pZKQndBB6DrwdZDCovpHeSN7pCeVtvs/edit?usp=sharing) on YouTube and found their channels.
3. Collected the channel IDs from their links if labeled as a channel. Else, used any video on the channel and used the function get_channel_id() in parse_through_playlists.py to find the channel ID.
4. Plugged in the list of channel IDs to the Python script parse_through_playlists.py which creates a directory for every channel and its playlists, then writes each video to its own file with title, publication date, playlist title, description, captions, and YouTube URL. (This can also be done with singular playlists or videos).

### Sources

- [Software events Wikipedia](https://en.wikipedia.org/wiki/List_of_free-software_events)
- [FOSS events calendar](https://calendify.com/@blinkenweb/foss-events)
- [Call for proposals calendar](https://lwn.net/Calendar/Monthly/cfp/)
- [Linux Foundation events](https://events.linuxfoundation.org)
- [Mozilla speakers caldendar](https://calendar.google.com/calendar/u/0/embed?src=mozilla.com_pn0rt7a2nop8tokpcsb25jnbj8@group.calendar.google.com&ctz=America/Los_Angeles)
- [Open Source Initiative events](https://opensource.org/events)
- [OpenSource.com archived events](https://web.archive.org/web/20190321192158/https://opensource.com/resources/conferences-and-events-monthly#event-node-50461)

