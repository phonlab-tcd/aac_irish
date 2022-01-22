from abair_voice import get_voice
from an_gramadoir import correct_errors_in_text

def tts_corrector(text,voice_type):
    corrected_text = correct_errors_in_text(text)
    sound_file = get_voice(corrected_text,voice_type)
    return corrected_text, sound_file


if __name__ == "__main__":
    tts_corrector()