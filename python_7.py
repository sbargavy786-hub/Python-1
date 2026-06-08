def get_motivational_quote(feeling):
    """Return a motivational quote based on the user's feeling."""
    quotes = {
        "sad": [
            "Every day is a fresh beginning. Take a deep breath and start again.",
            "Your struggle is temporary, but your strength is permanent.",
            "Don't let one bad day define your whole week."
        ],
        "anxious": [
            "You've survived 100% of your worst days. You're stronger than you think.",
            "Breathe. You are safe. Everything is okay.",
            "Worry is like a rocking chair: it keeps you moving but gets you nowhere."
        ],
        "tired": [
            "Rest when you're weary. Rest is not giving up; it's recharging.",
            "Progress isn't always about pushing harder; sometimes it's about pausing.",
            "You don't have to see the whole staircase, just take the next step."
        ],
        "unmotivated": [
            "Start small. Your future self will thank you for the effort today.",
            "Motivation follows action, not the other way around.",
            "You don't need to be great to start; you need to start to be great."
        ],
        "stressed": [
            "This too shall pass. You have overcome challenges before.",
            "Take it one task at a time. One step is progress.",
            "You're doing better than you think you are."
        ],
        "happy": [
            "Keep spreading that joy! Your happiness inspires others.",
            "Celebrate this moment. You deserve to feel good.",
            "Hold onto this feeling and use it as fuel for your goals."
        ]
    }
    
    feeling = feeling.lower().strip()
    
    if feeling in quotes:
        import random
        return random.choice(quotes[feeling])
    else:
        return "Remember: You are capable, you are worthy, and you will overcome."

def main():
    print("=== Motivational Quote Generator ===\n")
    print("How are you feeling today?")
    print("Options: sad, anxious, tired, unmotivated, stressed, happy\n")
    
    user_feeling = input("Enter your feeling: ")
    quote = get_motivational_quote(user_feeling)
    print(f"\n✨ Here's your quote: {quote} ✨\n")

if __name__ == "__main__":
    main()
