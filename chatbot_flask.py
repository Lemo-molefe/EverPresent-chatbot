from flask import Flask, request, jsonify
import random

app = Flask(__name__)


bible_verses = {
    "depression": [
        "The Lord is close to the brokenhearted and saves those who are crushed in spirit. - Psalm 34:18",
        "Cast your burden on the Lord, and He will sustain you. - Psalm 55:22"
    ],
    "anxiety": [
        "Cast all your anxiety on Him because He cares for you. - 1 Peter 5:7",
        "Do not be anxious about anything... - Philippians 4:6-7"
    ],
    "anger": [
        "A gentle answer turns away wrath, but a harsh word stirs up anger. - Proverbs 15:1",
        "Do not let the sun go down while you are still angry. - Ephesians 4:26"
    ],
    "sickness": [
        "He gives strength to the weary and increases the power of the weak. - Isaiah 40:29",
        "By His wounds, we are healed. - Isaiah 53:5"
    ],
    "motivation": [
        "I can do all things through Christ who strengthens me. - Philippians 4:13",
        "For I know the plans I have for you... - Jeremiah 29:11"
    ]
}


def get_response(user_input):
    
    if "depression" in user_input:
        return random.choice(bible_verses["depression"])
    elif "anxiety" in user_input:
        return random.choice(bible_verses["anxiety"])
    elif "anger" in user_input:
        return random.choice(bible_verses["anger"])
    elif "sick" in user_input or "illness" in user_input:
        return random.choice(bible_verses["sickness"])
    else:
        return random.choice(bible_verses["motivation"])

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
