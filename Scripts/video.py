from pytube import YouTube

class Video:

    def __init__(self, videoID, title, pub_date, word_searched, description):
        self.videoID = videoID
        self.url = "https://www.youtube.com/watch?v=" + videoID
        self.title = self.fix_title(title)
        self.pub_date = self.fix_pub_date(pub_date)
        self.word_searched = word_searched
        self.tags = {}
        self.captions = ""
        self.no_captions = False
        self.description = description

        self.next = None

    def fix_title(self, title):
        temp = ''
        for ch in title:
            if ch == '/':
                temp += ' '
            else:
                temp += ch
        return temp
    
    def get_tags(self):
        yt = YouTube(self.url)
        try:
            if 'en' in yt.captions:
                caption = yt.captions['en']
            elif 'a.en' in yt.captions:
                caption = yt.captions['a.en']
            self.format(caption.generate_srt_captions())
            #self.captions = str(caption.generate_srt_captions())
            self.filter()
        except: #Runs exception if there're no captions at all
            print("No captions invoked") 
            self.no_captions = True #this part works correctly

    def format(self, caption):

        nums = False #there are numbers in the line
        last = True #first character in line
        first = True
        saved = ""
        for ch in caption:
            if ch == '\n':
                last = True
                first = True
            elif first and last:
                last = False
                if not nums:
                    self.captions += saved
                saved = ""
            elif first and not last:
                first = False

            if nums and not(ch >= '0' and ch <= '9') and not ch == '\n':
                nums = False
            elif first and (ch >= '0' and ch <= '9'):
                nums = True
            saved += ch

    def filter(self):
        keywords = ["open source", "leave", "toxic", "quit", "pause", "disengage", "burnout", "maintainer", "core maintainer", "stepping down", "time", "money", "volunteer", "payment", "stress", "disappointment", "mental health", "hostile", "conflict", "hostility", "limited time", "no time", "lack of resources", "compensation"] #each key word has a count, leave
        #might want to change key words for each search term
        
        for keyword in keywords:
            if keyword in self.captions:
                if keyword in self.tags.keys():
                    self.tags[keyword] += 1
                else:
                    self.tags[keyword] = 1


    def fix_pub_date(self, pub_date):
        date = ""
        for i in range(10):
            date += pub_date[i]
        return date
        #2020-09-09T16:00:02Z  --> 2020-09-09

    def __str__(self):
        return f"Title: {self.title}\nPublication date: {self.pub_date} \nWord searched: {self.word_searched}\nKeywords found: {self.tags}\nCaptions: {self.captions}\nYouTube URL: {self.url}"
    
