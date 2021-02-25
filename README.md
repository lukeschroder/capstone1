# What Makes a Spotify Playlist Popular?

## Combining Spotify Playlists with Artist Features
*Capstone I Project for Galvanize Data Science Immersive, Week 4*

*A Project by Luke Schroder*
## Learning Objectives
- Learn how to work with pyspark for big data analysis
- Practice SQL querying in sparkSQL
- Practice EDA
## Table of Contents
- [Introduction](#Introduction)    
    - [Background and Overview](#background-and-overview)
    - [The Question](#the-question)
    - [The Data](#the-data)
- [Exploratory Data Analysis](#exploratory-data-analysis)
    - [Adressing the Join](#adressing-the-join)
    - [Missing Data in the Joined Data Set](#missing-data-in-the-joined-data-set)
    - [Distribution of Features by Artist](#distribution-of-features-by-artist)
    - [Who Are the Top Artists, What are their Features](#who-are-the-top-artists,-what-are-their-features)
- [What Makes for a Popular Playlist?](#what-makes-for-a-popular-playlist)
    - [Correlation Between Features and Playlist Popularity](#correlation-between-features-and-playlist-popularity)
- [Conclusion](#conclusion)
    - [Summary](#summary)
    - [Next Steps](#next-steps)

# Introduction
## Background and Overview
Since the advent of music streaming services at the turn of the millenium people have been intaking more songs than ever. One of the popular forms of music organization is the playlist, when a user creates a list of songs in their own collection. I've always been fascinated by the sharing of music and what makes a 'mixtape' popular.

For this project I wanted to see how a playlist gains popularity based on the types of sounds present in that playlist. 

## The Question
Are certain artists more likely to be seen in popular playlists? If the artists making up a playlist are more danceable/happy/faster will that playlist be more popular?

## The Data
To gain insights into these questions I will be looking at the conjuctions of two datasets:
    
- [The Spotify Million Playlist Challenge Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)

- [Audio features of 175k+ songs released in between 1921 and 2021 Gathered from the Spotify Web API](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data.csv)

The first of these sets contains information on playlists, number of followers and the tracks/artists contained in them, the next is a list of songs with features generated from the Spotify Web API. These features include sound descriptors such as tempo, valence(relative happiness), acousticness and many more ([see here](https://developer.spotify.com/documentation/web-api/reference/#object-audiofeaturesobject) for more details). For the purpose of this project I have decided to use a slice of the million playlist data so as to improve runtimes for my code.

# Exploratory Data Analysis
## Adressing the Join
As mentioned before I am looking at the conjuction of these two data sets in order to gain insights. I decided to use pyspark and sparkSQL to bring in the data and join these sets on artist name.
## Missing Data in the Joined Data Set
Because of the difference in size in the two datasets a fair amount of playlist data could not be matched to features. To mitigate this I decided to group the playlists by the artists they contained to match the most possible features.

- insert table showing rows for individual sets and joined

As you can see both tables contain data that is not in the other. Another piece of data cleaning that is important to mention is the fact that many artist names contain special character and formatting, to get around this issue I converted the artist names to raw strings prior to joining the data.
## Distribution of Features by Artist
- insert violinplot of features

Looking at the following chart we can see that instrumentalness (lack of lyrics) and speechiness(presence of spoken word speech-like recording) are very heavily distributed on the lower end of the possible range, this is likely due to the fact that most music has lyrics that are sung.
## Who Are the Top Artists, What are their Features
- insert barchart

An interesting thing to note here is the relative similarity between the most represented artists in the data set.

# What Makes for a Popular Playlist?
## Correlation Between Features and Playlist Popularity
- Show regplot

Something that I noticed here is the apparent negative correlation between dancability and playlist popularity I wanted to run a hypothesis test to see if this is indeed the case

- Show Alpha and P of U-test

Note that this is just based off of a slice of the playlist data, this could be different when using the whole set.

- bootstrap?

# Conclusion
## Summary
sum up section above

## Next Steps
- With a few tweaks to the code I will be able to bring in song and genre level data
- Create spotify web API applet to bring in full track feature data