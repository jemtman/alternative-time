A project currently known as: 
# "Timely Time"
 _A universal time format to draw ire._

## A displeasure with timezones
I loathe timezones and daylight savings time.  It's near impossible to know what time it is somewhere else in the world without looking it up on online. Timezones are also political and incredibly imprecise.  

This time format attempts to remedy some of those issues by turning time into two sets of numbers: a universal time, and a local time (which is based off of sunrises and sunsets). 

## Universal Time
Simply put, the universal time breaks the day down into 100 coarse time units.  Each course unit has 100 finer units. 

This universal time is the same everywhere.  The point of reference is currently the 180th meridian.  It's a better system than basing everthing around Greenwich, but still not perfect, I know. 

Every day, universal time starts at 00.00 and ends at 99.99.  

Scheduling events across timezones is easy...."let's do our call at  53.00"

## Local Time
If you're thinking that having a universal time for the whole world seems a bit cold, then you're right. 

The second element of this time offers connection with the day/night cycle, but with much more precision than 24-timezoned time.  

Two locallized numbers are given.  

When the user starts the program, they input their city.  With this information, the times of the next sunrise and sunset are shown.  

This updates every day and is accurate as the days lengthen and shorten throughout the year. 


## Advantages
As I write this, in Seattle, Washington, USA, it's around `63.00`.  The sun went down around `57.00`.  The sun will next rise around `9.00`.   With 57 minus 9 equalling almost fifty, it's appears that today might be quite near to an equinox, which is it (today is October 3rd). 

It's also nice to know that if I were scheduling a call with someone in, let's say, Tokyo, Japan, that I could figure out when a likely good time for a meeting is.  

As I write this, it's also `63.00` in Tokyo.  But the sun doesn't set there until around 85.00 today. Probably fine if I wanted to call them now.  

And if I thought tomorrow was better, we could probably figure out that something like `45.00` might be a good time, as their sunrise is at `36.00` and so they'll just be getting to work, and I'll be in the latter part of my own work day.  

## Issues
While this system simplifies and humanizes some elements of timekeeping, and collaboration, there's plenty new issues that it raises.  

Dates, for instance would become more annoying.  Especially if the date switches in the middle of your day.  That could be very confusing.  Luckily, I've kept dates out of this early version. A challenge though.

The other major issue is that I coded this like absolute trash.  I'm a beginner when it comes to coding and I've made some definite, um, comprimises where my knowledge or patience ran out. 

It needs a better interface, performance and accuracy improvements.  Support for characters that aren't printable by command prompt / terminal.  Better handling of exceptions. Currently requires and online lookup for coordinates. Plenty of other issues.  In this project's current state, it's merely a proof-of-concept, with much help needed if this ever goes anywhere. 

If this project intriuges you, please reach out.  And if you have a big math brain and/or want to help me fix the code, please also reach out.

Thanks for looking at this :) 

