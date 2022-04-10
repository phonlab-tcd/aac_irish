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
    text = re.sub("(\b|^)tá mé", "táim", text)
    text = re.sub("Tá mé", "Táim", text)
    text = re.sub("bhfuil mé", "bhfuilim", text)
    text = re.sub("eann mé", "im", text)
    text = re.sub("ann mé", "aim", text)
    text = re.sub("aíonn mé", "aím", text)
    text = re.sub("íonn mé", "ím", text)
        #plural
    text = re.sub("(\b|^)tá muid", "táimid", text)
    text = re.sub("Tá muid", "Táimid", text)
    text = re.sub("bhfuil muid", "bhfuilimid", text)
    text = re.sub("(\b|^)deir muid", "deirimid", text)
    text = re.sub("Deir muid", "Deirimid", text)
    text = re.sub("eann muid", "imid", text)
    text = re.sub("ann muid", "aimid", text)
    text = re.sub("aíonn muid", "aímid", text)
    text = re.sub("íonn muid", "ímid", text)

    #future
        #plural
    text = re.sub("(\b|^)eidh muid", "eimid", text)
    text = re.sub("eidh muid", "eimid", text)
    text = re.sub("faighidh muid(\W|$)", "faighimid", text)
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
    b = "[B|b]"
    c = "[C|c]"
    d = "[D|d]"
    t = "[T|t]"
    g = "[G|g]"
    p = "[P|p]"
    f = "[F|f]"
    #his
    text = re.sub(f"a\' ({seimhiu})", "a \g<1>h", text)
    #her
    #their
    text = re.sub(f"a, ({b})", "a m\g<1>", text)
    text = re.sub(f"a, ({c})", "a g\g<1>", text)
    text = re.sub(f"a, ({d})", "a n\g<1>", text)
    text = re.sub(f"a, ({t})", "a d\g<1>", text)
    text = re.sub(f"a, ({g})", "a n\g<1>", text)
    text = re.sub(f"a, ({p})", "a b\g<1>", text)
    text = re.sub(f"a, ({f})", "a bh\g<1>", text)
    return text

def morphological_parser(text):
    text = verb_correction(text)
    text = possessive_pronoun_correction(text)
    return text

def main():
    #possessive tests
    print("---possessive pronoun first person masculine singular test ---")
    print(morphological_parser("Tá a' cóta ann."))
    print(morphological_parser("Tá a' Cóta ann."))
    print(morphological_parser("Tá a' Dóta ann."))
    print(morphological_parser("Tá a' dóta ann."))
    print(morphological_parser("Tá a' Fóta ann."))
    print(morphological_parser("Tá a' fóta ann."))
    print(morphological_parser("Tá a' Góta ann."))
    print(morphological_parser("Tá a' góta ann."))
    print(morphological_parser("Tá a' Móta ann."))
    print(morphological_parser("Tá a' móta ann."))
    print(morphological_parser("Tá a' Póta ann."))
    print(morphological_parser("Tá a' póta ann."))
    print(morphological_parser("Tá a' Sóta ann."))
    print(morphological_parser("Tá a' sóta ann."))
    print(morphological_parser("Tá a' Tóta ann."))
    print(morphological_parser("Tá a' tóta ann."))
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