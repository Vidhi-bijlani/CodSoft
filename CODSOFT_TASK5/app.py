import streamlit as st
import face_recognition
import cv2
import os
import numpy as np
from PIL import Image
from datetime import datetime
import time

st.set_page_config(page_title="🧑‍💻 Face Detection & Recognition", layout="wide")
st.title("🧑‍💻 Face Detection and Recognition - CodSoft Task 5")

if not os.path.exists("known_faces"):
    os.makedirs("known_faces")

@st.cache_data
def load_known_faces():
    known_encodings = []
    known_names = []
    for filename in os.listdir("known_faces"):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join("known_faces", filename)
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(filename)[0])
    return known_encodings, known_names

known_encodings, known_names = load_known_faces()
st.sidebar.success(f"Loaded {len(known_names)} users: {known_names}")

last_seen = {}
frame_count = 0
last_face_data = [] 
face_memory = {} # NEW: Remember who we saw last

tab1, tab2 = st.tabs(["📸 Upload Image", "🎥 Live Webcam"])

with tab1:
    uploaded_file = st.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB') # <-- KEY FIX HERE
        img_array = np.array(image)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        face_locations = face_recognition.face_locations(img_array)
        face_encodings = face_recognition.face_encodings(img_array, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"
            color = (0, 0, 255)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_names[best_match_index]
                    color = (0, 255, 0)
            cv2.rectangle(img_bgr, (left, top), (right, bottom), color, 3)
            cv2.putText(img_bgr, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
        st.image(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))

with tab2:
    run = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.empty()
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while run:
        ret, frame = camera.read()
        if not ret: break
        
        frame_count += 1
        current_time = time.time()
        
        if frame_count % 3 == 0:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
            
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            last_face_data = [] 
            detected_positions = [] # Track positions to match with memory
            
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                top *= 4; right *= 4; bottom *= 4; left *= 4
                center = ((left+right)//2, (top+bottom)//2)
                detected_positions.append(center)
                
                matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
                name = "Unknown"
                color = (0, 0, 255)
                
                face_distances = face_recognition.face_distance(known_encodings, face_encoding)
                if len(face_distances) > 0:
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_names[best_match_index]
                        color = (0, 255, 0)
                        face_memory[center] = (name, color, current_time) # Save to memory
                        if name not in last_seen or current_time - last_seen[name] > 3:
                            st.toast(f"✅ ACCESS GRANTED: {name}")
                            last_seen[name] = current_time
                
                # FIX: If Unknown but we saw someone here <1 sec ago, use old name
                if name == "Unknown":
                    for mem_center, (mem_name, mem_color, mem_time) in face_memory.items():
                        dist = np.linalg.norm(np.array(center) - np.array(mem_center))
                        if dist < 100 and current_time - mem_time < 1.0: # within 100px and 1 sec
                            name, color = mem_name, mem_color
                            break
                
                last_face_data.append(((top, right, bottom, left), name, color))
        
        # Clean old memory
        face_memory = {k:v for k,v in face_memory.items() if current_time - v[2] < 1.0}
        
        for (top, right, bottom, left), name, color in last_face_data:
            cv2.rectangle(frame, (left, top), (right, bottom), color, 3)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    else:
        camera.release() 