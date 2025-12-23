# Book Image Validator

## Overview

The **Book Image Validator** is an automated system designed to classify book images as **VALID** or **INVALID**. The primary purpose of this project is to assist **book-selling platforms** by automatically detecting valid book images, eliminating the need for manual validation by an admin.

For example, instead of a platform admin manually checking if each uploaded book image is legitimate, this system uses a trained **MobileNetV2-based deep learning model** to verify images in real-time.

---

## Features

- Automatically classifies images as **VALID** or **INVALID**.
- Uses **MobileNetV2** pre-trained on ImageNet for feature extraction.
- Simple **Flask backend** for API predictions.
- Supports **image uploads via frontend** (with preview and instant feedback).
- Can handle **base64-encoded images** for API integration.

---

## How It Works

1. A user uploads a book image via a **web interface**.
2. The frontend converts the image to a format suitable for the backend (raw file or Base64).
3. The Flask backend receives the image and preprocesses it:
   - Resizes to **224x224 pixels**.
   - Converts to RGB.
   - Applies **MobileNetV2 preprocessing**.
4. The preprocessed image is passed through the trained **MobileNetV2 model** with a custom classification head.
5. The model outputs a **probability score**:
   - Above a threshold → **VALID**
   - Below the threshold → **INVALID**
6. The prediction is sent back to the frontend and displayed to the user.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/book-image-validator.git
cd book-image-validator
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Make sure you have the trained model saved as:

Copy code
book_validator_model.keras
Run the Flask app:

bash
Copy code
python app.py
Open the frontend in your browser:

cpp
Copy code
http://127.0.0.1:5000/
Usage
Upload a book image using the file input.

The image preview will appear.

Click Validate.

The system will return whether the image is VALID or INVALID along with a probability score.

Benefits
Saves time: Eliminates manual verification of book images.

Consistency: Standardizes image validation using machine learning.

Scalable: Can handle thousands of images in real-time.

Integration-ready: Can be integrated into any platform via REST API.

Future Enhancements
Fine-tune the model on a larger, more diverse dataset.

Implement multi-class validation for book covers, content pages, or invalid uploads.

Add batch processing for bulk uploads.

Display confidence heatmaps on images to highlight detected areas.

License
This project is open-source and available under the MIT License.
