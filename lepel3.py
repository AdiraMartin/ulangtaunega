import streamlit as st

def main():
    st.title("Ayok bedoa")
    
    prayer1 = st.text_input("Tulis doa pertama kamu di sini")
    prayer2 = st.text_input("Tulis doa kedua kamu di sini")
    prayer3 = st.text_input("Tulis doa ketiga kamu di sini")

    if prayer1:
        st.caption('Aamiin Ya Allah')
        st.image('mail_doa.jpg')

    elif prayer2:
        st.caption('AAMIIN YA ALLAH')
        st.image('spidermendoa.jpg')

    elif prayer3:
        st.caption('AAAAAMIIIIIIIN YA ALLAH🤲🤲😭😭😭')
        st.image('gettyimages-1134792776-612x612.jpg')

    video_path = 'Egaa.avi'

    play_button = st.button("Play Video")

    if play_button:
        st.write("Playing video...")

    st.video(video_path)

if __name__ == "__main__":
    main()
