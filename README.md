🧠 SmolVLM Image Captioning App

This is a lightweight image captioning web app built using the SmolVLM-500M-Instruct multimodal vision-language model. It runs locally (CPU or GPU) using a simple Gradio interface.
🚀 Features

    📷 Upload any image and generate a descriptive caption.

    ✍️ Add your own custom prompt to steer the caption style.

    ⚡ Runs completely offline, even on CPU.

    🌐 Web-based UI with Gradio – no frontend setup required.

🛠️ Installation
###### 1. Clone this repository
```bash
git clone https://github.com/mosharof24/Image_caption_gradio_app.git
```
###### 2. Create and activate a virtual environment (optional but recommended)
```bash
conda create -n smolvlm python=3.10
conda activate smolvlm
```
###### 3. Install dependencies
```bash
pip install -r requirements.txt
```
##### 📦 Folder Structure
```bash
.
├── models/                 # Contains the SmolVLM-500M-Instruct model (downloaded locally)
├── app.py                 # Main application script with Gradio interface
├── requirements.txt       # Python dependencies
└── README.md              # This file
```
##### ▶️ Run the App
```bash
python app.py
```
