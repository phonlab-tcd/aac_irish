from abair_voice import get_voice, get_voice_hts_params
from an_gramadoir import an_gramadoir_parser
from morphological_correction import morphological_parser
from genitive_parser import genitive_parser


def tts_corrector(text,voice_type):
    morphologically_corrected  = morphological_parser(text)
    corrected_text = an_gramadoir_parser(morphologically_corrected)
    corrected_text = genitive_parser(corrected_text)
    sound_file = get_voice(corrected_text,voice_type)
    return corrected_text, sound_file

def tts_corrector_with_hts_params(text,voice_type,alpha,all_pass_filter):
    morphologically_corrected  = morphological_parser(text)
    corrected_text = an_gramadoir_parser(morphologically_corrected)
    corrected_text = genitive_parser(corrected_text)
    sound_file = get_voice_hts_params(corrected_text,voice_type,alpha,all_pass_filter)
    return corrected_text, sound_file


if __name__ == "__main__":
    tts_corrector()