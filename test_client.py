import requests
import ubelt
timer = ubelt.Timer()



url = "http://localhost:8001"
#url = "https://abair.ie/aac_irish"




voices = ["Ulster"]
caches = [True, False]
corrections = [True, False]
audioformats = ["wav","mp3"]
texts = ["dia dhuit", "dia is muire dhuit", "dia duit", "dia is muire duit"]
#texts = ["dia dhuit"]



for voice in voices:
    for audioformat in audioformats:
        for correction in corrections:
            for cache in caches:
                for text in texts:
                    params = {
                        "voice": voice,
                        "audioformat": audioformat,
                        "text": text
                    }
                    if cache:
                        params["use_cache"] = "on"                        
                    else:
                        params["use_cache"] = "off"                        
                    if correction:
                        params["use_correction"] = "on"
                    else:
                        params["use_correction"] = "off"
                        
                    #print(params)
                    with timer:
                        data = requests.post(url,params)
                    outfile = f"test_out/{text}-{voice}-{cache}-{correction}.{audioformat}"
                    print(f"{timer.elapsed:.4f}\t{text}\t{voice}\t{audioformat}\t{cache}\t{correction}\t{outfile}", flush=True)
                    #print(data.elapsed)
                    with open(outfile, "wb") as fh:
                        fh.write(data.content)
