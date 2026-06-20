def emotion_detector(text):
    text = text.lower().split()
    
    # Define emotion word banks
    keywords = {
        "joy": ["happy", "love", "great", "excellent", "good", "amazing", "joyful", "awesome"],
        "anger": ["angry", "hate", "mad", "annoyed", "furious", "terrible", "frustrated"],
        "sadness": ["sad", "upset", "cry", "depressed", "gloomy", "sorry", "hurt"],
        "fear": ["fear", "afraid", "scared", "terrified", "anxious", "worried"],
        "disgust": ["disgust", "gross", "yuck", "hate", "dislike", "awful"]
    }
    
    # Base starting score out of 20 (e.g., 2.0 out of 20)
    scores = {emotion: 2.0 for emotion in keywords} 
    
    # Increase the score by 6.0 points for every keyword match found
    for word in text:
        for emotion, word_list in keywords.items():
            if word in word_list:
                scores[emotion] += 6.0 
                
    # Ensure no score exceeds the maximum cap of 20.0
    for emotion in scores:
        if scores[emotion] > 20.0:
            scores[emotion] = 20.0

    # Determine the dominant emotion based on the highest score
    dominant_emotion = max(scores, key=scores.get)
    
    # If no keywords matched, call it neutral
    if scores[dominant_emotion] == 2.0:
        dominant_emotion = "neutral"
        
    # Format the final output dictionary
    scores["dominant_emotion"] = dominant_emotion
    return scores