import streamlit as st

def main():
    st.write("Hei, aku tau kadang hidup bisa terasa berat. Yuk sebentar aja kita lihat hal-hal indah yang mungkin sering kita lupa 💖")

    # Pertanyaan 1
    q1 = st.text_input("✨ Hal kecil apa yang bikin kamu tersenyum akhir-akhir ini?")
    if q1:
        st.success("Indah banget... bahkan hal kecil seperti itu bisa jadi alasan buat bersyukur 🥰")

    # Pertanyaan 2
    q2 = st.text_input("💫 Kalau inget orang yang peduli sama kamu, siapa yang pertama kali terlintas?")
    if q2:
        st.success(f"{q2} pasti bersyukur banget punya kamu dalam hidupnya ✨")

    # Pertanyaan 3
    q3 = st.text_input("🌸 Hal apa yang bikin kamu merasa damai?")
    if q3:
        st.success("Damai itu berharga banget... itu tanda hati kamu masih hangat 💖")

    # Penutup
    if q1 and q2 and q3:
        st.balloons()
        st.write("---")
        st.subheader("💌 Surat kecil untukmu")
        st.write("""
        Hari ini mungkin terasa berat, tapi aku percaya tahun ini akan bawa banyak hal indah buatmu.  
        Kamu sudah melewati banyak hal, dan kamu tetap berdiri. Itu bukti kalau kamu luar biasa.  

        Aku bersyukur banget punya kamu di hidupku.  
        Semoga setiap kali kamu lupa, game kecil ini bisa jadi pengingat:  

        **kamu dicintai, kamu cukup, kamu berharga.** 💖  
        """)

if __name__ == "__main__":
    main()
