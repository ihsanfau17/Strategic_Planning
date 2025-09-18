#!/bin/bash

# Script untuk mentranskrip audio menggunakan Whisper secara lokal
# =================================================================

echo "Script Transcription Audio Lokal"
echo "================================="
echo ""

# Nama file
INPUT_FILE="Wawancara Renstra dg Ketua KK BRF.m4a"
OUTPUT_TXT="Transkrip_Wawancara_Renstra.txt"

# Check if file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' tidak ditemukan!"
    exit 1
fi

echo "Opsi 1: Menggunakan Whisper CLI (jika sudah terinstall)"
echo "---------------------------------------------------------"
echo "Jalankan command berikut:"
echo ""
echo "whisper \"$INPUT_FILE\" --language Indonesian --model small --output_format txt"
echo ""

echo "Opsi 2: Menggunakan Python dengan virtual environment"
echo "------------------------------------------------------"
echo "# Buat virtual environment"
echo "python3 -m venv venv_transcribe"
echo ""
echo "# Aktifkan virtual environment"
echo "source venv_transcribe/bin/activate"
echo ""
echo "# Install whisper"
echo "pip install openai-whisper"
echo ""
echo "# Jalankan transcription dengan Python"
echo "python3 -c \""
echo "import whisper"
echo "model = whisper.load_model('small')"
echo "result = model.transcribe('$INPUT_FILE', language='id')"
echo "with open('$OUTPUT_TXT', 'w', encoding='utf-8') as f:"
echo "    f.write('TRANSKRIP WAWANCARA\\n')"
echo "    f.write('=' * 50 + '\\n\\n')"
echo "    f.write(result['text'])"
echo "print('Transcription selesai! File disimpan ke: $OUTPUT_TXT')"
echo "\""
echo ""

echo "Opsi 3: Menggunakan layanan online gratis"
echo "------------------------------------------"
echo "1. Otter.ai:"
echo "   - Buka https://otter.ai"
echo "   - Sign up gratis (600 menit/bulan gratis)"
echo "   - Upload file audio"
echo "   - Download hasil transcription"
echo ""
echo "2. AssemblyAI:"
echo "   - Buka https://www.assemblyai.com"
echo "   - Sign up untuk API key gratis"
echo "   - Gunakan API untuk transcribe"
echo ""
echo "3. Sonix.ai:"
echo "   - Buka https://sonix.ai"
echo "   - Free trial 30 menit"
echo "   - Upload dan download hasil"
echo ""

echo "File audio ditemukan: $INPUT_FILE"
echo "Ukuran: $(ls -lh "$INPUT_FILE" | awk '{print $5}')"