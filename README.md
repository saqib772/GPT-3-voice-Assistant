# GPT-3-voice-Assistant
Explore the power of natural language processing and speech recognition with this Python chatbot! Using OpenAI's advanced language processing tools and Google's speech recognition API, this script can listen to your voice, understand your words, and generate responses based on your conversation history.

Yes, I am Talking about Making The Voice Assistant Using Chat-Gpt3 Where You can Speak and AI Will Tell The Answers According To What have Been Asked.

# *Lets Get Started Without wasting Time.*

You Just Need The VS Code IDE, Python and Some Libraries Which I will Discuss Below.

First You need To download The python Extension, then install open ai library, then pyttsx3 then speech recognition, and finally pyaudio so you can interact with device input/output.

Install The libraries:
!pip install pyaudio
!pip install openai
!pip install pyaudio
!pip install speech_recognition

Then Copy paste The code from File and Run it. Here You Go Now You can ask as Many Questions As You Can.
# Explanation of The code so You can Understand Better.

The first few lines of the code import the necessary libraries, including OpenAI for language processing, Pyttsx3 for text-to-speech conversion, and SpeechRecognition for speech-to-text conversion.

The OpenAI API key is then set using a unique code that allows the code to access OpenAI’s powerful natural language processing tools.

Visit Your Profile Dashboard and Click on your Profile Picture and Then You can Get The Secret API Keys.

![API key ](https://user-images.githubusercontent.com/121972215/224566161-01423efa-20f9-4364-ba77-4870efe79725.png)

Next, the text-to-speech engine and speech recognizer are initialized using Pyttsx3 and SpeechRecognition respectively.

The script then prints the available microphone names for troubleshooting purposes and sets the microphone index to use for speech recognition.

The conversation is then initiated with empty strings for user input, user name, bot name, and conversation history.

The while loop starts listening for user input using the specified microphone.

Once speech is detected, the speech-to-text conversion begins using Google Speech Recognition API.

If the speech is not recognized, the script continues listening for speech.

If speech is recognized, the user input is combined with previous conversation history to provide context, and the conversation history is updated.

The OpenAI API is then called to generate a response based on the conversation history and user input.

The response is extracted and cleaned up by removing any user input and adding it to the conversation history.

The response is then printed to the console and spoken out loud using the text-to-speech engine.

That’s All For Now, I hope All These works and Now You can talk as Much as You can With Chatbot powered By GPT-3. Feel Free To Ask Any Questions.


https://user-images.githubusercontent.com/121972215/224568792-1b210e5c-6aa5-4ebe-a0e5-7ff374d35313.mp4

