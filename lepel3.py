import streamlit as st

def main():
    st.title("Ayok bedoa")
    prayer1 = st.text_input("tulis doa lu disini")
    if prayer1:
            st.image(r'mail doa.jpg')
            st.text('aamiin Ya Allah')
 
    
    prayer2 = st.text_input("ayok doa lagi tulis nanti di aminin")
    if prayer2:
            st.image(r'spidermendoa.jpg')
            st.text('AAMIIN YA ALLAH')

    # Replace 'path_to_your_video.avi' with the actual path of your video
    video_path = r'C:\Users\user\STREAMLIT\egaa.264'

    play_button = st.button("Play Video")

    if play_button:
        st.write("Playing video...")
    
    st.video(video_path)

if __name__ == "__main__":
    main()
