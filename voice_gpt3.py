import openai
import pyttsx3
import speech_recognition as sr

# Set OpenAI API key
openai.api_key = "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"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
r = sr.Recognizer()

# Print available microphone names (for troubleshooting)
print(sr.Microphone.list_microphone_names())

# Set microphone index
mic = sr.Microphone(device_index=2)

# Set initial conversation state and names
conversation = ""
user_name = "You"
bot_name = "Explorer"

while True:
    with mic as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.9)
        audio = r.listen(source)
    print("No longer listening.\n")

    try:
        # Convert speech to text using Google Speech Recognition API
        user_input = r.recognize_google(audio)
    except:
        # If speech is not recognized, continue listening
        continue

    # Combine user input with previous conversation history for context
    prompt = user_name + ": " + user_input + "\n" + bot_name + ": "
    conversation += prompt

    # Fetch response from OpenAI API
    response = openai.Completion.create(engine='text-davinci-003', prompt=conversation, max_tokens=100)
    response_str = response["choices"][0]["text"].replace("\n", "")

    # Extract bot response and remove any user input that may be included
    response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

    # Add bot response to conversation history
    conversation += response_str + "\n"

    # Print bot response to console
    print(response_str)

    # Use text-to-speech engine to speak bot response
    engine.say(response_str)
    engine.runAndWait()
