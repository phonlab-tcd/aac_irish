from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home_page():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        voice_type = request.form['voice']
        from tts_corrector import tts_corrector
        corrected_text, sound_file = tts_corrector(text, voice_type)
        print(corrected_text)
        from flask import send_file
        number = 0
        import os
        while True:
            if os.path.isfile(f"temp_{number}.mp3"):
                number += 1
            else:
                break  
        with open(f"temp_{number}.mp3","wb") as f:
            f.write(sound_file)
        return send_file(f"temp_{number}.mp3",mimetype="audio/mp3")
        return {
            "text": corrected_text,
            "sound_file": json.dumps(sound_file.decode("base64"))
        }
    return '''
        <form method="post">
            <p><input type=text name=text>
             <label for="voice">Choose a voice:</label>
             <select id="voice" name="voice">
             <option value="irish_1">ga_UL_anb_exthts</option>
             <option value="irish_2">ga_UL_anb_nnmnkwii</option>
             <option value="irish_3">ga_CO_pmc_exthts</option>
             <option value="irish_4">ga_CO_pmg_nnmnkwii</option>
             <option value="irish_5">ga_CO_snc_exthts</option>
             <option value="irish_6">ga_CO_snc_nnmnkwii</option>
             <option value="irish_7">ga_MU_nnc_exthts</option>
             <option value="irish_8">ga_MU_nnc_nnmnkwii</option>
             <option value="irish_9">ga_MU_cmg_nnmnkwii</option>
             </select> 
            <p><input type=submit value=Submit>
        </form>
        '''
