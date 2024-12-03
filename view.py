from django.shortcuts import render
from django.http import JsonResponse
import random


responses = {
    "depression": [
        "I'm really sorry you're feeling this way, but I know you have the strength to overcome this.",
        "It's okay to feel down sometimes, remember to take it one step at a time. You're not alone."
    ],
    "anxiety": [
        "Take a deep breath, everything will be okay. You're doing the best you can.",
        "It's normal to feel anxious, but try to focus on what you can control right now."
    ],
    "anger": [
        "It's okay to feel angry. Try to breathe deeply and let go of what you can't control.",
        "Take a moment to calm down. Anger is just an emotion, and it will pass."
    ],
    "sickness": [
        "I'm really sorry you're feeling unwell. Rest, hydrate, and take care of yourself.",
        "Your health matters. Make sure you're taking the time to recover and feel better soon."
    ],
    "motivation": [
        "You are stronger than you think, keep pushing forward. You've got this!",
        "Believe in yourself, every day is a new opportunity to grow and improve."
    ]
}


def get_response(user_input):
    if "depression" in user_input:
        return random.choice(responses["depression"])
    elif "anxiety" in user_input:
        return random.choice(responses["anxiety"])
    elif "anger" in user_input:
        return random.choice(responses["anger"])
    elif "sick" in user_input or "illness" in user_input:
        return random.choice(responses["sickness"])
    else:
        return random.choice(responses["motivation"])


def index(request):
    return render(request, 'chatbot/index.html')

def chat(request):
    user_message = request.GET.get('message', '').lower()
    response = get_response(user_message)
    return JsonResponse({'response': response})
