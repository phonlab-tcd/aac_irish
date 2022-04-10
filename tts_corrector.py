from abair_voice import get_voice, get_voice_hts_params
from an_gramadoir import an_gramadoir_parser
from morphological_correction import morphological_parser
from genitive_parser import genitive_parser


def tts_corrector(text,voice_type):
    corrected_text = correct_text(text)
    sound_file = get_voice(corrected_text,voice_type)
    return corrected_text, sound_file

def tts_corrector_with_hts_params(text,voice_type,alpha,all_pass_filter):
    corrected_text = correct_text(text)
    sound_file = get_voice_hts_params(corrected_text,voice_type,alpha,all_pass_filter)
    return corrected_text, sound_file

def correct_text(text):
    morphologically_corrected  = morphological_parser(text)
    print(morphologically_corrected)
    grammatically_corrected = an_gramadoir_parser(morphologically_corrected)
    print(grammatically_corrected)
    corrected_text = genitive_parser(grammatically_corrected)
    return corrected_text

if __name__ == "__main__":
    #print(correct_text("An gheobhaidh muid a' cóta ó fear an post?"))
    #print(correct_text("An bhfuil sé níos cairdiúil ná mé?"))
    #print(correct_text("An bhfuil sé níos furasta ná mé?"))
    print(correct_text("An bhfuil sé níos ba furasta ná mé?"))
    print(correct_text("An bhfuil sé níos ba aisteach ná mé?"))
    print(correct_text("An bhfuil sé ba furasta ná mé?"))
    print(correct_text("An bhfuil sé ba ionraic ná mé?"))
    #print(correct_text("An bhfuil sé níos daor ná mé?"))
    print(correct_text("An bhfuil sé níos ba cairdiúil ná mé?"))
    #print(correct_text("An bhfuil an bean anseo?"))