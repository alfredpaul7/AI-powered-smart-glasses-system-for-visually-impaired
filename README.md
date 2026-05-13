 # AI-powered smart glasses system for visually impaired 

An intelligent wearable assistive system designed to help visually impaired individuals understand and safely navigate their surroundings using real-time artificial intelligence-powered scene interpretation, multilingual translation, and voice feedback.

The system integrates:

- Raspberry Pi Zero
- 5MP Pi Camera (120° FOV)
- Flask-based secure image transmission
- Moondream Vision Language Model
- LLAMA-powered scene understanding
- pyttsx3 Offline Text-to-Speech
- MAX98357 I2S Audio Amplifier
- Bluetooth / Wired Audio Output

The smart module is:

✔ Lightweight  
✔ Detachable  
✔ 3D Printable  
✔ Compatible with personal spectacle frames  
✔ Privacy-aware  
✔ Cost-effective  

---

# Project Highlights

✔ Wearable AI smart glasses for visually impaired users  
✔ Real-time scene understanding using Moondream + LLAMA  
✔ Offline voice assistance using pyttsx3  
✔ Multilingual translation support  
✔ Bluetooth / wired audio support  
✔ Secure local processing  
✔ Detachable modular design  
✔ Live testing module using `det.py`

---
# Key Features

## Real-Time Scene Understanding

Examples:

- "A person is standing near a bicycle."
- "A chair is placed beside a table."
- "A vehicle is approaching from the left."

---
# Repository Structure

```text
AI-powered-smart-glasses-system-for-visually-impaired/
│
├── raspberry_pi/
│   ├── config.py
│   ├── camera_capture.py
│   ├── text_to_speech.py
│   ├── pi_client.py
│   └── requirements.txt
│
├── server/
│   ├── config.py
│   ├── moondream_inference.py
│   ├── app.py
│   ├── det.py
│   └── requirements.txt
│
└── README.md
```

---

# System Architecture

```text
User Environment
       ↓
5MP Pi Camera
       ↓
Raspberry Pi Zero
       ↓
Flask HTTPS Transmission
       ↓
Local AI Server
(Moondream + LLAMA)
       ↓
Scene Description
       ↓
Language Translation
       ↓
pyttsx3
       ↓
MAX98357 Amplifier
       ↓
Bluetooth / Speaker Output
       ↓
User Feedback
```

---

# System Block Diagram

<img width="1037" height="499" alt="image" src="https://github.com/user-attachments/assets/59e9b677-e8f1-41ac-ae8c-5ef5222ef303" />



---

# Circuit Diagram

<img width="803" height="661" alt="image" src="https://github.com/user-attachments/assets/cb942c4e-fd1f-40b9-91fe-6bde1aa71dff" />



---

# CAD Design

<img width="535" height="257" alt="image" src="https://github.com/user-attachments/assets/796266f7-8147-43b8-bdff-726d1e0cad40" />

<img width="370" height="245" alt="image" src="https://github.com/user-attachments/assets/63a9e5eb-a51e-4d8a-896c-fb4ff1ff58e2" />


---

# PCB Assembly

 <img width="459" height="360" alt="image" src="https://github.com/user-attachments/assets/23bf2209-67c5-49f2-a4b5-d798165aba1d" />

---

# Enclosure Design

<img width="409" height="289" alt="image" src="https://github.com/user-attachments/assets/3078aa24-f875-4b3a-b4e5-5638814976a1" />



---

# Final Prototype


<img width="831" height="623" alt="image" src="https://github.com/user-attachments/assets/b642a4ab-65e7-45d0-a539-506b44722485" />

<img width="833" height="625" alt="image" src="https://github.com/user-attachments/assets/0d10ac1b-53aa-409a-8503-5b34b9e8b4fa" />



---


# Hardware Components

| Component | Description |
|-----------|-------------|
| Raspberry Pi Zero | Main embedded controller |
| Pi Camera 5MP | 120° scene capture |
| MAX98357 | Audio amplifier |
| Bluetooth Module | Wireless audio |
| Speaker / Earbuds | Audio feedback |
| Li-ion Battery | Portable power |
| 3D Printed Enclosure | Wearable mounting |

---

# Software Modules

## Raspberry Pi Module

Responsible for:

- Capturing images
- Compressing frames
- Sending images to server
- Receiving scene descriptions
- Performing text-to-speech

Files:

```text
config.py
camera_capture.py
text_to_speech.py
pi_client.py
```

---

## Server Module

Responsible for:

- Receiving images
- Running Moondream inference
- Generating contextual scene descriptions
- Translation

Files:

```text
config.py
moondream_inference.py
app.py
```

---

## Live Testing Module

`det.py`

Features:

- Live stream preview
- Press `s` to capture frame
- Real-time Moondream inference
- Speech playback

Run:

```bash
python det.py
```

# Installation

## Clone Repository

```bash
git clone https://github.com/alfredpaul7/AI-powered-smart-glasses-system-for-visually-impaired.git

cd AI-powered-smart-glasses-system-for-visually-impaired
```

---

# Install Ollama

```bash
ollama pull moondream
```
---

# Run Server

```bash
cd server

pip install -r requirements.txt

python app.py
```

---

# Run Raspberry Pi

```bash
cd raspberry_pi

pip install -r requirements.txt

python pi_client.py
```

---

# Run Debug Mode

```bash
cd server

python det.py
```

---

# Applications

- Assistive Technology
- Smart Healthcare
- Elderly Assistance
- Navigation Assistance
- Accessibility Systems
- Wearable Robotics

---

# Future Enhancements

- Object distance estimation
- Face recognition
- OCR
- Currency recognition
- GPS navigation
- Emergency SOS
- Obstacle detection

---
