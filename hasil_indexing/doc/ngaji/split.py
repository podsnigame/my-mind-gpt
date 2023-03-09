import os

# Membaca teks dari file
with open('./ngaji.txt', 'r') as f:
    text = f.read()

# Membagi teks menjadi halaman-halaman dengan panjang 3000 karakter
pages = [text[i:i+3000] for i in range(0, len(text), 3000)]

# Membuat direktori untuk menyimpan file txt terpisah
directory = 'pages'
if not os.path.exists(directory):
    os.makedirs(directory)

# Menyimpan setiap halaman sebagai file txt terpisah
for i, page in enumerate(pages):
    filename = os.path.join(directory, f'page_{i+1}.txt')
    with open(filename, 'w') as f:
        f.write(page)
