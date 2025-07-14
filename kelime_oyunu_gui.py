import pandas as pd
import random
import tkinter as tk

# Veriyi yükle
data = pd.read_csv("yenikel.csv")
df = data.copy()

class KelimeOyunu:
    def __init__(self, root):
        self.root = root
        self.root.title("İngilizce Kelime Oyunu")
        self.root.geometry("400x320")
        self.df = df
        self.min_index = df.index.min()
        self.max_index = df.index.max()
        self.dogru_sayisi = 0
        self.reset_kelime()

        # Arayüz Elemanları
        self.label_ingilizce = tk.Label(root, text=self.english_word, font=("Arial", 20))
        self.label_ingilizce.pack(pady=10)

        self.entry_cevap = tk.Entry(root, font=("Arial", 14))
        self.entry_cevap.pack(pady=5)
        self.entry_cevap.bind("<Return>", lambda event: self.kontrol_et())

        self.btn_kontrol = tk.Button(root, text="Cevabı Kontrol Et", command=self.kontrol_et)
        self.btn_kontrol.pack(pady=5)

        self.label_ipucu = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.label_ipucu.pack(pady=5)

        self.label_skor = tk.Label(root, text=f"Doğru: {self.dogru_sayisi}", font=("Arial", 12), fg="green")
        self.label_skor.pack(pady=5)

        self.label_mesaj = tk.Label(root, text="", font=("Arial", 14))
        self.label_mesaj.pack(pady=5)

    def reset_kelime(self):
        self.rastgele_index = random.randint(self.min_index, self.max_index)
        self.veri = self.df.loc[self.rastgele_index]
        self.english_word = self.veri["English"]
        self.turkish_word = self.veri["Turkish"]
        self.ipucu_index = 0
        self.ipucu_metin = ""

    def kontrol_et(self):
        cevap = self.entry_cevap.get().strip().lower()
        if cevap == self.turkish_word.lower():
            self.dogru_sayisi += 1
            self.label_skor.config(text=f"Doğru: {self.dogru_sayisi}")
            self.label_mesaj.config(text="✅ Doğru bildin!", fg="green")
            self.yeni_kelime_oto()
        else:
            if self.ipucu_index < len(self.turkish_word):
                self.ipucu_metin += self.turkish_word[self.ipucu_index]
                self.ipucu_index += 1
            self.label_ipucu.config(text=f"İpucu: {self.ipucu_metin}")
            self.label_mesaj.config(text="❌ Yanlış cevap!", fg="red")

    def yeni_kelime_oto(self):
        self.reset_kelime()
        self.label_ingilizce.config(text=self.english_word)
        self.entry_cevap.delete(0, tk.END)
        self.label_ipucu.config(text="")
        self.label_mesaj.config(text="")
        self.entry_cevap.focus_set()

# Uygulama başlat
root = tk.Tk()
app = KelimeOyunu(root)
root.mainloop()
