#currenly want to files.py and app.py is running in stramlit so nned to stop it
import streamlit as st
import pandas as pd


st.subheader("Uploading the CSV FIle")
#2 ways to upload csv file  #1st way is upload as it is
df=st.file_uploader("Upload the CSV file:",type=["csv","xlsx"])
#if df is not None:#there is some value in it the path of the file
 #st.dataframe(df)#here also download fileand zoom also

st.subheader("Loading the CSV FIle")
df=pd.read_csv("Products.csv")
if df is not None:
    st.table(df.head())#want to print in table format

st.subheader("Dealing with images directly")
st.image("img.png")#also define type

st.subheader("Dealing with images while uploading")
img_file=st.file_uploader("Upload the Image file:",type=["png","jpeg"])
if img_file is not None:
    st.image(img_file)

st.subheader("Working with Videos")
video_file=st.file_uploader("Upload the video file:",type=["mkv",'mp4',"mp3"])
if video_file is not None:
    st.video(video_file,start_time=0)#motion slow or fast by start time

st.subheader("Working with Audio")
audio_file=st.file_uploader("Upload the audio file:",type=["wav","mp3"])
if audio_file is not None:
    st.audio(audio_file.read())