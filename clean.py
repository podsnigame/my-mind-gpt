import sys
import re

# membaca argumen command line
filename = sys.argv[1]

# membaca file teks
with open(filename, 'r') as file:
    text = file.read()

# menghapus teks yang diinginkan
text = re.sub(r'\(\d+:\d+\)\s*', '', text)

# menulis teks yang telah dibersihkan ke dalam file baru
with open(f'bersih_{filename}', 'w') as file:
    file.write(text)
