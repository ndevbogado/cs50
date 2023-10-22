import pyttsx3
import sys

def main():
    if len(sys.argv) == 1:
        run_voice(input("Type a message: "))

    else:
        message = ""
        for word in sys.argv:
            if sys.argv.index(word) != 0:
                message += f"{word} "
        run_voice(message)

def run_voice(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


if __name__ == "__main__":
    main()
