# Final Project: AI Emotion Detector

## Features

- Detects emotions from text input
- Identifies the dominant emotion
- Supports:
  - Joy
  - Anger
  - Sadness
  - Fear
  - Disgust
- Real-time web interface using Flask
- Error handling for empty input
- Unit testing support
- Clean project structure

## Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Git
- GitHub

## Emotion Detection Logic

The application uses a keyword-based scoring mechanism.

Each emotion category contains a predefined set of keywords:

- Joy
- Anger
- Sadness
- Fear
- Disgust

When a keyword is found in the user input, the corresponding emotion score increases.

The emotion with the highest score is selected as the dominant emotion.

## Example

### Input

```text
I am very happy and excited today
```

### Output

python
    "joy": 14.0,
    "anger": 2.0,
    "sadness": 2.0,
    "fear": 2.0,
    "disgust": 2.0,
    "dominant_emotion": "joy"

## Installation

### Clone Repository

```bash
git clone https://github.com/Yashil2007/Ai-Emotion-Detector.git
```
### Move Into Project Directory

```bash
cd Ai-Emotion-Detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

## Running Tests

```bash
python -m unittest discover tests
```

## Author

Yashil Pandya
