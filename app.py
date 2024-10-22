import tkinter as tk
from googletrans import Translator, LANGUAGES

def cevir():
    metin = giris.get("1.0", tk.END).strip()
    dil = dilsec.get()
    # Çeviriyi yap
    translator = Translator()
    try:
        ceviri = translator.translate(metin, dest=dil)
        sonuc_alani.delete("1.0", tk.END)  # Sonuç alanını temizle
        sonuc_alani.insert(tk.END, ceviri.text)  # Çeviri sonucunu göster
    except Exception as e:
        sonuc_alani.delete("1.0", tk.END)
        sonuc_alani.insert(tk.END, f"Hata: {e}")

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Python Çeviri Uygulaması")

# Kullanıcıdan çevrilecek metni almak için metin alanı
tk.Label(pencere, text="Çevirmek istediğiniz metni girin:").pack()
giris = tk.Text(pencere, height=10, width=60)
giris.pack()

# Hedef dil seçim kutusu
tk.Label(pencere, text="Hedef dili seçin:").pack()

# Dil seçeneklerini dropdown menüye ekle
dilsec = tk.StringVar(pencere)
dilsec.set("en")  # Varsayılan olarak İngilizce seçili

dil_listesi = tk.OptionMenu(pencere, dilsec, *LANGUAGES.keys())
dil_listesi.pack()

# Çevir butonu
cevir_butonu = tk.Button(pencere, text="Çevir", command=cevir)
cevir_butonu.pack()

# Çeviri sonucunu göstermek için metin alanı
tk.Label(pencere, text="Çeviri Sonucu:").pack()
sonuc_alani = tk.Text(pencere, height=10, width=60)
sonuc_alani.pack()

# Pencereyi sürekli açık tut
pencere.mainloop()
