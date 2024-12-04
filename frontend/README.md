# PHOTO CLOUD

## Table of content

- [Introduction ⚡](#introduction)
- [Features 🗂️](#features)
- [Build 🏗️](#build)


## Introduction
> This is a personal project of which I had the idea for myself. I used all of my free google storage and so wanted to create an alternative to google photo that I could self host at home


## Features
The intended features for the app are the following

>**Authentication**\
>The app must be able to handle multiple users and allow them to see only their media and the ones shared with them

>**Upload files & directories**\
>The app must enable the user to upload his own pictures / media or directly load a directory and have the media / content of the directory uploaded

>**Display media**\
>The app must present your media in a nice an easy to use interface as well as download the files back to you computer

## Build

This app is built with svelte and vite, pocketbase is used as a backend. To start it locally, use the following commands

```bash
# Node js and npm are required

## Frontend
git clone https://github.com/zornyy/photocloud.git

cd photoCloud

npm install

npm run dev

## Backend

# Download the pocketbase executable for your os
# Run it locally and open the webview
# From there, load the databaseSchema.pb file to get the database
```