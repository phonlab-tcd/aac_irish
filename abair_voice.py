import requests

voices = {"irish_1":"ga_UL_anb_exthts", "irish_2":"ga_UL_anb_nnmnkwii", "irish_3":"ga_CO_pmc_exthts", "irish_4":"ga_CO_pmg_nnmnkwii", "irish_5":"ga_CO_snc_exthts", "irish_6":"ga_CO_snc_nnmnkwii", "irish_7":"ga_MU_nnc_exthts", "irish_8":"ga_MU_nnc_nnmnkwii", "irish_9":"ga_MU_cmg_nnmnkwii"}

def get_voice(text,voice_type):
    myobj = {'input':f"{text}", "format":"mp3", "synth":voices[voice_type], "speed":1}
    url = "https://abair.ie/api"
    receive = requests.get(url, params = myobj)
    sound_in_bytes = receive.content
    return sound_in_bytes

def main():
    x = get_voice("Dia duit","irish_4")
    print(x)

if __name__ == "__main__":
    main()