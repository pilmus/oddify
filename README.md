# Oddify

## Idea/origin

What if Spotify, but weirder? Spotify's recommendations are one of its greatest features, but they can get kind of stale. The idea is to build a tool that can make sure your recommendations are sufficiently _odd_.

## Goal(s?) (to be defined further)
Some ideas (not all of which play into the main idea...):
- Sliders so user can affect their recommendations on a fine-grained level
  - Candidates for the sliders could be the audio features Spotify exposes, energy, danceability, speechiness, etc.
- Place more emphasis on short or long-tailiness of the artist


Perhaps to start: 
- Find the songs you've liked, perhaps also take into account number of plays?
- Check if there's a dimension in which they are similar
  - Perhaps that is a dimension in which the user prefers consistency?
- Look for songs that are similar in the dimensions the user (apparently) considers important and dissimilar in the other dimensions.
  - Can first visualize the statistics on the audio features of my own liked songs

    
- Play only songs this user has never heard before
- One step further: play songs from artists the user has never listened to before


- How to account for growing gems? Songs that need a couple of listens for you to warm up to them?
  - Allow for songs that meet the other criteria but have been listened to only a couple of times to resurface
  - The more often they're listened to but not liked the lower the chance they'll resurface again?


- Requires access to the user's data? Or allow user to upload a playlist as a starting point?