import re
def dependent_forms(text):
    #past
    text = re.sub("([an|nach]) rinne", "\g<1> ndearna", text)
    text = re.sub("ní rinne", "ní dhearna", text)
    text = re.sub("([an|nach]) dúirt", "\g<1> ndúirt", text)
    text = re.sub("([an|nach]) chuaigh", "\g<1> ndeachaigh", text)
    text = re.sub("([an|ní|nach]) bhí", "\g<1> raibh", text)
    text = re.sub("([an|nach]) chonaic", "\g<1> bhfaca", text)
    text = re.sub("ní chonaic", "ní fhaca", text)
    text = re.sub("ní chuaigh", "ní dheachaigh", text)
    #future
    text = re.sub("ní gheobhaidh", "ní bhfaighidh", text)
    text = re.sub("an gheobhaidh", "an bhfaighidh", text)
    text = re.sub("Ní gheobhaidh", "Ní bhfaighidh", text)
    text = re.sub("An gheobhaidh", "An bhfaighidh", text)
    return text

def synthetic_verbs(text):
    #present
        #singular
    text = re.sub("(\b|^)tá mé", "\g<1>táim", text)
    text = re.sub("Tá mé", "Táim", text)
    text = re.sub("bhfuil mé", "bhfuilim", text)
    text = re.sub("eann mé", "im", text)
    text = re.sub("ann mé", "aim", text)
    text = re.sub("aíonn mé", "aím", text)
    text = re.sub("íonn mé", "ím", text)
        #plural
    text = re.sub("(\b|^)tá muid", "\g<1>táimid", text)
    text = re.sub("Tá muid", "Táimid", text)
    text = re.sub("bhfuil muid", "bhfuilimid", text)
    text = re.sub("(\b|^)deir muid", "\g<1>deirimid", text)
    text = re.sub("Deir muid", "Deirimid", text)
    text = re.sub("eann muid", "imid", text)
    text = re.sub("ann muid", "aimid", text)
    text = re.sub("aíonn muid", "aímid", text)
    text = re.sub("íonn muid", "ímid", text)

    #future
    text = re.sub("(\b|^)eidh muid", "\g<1>eimid", text)
    text = re.sub("eidh muid", "eimid", text)
    text = re.sub("faighidh muid(\W|$)", "faighimid\g<1>", text)
    text = re.sub("bhaidh muid", "bhaimid", text)
    text = re.sub("fidh muid", "fimid", text)
    text = re.sub("faidh muid", "faimid", text)
    text = re.sub("óidh muid", "óimid", text)
    text = re.sub("eoidh muid", "eoimid", text)

    #mc
    #aon siollach
    text = re.sub("feadh mé","finn",text)
    text = re.sub("feadh tú","feá",text)
    text = re.sub("feadh muid","fimis",text)
    text = re.sub("feadh siad","fidís",text)
    text = re.sub("fadh mé","fainn",text)
    text = re.sub("fadh tú","fá",text)
    text = re.sub("fadh muid","faimis",text)
    text = re.sub("fadh siad","faidís",text)
    #dhá shiollach
    text = re.sub("feodh mé","eoinn",text)
    text = re.sub("feodh tú","eofá",text)
    text = re.sub("feodh muid","eoimis",text)
    text = re.sub("feodh siad","eoidís",text)
    text = re.sub("fódh mé","fóinn",text)
    text = re.sub("fódh tú","ófá",text)
    text = re.sub("fódh muid","óimis",text)
    text = re.sub("fódh siad","óidís",text)
    #gc
    #aon siollach
    text = re.sub("eadh mé","inn",text)
    text = re.sub("eadh tú","teá",text)
    text = re.sub("eadh muid","imis",text)
    text = re.sub("eadh siad","idís",text)
    text = re.sub("adh mé","ainn",text)
    text = re.sub("adh tú","tá",text)
    text = re.sub("adh muid","aimis",text)
    text = re.sub("adh siad","aidís",text)
    #dhá shiollach
    text = re.sub("aíodh mé","aínn",text)
    text = re.sub("aíodh tú","aíteá",text)
    text = re.sub("aíodh muid","aímis",text)
    text = re.sub("aíodh siad","aídís",text)
    text = re.sub("íodh mé","ínn",text)
    text = re.sub("íodh tú","íteá",text)
    text = re.sub("íodh muid","ímis",text)
    text = re.sub("íodh siad","ídís",text)
    return text


def verb_correction(text):
    text = dependent_forms(text)
    text  = synthetic_verbs(text)
    return text

def possessive_pronoun_correction(text):
    seimhiu = "[B|b|C|c|D|d|F|f|G|g|M|m|P|p|S|s|T|t]"
    vowel = "[A|a|O|o|U|u|I|i|E|e|Á|É|Í|Ó|Ú|á|é|í|ó|ú]"
    b = "[B|b]"
    c = "[C|c]"
    d = "[D|d]"
    t = "[T|t]"
    g = "[G|g]"
    p = "[P|p]"
    f = "[F|f]"
    #his
    text = re.sub(f" a ({seimhiu})", " a \g<1>h", text)
    #her
    text = re.sub(f" a\' ({vowel})", " a h\g<1>", text)
    text = re.sub(f" a\' ", " a ", text)
    #their
    text = re.sub(f"a, ({b})", "a m\g<1>", text)
    text = re.sub(f"a, ({c})", "a g\g<1>", text)
    text = re.sub(f"a, ({d})", "a n\g<1>", text)
    text = re.sub(f"a, ({t})", "a d\g<1>", text)
    text = re.sub(f"a, ({g})", "a n\g<1>", text)
    text = re.sub(f"a, ({p})", "a b\g<1>", text)
    text = re.sub(f"a, ({f})", "a bh\g<1>", text)
    return text

def ba_case(text):
    ba = "[ba|Ba]"
    ni = "[ní|Ní]"
    not_ni = "[^ní]"
    b = "[b|B]"
    f = "[F|f]"
    n = "[^Nn]"
    consonants = "[B|b|C|c|D|d|G|g|M|m|P|p|S|s|T|t]"
    vowel = "[A|a|O|o|U|u|I|i|E|e|Á|É|Í|Ó|Ú|á|é|í|ó|ú]"
    #comparative and superlative cases
    text = re.sub(f"({ni}) ba f({vowel})","\g<1> b'fh\g<2>",text)
    text = re.sub(f"([^ní]) ba f({vowel})","\g<1> ab fh\g<2>",text)
    text = re.sub(f"ba ({consonants})","ba \g<1>h",text)
    text = re.sub(f"({ni}) ba ({vowel})","\g<1> b'\g<2>",text)
    text = re.sub(f"([^ní]) ba ({vowel})","\g<1> ab \g<2>",text)
    return text

def adjective_correction(text):
    caol = "[e|i]"
    leathan = "[a|o|u]"
    consonants = "[b|c|d|f|g|l|m|n|p|r|s|t]"
    punctuation = "[\.|,|\?|\"|\'|:|;|!]"
    text_words = text.split(" ")
    text_words_copy = text_words.copy()
    for index, word in enumerate(text_words_copy):
        if word in ["Níos","níos","is","Is","ní","Ní","Ba","ba"]:
            past_offset = 0
            punctuation = ""
            if index +2 < len(text_words_copy):
                if text_words_copy[index+1] == "ba":
                    past_offset = 1
                    text_words[index] = text_words[index][:2]
            if index +1 < len(text_words_copy):
                if len(text_words_copy[index+1+past_offset]) > 1:
                    if text_words_copy[index+1+past_offset][0] in [".",",","?","\"","\'",":",";","!"]:
                        punctuation = text_words_copy[index+1+past_offset][0]
                        text_words_copy[index+1+past_offset] = text_words_copy[index+1+past_offset][1:]
                    elif text_words_copy[index+1+past_offset][-1] in [".",",","?","\"","\'",":",";","!"]:
                        punctuation = text_words_copy[index+1+past_offset][-1]
                        text_words_copy[index+1+past_offset] = text_words_copy[index+1+past_offset][:-1]
                if text_words_copy[index+1+past_offset] in ["é","í","iad","muid"]:
                    break
                #irregular
                if text_words_copy[index+1+past_offset] == "álainn":
                    text_words[index+1+past_offset] = "áille"
                elif text_words_copy[index+1+past_offset] == "beag":
                    text_words[index+1+past_offset] = "lú"
                elif text_words_copy[index+1+past_offset] == "breá":
                    text_words[index+1+past_offset] = "breátha"
                elif text_words_copy[index+1+past_offset] == "dian":
                    text_words[index+1+past_offset] = "déine"
                elif text_words_copy[index+1+past_offset] == "fada":
                    text_words[index+1+past_offset] = "faide"
                elif text_words_copy[index+1+past_offset] == "fliuch":
                    text_words[index+1+past_offset] = "fliche"
                elif text_words_copy[index+1+past_offset] == "furasta":
                    text_words[index+1+past_offset] = "faide"
                elif text_words_copy[index+1+past_offset] == "gearr":
                    text_words[index+1+past_offset] = "giorra"
                elif text_words_copy[index+1+past_offset] == "leathan":
                    text_words[index+1+past_offset] = "leithne"            
                #elif text_words_copy[index+1+past_offset] == "maith":
                    #HB 220805 Turned off is maith liom -> is fearr liom
                    #text_words[index+1+past_offset] = "fearr"
                elif text_words_copy[index+1+past_offset] == "mór":
                    text_words[index+1+past_offset] = "mó"
                elif text_words_copy[index+1+past_offset] == "olc":
                    text_words[index+1+past_offset] = "measa"
                elif text_words_copy[index+1] == "ramhar":
                    text_words[index+1+past_offset] = "raimhre"
                elif text_words_copy[index+1+past_offset] == "saibhir":
                    text_words[index+1+past_offset] = "saibhre"
                elif text_words_copy[index+1+past_offset] == "tapa":
                    pass
                elif text_words_copy[index+1+past_offset] == "te":
                    text_words[index+1+past_offset] = "teo"
                elif text_words_copy[index+1+past_offset] == "tréan":
                    text_words[index+1+past_offset] = "treise"
                elif text_words_copy[index+1+past_offset] == "nua":
                    text_words[index+1+past_offset] = "nuaí"
                else:
                    #regular
                    text_words[index+1+past_offset] = re.sub(f"air$","ra",text_words_copy[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"each$","í",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"ach$","aí",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"úil$","úla",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"úil$","úla",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"aíoch$","aíche",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"íoch$","íche",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"({caol})({consonants})$","\g<1>\g<2>e",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"({leathan})({consonants})$","\g<1>i\g<2>e",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"({leathan})({consonants})$","\g<1>i\g<2>e",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"({leathan})({consonants})$","\g<1>i\g<2>e",text_words[index+1+past_offset])
                    text_words[index+1+past_offset] = re.sub(f"({leathan})({consonants})$","\g<1>i\g<2>e",text_words[index+1+past_offset])
                text_words[index+1+past_offset] += punctuation
    text = ba_case(" ".join(text_words))           
    return text

def morphological_parser(text):
    text = verb_correction(text)
    text = possessive_pronoun_correction(text)
    text = adjective_correction(text)
    return text

def main():
    pass
if __name__ == "__main__":
    main()
