import streamlit as st
import textnya

def buat_lepel1():
    st.header('Is this real ega?')
    st.markdown(textnya.lepel1)

    jawaban_Q1 = st.selectbox(textnya.Q1, textnya.pilihan_Q1)

    if jawaban_Q1 == ' ':
        st.write(' ')
    elif jawaban_Q1 == 'gurita hape':
        st.info("BENEERR WKWKKW GURITA HP LU ITUU, kita kan di mekdi waktu itu ye kan")
    elif jawaban_Q1 == 'mainin idup orang':
        st.warning("WWKKWKWKWKWK MASA SIH? enggaaa laaaa")
    else:
        st.warning("bukan ih pilih lagi coba")

    
    jawaban_Q2 = st.text_input(textnya.Q2)

    if 'sulawesih' in jawaban_Q2.lower():
        st.info("bener ini namanya, emotnya 🦄 wkwkkwkwkw")
    elif 'belarus' in jawaban_Q2.lower():
        st.info(textnya.rubela)
    else:
        st.write('tar tambahin potonye')
        st.write('yelah masa kaga tau lu ah')

    audio_file = open(r"WhatsApp Audio 2023-07-16 at 15.08.08.ogg", "rb").read()

    st.markdown(f'<p style="font-size: 14px;">{textnya.Q3}</p>', unsafe_allow_html=True)
    st.audio(audio_file, format="audio/mp3")



def main():
    jawaban_Q3 = st.text_input("**Q3** di voicenote diatas kita lagi ngobrolin apa?")
    
    if 'thailand' in jawaban_Q3.lower() or 'tailan' in jawaban_Q3.lower():
        st.info('iya lagi maen maen bahasa thailand sama bahasa binatang wkwkwkkw')
        st.info(textnya.cikal)
    elif 'bahasa' in jawaban_Q3.lower():
        st.info("yaaa kita maen bahasa bahasa luar negeri sama bahasa binatang wkwkkwkw")
        st.info(textnya.cikal)
    else:
        st.info(f'wkwkwkkw gapapa kalo gatau {textnya.cikal}')
    

if __name__ == "__main__":
    main()
