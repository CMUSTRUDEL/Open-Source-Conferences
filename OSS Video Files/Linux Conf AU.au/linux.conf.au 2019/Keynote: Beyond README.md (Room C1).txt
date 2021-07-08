Title: Keynote: Beyond README.md (Room C1)
Publication date: 2020-01-09
Playlist: linux.conf.au 2019
Description: 
	Rory Aronson

https://2019.linux.conf.au/schedule/presentation/280/

We all understand the importance of the README.md file in open-source software. But what happens when you go beyond software and begin to document your hardware and your business model too? What could happen if you transformed your documentation from a file, to a product? In this talk, Rory Aronson tells the story of how FarmBot Inc is raising the bar of what it means to have great documentation, and why it is vital to his mission and vision.

linux.conf.au is a conference about the Linux operating system, and all aspects of the thriving ecosystem of Free and Open Source Software that has grown up around it. Run since 1999, in a different Australian or New Zealand city each year, by a team of local volunteers, LCA invites more than 500 people to learn from the people who shape the future of Open Source. For more information on the conference see https://linux.conf.au/

#linux.conf.au #linux #foss #opensource
Captions: 
	00:00:00,030 --> 00:00:07,649
Rory Aronson so worries doing a talk

00:00:03,810 --> 00:00:09,780
about beyond read meet in D and we all

00:00:07,649 --> 00:00:11,940
understand the importance of the read me

00:00:09,780 --> 00:00:17,400
MD file and open source and I've lost my

00:00:11,940 --> 00:00:19,770
mouse cursor but what happens when you

00:00:17,400 --> 00:00:22,640
go beyond software and begin to document

00:00:19,770 --> 00:00:25,470
your hardware and your business model to

00:00:22,640 --> 00:00:28,470
what could happen if you transform your

00:00:25,470 --> 00:00:31,590
document your documentation from a file

00:00:28,470 --> 00:00:33,780
to a product Rory's talk and he tells

00:00:31,590 --> 00:00:36,270
the story of how farmbot Incorporated is

00:00:33,780 --> 00:00:39,000
raising the bar of what it means to have

00:00:36,270 --> 00:00:41,790
a great documentation and why it's vital

00:00:39,000 --> 00:00:53,940
to his mission and vision and give you

00:00:41,790 --> 00:01:00,059
re all right good morning LCA let's get

00:00:53,940 --> 00:01:02,489
this laptop going here all right so my

00:01:00,059 --> 00:01:05,010
name is Rory Aronson and I'm excited to

00:01:02,489 --> 00:01:07,260
be here I flew in from California to

00:01:05,010 --> 00:01:09,360
talk about going beyond the readme IMD

00:01:07,260 --> 00:01:11,159
file with your projects with your

00:01:09,360 --> 00:01:14,880
documentation and and what the

00:01:11,159 --> 00:01:17,670
ramifications of that could be so before

00:01:14,880 --> 00:01:18,810
I get started in the documentation side

00:01:17,670 --> 00:01:19,439
of things I want to take a trip down

00:01:18,810 --> 00:01:21,479
memory lane

00:01:19,439 --> 00:01:26,729
and set some context for where I'm

00:01:21,479 --> 00:01:28,320
coming from so here I am 2009 I'd had

00:01:26,729 --> 00:01:30,689
just moved out of the dorms I studied

00:01:28,320 --> 00:01:34,680
mechanical engineering in California and

00:01:30,689 --> 00:01:37,200
I'm planting my first garden so I was

00:01:34,680 --> 00:01:38,820
excited about being on my own and

00:01:37,200 --> 00:01:40,770
growing my own food and being

00:01:38,820 --> 00:01:43,140
self-sufficient so I went to the

00:01:40,770 --> 00:01:47,040
hardware store got some starters and put

00:01:43,140 --> 00:01:48,930
him in the ground and grew myself a

00:01:47,040 --> 00:01:53,399
salad there were many more of these to

00:01:48,930 --> 00:01:56,850
come but after a few months the garden

00:01:53,399 --> 00:01:58,890
kind of turned to a rubbish pile maybe

00:01:56,850 --> 00:02:01,170
some of you have been here you know I

00:01:58,890 --> 00:02:04,079
got busy with school I went out of town

00:02:01,170 --> 00:02:06,930
I got lazy I forgot to water for forgot

00:02:04,079 --> 00:02:09,690
to weed and you know inevitably the

00:02:06,930 --> 00:02:12,239
garden kind of just went to this so over

00:02:09,690 --> 00:02:13,769
the years I made a few more attempts but

00:02:12,239 --> 00:02:16,500
you know every time it kind of ended in

00:02:13,769 --> 00:02:18,180
some similar story here and that's

00:02:16,500 --> 00:02:20,659
that's really because gardening isn't my

00:02:18,180 --> 00:02:23,370
passion it's not my pastime I don't

00:02:20,659 --> 00:02:26,250
really enjoy getting down and dirty at

00:02:23,370 --> 00:02:27,930
least not really regularly you know it's

00:02:26,250 --> 00:02:32,459
fun every once in a while but it's not

00:02:27,930 --> 00:02:34,859
my passion so a few years later I was in

00:02:32,459 --> 00:02:37,349
the middle of school I decided to take

00:02:34,859 --> 00:02:39,000
in organic agriculture class and I

00:02:37,349 --> 00:02:41,579
learned about this machine this is the

00:02:39,000 --> 00:02:43,319
lettuce bot which was developed by a

00:02:41,579 --> 00:02:46,109
company blue river technologies which

00:02:43,319 --> 00:02:48,530
was later acquired by John Deere and

00:02:46,109 --> 00:02:51,000
this is actually a pretty cool machine

00:02:48,530 --> 00:02:53,549
the way this thing works is it has a

00:02:51,000 --> 00:02:56,129
camera and computer vision software

00:02:53,549 --> 00:02:58,950
price and machine learning on there and

00:02:56,129 --> 00:03:01,139
it is constantly taking pictures of the

00:02:58,950 --> 00:03:03,060
soil and the plants and it's identifying

00:03:01,139 --> 00:03:04,889
what what green things are weeds and

00:03:03,060 --> 00:03:07,739
what green things are the lettuce plants

00:03:04,889 --> 00:03:11,040
and then it uses a tilling implement to

00:03:07,739 --> 00:03:12,810
go through and selectively till the

00:03:11,040 --> 00:03:14,670
weeds under the soil I think they also

00:03:12,810 --> 00:03:16,319
have a version that that selectively

00:03:14,670 --> 00:03:19,590
sprays something to mitigate the weeds

00:03:16,319 --> 00:03:20,669
so this is pretty cool so I'm kind of

00:03:19,590 --> 00:03:22,500
looking at this and you're like wow

00:03:20,669 --> 00:03:24,989
that's neat technology I'm a

00:03:22,500 --> 00:03:27,419
technologist I'm an engineer pretty

00:03:24,989 --> 00:03:31,109
inspired by this and then I'm looking at

00:03:27,419 --> 00:03:33,900
this I'm like well you know where's the

00:03:31,109 --> 00:03:35,970
version for my backyard you know how

00:03:33,900 --> 00:03:38,099
come all I have is a hose where I'm just

00:03:35,970 --> 00:03:39,659
kind of blindly spraying water I don't

00:03:38,099 --> 00:03:41,579
really know how much and all I have is

00:03:39,659 --> 00:03:43,650
you know a shovel in my hands where's

00:03:41,579 --> 00:03:47,790
the technology that could help me do

00:03:43,650 --> 00:03:49,500
what John Deere is doing so I begin

00:03:47,790 --> 00:03:51,810
thinking about this problem I had some

00:03:49,500 --> 00:03:54,299
experience with CNC routers open source

00:03:51,810 --> 00:03:56,310
3d printers and I said hey all this

00:03:54,299 --> 00:03:58,349
stuff kind of already exists let's just

00:03:56,310 --> 00:04:01,019
combine these ideas into something that

00:03:58,349 --> 00:04:03,900
would solve my problem so I kind of took

00:04:01,019 --> 00:04:06,680
the the open-source framework of 3d

00:04:03,900 --> 00:04:10,859
printers you know three axis CNC control

00:04:06,680 --> 00:04:12,030
all precision equipment and I said all

00:04:10,859 --> 00:04:13,620
right well let's make it plant seeds

00:04:12,030 --> 00:04:15,299
let's make it Watt spray some water out

00:04:13,620 --> 00:04:17,070
there we can put some sensors on it

00:04:15,299 --> 00:04:18,209
we'll connect it to the internet and

00:04:17,070 --> 00:04:20,039
we'll control from anywhere in the world

00:04:18,209 --> 00:04:24,810
and it will grow the garden

00:04:20,039 --> 00:04:26,340
automatically in theory so in 2013 I

00:04:24,810 --> 00:04:28,770
graduated from

00:04:26,340 --> 00:04:31,560
from school and I began working on this

00:04:28,770 --> 00:04:33,480
project more seriously so I I put

00:04:31,560 --> 00:04:38,190
together a white paper about 50 pages

00:04:33,480 --> 00:04:40,980
long where I described farmbot so that's

00:04:38,190 --> 00:04:42,750
the farming robot concept that is the

00:04:40,980 --> 00:04:46,139
big 3d printer for growing your garden

00:04:42,750 --> 00:04:50,540
so I described the hardware the software

00:04:46,139 --> 00:04:50,540
I'm so embarrassed by this mock-up now

00:04:50,570 --> 00:04:55,950
the data what you could possibly do if

00:04:53,490 --> 00:04:57,720
you were you know collecting data points

00:04:55,950 --> 00:05:01,590
of the soil moisture content or the

00:04:57,720 --> 00:05:03,090
temperature every single day I developed

00:05:01,590 --> 00:05:05,010
the Bill of Materials where I did some

00:05:03,090 --> 00:05:06,540
basic research I looked at it what was

00:05:05,010 --> 00:05:08,070
out there some off-the-shelf parts and I

00:05:06,540 --> 00:05:09,150
put together this bomb and said you know

00:05:08,070 --> 00:05:12,510
what would it take to actually build

00:05:09,150 --> 00:05:14,010
this thing and I took all that and put

00:05:12,510 --> 00:05:16,500
it in this paper in open source dis I

00:05:14,010 --> 00:05:18,030
put it on the Internet under a Creative

00:05:16,500 --> 00:05:21,090
Commons license and I said you know who

00:05:18,030 --> 00:05:24,090
wants to help this ideas for everyone

00:05:21,090 --> 00:05:26,550
and I'm in chemical engineer but I need

00:05:24,090 --> 00:05:28,320
software developers and designers and

00:05:26,550 --> 00:05:32,130
all sorts of people to help make this

00:05:28,320 --> 00:05:34,710
actually happen so backing up a little

00:05:32,130 --> 00:05:36,750
bit in case you don't know john deere is

00:05:34,710 --> 00:05:39,419
not exactly the most open-source company

00:05:36,750 --> 00:05:43,440
out there they're actually quite

00:05:39,419 --> 00:05:45,690
adamantly against it in some regards so

00:05:43,440 --> 00:05:49,020
I gotta just be thinking you know kind

00:05:45,690 --> 00:05:50,850
of puts a smile on my face that some

00:05:49,020 --> 00:05:52,800
higher-ups at John Deere are just you

00:05:50,850 --> 00:05:55,380
know like oh man like open-source this

00:05:52,800 --> 00:05:58,129
is this is a kind of ridiculous like

00:05:55,380 --> 00:06:01,199
this thing is

00:05:58,129 --> 00:06:03,089
you know but they're probably thinking

00:06:01,199 --> 00:06:06,599
I'm crazy but I don't think I'm not

00:06:03,089 --> 00:06:09,330
crazy I just have different values so

00:06:06,599 --> 00:06:13,110
you know in the open sourcing of farmbot

00:06:09,330 --> 00:06:15,259
I was taking the value of of impact and

00:06:13,110 --> 00:06:18,259
putting it above the value of money

00:06:15,259 --> 00:06:18,259
where

00:06:21,229 --> 00:06:26,759
because what's what's more important to

00:06:23,369 --> 00:06:29,009
me is the ability for the work to affect

00:06:26,759 --> 00:06:30,869
change moreso than the ability for the

00:06:29,009 --> 00:06:34,050
work to make me money now I'm not ruling

00:06:30,869 --> 00:06:37,199
out the possibility of the work making

00:06:34,050 --> 00:06:41,729
money but I am putting very explicitly

00:06:37,199 --> 00:06:43,019
the impact above the money but apart

00:06:41,729 --> 00:06:44,699
from impact you know I also felt

00:06:43,019 --> 00:06:46,169
strongly about these things distributed

00:06:44,699 --> 00:06:48,629
ownership individual control the right

00:06:46,169 --> 00:06:51,149
to repair you know you go to the

00:06:48,629 --> 00:06:53,309
supermarket and you can vote with your

00:06:51,149 --> 00:06:54,779
dollars on what type of food you want to

00:06:53,309 --> 00:06:57,990
put in your body and how its produced is

00:06:54,779 --> 00:06:59,999
it done sustainably is it done and with

00:06:57,990 --> 00:07:01,860
certain practices but it's even better

00:06:59,999 --> 00:07:03,449
if you can you know control the whole

00:07:01,860 --> 00:07:05,399
process yourself either by gardening by

00:07:03,449 --> 00:07:06,839
hand or by you know potentially having a

00:07:05,399 --> 00:07:09,240
machine or an appliance to help you do

00:07:06,839 --> 00:07:12,389
that the rights repair of course is very

00:07:09,240 --> 00:07:14,869
important having true ownership over

00:07:12,389 --> 00:07:17,610
over your equipment is very important

00:07:14,869 --> 00:07:20,969
and one last thing you know everybody

00:07:17,610 --> 00:07:23,339
eats hopefully three times a day ish so

00:07:20,969 --> 00:07:26,249
of course I want to share this idea it

00:07:23,339 --> 00:07:27,360
just kind of feels right if I have food

00:07:26,249 --> 00:07:29,699
and you're hungry I want to feed you

00:07:27,360 --> 00:07:33,149
it's just a very human thing to do if I

00:07:29,699 --> 00:07:34,619
have an idea for how to grow food and I

00:07:33,149 --> 00:07:36,240
can share it with potentially millions

00:07:34,619 --> 00:07:38,969
of people on the internet for free or

00:07:36,240 --> 00:07:40,469
virtually no cost to me I should want to

00:07:38,969 --> 00:07:44,069
do that if you feel compelled to share

00:07:40,469 --> 00:07:45,959
that idea so like a lot of open source

00:07:44,069 --> 00:07:48,119
projects once you put an idea out there

00:07:45,959 --> 00:07:49,829
and if it's halfway decent and a group

00:07:48,119 --> 00:07:52,229
of people starts forming around that

00:07:49,829 --> 00:07:54,269
idea and starts working on it so these

00:07:52,229 --> 00:07:57,449
are photos from my now co-founder Tim

00:07:54,269 --> 00:07:58,889
he's over in Belgium who read the white

00:07:57,449 --> 00:08:01,829
paper he emailed me said you know I

00:07:58,889 --> 00:08:04,679
develop firmware for factory automation

00:08:01,829 --> 00:08:06,870
I want to help develop the firmware for

00:08:04,679 --> 00:08:09,160
the farmbot said great so we got him an

00:08:06,870 --> 00:08:12,850
Arduino and a ramps kit

00:08:09,160 --> 00:08:14,410
stepper motor an old 3d printer and he

00:08:12,850 --> 00:08:17,200
kind of turned it into a farm bot so

00:08:14,410 --> 00:08:19,200
there it is spraying water out so that

00:08:17,200 --> 00:08:21,670
was one of the very first prototypes

00:08:19,200 --> 00:08:24,580
there's one of my first prototypes which

00:08:21,670 --> 00:08:26,470
I used to apply for a grant from the

00:08:24,580 --> 00:08:27,970
Mark Shuttleworth Foundation I was very

00:08:26,470 --> 00:08:29,740
fortunate to get that and be able to

00:08:27,970 --> 00:08:33,669
continue working on this project with

00:08:29,740 --> 00:08:37,810
some funding so we built some prototypes

00:08:33,669 --> 00:08:39,520
this is uh in my makerspace we started

00:08:37,810 --> 00:08:42,930
kind of picking up seeds I think that's

00:08:39,520 --> 00:08:44,980
actually just a rock but close enough

00:08:42,930 --> 00:08:47,020
those are actually just a bunch of weeds

00:08:44,980 --> 00:08:51,070
but it's a cool photo looks like we're

00:08:47,020 --> 00:08:53,020
growing things and we started building

00:08:51,070 --> 00:08:56,560
you know more full-scale prototypes

00:08:53,020 --> 00:09:01,000
outdoors this is at my house in San Luis

00:08:56,560 --> 00:09:04,300
Obispo meanwhile my other now co-founder

00:09:01,000 --> 00:09:07,240
Rick he's in Chicago he was developing

00:09:04,300 --> 00:09:10,180
the web application so the control

00:09:07,240 --> 00:09:12,760
interface for for the farm bot and

00:09:10,180 --> 00:09:15,910
eventually we grew a whole garden so

00:09:12,760 --> 00:09:17,290
that's a whole bunch of Swiss chard that

00:09:15,910 --> 00:09:20,050
was the first kind of full garden that

00:09:17,290 --> 00:09:24,160
we grew we made some delicious raviolis

00:09:20,050 --> 00:09:26,530
with that and when we got to this point

00:09:24,160 --> 00:09:28,390
this was about the beginning of 2016

00:09:26,530 --> 00:09:30,310
you know our small still open source

00:09:28,390 --> 00:09:32,530
just ragtag team said you know hey we

00:09:30,310 --> 00:09:35,440
can we could probably build this into a

00:09:32,530 --> 00:09:36,490
product and bring this to the market we

00:09:35,440 --> 00:09:38,500
had been documenting everything

00:09:36,490 --> 00:09:39,880
open-source hook at this point but there

00:09:38,500 --> 00:09:42,160
are some very small number of people

00:09:39,880 --> 00:09:43,810
that were actually taking all of the

00:09:42,160 --> 00:09:44,740
initiative to build it themselves but

00:09:43,810 --> 00:09:48,030
there are a lot of people who are

00:09:44,740 --> 00:09:51,760
interested in working with the machine

00:09:48,030 --> 00:09:53,500
so we ended up making this crowdfunding

00:09:51,760 --> 00:09:55,240
video this is actually a shortened

00:09:53,500 --> 00:10:04,330
version it's just one minute long which

00:09:55,240 --> 00:10:06,130
oops oh there we go so it shows how the

00:10:04,330 --> 00:10:08,890
farm bot works and I don't need to speak

00:10:06,130 --> 00:10:11,140
because it I made it into a meme format

00:10:08,890 --> 00:10:12,250
so it tells you exactly how you how it

00:10:11,140 --> 00:10:17,600
works without you having to listen with

00:10:12,250 --> 00:10:21,940
audio so we post what was that

00:10:17,600 --> 00:10:26,540
Oh perfect who here saw the video nice

00:10:21,940 --> 00:10:28,670
it's about half of you so this thing we

00:10:26,540 --> 00:10:30,560
put it on Facebook we had a crowdfunding

00:10:28,670 --> 00:10:31,910
campaign on our website going we said

00:10:30,560 --> 00:10:34,610
you know if you're interested in this

00:10:31,910 --> 00:10:36,920
it's available for pre-order we had

00:10:34,610 --> 00:10:39,500
never really manufactured anything you

00:10:36,920 --> 00:10:47,780
know we don't really that always gets

00:10:39,500 --> 00:10:49,880
laughs that's a scene one day I need to

00:10:47,780 --> 00:10:53,780
make some documentation about the the

00:10:49,880 --> 00:10:56,960
fake it till you make it thing because

00:10:53,780 --> 00:10:58,520
there's some funny footage this is

00:10:56,960 --> 00:11:00,470
actually one of the open-source builds

00:10:58,520 --> 00:11:04,130
that somebody made in Japan at that farm

00:11:00,470 --> 00:11:05,990
all right there so we put this video on

00:11:04,130 --> 00:11:10,130
Facebook and it really just kind of blew

00:11:05,990 --> 00:11:11,810
up I think in total it probably got

00:11:10,130 --> 00:11:33,170
viewed and in about a month's time a

00:11:11,810 --> 00:11:35,720
hundred million times there we go all

00:11:33,170 --> 00:11:38,510
right so this is just an example it got

00:11:35,720 --> 00:11:40,430
reposted by a bunch of big Facebook

00:11:38,510 --> 00:11:42,620
pages tech insider was one of them so

00:11:40,430 --> 00:11:44,720
just this repost got 58 million views

00:11:42,620 --> 00:11:47,660
six hundred thousand shares a whole

00:11:44,720 --> 00:11:48,890
bunch of comments just it really blew up

00:11:47,660 --> 00:11:50,420
it kind of took the world over because

00:11:48,890 --> 00:11:52,700
it was this brand new idea people had

00:11:50,420 --> 00:11:54,320
never seen anything like it which was

00:11:52,700 --> 00:11:56,930
pretty exciting and in that first month

00:11:54,320 --> 00:12:00,260
we raised over $100,000 in preorder

00:11:56,930 --> 00:12:04,220
sales and then we were like oh great now

00:12:00,260 --> 00:12:07,460
now now we need to you know manufacture

00:12:04,220 --> 00:12:09,200
this thing and ship out 300 something

00:12:07,460 --> 00:12:10,460
pre-orders to people all over the world

00:12:09,200 --> 00:12:13,550
and up to this point we had just built

00:12:10,460 --> 00:12:16,970
ten really janky prototypes so we

00:12:13,550 --> 00:12:18,200
started kind of doing research we

00:12:16,970 --> 00:12:20,450
started working with some contract

00:12:18,200 --> 00:12:23,120
manufacturers and reviewing sample parts

00:12:20,450 --> 00:12:25,670
and injection molding stuff and getting

00:12:23,120 --> 00:12:28,000
motors made with our with our logo on it

00:12:25,670 --> 00:12:30,740
and all sorts of stuff and eventually

00:12:28,000 --> 00:12:31,230
began manufacturing a whole bunch of

00:12:30,740 --> 00:12:33,270
kits

00:12:31,230 --> 00:12:36,570
is our first warehouse back in

00:12:33,270 --> 00:12:38,100
California and eventually she started

00:12:36,570 --> 00:12:40,920
shipping them out so the first one went

00:12:38,100 --> 00:12:43,380
to my mom so that's on the left is in

00:12:40,920 --> 00:12:45,600
the FedEx office on the right is is down

00:12:43,380 --> 00:12:48,210
in San Diego in California actually made

00:12:45,600 --> 00:12:50,610
it alright and we ended up shaping them

00:12:48,210 --> 00:12:52,740
all over the world so this is kind of

00:12:50,610 --> 00:12:54,570
the first batch of the the farm bot kits

00:12:52,740 --> 00:12:56,910
and where they went about half in the US

00:12:54,570 --> 00:12:59,550
and half everywhere else including

00:12:56,910 --> 00:13:01,340
actually one here in Christchurch st.

00:12:59,550 --> 00:13:03,900
Margaret's college which i think is just

00:13:01,340 --> 00:13:07,250
well I'm all turned around about a few

00:13:03,900 --> 00:13:11,420
kilometers away for their tech to table

00:13:07,250 --> 00:13:13,470
programs that's that's pretty cool and

00:13:11,420 --> 00:13:15,420
just an example of a few of our other

00:13:13,470 --> 00:13:16,920
customers this is Garrett and Lexi Sud

00:13:15,420 --> 00:13:18,960
weeks we have a little mini documentary

00:13:16,920 --> 00:13:21,720
on our website about them they're in

00:13:18,960 --> 00:13:23,790
Utah in the United States they are

00:13:21,720 --> 00:13:25,710
really into sustainability and being

00:13:23,790 --> 00:13:27,630
self-sufficient so they got the farm

00:13:25,710 --> 00:13:29,990
about to grow their own food there's a

00:13:27,630 --> 00:13:32,970
non-profit using the technology as an

00:13:29,990 --> 00:13:35,130
accessibility tool for people who can't

00:13:32,970 --> 00:13:38,810
garden like you normally would you know

00:13:35,130 --> 00:13:42,000
down on the ground out in the garden

00:13:38,810 --> 00:13:45,720
NASA actually purchased one to figure

00:13:42,000 --> 00:13:47,220
out to how to grow food in space on the

00:13:45,720 --> 00:13:49,200
Moon and Mars one day so they kind of

00:13:47,220 --> 00:13:53,730
got it as a as something to get

00:13:49,200 --> 00:13:56,850
inspiration from so how do we get here

00:13:53,730 --> 00:13:59,300
you know it's really going back to 2013

00:13:56,850 --> 00:14:04,520
to the open sourcing of that white paper

00:13:59,300 --> 00:14:04,520
let's see I want to get my notes back up

00:14:09,560 --> 00:14:18,230
sorry about that so it really goes back

00:14:14,310 --> 00:14:18,230
to the open sourcing of the white paper

00:14:18,460 --> 00:14:22,149
but it's not like the white paper was

00:14:20,410 --> 00:14:24,550
the end-all document you know it's not

00:14:22,149 --> 00:14:26,410
like we we built that machine and then

00:14:24,550 --> 00:14:28,930
called it good and we never updated the

00:14:26,410 --> 00:14:31,089
documentation again or the source you

00:14:28,930 --> 00:14:33,760
know we were now on version 14 of

00:14:31,089 --> 00:14:36,160
farmbot which is 14 versions later than

00:14:33,760 --> 00:14:38,800
this this mock-up here of the first one

00:14:36,160 --> 00:14:41,740
so all the while we were you know making

00:14:38,800 --> 00:14:43,240
additions deletions changes and

00:14:41,740 --> 00:14:45,610
documenting all of that and updating

00:14:43,240 --> 00:14:47,050
those source files and that's really

00:14:45,610 --> 00:14:48,520
what I want to share with you today all

00:14:47,050 --> 00:14:50,339
this so far has just been kind of

00:14:48,520 --> 00:14:53,920
context for where we've come from

00:14:50,339 --> 00:14:55,870
because what's really important is how

00:14:53,920 --> 00:14:57,520
we've been open sourcing stuff and how

00:14:55,870 --> 00:14:59,589
we've been documenting and specifically

00:14:57,520 --> 00:15:00,910
how we've actually gone beyond what you

00:14:59,589 --> 00:15:04,510
all are probably used to which is just

00:15:00,910 --> 00:15:06,940
the readme file so let's let's move on

00:15:04,510 --> 00:15:08,680
here so this is the readme file here's a

00:15:06,940 --> 00:15:11,020
classic one for react JavaScript

00:15:08,680 --> 00:15:13,810
framework in theory this has everything

00:15:11,020 --> 00:15:15,790
you need to to run that work and do

00:15:13,810 --> 00:15:17,350
something useful with it this is

00:15:15,790 --> 00:15:19,360
tried-and-true stuff you all know it's

00:15:17,350 --> 00:15:22,779
this has been what we've been doing for

00:15:19,360 --> 00:15:25,990
ever but not everything is is software

00:15:22,779 --> 00:15:28,930
farmbot is obviously a lot of hardware

00:15:25,990 --> 00:15:32,050
it's also data it's community it's also

00:15:28,930 --> 00:15:34,930
a business now so how can we go beyond

00:15:32,050 --> 00:15:36,279
the readme file for these other projects

00:15:34,930 --> 00:15:38,440
and there's so many of them out there

00:15:36,279 --> 00:15:41,380
now that are not just software they're

00:15:38,440 --> 00:15:46,630
hardware they're their communities how

00:15:41,380 --> 00:15:48,700
might we go beyond readme MD so open

00:15:46,630 --> 00:15:51,779
source hardware that's a big aspect of

00:15:48,700 --> 00:15:54,970
farmbot so I want to just do a little

00:15:51,779 --> 00:15:57,089
show you really quick what we're doing

00:15:54,970 --> 00:16:00,700
this is our hardware documentation hub

00:15:57,089 --> 00:16:03,990
so it's at Genesis farmbot you can also

00:16:00,700 --> 00:16:06,430
get there at doc stuff are not BOTS oops

00:16:03,990 --> 00:16:09,670
so we have all sorts of pages here on

00:16:06,430 --> 00:16:12,880
the left you can look at the changelog

00:16:09,670 --> 00:16:14,980
of you know what we've changed over

00:16:12,880 --> 00:16:16,899
those 14 versions you have your version

00:16:14,980 --> 00:16:20,290
picker up here so you can go all the way

00:16:16,899 --> 00:16:22,300
back to that first version which many of

00:16:20,290 --> 00:16:23,980
them are not deprecated so this is kind

00:16:22,300 --> 00:16:25,600
of like diffing and github right you can

00:16:23,980 --> 00:16:27,370
see exactly what's changed here it's a

00:16:25,600 --> 00:16:31,089
little bit harder with hardware because

00:16:27,370 --> 00:16:31,660
it's not code but we do our best kind of

00:16:31,089 --> 00:16:35,080
show

00:16:31,660 --> 00:16:38,260
why we changed things and how we did

00:16:35,080 --> 00:16:40,540
that and you get down into you know the

00:16:38,260 --> 00:16:44,280
assembly instructions so how do you put

00:16:40,540 --> 00:16:47,020
everything together you know that's a

00:16:44,280 --> 00:16:49,120
basic aspect of open source hardware

00:16:47,020 --> 00:16:51,130
just how to put the thing together but

00:16:49,120 --> 00:16:52,720
even you know most products that you buy

00:16:51,130 --> 00:16:57,070
have assembly instruction so what have

00:16:52,720 --> 00:16:58,960
we done more than this in one way we've

00:16:57,070 --> 00:17:03,100
released all the CAD models so this is

00:16:58,960 --> 00:17:05,890
the source documents for the actual

00:17:03,100 --> 00:17:07,750
hardware design so if you go here we use

00:17:05,890 --> 00:17:10,600
this really awesome tool called on shape

00:17:07,750 --> 00:17:12,030
it's it's being created by from the

00:17:10,600 --> 00:17:14,800
founders of SolidWorks

00:17:12,030 --> 00:17:16,720
so if you want to figure out what is the

00:17:14,800 --> 00:17:18,970
watering also look like and maybe you

00:17:16,720 --> 00:17:22,260
want a 3d print your own you can click

00:17:18,970 --> 00:17:26,020
this and hopefully it loads up fine and

00:17:22,260 --> 00:17:28,660
within on shape you can measure you know

00:17:26,020 --> 00:17:30,730
hole diameters and and links of things

00:17:28,660 --> 00:17:33,370
you can look at the material properties

00:17:30,730 --> 00:17:35,470
you can right click and export to an STL

00:17:33,370 --> 00:17:37,840
so you can 3d print one of these parts

00:17:35,470 --> 00:17:39,370
yourself so here's the watering nozzle

00:17:37,840 --> 00:17:40,690
so anyone can load this anywhere in the

00:17:39,370 --> 00:17:44,410
world you don't even need an account to

00:17:40,690 --> 00:17:47,080
view it up here is essentially the

00:17:44,410 --> 00:17:49,720
equivalent of stars and forks on github

00:17:47,080 --> 00:17:51,670
so a bunch of people like this and two

00:17:49,720 --> 00:17:53,170
thousand something people have copied

00:17:51,670 --> 00:17:55,870
this it's the equivalent of a fork in

00:17:53,170 --> 00:17:58,360
kind of this hardware system over on the

00:17:55,870 --> 00:18:01,210
left here you can see that this watering

00:17:58,360 --> 00:18:03,430
nozzle is part of a whole folder

00:18:01,210 --> 00:18:04,720
structure of different parts of farm

00:18:03,430 --> 00:18:06,880
button at the top level you have the

00:18:04,720 --> 00:18:08,260
entire machine so people can go in here

00:18:06,880 --> 00:18:10,540
and you can actually even you do this on

00:18:08,260 --> 00:18:13,950
your phone and look at all of the

00:18:10,540 --> 00:18:13,950
different hardware it's it's pretty cool

00:18:14,670 --> 00:18:19,390
going back we also have a maintenance

00:18:17,020 --> 00:18:21,550
guide troubleshooting we will full bill

00:18:19,390 --> 00:18:23,800
of materials a lot of people come to us

00:18:21,550 --> 00:18:26,470
and say hey this is really cool but I'm

00:18:23,800 --> 00:18:28,150
not in the US and I want to build this

00:18:26,470 --> 00:18:31,300
with local materials and I want to build

00:18:28,150 --> 00:18:32,710
this with you know stuff that I can more

00:18:31,300 --> 00:18:34,240
easily access and don't need to pay a

00:18:32,710 --> 00:18:36,630
lot of shipping and import the use for

00:18:34,240 --> 00:18:38,980
and so in our building materials we have

00:18:36,630 --> 00:18:41,440
listed before you know different places

00:18:38,980 --> 00:18:43,630
of where you can buy stuff all of the

00:18:41,440 --> 00:18:44,940
tech specs so if you want to you know

00:18:43,630 --> 00:18:47,320
okay let's

00:18:44,940 --> 00:18:50,350
going to the drivetrain here I want to

00:18:47,320 --> 00:18:52,930
learn about the V wheels you can click

00:18:50,350 --> 00:18:55,140
down there and say okay look the

00:18:52,930 --> 00:18:58,390
bearings that are used are the SS loops

00:18:55,140 --> 00:19:01,420
625 - RS riffs SS equals stainless steel

00:18:58,390 --> 00:19:03,790
625 is the bearing size and - RS equals

00:19:01,420 --> 00:19:05,860
- rubber seals so you can really get in

00:19:03,790 --> 00:19:08,980
to these documents and learn all about

00:19:05,860 --> 00:19:10,180
them we have videos photos and it's

00:19:08,980 --> 00:19:13,270
really accessible it's really well

00:19:10,180 --> 00:19:17,350
organized it's all searchable and it's

00:19:13,270 --> 00:19:19,270
all versions as well we also have mods

00:19:17,350 --> 00:19:21,310
and add-ons so people come to us and

00:19:19,270 --> 00:19:23,040
they say you know oh I want to power

00:19:21,310 --> 00:19:25,600
farm about with solar how do I do that

00:19:23,040 --> 00:19:28,060
so we have ideas here it's for

00:19:25,600 --> 00:19:30,760
inspiration only you know not it's not

00:19:28,060 --> 00:19:32,710
guaranteed to work but you know these

00:19:30,760 --> 00:19:34,720
are ideas of how you can do it I did do

00:19:32,710 --> 00:19:36,370
it for that farm bot on the front so we

00:19:34,720 --> 00:19:40,750
talk about understanding hormones energy

00:19:36,370 --> 00:19:43,660
usage all sorts of stuff so that's kind

00:19:40,750 --> 00:19:45,990
of what we've done with our hardware and

00:19:43,660 --> 00:19:49,150
when you do this and you do it well

00:19:45,990 --> 00:19:50,830
people start tinkering they start

00:19:49,150 --> 00:19:52,480
building their own farm BOTS on the left

00:19:50,830 --> 00:19:54,400
there are some students in India

00:19:52,480 --> 00:19:56,650
building their own farm BOTS with kind

00:19:54,400 --> 00:20:00,220
of a modified Endor style raised bed on

00:19:56,650 --> 00:20:02,890
the right is two groups of students who

00:20:00,220 --> 00:20:06,100
both showed up independently to the same

00:20:02,890 --> 00:20:09,720
vex robotics conference with their own

00:20:06,100 --> 00:20:12,250
farm bot projects which is pretty cool

00:20:09,720 --> 00:20:14,140
we have some students at the university

00:20:12,250 --> 00:20:16,120
I went to that I sponsored who are

00:20:14,140 --> 00:20:18,790
developing a polar coordinate farmbot so

00:20:16,120 --> 00:20:21,370
it rotates around so they just right off

00:20:18,790 --> 00:20:23,500
the bat they they copied our on shape

00:20:21,370 --> 00:20:25,060
files all the CAD models and they began

00:20:23,500 --> 00:20:29,650
modifying them and changing them around

00:20:25,060 --> 00:20:31,240
to their own project you have people all

00:20:29,650 --> 00:20:33,580
over experimenting with it these are

00:20:31,240 --> 00:20:36,520
some folks in news not museum stir

00:20:33,580 --> 00:20:38,380
damned that I visited and eventually

00:20:36,520 --> 00:20:40,060
people actually compile your source into

00:20:38,380 --> 00:20:41,620
something useful and run it and you get

00:20:40,060 --> 00:20:44,920
this cool output which is stuff that you

00:20:41,620 --> 00:20:47,260
can actually eat people start sharing it

00:20:44,920 --> 00:20:48,670
on Instagram and Twitter garden robot

00:20:47,260 --> 00:20:51,670
has been working hard nothing like fresh

00:20:48,670 --> 00:20:53,650
carrots right from the ground and this

00:20:51,670 --> 00:20:56,210
one just speaks for itself pretty

00:20:53,650 --> 00:20:59,119
awesome this is in Japan

00:20:56,210 --> 00:21:01,279
all right so open-source community how

00:20:59,119 --> 00:21:03,350
can you do that we actually have a

00:21:01,279 --> 00:21:06,980
really good example right here at LCA

00:21:03,350 --> 00:21:09,230
it's the code of conduct so huge hats

00:21:06,980 --> 00:21:11,600
off to the organizers of this event for

00:21:09,230 --> 00:21:14,809
not only having the code of conduct but

00:21:11,600 --> 00:21:16,369
making it very clear that hey this is a

00:21:14,809 --> 00:21:17,840
guiding document this is the source

00:21:16,369 --> 00:21:19,759
document for our community this is

00:21:17,840 --> 00:21:21,080
really important it's posted up all over

00:21:19,759 --> 00:21:23,450
the place it's on the website

00:21:21,080 --> 00:21:25,759
it's in the opening presentations this

00:21:23,450 --> 00:21:28,399
is really important this is the source

00:21:25,759 --> 00:21:30,379
of a community so anytime somebody on

00:21:28,399 --> 00:21:32,720
your team if you're gonna try and adopt

00:21:30,379 --> 00:21:34,720
a code of conduct ask them would you run

00:21:32,720 --> 00:21:36,169
a library that didn't have a readme file

00:21:34,720 --> 00:21:38,149
probably not

00:21:36,169 --> 00:21:39,740
would you join a community that didn't

00:21:38,149 --> 00:21:42,409
have a code of conduct probably

00:21:39,740 --> 00:21:45,320
shouldn't so this is this has been a

00:21:42,409 --> 00:21:48,470
huge trend in recent years of adopting

00:21:45,320 --> 00:21:50,960
these big thanks to the people at

00:21:48,470 --> 00:21:53,539
contributor covenant over 200,000

00:21:50,960 --> 00:21:55,009
projects are not using that code of

00:21:53,539 --> 00:21:57,710
conduct so it's a great way to see it

00:21:55,009 --> 00:22:01,159
started quickly and you know this is

00:21:57,710 --> 00:22:03,860
this is open sourcing how to build a

00:22:01,159 --> 00:22:05,950
community so that's really cool Def Con

00:22:03,860 --> 00:22:07,970
it just came to my attention from

00:22:05,950 --> 00:22:10,070
Shannon who told me yesterday she

00:22:07,970 --> 00:22:12,799
another speaker that Def Con has

00:22:10,070 --> 00:22:15,919
transparency reports for how their code

00:22:12,799 --> 00:22:19,639
of conduct has been enforced so this is

00:22:15,919 --> 00:22:21,980
really important places to improve and

00:22:19,639 --> 00:22:24,740
in this area I think how to actually

00:22:21,980 --> 00:22:27,440
build a safety team I selected a few

00:22:24,740 --> 00:22:28,700
people that I trust but like there's got

00:22:27,440 --> 00:22:30,220
to be a little bit more of a process how

00:22:28,700 --> 00:22:32,690
do you prevent burnout stuff like that

00:22:30,220 --> 00:22:34,039
incident case studies DEFCON is moving

00:22:32,690 --> 00:22:36,289
in that direction but I'd like to see

00:22:34,039 --> 00:22:38,600
you know when a certain type of incident

00:22:36,289 --> 00:22:41,299
happens what are some like steps I

00:22:38,600 --> 00:22:43,999
should go through to protect privacy to

00:22:41,299 --> 00:22:48,470
protect the safety team all of that

00:22:43,999 --> 00:22:51,049
stuff open-source business is an

00:22:48,470 --> 00:22:53,809
interesting one so what does it look

00:22:51,049 --> 00:22:56,330
like to open source your company not

00:22:53,809 --> 00:22:59,149
just the products but you know the

00:22:56,330 --> 00:23:02,119
actual inner workings of a business the

00:22:59,149 --> 00:23:03,200
legalities the taxes all that stuff so

00:23:02,119 --> 00:23:05,029
this is some steps that we're taking

00:23:03,200 --> 00:23:08,889
with farmbot we actually just announced

00:23:05,029 --> 00:23:12,230
a new documentation hub for

00:23:08,889 --> 00:23:14,029
there's this great TED talk by nathan

00:23:12,230 --> 00:23:15,440
seidle he's the the founder of spark

00:23:14,029 --> 00:23:18,350
funny electronics they do all open

00:23:15,440 --> 00:23:20,450
source hardware electronic gizmos and

00:23:18,350 --> 00:23:22,549
and the point of his talk is that if

00:23:20,450 --> 00:23:24,169
your idea can be sold it will be do you

00:23:22,549 --> 00:23:25,940
take that and you extend it to business

00:23:24,169 --> 00:23:32,509
I think it's you know if you have a

00:23:25,940 --> 00:23:34,279
business you have competitors and so you

00:23:32,509 --> 00:23:37,850
know when you look at this and you look

00:23:34,279 --> 00:23:41,059
at the global economy and all the people

00:23:37,850 --> 00:23:42,889
out there you know what if we just

00:23:41,059 --> 00:23:46,129
flipped this whole ruthlessly

00:23:42,889 --> 00:23:48,259
competitive profit-mongering business

00:23:46,129 --> 00:23:52,090
world on its head and we actually looked

00:23:48,259 --> 00:23:56,059
at our competitors more as collaborators

00:23:52,090 --> 00:23:58,039
and we instead of being afraid of

00:23:56,059 --> 00:24:00,230
competitors we actually welcomed them

00:23:58,039 --> 00:24:02,149
with open arms and said hey we're all

00:24:00,230 --> 00:24:07,129
working towards some common goal here

00:24:02,149 --> 00:24:08,869
how can we learn from each other so we

00:24:07,129 --> 00:24:12,830
just launched this other documentation

00:24:08,869 --> 00:24:15,559
hub for farmbot Inc itself you can look

00:24:12,830 --> 00:24:18,169
at in case you're interested how to pay

00:24:15,559 --> 00:24:19,879
your California sales and use tax which

00:24:18,169 --> 00:24:21,409
is quite a convoluted process but I

00:24:19,879 --> 00:24:23,090
documented it and hopefully somebody can

00:24:21,409 --> 00:24:27,289
learn from that you can see what vendors

00:24:23,090 --> 00:24:29,210
we use you can see oops statistics about

00:24:27,289 --> 00:24:31,070
our products so you can see stuff like

00:24:29,210 --> 00:24:33,649
how many units we manufactured what the

00:24:31,070 --> 00:24:38,090
cost was to manufacture those the sales

00:24:33,649 --> 00:24:39,619
the margin the profit the complexity as

00:24:38,090 --> 00:24:42,580
it's changed over time you can get a

00:24:39,619 --> 00:24:45,409
look into the impact that we're making

00:24:42,580 --> 00:24:47,389
we have our documentation style guide a

00:24:45,409 --> 00:24:48,980
lot of these things are what you might

00:24:47,389 --> 00:24:51,200
find on an internal company wiki or

00:24:48,980 --> 00:24:53,830
maybe we be provided to shareholders

00:24:51,200 --> 00:24:56,480
only but we're making all this public

00:24:53,830 --> 00:24:58,220
you can figure out how we fulfill orders

00:24:56,480 --> 00:24:59,929
if you're a hardware business trying to

00:24:58,220 --> 00:25:01,700
figure out how to ship with UPS

00:24:59,929 --> 00:25:03,590
internationally using shipstation

00:25:01,700 --> 00:25:04,789
you can look at our documentation and

00:25:03,590 --> 00:25:06,619
get a little bit more insight into how

00:25:04,789 --> 00:25:08,389
to do that because it's it's not always

00:25:06,619 --> 00:25:10,220
the easiest to set up these processes

00:25:08,389 --> 00:25:13,809
and especially making them streamlined

00:25:10,220 --> 00:25:16,429
and before specific types of businesses

00:25:13,809 --> 00:25:18,679
our compensation formula this is

00:25:16,429 --> 00:25:21,109
actually inspired by an open

00:25:18,679 --> 00:25:23,889
compensation formula from buffer which

00:25:21,109 --> 00:25:23,889
I'll talk about short

00:25:24,490 --> 00:25:29,990
let's see here replacement parts and

00:25:27,470 --> 00:25:31,820
returns so this is also really good for

00:25:29,990 --> 00:25:33,620
just even onboarding new employees and

00:25:31,820 --> 00:25:35,660
training them because all of its in this

00:25:33,620 --> 00:25:42,020
document that's that's very available

00:25:35,660 --> 00:25:44,150
for people let's see here so going back

00:25:42,020 --> 00:25:45,440
to this I think you know a lot of people

00:25:44,150 --> 00:25:46,970
probably are out there being like you

00:25:45,440 --> 00:25:48,380
know you're gonna collaborate with your

00:25:46,970 --> 00:25:54,050
competitors like what is what does that

00:25:48,380 --> 00:25:57,050
even mean but I think it's really

00:25:54,050 --> 00:25:58,610
valuable this is how I've built farmbot

00:25:57,050 --> 00:26:00,440
to what it is today I was looking at

00:25:58,610 --> 00:26:02,570
companies like buffer and their

00:26:00,440 --> 00:26:04,130
transparency dashboard so they share all

00:26:02,570 --> 00:26:05,870
sorts of stuff they have a salary

00:26:04,130 --> 00:26:07,940
calculator they share their revenues

00:26:05,870 --> 00:26:11,180
they share their pricing model their

00:26:07,940 --> 00:26:12,830
values they even have a public Trello

00:26:11,180 --> 00:26:14,810
board for their product roadmap where

00:26:12,830 --> 00:26:17,450
people can go in and make requests and

00:26:14,810 --> 00:26:19,040
see what's going on this is all really

00:26:17,450 --> 00:26:22,420
valuable and I learned a lot from it and

00:26:19,040 --> 00:26:22,420
I kind of want to give back in that way

00:26:22,660 --> 00:26:27,290
so I guess I hardly did that demo I

00:26:25,370 --> 00:26:29,510
skipped ahead there so you can look at

00:26:27,290 --> 00:26:32,810
our company docks at Meadow dot farm da

00:26:29,510 --> 00:26:35,750
pod and already we just we just

00:26:32,810 --> 00:26:37,130
published those about two months ago and

00:26:35,750 --> 00:26:38,930
we've gotten some great feedback we're

00:26:37,130 --> 00:26:40,520
thinking about the future of one of our

00:26:38,930 --> 00:26:41,960
hardware projects and this is an

00:26:40,520 --> 00:26:43,850
interesting reference as we move forward

00:26:41,960 --> 00:26:47,600
such a great demonstration of openness

00:26:43,850 --> 00:26:50,210
that's from an executive director of a

00:26:47,600 --> 00:26:52,730
research institute so you know kind of a

00:26:50,210 --> 00:26:54,920
higher up in a larger organization all

00:26:52,730 --> 00:26:57,320
the way down to you know just a person

00:26:54,920 --> 00:26:59,630
on hackaday comm who's excited about

00:26:57,320 --> 00:27:01,820
starting a chicken coop operation and

00:26:59,630 --> 00:27:03,410
automating it so I think there's a lot

00:27:01,820 --> 00:27:07,430
of value in sharing these types of

00:27:03,410 --> 00:27:11,090
things especially for people or aspiring

00:27:07,430 --> 00:27:15,140
entrepreneurs so what does it all mean

00:27:11,090 --> 00:27:17,620
well when we open sourced something or

00:27:15,140 --> 00:27:22,820
giving people power or empowering them

00:27:17,620 --> 00:27:25,840
to develop software to build hardware to

00:27:22,820 --> 00:27:29,570
make communities and to start businesses

00:27:25,840 --> 00:27:32,090
so I'm really really excited to see what

00:27:29,570 --> 00:27:35,530
all of you do when you go beyond the

00:27:32,090 --> 00:27:35,530
readme MD thank you

00:27:40,700 --> 00:27:43,869

YouTube URL: https://www.youtube.com/watch?v=492NBT-BCso


