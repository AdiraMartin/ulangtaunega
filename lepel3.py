import streamlit as st

def main():
    st.title("Ayok Bedoa")

    # Prayer 1
    prayer1 = st.text_input("Tulis doa pertama lu disini, jangan lupa enter")
    if prayer1:
        with st.container():
            st.write(f"Doa kamu: **{prayer1}**")
            st.image("mail doa.jpg")
            st.caption("aamiin Ya Allah")

    # Prayer 2
    prayer2 = st.text_input("Ayok tulis lagi doa ke-2 nanti di aminin, ENTER")
    if prayer2:
        with st.container():
            st.write(f"Doa kamu: **{prayer2}**")
            st.image("spidermendoa.jpg")
            st.caption("AAMIIN YA ALLAH")

    # Prayer 3
    prayer3 = st.text_input("1 lagi deh yu deh, ENTEERRRRR, BIAR AAMIN PALING KERASS")
    if prayer3:
        with st.container():
            st.write(f"Doa kamu: **{prayer3}**")
            st.image("gettyimages-1134792776-612x612.jpg")
            st.caption("AAAAAMIIIIIIIN YA ALLAH 🤲🤲😭😭😭")

    # Video
    video_path = "https://youtu.be/xyMGELBwt0w"
    play_button = st.button("Play Video")

    if play_button:
        st.write("Playing video...")

    st.video(video_path)


if __name__ == "__main__":
    main()



