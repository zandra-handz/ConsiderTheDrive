# Consider The Drive

## Video Demo
https://youtu.be/8n9IwbZO6YI

## Description

Welcome to Consider The Drive, an in-terminal guide to help you choose meet-up locations for you and your friends with quick(er) drives! This program offers two features:

1. **Travel Times:** It returns varying travel times for you and your friends given a valid destination address.
2. **Meet-up Locations:** It searches for meet-up locations between friend addresses and returns a list for browsing. It utilizes an object class (`DistanceClass.py`) as its calculator vehicle for each time the program runs. Although not initially intended, the class made writing the menu program much easier!

### Entering a Destination

The program will prompt for your address, at least one friend's (plus their name), and a potential destination address. All addresses must be valid to proceed using this program. Initially built for a meetup between you and one friend, it can accommodate as many friends as you'd like for group events. It uses Google Map's API to obtain travel times and distances.

### Browsing Locations by Keyword 

The program will then ask if you want it to suggest places to meet instead. If you're already satisfied with the destination, you can decline this offer. If you accept, you can search as many keywords as you'd like ('restaurants', 'coffee', 'pizza', etc.). You will be prompted if you want to customize the settings (change the radius size or the length of the browse list) and then asked for a keyword. 

**HINT:** If this returns nothing, try modifying your keyword or adjusting the radius size of the search.

Once you are finished, the program will exit.

**Note:** I did not build a GUI for this as I intend to use it in a React app I'm developing later down the line.

Thanks for checking this out! I am deeply interested in tech that aids us in being more considerate towards each other—technological usage that serves as expressions of our compassion for our friends and loved ones. This is only the teeny-tiniest of beginnings, but I'm very excited nonetheless! Thank you for reading, and if you happen to give this a try, happy—and quicker—travels! :)
