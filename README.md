# CodSoft
# Artificial Internship - 2026


# 🖼️ Image Captioning AI - CodSoft Task 3

An AI-powered web application that generates smart captions for any uploaded image.  
Built with **Python, Streamlit, and BLIP Transformer Model**.

---

## ✨ Features

- **📤 Upload Any Image**: JPG, JPEG, PNG supported
- **🎭 4 Caption Styles**:
    - **Normal** → Simple and direct description
    - **Detailed** → Rich, descriptive captions
    - **😂 Funny** → Meme-style, car-meet captions 
    - **✨ Poetic** → Beautiful, dramatic descriptions
- **⚡ Fast & Interactive**: Powered by Streamlit for a smooth web experience
- **🧠 AI Model**: Uses `Salesforce/blip-image-captioning-base` from Hugging Face

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: Streamlit
- **AI Model**: BLIP - Bootstrapping Language-Image Pre-training
- **Libraries**: `transformers`, `torch`, `Pillow`

---

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Vidhi-bijlani/CodSoft.git
cd Image-Captioning-AI/CodSoft/Task3
```

## Demo

### Generated caption
![Error Case](Demo4.png)


# 🎬 Movie Recommendation System - CodSoft Task 4

An AI-powered Hybrid Recommendation System that suggests movies using both Collaborative and Content-Based Filtering.  
Built with **Python, Streamlit, Pandas, and Scikit-learn**.

---

## ✨ Features
- **👤 By User**: Get recommendations based on similar users' preferences
- **🔍 By Movie**: Find movies similar to the one you like based on genres
- **⚡ Fast & Interactive**: Clean Streamlit web interface with 2 tabs
- **📊 Dataset**: MovieLens Dataset - 27,000+ ratings on 9,742 movies

## 🛠️ Tech Stack
`Python` `Streamlit` `Pandas` `Scikit-learn` `Cosine Similarity` `TF-IDF`

## 🚀 How to Run
1. Install dependencies: `pip install streamlit pandas scikit-learn`
2. Run the app: `streamlit run app.py`
3. Open browser at `http://localhost:8501`

## Demo

### 📸 Way 1
![App Screenshot](Screenshot.png)

### 📸 Way 2
![App Screenshot](Screenshot2.png)


# 🧑‍💻 Face Detection and Recognition - CodSoft Task 5

A real-time AI web app that detects and recognizes faces using `Streamlit` + `OpenCV` + `face_recognition`.  
Also includes basic 🔐 **Access Control System**.

## ✨ Features
- 🎥 **Live Webcam Recognition** - Real-time face detection and recognition
- 📸 **Upload Image** - Upload any image and get instant results
- 👤 **Easy User Management** - Add new users from sidebar, no coding needed
- 🔐 **Access Control** - 🟢 Green Box = Access Granted | 🔴 Red Box = Access Denied
- ⚡ **Optimized** - Fast processing with continuous box tracking
- 📊 **User Log** - Shows "Welcome" toast when known face is detected

## 🛠️ Tech Stack
`Python` `Streamlit` `OpenCV` `dlib` `face-recognition` `Pillow` `NumPy`

## 🚀 How to Run
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
2. **Run the app**
   ```bash
   streamlit run app.py
   ```

## 📸 Demo

### Loading the website
![Demo Screenshot](loading.png)

### Way 1: Upload Image
![Demo Screenshot](upload.png)

### Way 2: Live Detection and Recognition
![Demo Screenshot](live.png)

### DEMO 1
![Demo Screenshot](live2.png)

### DEMO 2
![Demo Screenshot](live3.png)

## 📁 Project Structure
    ## 📁 Project Structure
    CODSOFT_TASK5/
    ├── app.py
    ├── known_faces/
    ├── haarcascade_frontalface_default.xml
    ├── requirements.txt
    └── README.md

# Build for CodSoft Artificial Internship - 2026
