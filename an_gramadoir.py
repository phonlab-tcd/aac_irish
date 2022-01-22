import requests
import re


def process_errors(text, errors):
    if errors:
        my = 0
        mx = 0
        ty = 0
        tx = 0
        ruleId = ""
        message = ""
        context = ""
        contextoffset = 0
        errorlength = 0
        original_context = ""
        last_tx = 10000
        tx_offset = 0
        last_y = -1
        final_text = []
        add_in_line = False
        change_text = []
        for error in reversed(errors):
            if original_context == "" or last_y != error["toy"]:
                if original_context != "":
                    final_text.append(context)
                context = error["context"]
                original_context = context
                last_y = error["toy"]
                add_in_line = False
            elif original_context == error["context"] and int(error["fromx"]) > len(error["context"]):
                if final_text:
                    final_text[-1] += f" {context}"
                else:
                   final_text.append(context) 
                context = error["context"]
                original_context = context
                last_y = error["toy"]
                add_in_line = True
            my = int(error["fromy"])
            mx = int(error["fromx"])
            ty = int(error["toy"])
            tx = int(error["tox"])
            rule_match =  re.search("Lingua::GA::Gramadoir/.*",error["ruleId"])
            ruleId = rule_match.group(0).replace("Lingua::GA::Gramadoir/","").replace("\"","").strip()
            message = error["msg"]
            contextoffset = error["contextoffset"]
            errorlength = error["errorlength"]
            error_text = error["errortext"]
            if tx < last_tx:
                last_tx = tx
            else:
                tx = tx + tx_offset
                tx_offset = 0
            if ruleId == "SEIMHIU" and message == "Lenition missing":
                context = context[mx:tx+1].split(" ")
                index = 0
                for word in context:
                    if word in ["na", "an","Na", "An"]:
                        index += len(word) +1
                        continue
                    elif word[0] in ["a","e","i","o","u","l","n","r","A","E","I","O","U","L","N","R"]:
                        index += len(word) +1
                        continue
                    else:
                        index +=1
                        break
                context = context[0:mx+index] + "h" + context[index+mx:]
                tx_offset += 1
            elif ruleId == "NIAITCH" and message == "Unnecessary prefix /h/":
                m10 = re.search("/.*/",message)
                prefix = m10.group(0).replace("/","")
                context = context[mx:tx+1].split(" ")
                index = 0
                for word in context:
                    if word[0] == prefix:
                        break
                    else:
                        index += len(word) + 1
                context = context[0:mx+index] + context[mx+index+1:]
                tx_offset -= 1
            elif re.search("MICHEART",ruleId) != None:
                m10 = re.search("/.*/",message)
                word = m10.group(0).replace("/","")
                context = context[0:mx] + word + context[tx+1:]
                tx_offset = (tx+1-mx - len(word))
            elif ruleId == "CLAOCHLU" and message == "Initial mutation missing":
                context_ = context[mx:tx+1].split(" ")
                index = 0
                uru = ""
                initial_letter = ""
                for word in context_:
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
                    context = context[:mx+index] + uru + context[mx+index:]
                    tx_offset += len(uru)
            elif re.search("CAIGHDEAN",ruleId):
                substitute = ruleId.replace("CAIGHDEAN{","").replace("}","")
                change_text.append([error_text,substitute])
        if add_in_line:
            if final_text:
                final_text[-1] += f" {context}"
            else:
               final_text.append(context) 
        else:
            final_text.append(context)
        for index,pair in enumerate(change_text):
            for index_,text_chunk in enumerate(final_text):
                final_text[index_] = text_chunk.replace(pair[0],pair[1])
        return "\n".join(final_text)
    else:
        return text

def an_gramadoir(text):
    url = 'https://abair.ie/cgi-bin/api-gramadoir-1.0.pl'
    myobj = {'teanga': 'en',"teacs":f"{text}"}
    errors = requests.post(url, data = myobj).json()
    return text, errors

def correct_errors_in_text(text):
    text,errors = an_gramadoir(text)
    final_text = process_errors(text, errors)
    return final_text

def main():
    x = correct_errors_in_text("Dia Dhuit.")
    print(x)

if __name__ == "__main__":
    main()