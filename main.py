from abair_voice import get_voice
from an_gramadoir import correct_errors_in_text

def main():
    corrected_text = correct_errors_in_text("Dia Dhuit")
    sound_file = get_voice(corrected_text,"irish_4")
    return corrected_text, sound_file


if __name__ == "__main__":
    main()