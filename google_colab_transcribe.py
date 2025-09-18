# Script untuk Google Colab - Transcribe Audio menggunakan Whisper
# ================================================================
#
# INSTRUKSI PENGGUNAAN:
# 1. Upload file "Wawancara Renstra dg Ketua KK BRF.m4a" ke Google Drive Anda
# 2. Buka Google Colab (https://colab.research.google.com)
# 3. Buat notebook baru dan copy-paste kode di bawah ini
# 4. Jalankan setiap cell satu per satu

# Cell 1: Install Whisper
!pip install openai-whisper

# Cell 2: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Cell 3: Import libraries
import whisper
import os

# Cell 4: Load model dan transcribe
# Ganti path sesuai lokasi file Anda di Google Drive
audio_path = "/content/drive/MyDrive/Wawancara Renstra dg Ketua KK BRF.m4a"

# Load model (pilih salah satu):
# - "tiny" : Paling cepat, akurasi rendah
# - "base" : Cepat, akurasi sedang
# - "small" : Sedang, akurasi bagus (RECOMMENDED)
# - "medium" : Lambat, akurasi sangat bagus
# - "large" : Paling lambat, akurasi terbaik

model = whisper.load_model("small")

# Transcribe audio
print("Memulai transcription... (ini mungkin memakan waktu beberapa menit)")
result = model.transcribe(audio_path, language="id")  # Gunakan language="id" untuk Bahasa Indonesia

# Cell 5: Tampilkan hasil
print("HASIL TRANSCRIPTION:")
print("=" * 50)
print(result["text"])

# Cell 6: Simpan ke file teks
output_path = "/content/drive/MyDrive/Transkrip_Wawancara_Renstra.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write("TRANSKRIP WAWANCARA RENSTRA DENGAN KETUA KK BRF\n")
    f.write("=" * 50 + "\n\n")
    f.write(result["text"])

    # Optional: Simpan dengan timestamp
    f.write("\n\n" + "=" * 50 + "\n")
    f.write("TRANSKRIP DENGAN TIMESTAMP:\n")
    f.write("=" * 50 + "\n\n")

    for segment in result["segments"]:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        f.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")

print(f"\nTranskrip telah disimpan ke: {output_path}")

# Cell 7: Download file hasil (optional)
from google.colab import files
files.download(output_path)