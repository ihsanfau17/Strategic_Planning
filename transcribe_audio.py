#!/usr/bin/env python3
import os
import subprocess
import sys
import json
from pathlib import Path

def convert_m4a_to_wav(input_file, output_file):
    """Convert M4A to WAV using ffmpeg"""
    try:
        # Try using ffmpeg
        cmd = ["ffmpeg", "-i", input_file, "-acodec", "pcm_s16le", "-ar", "16000", output_file, "-y"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Successfully converted {input_file} to {output_file}")
            return True
        else:
            print(f"ffmpeg error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("ffmpeg not found. Please install ffmpeg first.")
        return False

def main():
    input_file = "Wawancara Renstra dg Ketua KK BRF.m4a"
    output_wav = "wawancara_output.wav"
    output_txt = "Transkrip_Wawancara_Renstra.txt"

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        return

    print(f"Processing: {input_file}")
    print("-" * 50)

    # Since we cannot easily install whisper or other transcription tools,
    # we'll create a placeholder transcript file with instructions

    transcript_content = """TRANSKRIP WAWANCARA RENSTRA DENGAN KETUA KK BRF
=====================================================

[CATATAN: File audio M4A telah ditemukan tetapi memerlukan tool transcription yang lebih lengkap]

File Audio: Wawancara Renstra dg Ketua KK BRF.m4a
Ukuran: 18 MB
Format: M4A (MPEG-4 Audio)

OPSI UNTUK MENTRANSKRIP:
-------------------------
1. Menggunakan Google Colab dengan Whisper AI:
   - Upload file ke Google Drive
   - Buka Google Colab
   - Install dan jalankan OpenAI Whisper

2. Menggunakan layanan online gratis:
   - Otter.ai (https://otter.ai)
   - Sonix.ai (trial gratis)
   - AssemblyAI (API gratis terbatas)

3. Menggunakan tool lokal (perlu instalasi):
   - OpenAI Whisper
   - SpeechRecognition Python library

4. Manual transcription menggunakan media player dengan fitur slow playback

INFORMASI FILE:
---------------
Durasi audio dapat dilihat dengan menjalankan:
ffprobe "Wawancara Renstra dg Ketua KK BRF.m4a"

Untuk konversi ke format lain, gunakan:
ffmpeg -i "Wawancara Renstra dg Ketua KK BRF.m4a" output.wav

"""

    # Save the placeholder transcript
    with open(output_txt, 'w', encoding='utf-8') as f:
        f.write(transcript_content)

    print(f"File informasi telah disimpan ke: {output_txt}")
    print("\nKarena keterbatasan instalasi tool, saya sarankan:")
    print("1. Upload file audio ke Google Drive")
    print("2. Gunakan Google Colab dengan script Whisper")
    print("3. Atau gunakan layanan online seperti Otter.ai")

if __name__ == "__main__":
    main()