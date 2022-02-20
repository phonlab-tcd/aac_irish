import re
def dependent_forms(text):
    #past
    #present
    #future
    text = re.sub("ní gheobhaidh", "ní bhfaighidh", text)
    text = re.sub("Ní gheobhaidh", "Ní bhfaighidh", text)
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

def noun_correction(text):

    return text
def adj_correction(text):

    return text

def text_correction(text):
    text = verb_correction(text)
    text = noun_correction(text)
    text = adj_correction(text)
    return text

def main():
    #present tests
    print("---present test ---")
    print(text_correction("Tá mé anseo"))
    print(text_correction("An bhfuil mé anseo"))
    print(text_correction("Cuireann mé anseo"))
    print(text_correction("Gabhann mé anseo"))
    print(text_correction("Ceannaíonn mé anseo"))
    print(text_correction("Imíonn muid anseo"))
    print(text_correction("Tá muid anseo"))
    print(text_correction("An bhfuil muid anseo"))
    print(text_correction("Cuireann muid anseo"))
    print(text_correction("Gabhann muid anseo"))
    print(text_correction("Ceannaíonn muid anseo"))
    print(text_correction("Imíonn muid anseo"))
    #future tests
    print("---future test ---")
    print(text_correction("Bheidh muid anseo"))
    print(text_correction("Gheobhaidh muid anseo"))
    print(text_correction("Ceannóidh muid anseo"))
    print(text_correction("Inseoidh muid anseo"))
    print(text_correction("Suífidh muid anseo"))
    print("---future dependency test ---")
    print(text_correction("Ní gheobhaidh mé"))
    print(text_correction("ní gheobhaidh mé"))
    print(text_correction("Ní gheobhaidh muid"))
if __name__ == "__main__":
    main()