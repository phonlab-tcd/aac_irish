import requests
import re

def apply_changes(text,error_text,ruleId,message):
    if ruleId == "GENITIVE":
        replace_words = message.replace("consider use of genitive: ","")
        text = replace_words
    return text

def process_errors(text,errors):
    if errors:
        text = text.split("\n")
        my = 0
        mx = 0
        ruleId = ""
        message = ""
        utterance_parts = [[]]
        add = 0
        for error in errors:
            c_my = int(error["fromy"])
            c_mx = int(error["fromx"])
            c_tx = int(error["tox"])
            if c_my != my:
                utterance_parts[my].append(text[my][mx:])
                add += 1
                utterance_parts.append([])
                my = c_my
            if c_mx > mx:
                utterance_parts[my].append(text[my][mx:c_mx])
                add += 1
            elif mx < c_mx:
                continue
            rule_match =  re.search("Lingua::GA::Gramadoir/.*",error["ruleId"])
            ruleId = rule_match.group(0).replace("Lingua::GA::Gramadoir/","").replace("\"","").strip()
            message = error["msg"]
            error_text = error["errortext"]
            utterance_parts[my].append(apply_changes(text[my][c_mx:c_tx+1],error_text,ruleId,message))
            add += 1
            mx = c_tx +1
        if mx < len(text[my]):
            utterance_parts[my].append(text[my][mx:])
            add += 1
        output_text = ""
        for paragraph in utterance_parts:
            if output_text != "":
                output_text += "\n"
            for x in paragraph:
                output_text += "".join(x)
        return output_text
    else:
        return text

def genitive_parser(text):
    url = f'https://phoneticsrv3.lcs.tcd.ie/gramsrv/api/grammar?text={text}&check=genitive'
    errors = requests.get(url).json()
    output_text = process_errors(text, errors)
    return output_text

def main():
    o = genitive_parser("fear mór an post ")
    print(o)
    o = genitive_parser("hata an fear")
    print(o)
    o = genitive_parser("fear an post")
    print(o)

if __name__ == "__main__":
    main()