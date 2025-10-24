theme: jekyll-theme-minimal
title: Octocat's homepage
description: Bookmark this to keep an eye on my project updates!

import tkinter as tk

# membuat jendela utama dan variabel 'tampilan' HARUS diinisialisasi
# sebelum fungsi 'tombol_klik' didefinisikan/digunakan.
root = tk.Tk()
root.title("kalkulator")
tampilan = tk.StringVar()

# fungsi untuk menangani klik tombol
def tombol_klik(simbol):
    # mengambil ekspresi yang saat ini ditampilkan di layar
    saat_ini = tampilan.get()

    # jika layar menampilkan "Error", menghapus pesan error tersebut
    if saat_ini == "Error":
        tampilan.set("")
        saat_ini = ""  # Reset saat_ini agar simbol baru bisa ditambahkan

    # jika tombol (=) diklik, menghitung hasil ekspresi yang ditampilkan
    elif simbol == "=":
        try:
            # melakukan evaluasi ekspresi matematika
            hasil = eval(saat_ini)
            # menampilkan hasil evaluasi di layar
            tampilan.set(hasil)
        except:
            # menampilkan (Error) jika terjadi kesalahan
            tampilan.set("Error")
          
    # jika tombol (AC) diklik, menghapus semua yang ada di layar
    elif simbol == "AC":
        tampilan.set("")

    # jika tombol (DEL) diklik, menghapus karakter terakhir dari layar
    elif simbol == "DEL":
        # menghapus karakter terakhir dari string
         tampilan.set(saat_ini[:-1])

    # jika tombol selain (=) dan (AC) diklik, menambahkan simbol ke ekspresi yang ada
    else:
        # menambahkan simbol ekspresi yang ada
        tampilan.set(saat_ini + simbol)

    # widget entry untuk menampilkan dan mengedit ekspresi
    masukan = tk.Entry(root, textvariable=tampilan, font=('Arial',20), bd=10, insertwidth=4, width=14, justify='right')
    masukan.grid(row=0, column=0, columnspan=4)

    # daftar simbol untuk tombol
    tombol = [
        ("AC", "DEL", "%", "/"),
        ("7", "8", "9", "*"),
        ("4", "5", "6", "-"),
        ("1", "2", "3", "+"),
        ("00", "0", ".", "="),
    ]

    # menentukan lebar tombol
    lebar_tombol = 5

    # membuat tombol2
    for i, baris in enumerate(tombol):
        for j, simbol in enumerate(baris):
            # membuat tombol dengan simbol dan menentukan fungsi yang akan dijalankan ketika tombol di klik
            tombol_baru = tk.Button(root, text=simbol, font=('Arial', 14), padx=5, pady=5, command=lambda simbol=simbol:tombol_klik(simbol))
            tombol_baru.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
            # menetapkan lebar tombol
            tombol_baru.config(width=lebar_tombol)

            #menetapkan lebar yang sama untuk setiap tombol
            root.grid_columnconfigure(j, uniform="tombol")

    # menentukan ukuran jendela
    root.resizable(False, False)

    # menjalankan aplikasi
    root.mainloop()
  
