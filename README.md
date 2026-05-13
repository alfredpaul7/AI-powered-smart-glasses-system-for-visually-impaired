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

<img width="1037" height="499" alt="image" src="https://github.com/user-attachments/assets/f7dacd55-4be7-4871-b8e7-aa30aec6ac97" />


---

# Circuit Diagram

<img width="803" height="661" alt="image" src="https://github.com/user-attachments/assets/d8847c87-332f-46e1-af06-a9b4ef27aa8e" />


---

# CAD Design

<img width="535" height="257" alt="image" src="https://github.com/user-attachments/assets/7e7e6150-3ac4-4c2f-a886-2309d00d71c9" />
<img width="370" height="245" alt="image" src="https://github.com/user-attachments/assets/06679c55-642f-476b-b571-e0dfa91598c6" />

---

# PCB Assembly

<img width="459" height="360" alt="image" src="https://github.com/user-attachments/assets/e6c2957a-7583-4281-98f6-9b81c16cacf7" />
---

# Enclosure Design

<img width="449" height="287" alt="image" src="https://github.com/user-attachments/assets/057cd9e6-8ca4-4702-988d-2795ed16dcb4" />


---

# Final Prototype


<img width="831" height="623" alt="image" src="https://github.com/user-attachments/assets/9a7c6df1-26a0-4d3c-bfa6-338af9db5893" />

<img width="833" height="625" alt="image" src="https://github.com/user-attachments/assets/d7a573bd-3bcd-4de5-a9e6-48aaea1fcd7f" />


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
