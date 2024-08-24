import streamlit as st
import pandas as pd

# Contoh data buku dengan tambahan kolom "Isi"
data_buku = {
    'Judul': ['Hadist A', 'Hadist A', 'Hadist B', 'Hadist C', 'Hadist C'],
    'Penulis': ['Penulis A1', 'Penulis A2', 'Penulis B', 'Penulis C1', 'Penulis C2'],
    'Tahun': [2020, 2021, 2021, 2022, 2023],
    'Isi': ['lorem iskn bsbkv fe vwvwv hwre vvhwwvsvhs vsjvljvlna', 'Isi dari Hadist A2', 'Isi dari Hadist B', 'Isi dari Hadist C1', 'Isi dari Hadist C2'],
}

# Convert data ke dataframe
df_buku = pd.DataFrame(data_buku)

# Sidebar menu
st.sidebar.title("Dashboard")
# st.sidebar.image("sidebar_logo.png", use_column_width=True)
app_mode = st.sidebar.selectbox("Pilih halaman", ["Home", "Pencarian", "Daftar Hadist"])

st.sidebar.markdown("---")
# Dashboard

#Main Page
if(app_mode=="Home"):
    st.header("Dasboard")
    # image_path = "home_page.jpeg"
    # st.image(image_path,use_column_width=True)
    st.markdown("""
    Selamat datang di Web Hadist!
    """)
    st.write(f"Total Hadist: {len(df_buku)}")
    
if app_mode == "Dashboard":
    st.title("Dashboard")
    st.write("Ini adalah halaman dashboard.")
    st.write(f"Total Hadist: {len(df_buku)}")

# Pencarian
elif app_mode == "Pencarian":
    st.title("Pencarian Hadist")
    query = st.text_input("Cari Hadist berdasarkan judul atau penulis")
    if query:
        hasil = df_buku[(df_buku['Judul'].str.contains(query, case=False)) | 
                        (df_buku['Penulis'].str.contains(query, case=False))]
        
        if not hasil.empty:
            st.write(f"Hasil pencarian untuk '{query}':")
            for index, row in hasil.iterrows():
                st.markdown(f"**Judul**: {row['Judul']}  \n"
                            f"**Penulis**: {row['Penulis']}  \n"
                            f"**Tahun**: {row['Tahun']}  \n"
                            f"**Isi**: {row['Isi']}")
                st.write("---")  # Garis pemisah antar buku
        else:
            st.write("Tidak ada Hadist yang ditemukan.")
    else:
        st.write("Masukkan kata kunci untuk mencari Hadist.")

# Daftar Buku
elif app_mode == "Daftar Hadist":
    st.title("Daftar Hadist")
    st.write("Pilih judul Hadist:")

    # Menampilkan tombol untuk setiap judul buku unik
    judul_terpilih = None
    for judul in df_buku['Judul'].unique():
        if st.button(f'{judul}'):
            judul_terpilih = judul

    # Jika tombol ditekan, tampilkan buku dalam grup yang dipilih
    if judul_terpilih:
        buku_terpilih = df_buku[df_buku['Judul'] == judul_terpilih]
        st.write(f"Daftar semua '{judul_terpilih}':")
        for index, row in buku_terpilih.iterrows():
            st.markdown(f"**Judul**: {row['Judul']}  \n"
                        f"**Penulis**: {row['Penulis']}  \n"
                        f"**Tahun**: {row['Tahun']}  \n"
                        f"**Isi**: {row['Isi']}")
            st.write("---")  # Garis pemisah antar buku
