# What Makes a Spotify Playlist Popular?

## Combining Spotify Playlists with Artist Features
---
*Capstone I Project for Galvanize Data Science Immersive, Week 4*

*A Project by Luke Schroder*
## Table of Contents
---
idk fill this in later
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

The first of these sets contains information on playlists, number of followers and the tracks/artists contained in them, the next is a list of songs with features generated from the Spotify Web API. These features include sound descriptors such as tempo, valence(relative happiness), acousticness and many more ([see here](https://developer.spotify.com/documentation/web-api/reference/#object-audiofeaturesobject) for more details).

# Exploratory Data Analysis
