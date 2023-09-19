import streamlit as st

def main():
    st.title("Ayok bedoa")
    prayer1 = st.text_input("tulis doa lu disini")
    if prayer1:
            st.caption('aamiin Ya Allah')
            st.image(r'mail doa.jpg')
            
    
    prayer2 = st.text_input("ayok doa lagi tulis nanti di aminin")
    if prayer2:
            st.caption('AAMIIN YA ALLAH')
            st.image(r'spidermendoa.jpg')

    prayer3 = st.text_input("1 lagi deh yu deh")
    if prayer2:
            st.caption('AAAAAMIIIIIIIN YA ALLAH🤲🤲😭😭😭')
            st.image(r'gettyimages-1134792776-612x612.jpg')

    video_path = r'C:\Users\user\STREAMLIT\egaa.264'

    play_button = st.button("Play Video")

    if play_button:
        st.write("Playing video...")
    
    st.video(video_path)

if __name__ == "__main__":
    main()
