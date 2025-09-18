# Strategic_Planning
Workflow for strategic planning using analytical framework. One of the analysis parts is audio transcriptor from Interview, processed using qualitative methodology framework which can turns into insight for business strategy

# 🎙️ Transcriptor - Audio Transcription & SWOT Analysis Tool

## 📋 Overview
Transcriptor adalah toolkit komprehensif untuk mentranskrip audio wawancara dan melakukan analisis tematik SWOT. Tool ini dirancang untuk membantu peneliti dan analis dalam mengolah data kualitatif dari wawancara menjadi insights strategis yang actionable.

## ✨ Features

### 🎧 Audio Transcription
- Support format audio M4A, WAV, MP3
- Multiple metode transkripsi (lokal dan cloud)
- Integrasi dengan OpenAI Whisper
- Script siap pakai untuk Google Colab

### 📊 Analisis Tematik SWOT
- Dashboard HTML interaktif
- Visualisasi SWOT Matrix
- Metodologi sistematis berdasarkan Naeem et al. (2023)
- Ekstraksi tema dari transkrip wawancara

### 🐳 Docker Support
- Whishper self-hosted transcription service
- LibreTranslate untuk terjemahan
- MongoDB untuk data storage
- Setup otomatis dengan script

## 📁 Struktur Folder

```
transcriptor/
├── 📄 Core Scripts
│   ├── transcribe_audio.py           # Script Python untuk transkripsi lokal
│   ├── google_colab_transcribe.py    # Script untuk Google Colab dengan Whisper
│   ├── local_transcribe.sh           # Bash script dengan berbagai opsi transkripsi
│   └── thematic_prompt.md            # Prompt untuk analisis tematik SWOT
│
├── 📊 Analisis & Output
│   ├── analisis_tematik_swot/
│   │   └── dashboard_swot_analysis.html  # Dashboard visualisasi SWOT
│   ├── Result_Transkrip_Wawancara_Renstra.txt  # Hasil transkripsi lengkap
│   └── Transkrip_Wawancara_Renstra.txt         # Transkrip singkat
│
├── 🎵 Sample Data
│   └── Wawancara Renstra dg Ketua KK BRF.m4a  # File audio sample (18MB)
│
├── 🐳 Docker Configuration
│   ├── docker-compose.yml            # Konfigurasi Docker services
│   ├── get-whishper.sh              # Script instalasi Whishper
│   ├── .env                          # Environment variables
│   └── whishper_data/               # Data directory untuk Whishper
│
└── 🐍 Python Environment
    └── transcription_env/            # Virtual environment Python

```

## 🚀 Quick Start

### Opsi 1: Google Colab (Recommended untuk pemula)

1. **Upload audio ke Google Drive**
2. **Buka Google Colab**: https://colab.research.google.com
3. **Copy script dari `google_colab_transcribe.py`**
4. **Jalankan cell demi cell**

```python
# Install Whisper
!pip install openai-whisper

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Transcribe
import whisper
model = whisper.load_model("small")
result = model.transcribe("path/to/audio.m4a", language="id")
print(result["text"])
```

### Opsi 2: Local Installation

#### Prerequisites
- Python 3.8+
- ffmpeg (untuk konversi audio)
- 4GB+ RAM untuk model Whisper

#### Setup

```bash
# Clone repository
git clone [repository-url]
cd transcriptor

# Setup Python environment
python -m venv transcription_env
source transcription_env/bin/activate  # Linux/Mac
# atau
transcription_env\Scripts\activate     # Windows

# Install dependencies
pip install openai-whisper
```

#### Run Transcription

```bash
# Menggunakan Python script
python transcribe_audio.py

# Atau menggunakan bash script
bash local_transcribe.sh
```

### Opsi 3: Docker dengan Whishper

```bash
# Run installation script
bash get-whishper.sh

# Start services
docker-compose up -d

# Access Whishper UI
# Buka browser: http://localhost:8082
```

## 📊 SWOT Analysis Dashboard

Dashboard SWOT Analysis menyediakan visualisasi interaktif dari hasil analisis tematik:

1. **Buka file**: `analisis_tematik_swot/dashboard_swot_analysis.html`
2. **Features dashboard**:
   - Matrix SWOT 2x2 interaktif
   - Tema dan sub-tema terstruktur
   - Quotation tracking
   - Export capabilities

## 🔧 Configuration

### Environment Variables (.env)
```env
# Database Configuration
DB_USER=whishper
DB_PASS=whishper

# Whishper Configuration
WHISHPER_HOST=http://localhost:8082
WHISHPER_VERSION=latest

# Performance
CPU_THREADS=4
```

### Model Options untuk Whisper
- `tiny`: Tercepat, akurasi rendah (39 MB)
- `base`: Cepat, akurasi sedang (74 MB)
- `small`: Seimbang, akurasi bagus (244 MB) **[RECOMMENDED]**
- `medium`: Lambat, akurasi sangat bagus (769 MB)
- `large`: Terlambat, akurasi terbaik (1550 MB)

## 📝 Metodologi Analisis Tematik

Tool ini mengimplementasikan metodologi 6-langkah untuk analisis tematik SWOT:

1. **Selection of Relevant Quotations**: Ekstraksi kutipan relevan
2. **Selection of Keywords**: Identifikasi kata kunci dengan kriteria 6Rs
3. **Coding**: Pengelompokan kata kunci menjadi kode
4. **Theme Development**: Organisasi kode ke dalam tema SWOT
5. **Conceptualization**: Interpretasi naratif dari tema
6. **SWOT Matrix Development**: Sintesis final dalam matrix SWOT

## 🛠️ Troubleshooting

### Issue: ffmpeg not found
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# MacOS
brew install ffmpeg

# Windows
# Download dari: https://ffmpeg.org/download.html
```

### Issue: Memory error dengan Whisper
- Gunakan model yang lebih kecil (`tiny` atau `base`)
- Atau gunakan Google Colab untuk akses GPU gratis

### Issue: Docker permission denied
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Logout dan login kembali
```

## 📚 Use Cases

1. **Penelitian Kualitatif**
   - Transkripsi wawancara mendalam
   - Focus Group Discussion (FGD)
   - Analisis tematik sistematis

2. **Strategic Planning**
   - Gap analysis organisasi
   - SWOT analysis dari data kualitatif
   - Ekstraksi insights strategis

3. **Documentation**
   - Meeting minutes automation
   - Webinar transcription
   - Podcast to text conversion

## 🤝 Contributing

Kontribusi sangat welcome! Beberapa area yang bisa dikembangkan:

- [ ] Support untuk lebih banyak format audio
- [ ] Real-time transcription
- [ ] Multi-language support
- [ ] Integration dengan cloud services (AWS, GCP, Azure)
- [ ] Advanced NLP analysis

## 🔗 Resources

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Whishper Documentation](https://whishper.net)
- [LibreTranslate](https://libretranslate.com)
- [Google Colab](https://colab.research.google.com)

## 📧 Support

Untuk bantuan dan pertanyaan:
- Buka issue di GitHub repository
- Email: [ihsanfau17@gmail.com]

---
*Last Updated: September 2024*
*Version: 1.0.0*
