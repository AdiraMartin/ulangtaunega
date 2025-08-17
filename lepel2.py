import streamlit as st

def buatlepel2():
    st.write("egaaa, gue tauuu kadang kadang hidup tuh bisa terasa berat. mau gaaaa sebentaar aja kita lihat hal-hal indah yang mungkin sering kita lupa 💖")

    # Pertanyaan 1
    q1 = st.text_input("✨ Hal kecil apa yang bikin lu tersenyum akhir-akhir ini? cobak tulis yang beneerrrr")
    if q1:
        st.success("Indah banget... bahkan hal kecil seperti itu bisa jadi alasan buat bersyukur 🥰")

    # Pertanyaan 2
    q2 = st.text_input("💫 Kalau inget orang yang peduli sama lu, siapa yang pertama kali terlintas?")
    if q2:
        st.success(f"daaammn {q2} pasti bersyukur banget punya kamu dalam hidupnya ✨")

    # Pertanyaan 3
    q3 = st.text_input("🌸 Hal apa yang bikin lu merasa kek damai ajaa gituu?")
    if q3:
        st.success("Damai itu berharga banget... itu tanda hati kamu masih hangat 💖")

    # Penutup
    if q1 and q2 and q3:
        st.balloons()
        st.write("---")
        st.subheader("💌 Surat kecil untukmu")
        st.write("""
        gaaa, mungkin akhir akhir ini terasa berat, tapi guaah percaya tahun ini akan bawa banyak hal indah buat luu.  
        lu tuh keren tau udah ngelewatin banyak hal, dan LU TETEP BERDIRI. Itu bukti kalau lu luar biasaballahuakbaaarrrr.  

        guah bersyukur banget kenal ama laubrek.  
        semoga kalau setiap kali lu lupa, game kecil ini bisa jadi pengingat:  

        ven when days feel heavy, never forget this:  
        ✨ **You are worthy of love.**  
        ✨ **You are enough.**  
        ✨ **You are valuable.**  
        
        And remember...  
        🌟 You will be wealthy.  
        🌟 You will be successful.  
        🌟 You will be happy.  
        🌟 You will be at peace.  
        Because you deserve all the beautiful things life has to offer 💖 💖  aseeeekkkkkkkk ah malu
        """)

if __name__ == "__main__":
    buatlepel2()
