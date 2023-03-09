import streamlit as st
import re

# fungsi untuk membersihkan teks


def clean_text(text):
    # menghapus waktu pada awal teks
    text = re.sub(r'^\(\d+:\d+:\d+\)\s*', '', text)
    # menghapus karakter selain huruf, angka, spasi, dan tanda hubung
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()  # menghapus spasi yang berlebihan
    return text


# tampilan halaman web
st.title('Membersihkan Teks')
uploaded_file = st.file_uploader('Upload file teks', type='txt')

# memproses file teks yang diupload
if uploaded_file is not None:
    # membaca teks dari file
    text = uploaded_file.read().decode('utf-8')

    # membersihkan teks
    cleaned_text = clean_text(text)

    # menampilkan teks yang telah dibersihkan
    st.subheader('Teks yang telah dibersihkan:')
    st.text_area(' ', value=cleaned_text, height=500)

    # membuat tombol untuk mengunduh teks yang telah dibersihkan
    st.download_button(
        'Unduh teks yang telah dibersihkan',
        data=cleaned_text,
        file_name='teks_bersih.txt',
        mime='text/plain'
    )
else:
    st.warning('Mohon upload file terlebih dahulu.')
