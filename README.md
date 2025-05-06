# PicWizard 🪄✨  
**AI Text-to-Image Generation Platform**
![image](https://github.com/user-attachments/assets/5c34f802-e3bd-41cc-8ea0-fbae838e96c0)
![image](https://github.com/user-attachments/assets/adbdd4c8-3659-4bed-8e0e-f5cc8d5ed371)

---

## 🌟 Key Features
- **Instant AI Art Generation** from text prompts
- **Multiple Art Styles** (Realistic, Anime, Fantasy, Cyberpunk)
- **Customizable Settings**:
  - Image dimensions (256x256 to 1024x1024)
  - Creativity level control
  - Seed value adjustment
- **One-Click Download** (PNG/JPG formats)
- **Responsive Design** works on desktop & mobile

---

## 🛠️ Tech Stack
### Backend
| Component | Technology |
|-----------|------------|
| Framework | Flask (Python) |
| AI Engine | Stable Diffusion (PyTorch) |
| Image Processing | Pillow, OpenCV |
| API Layer | Flask-RESTful |

### Frontend
| Component | Technology |
|-----------|------------|
| Markup | HTML5 |
| Styling | CSS3, Bootstrap |
| Interactivity | JavaScript (ES6+) |
| UI Components | Modal Windows |

### Python Libraries
```python
# Core AI
"torch>=2.0.0",
"transformers>=4.26.0",
"diffusers>=0.12.0",

# Backend
"flask>=2.2.0",
"flask-cors>=3.0.0",

# Utilities
"numpy>=1.24.0",
"pillow>=9.4.0",

   `` # Clone the repository
git clone https://github.com/yourusername/PicWizard.git
cd PicWizard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt


PicWizard/
├── app/
│   ├── static/
│   │   ├── css/        # Stylesheets
│   │   ├── js/         # Client-side scripts
│   │   └── outputs/    # Generated images
│   ├── templates/      # HTML files
│   │   └── index.html  # Main UI
│   ├── routes.py       # Flask routes
│   └── generator.py    # AI model handler
├── config.py           # Configuration
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── README.md           # This file
