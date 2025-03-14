
import time

def get_time_greeting():
    current_hour = time.localtime().tm_hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def main():
    print("🌟 Welcome to the Personalized Greeting App! 🌟")
    print("---------------------------------------------")
    
    
    name = input("What's your name? ")
    color = input("What's your favorite color? ")
    
    
    time_greeting = get_time_greeting()
    
    
    print("\n" + "=" * 50)
    print(f"{time_greeting}, {name}!")
    print(f"Your favorite color, {color}, is awesome!")
    
    
    if color.lower() in ["blue", "azure", "navy", "teal"]:
        print(f"Blue shades like {color} represent calm and tranquility.")
    elif color.lower() in ["red", "crimson", "maroon", "scarlet"]:
        print(f"{color.capitalize()} shows passion and energy!")
    elif color.lower() in ["green", "emerald", "lime", "olive"]:
        print(f"{color.capitalize()} represents growth and harmony with nature.")
    elif color.lower() in ["yellow", "gold", "amber"]:
        print(f"{color.capitalize()} brings sunshine and optimism!")
    else:
        print(f"{color.capitalize()} is a wonderful choice!")
    
    print("=" * 50)
    print("\nThanks for using the Personalized Greeting App! Have a great day! 👋")

if __name__ == "__main__":
    main()