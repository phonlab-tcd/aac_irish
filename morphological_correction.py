import re
def dependent_forms(text):
    #past
    #present
    #future
    text = re.sub("ní gheobhaidh", "ní bhfaighidh", text)
    text = re.sub("an gheobhaidh", "an bhfaighidh", text)
    text = re.sub("Ní gheobhaidh", "Ní bhfaighidh", text)
    text = re.sub("An gheobhaidh", "An bhfaighidh", text)
    #command
    #mc
    #gc
    return text

def synthetic_verbs(text):
    #past

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
        #plural
    text = re.sub("(\b|^)eidh muid", "\g<1>eimid", text)
    text = re.sub("eidh muid", "eimid", text)
    text = re.sub("faighidh muid(\W|$)", "faighimid\g<1>", text)
    text = re.sub("bhaidh muid", "bhaimid", text)
    text = re.sub("fidh muid", "fimid", text)
    text = re.sub("faidh muid", "faimid", text)
    text = re.sub("óidh muid", "óimid", text)
    text = re.sub("eoidh muid", "eoimid", text)

    #future

    #command

    # v-iol

    #mc

    #gc

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
                elif text_words_copy[index+1+past_offset] == "maith":
                    text_words[index+1+past_offset] = "fearr"
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
    #possessive tests
    print("---possessive pronoun first person masculine singular test ---")
    print(morphological_parser("Tá a cóta ann."))
    print(morphological_parser("Tá a Cóta ann."))
    print(morphological_parser("Tá a Dóta ann."))
    print(morphological_parser("Tá a dóta ann."))
    print(morphological_parser("Tá a Fóta ann."))
    print(morphological_parser("Tá a fóta ann."))
    print(morphological_parser("Tá a Góta ann."))
    print(morphological_parser("Tá a góta ann."))
    print(morphological_parser("Tá a Móta ann."))
    print(morphological_parser("Tá a móta ann."))
    print(morphological_parser("Tá a Póta ann."))
    print(morphological_parser("Tá a póta ann."))
    print(morphological_parser("Tá a Sóta ann."))
    print(morphological_parser("Tá a sóta ann."))
    print(morphological_parser("Tá a Tóta ann."))
    print(morphological_parser("Tá a tóta ann."))
    print("---possessive pronoun second person singular test ---")
    print(morphological_parser("Tá a, bóta ann."))
    print(morphological_parser("Tá a, Bóta ann."))
    print(morphological_parser("Tá a, cóta ann."))
    print(morphological_parser("Tá a, Cóta ann."))
    print(morphological_parser("Tá a, dóta ann."))
    print(morphological_parser("Tá a, Dóta ann."))
    print(morphological_parser("Tá a, tóta ann."))
    print(morphological_parser("Tá a, Tóta ann."))
    print(morphological_parser("Tá a, góta ann."))
    print(morphological_parser("Tá a, Góta ann."))
    print(morphological_parser("Tá a, póta ann."))
    print(morphological_parser("Tá a, Póta ann."))
    print(morphological_parser("Tá a, fóta ann."))
    print(morphological_parser("Tá a, Fóta ann."))
    #present tests
    print("---present test ---")
    print(morphological_parser("Tá mé anseo"))
    print(morphological_parser("An bhfuil mé anseo"))
    print(morphological_parser("Cuireann mé anseo"))
    print(morphological_parser("Gabhann mé anseo"))
    print(morphological_parser("Ceannaíonn mé anseo"))
    print(morphological_parser("Imíonn muid anseo"))
    print(morphological_parser("Tá muid anseo"))
    print(morphological_parser("An bhfuil muid anseo"))
    print(morphological_parser("Cuireann muid anseo"))
    print(morphological_parser("Gabhann muid anseo"))
    print(morphological_parser("Ceannaíonn muid anseo"))
    print(morphological_parser("Imíonn muid anseo"))
    #future tests
    print("---future test ---")
    print(morphological_parser("Bheidh muid anseo"))
    print(morphological_parser("Gheobhaidh muid anseo"))
    print(morphological_parser("Ceannóidh muid anseo"))
    print(morphological_parser("Inseoidh muid anseo"))
    print(morphological_parser("Suífidh muid anseo"))
    print("---future dependency test ---")
    print(morphological_parser("Ní gheobhaidh mé"))
    print(morphological_parser("Ní gheobhaidh muid"))
    print(morphological_parser("An gheobhaidh mé"))
    print(morphological_parser("An gheobhaidh muid"))
    print(morphological_parser("ní gheobhaidh mé"))
    print(morphological_parser("ní gheobhaidh muid"))
    print(morphological_parser("an gheobhaidh mé"))
    print(morphological_parser("an gheobhaidh muid"))
if __name__ == "__main__":
    main()