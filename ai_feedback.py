import os
import requests

# -------------------------------------------------
# AI Resume Feedback using Gemini API
# -------------------------------------------------
def get_ai_feedback(resume_details, resume_text):
    """
    Sends parsed resume text and extracted details to Gemini API
    to generate feedback and suggestions.
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return "⚠️ Gemini API key not found. Please set GEMINI_API_KEY environment variable."

        # Construct prompt
        prompt = f"""
        You are an AI career coach and resume expert.
        Analyze the following resume details and text, and provide feedback.

        Extracted Details:
        {resume_details}

        Resume Text:
        {resume_text[:1500]}  # Limit length for API

        Please provide:
        1. Overall feedback (1 paragraph)
        2. 3 key strengths
        3. 3 areas of improvement
        4. Suggestions to make the resume ATS-friendly.
        """

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ]
        }

        response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)

        if response.status_code == 200:
            ai_text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return ai_text
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"❌ Error generating AI feedback: {str(e)}"
