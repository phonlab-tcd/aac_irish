import requests


def get_voice(text,voice_type,audioformat="MP3",cut_silence=False):
    voices = {"Ulster":"ga_UL_anb_exthts", "Connaught":"ga_CO_pmc_exthts", "Connaught (boy)":"ga_CO_snc_exthts", "Connaught (girl)":"ga_CO_snc_exthts", "Munster":"ga_MU_nnc_exthts"}
    receive = None
    if voice_type == "Connaught (boy)":
        receive = requests.get(f"https://abair.ie/api2/synthesise?input={text}&voice={voices[voice_type]}&audioEncoding=MP3&timing=WORD&htsParams=-fm%206.9%20-a%200.43%20-r%200.8")
    elif voice_type == "Connaught (girl)":
        receive = requests.get(f"https://abair.ie/api2/synthesise?input={text}&voice={voices[voice_type]}&audioEncoding=MP3&timing=WORD&htsParams=-fm%203%20-a%200.45%20-r%200.8")
    elif voice_type == "Ulster":
        #receive = requests.get(f"https://phoneticsrv3.lcs.tcd.ie/nemo/synthesise?outputType=JSON&audioEncoding={audioformat}&cutSilence={cut_silence}&voice=snc.multidialect&input={text}")
        url = f"https://phoneticsrv3.lcs.tcd.ie/nemo/synthesise?outputType=JSON&audioEncoding={audioformat}&cutSilence={cut_silence}&voice=anyspeaker&speaker=0&input={text}"
        print(url)
        receive = requests.get(url)

    else:
        receive = requests.get(f"https://abair.ie/api2/synthesise?input={text}&voice={voices[voice_type]}&audioEncoding=MP3&timing=WORD")
    return receive

def get_voice_hts_params(text,voice_type,alpha,all_pass_filter):
    voices = {"irish_1":"ga_UL_anb_exthts", "irish_2":"ga_UL_anb_nnmnkwii", "irish_3":"ga_CO_pmc_exthts", "irish_4":"ga_CO_pmg_nnmnkwii", "irish_5":"ga_CO_snc_exthts", "irish_6":"ga_CO_snc_nnmnkwii", "irish_7":"ga_MU_nnc_exthts", "irish_8":"ga_MU_nnc_nnmnkwii", "irish_9":"ga_MU_cmg_nnmnkwii"}
    receive = requests.get(f"https://abair.ie/api2/synthesise?input={text}&voice={voices[voice_type]}&audioEncoding=MP3&timing=WORD&htsParams=-fm%20{all_pass_filter}%20-a%20{alpha}%20-r%200.8")
    return receive


def main():
    #x = get_voice("Dia duit","Ulster")
    x = get_voice_hts_params("Dia duit","irish_7", 0.4, 0)
    print(x.json())

if __name__ == "__main__":
    main()
