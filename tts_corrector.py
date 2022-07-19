from abair_voice import get_voice, get_voice_hts_params
from an_gramadoir import an_gramadoir_parser
from morphological_parser import morphological_parser
from genitive_parser import genitive_parser


def tts_corrector(text,voice_type, turn_off_corrections=False, audioformat="wav"):
    if turn_off_corrections:
        corrected_text = text
    else:
        corrected_text = correct_text(text)
    sound_file = get_voice(corrected_text,voice_type, audioformat)
    return corrected_text, sound_file

def tts_corrector_with_hts_params(text,voice_type,alpha,all_pass_filter):
    corrected_text = correct_text(text)
    sound_file = get_voice_hts_params(corrected_text,voice_type,alpha,all_pass_filter)
    return corrected_text, sound_file

def correct_text(text):
    morphologically_corrected  = morphological_parser(text)
    grammatically_corrected = an_gramadoir_parser(morphologically_corrected)
    corrected_text = genitive_parser(grammatically_corrected)
    return corrected_text

if __name__ == "__main__":
    pass
