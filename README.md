# AI Emotion Detector

A light, dynamic Flask web application that analyzes user feedback text locally and rates emotion intensities out of 20.

## Features
- Dynamic word-matching keyword analysis.
- Scores calculated transparently out of 20.0 max.
- Zero-dependency local setup (no external API keys needed).

## Project Structure
- `app.py`: Main Flask controller app.
- `EmotionDetection/`: Contains the local analysis module.
- `templates/`: HTML interface templates.
- `static/`: CSS styling stylesheets.

## How to Run Locally
1. Install Flask:
   ```bash
   pip install flask