from flask import Flask, render_template, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime
from PIL import Image
import io
import base64
import logging
from diffusers.utils import logging as diffusers_logging

# Configure environment
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Enable detailed logging
diffusers_logging.set_verbosity_info()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def load_model():
    try:
        logger.info("Loading Stable Diffusion model...")
        
        # Using a more reliable model
        model_id = "runwayml/stable-diffusion-v1-5"
        
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32,
            safety_checker=None,
            requires_safety_checker=False
        )
        
        # Force CPU mode with optimizations
        pipe = pipe.to("cpu")
        pipe.enable_attention_slicing()
        
        logger.info("Model successfully loaded")
        return pipe
        
    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        raise

# Initialize model
try:
    pipe = load_model()
    logger.info("Model is ready for generation")
except Exception as e:
    logger.critical(f"Failed to initialize model: {str(e)}")
    pipe = None

# Ensure directories exist
os.makedirs("static/images", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    if not pipe:
        return jsonify({"error": "Model not available"}), 503
    
    data = request.get_json()
    prompt = data.get("prompt", "").strip()  # Fixed typo from 'prompt' to 'prompt'
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    try:
        logger.info(f"Generating image for: '{prompt}'")
        
        # Generate image
        result = pipe(
            prompt=prompt,
            num_inference_steps=25,
            guidance_scale=7.5,
            height=512,
            width=512
        )
        
        if not result.images:
            raise ValueError("No image generated")
            
        image = result.images[0]

        # Save image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"generated_{timestamp}.png"
        filepath = os.path.join("static", "images", filename)
        image.save(filepath)
        logger.info(f"Image saved to {filepath}")

        # Create base64 response
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return jsonify({
            "status": "success",
            "image_url": f"data:image/png;base64,{img_str}",
            "file_url": f"/static/images/{filename}"
        })
        
    except Exception as e:
        logger.error(f"Generation failed: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/test")
def test_model():
    """Test endpoint to verify model works"""
    if not pipe:
        return jsonify({"status": "model_not_loaded"}), 500
        
    try:
        test_img = pipe(prompt="a red apple", num_inference_steps=5).images[0]
        return jsonify({"status": "working"})
    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True  # Keep True for development
    )