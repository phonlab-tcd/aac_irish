from abair_voice import get_voice, get_voice_hts_params
from an_gramadoir import an_gramadoir_parser
from morphological_parser import morphological_parser
from genitive_parser import genitive_parser


def tts_corrector(text,voice_type, skip_corrections=False, audioformat="mp3", cut_silence=False):
    if skip_corrections:
        corrected_text = text
    else:
        corrected_text = correct_text(text)

    #HB changed to be able to display the correction steps
    if len(corrected_text) == 3:
        sound_file = get_voice(corrected_text[0],voice_type, audioformat, cut_silence)
    else:
        sound_file = get_voice(corrected_text,voice_type, audioformat, cut_silence)
    return corrected_text, sound_file

def tts_corrector_with_hts_params(text,voice_type,alpha,all_pass_filter):
    corrected_text = correct_text(text)
    #HB changed to be able to display the correction steps
    if len(corrected_text) == 3:
        sound_file = get_voice_hts_params(corrected_text[0],voice_type,alpha,all_pass_filter)
    else:
        sound_file = get_voice_hts_params(corrected_text,voice_type,alpha,all_pass_filter)
    return corrected_text, sound_file

def correct_text(text):
    print(f"INPUT TEXT: {text}")
    morphologically_corrected  = morphological_parser(text)
    print(f"MORPH: {morphologically_corrected}")
    grammatically_corrected = an_gramadoir_parser(morphologically_corrected)
    print(f"GRAM:  {grammatically_corrected}")
    corrected_text = genitive_parser(grammatically_corrected)
    print(f"GEN:   {corrected_text}")
    #return corrected_text
    #HB changed to be able to display the correction steps
    return (corrected_text, morphologically_corrected, grammatically_corrected)

if __name__ == "__main__":
    pass
