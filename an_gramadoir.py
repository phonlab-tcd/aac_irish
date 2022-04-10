import requests, re

def apply_changes(text,error_text,ruleId,message):
    if ruleId == "SEIMHIU" and message == "Lenition missing":
        context = text.split(" ")
        index = 0
        for word in context:
            if word in ["na", "an","Na", "An"]:
                index += len(word) +1
                continue
            elif word[0] in ["á","é","í","ó","ú","a","e","i","o","u","l","n","r","A","E","I","O","U","Á","É","Í","Ó","Ú","L","N","R"]:
                index += len(word) +1
                continue
            else:
                index +=1
                break
        output_text = text[0:index] + "h" + text[index:]
        return output_text
    elif ruleId == "NIAITCH" and message == "Unnecessary prefix /h/":
        m10 = re.search("/.*/",message)
        prefix = m10.group(0).replace("/","")
        context = text.split(" ")
        index = 0
        for word in context:
            if word[0] == prefix:
                break
            else:
                index += len(word) + 1
        output_text = text[0:index] + text[index+1:]
        return output_text
    elif ruleId == "CLAOCHLU" and message == "Initial mutation missing":
        context_ = text.split(" ")
        index = 0
        uru = ""
        initial_letter = ""
        for word in context_:
            if word == "":
                continue
            if word in ["na", "an","Na", "An"]:
                index += len(word) +1
                continue
            elif word[0] in ["a","e","i","o","u","l","n","r","A","E","I","O","U","L","N","R"]:
                index += len(word) +1
                continue
            initial_letter = word[0]
            break
        if initial_letter == "b" or initial_letter == "B":
            uru = "m"
        elif initial_letter == "c" or initial_letter == "C":
            uru = "g"
        elif initial_letter == "d" or initial_letter == "D":
            uru = "n"
        elif initial_letter == "t" or initial_letter == "t":
            uru = "d"
        elif initial_letter == "g" or initial_letter == "g":
            uru = "n"   
        elif initial_letter == "p" or initial_letter == "P":
            uru = "b"
        elif initial_letter == "f" or initial_letter == "F":
            uru = "bh"
        if uru:
            output_text = text[:index] + uru + text[index:]
        return output_text
    elif re.search("CAIGHDEAN",ruleId):
        substitute = ruleId.replace("CAIGHDEAN{","").replace("}","")
        return text.replace(error_text,substitute)
    return text

def process_errors(text, errors):
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


def an_gramadoir(text):
    url = 'https://abair.ie/cgi-bin/api-gramadoir-1.0.pl'
    myobj = {'teanga': 'en',"teacs":f"{text}"}
    errors = requests.post(url, data = myobj).json()
    return text, errors

def an_gramadoir_parser(text):
    text,errors = an_gramadoir(text)
    final_text = process_errors(text, errors)
    return final_text

def main():
    pass

if __name__ == "__main__":
    main()