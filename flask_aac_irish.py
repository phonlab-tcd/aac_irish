from flask import Flask, render_template
import os

from tts_corrector import tts_corrector
import base64
import io
from flask import send_file

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#HB for timing
import ubelt
timer = ubelt.Timer()

input_form = '''
<form method="post">
<p><input type=text name=text>
<label for="voice">Choose a voice:</label>
<select id="voice" name="voice">
<option value="Ulster">Ulster</option>
<option value="Connaught">Connaught</option>
<option value="Connaught (girl)">Connaught (girl)</option>
<option value="Connaught (boy)">Connaught (boy)</option>
<option value="Munster">Munster</option>
</select> 
<p>
<label for="skip_corrections">Skip corrections:</label>
<input type="checkbox" id="skip_corrections" name="skip_corrections"/>
<label for="show_corrections">Show corrections:</label>
<input type="checkbox" id="show_corrections" name="show_corrections" checked/>
<label for="skip_cache">Skip cache:</label>
<input type="checkbox" id="skip_cache" name="skip_cache" checked/>
<label for="cut_silence">Cut silence:</label>
<input type="checkbox" id="cut_silence" name="cut_silence"/>
<label for="audioformat">Audioformat:</label>
<select id="audioformat" name="audioformat">
<option value="wav">wav</option>
<option value="mp3" selected>mp3</option>
</select>
<p><input type=submit value=Submit>
</form>
'''

@app.route('/', methods=['POST', 'GET'])
def home_page():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        voice_type = request.form['voice']

        #HB added for Julie, test latency
        print(request.form)
        if "skip_corrections" in request.form:
            if request.form["skip_corrections"] == "on":
                skip_corrections = True
            else:
                skip_corrections = False
        else:
            skip_corrections = False
        if "show_corrections" in request.form:
            if request.form["show_corrections"] == "on":
                show_corrections = True
            else:
                show_corrections = False
        else:
            show_corrections = False
        if "skip_cache" in request.form:
            if request.form["skip_cache"] == "on":
                skip_cache = True
            else:
                skip_cache = False
        else:
            skip_cache = False 
        if "cut_silence" in request.form:
            if request.form["cut_silence"] == "on":
                cut_silence = True
            else:
                cut_silence = False
        else:
            #HB cut silence by default
            #cut_silence = False 
            cut_silence = True
        if "audioformat" in request.form:
            audioformat = request.form["audioformat"]
        else:
            audioformat = "mp3" 

        
        with timer:
            if skip_cache:
                (mem, encodedAudio, correctedText) = synthesise_no_cache(text,voice_type,skip_corrections,audioformat,cut_silence)
            else:
                (mem, encodedAudio, correctedText) = synthesise_cache(text,voice_type,skip_corrections,audioformat,cut_silence)

        print(f"TIME in synthesise: {timer.elapsed} -  skip correction: {skip_corrections}, skip cache: {skip_cache}, audioformat: {audioformat}, cut silence: {cut_silence}, text: {text}", flush=True)

        
        if show_corrections:
            print(correctedText)
            print(len(correctedText))
            
            if len(correctedText) == 3:
                gen = correctedText[0]
                morph = correctedText[1]
                gram = correctedText[2]
                correctedText = f"MORPH: {morph}</p><p>GRAM: {gram}</p><p>GEN: {gen}"
            #return {"encodedAudio":encodedAudio, "correctedText":correctedText}
            return input_form + f'<p>{correctedText}<p><audio controls autoplay><source src="data:audio/{audioformat};base64,{encodedAudio}"/></audio>'
            
        else:            
            return send_file(mem, mimetype="audio/mp3")
    return input_form


@app.route('/corrector', methods=['POST', 'GET'])
def corrector():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        #from an_gramadoir import correct_errors_in_text
        #corrected_text = correct_errors_in_text(text)
        from tts_corrector import correct_text
        corrected_text = correct_text(text)
        return {
            "text": corrected_text,
        }
    return '''
        <form method="post">
            <p><input type=text name=text>
        </form>
        '''


@app.route('/voice', methods=['POST', 'GET'])
def voice():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        voice_type = request.form['voice']
        alpha = request.form['alpha']
        all_pass_filter = request.form['filter']
        from tts_corrector import tts_corrector_with_hts_params
        _, sound_file = tts_corrector_with_hts_params(text, voice_type,alpha,all_pass_filter)
        file = sound_file.json()
        sound = file["audioContent"]
        import base64
        sound_ = base64.b64decode(sound)
        import io
        mem = io.BytesIO()
        mem.write(sound_)
        mem.seek(0)
        from datetime import datetime
        now = datetime.now()
        date_time = now.strftime("%m%d%Y%H%M%S")
        filename = f"sound_{date_time}.mp3"
        filename_to_save = os.path.join(basedir,"static/sounds", filename)
        with open(filename_to_save, "wb") as file_to_save:
            file_to_save.write(sound_)
        return render_template("index.html",filename=f"/sounds/{filename}")
    return render_template("index.html")



from joblib import Memory
cachelocation = 'synthesis_cache'
memory = Memory(location=cachelocation, bytes_limit=100000)


@memory.cache    
def synthesise_cache(text,voice_type,skip_corrections=False,audioformat="mp3", cut_silence=False):
    return synthesise(text,voice_type,skip_corrections,audioformat, cut_silence)


def synthesise_no_cache(text,voice_type,skip_corrections=False,audioformat="mp3", cut_silence=False):
    return synthesise(text,voice_type,skip_corrections,audioformat,cut_silence)

def synthesise(text,voice_type,skip_corrections=False,audioformat="mp3", cut_silence=False):
    print(f"synthesise: skip_corrections: {skip_corrections}")
    corrected_text, sound_file = tts_corrector(text, voice_type, skip_corrections, audioformat, cut_silence)
    if not skip_corrections:
        print(f"Original:\t{text}\nCorrected:\t{corrected_text}")

    file = sound_file.json()
    sound = file["audioContent"]
    
    sound_ = base64.b64decode(sound)
    mem = io.BytesIO()
    mem.write(sound_)
    mem.seek(0)
    return (mem, sound, corrected_text)

    

    



if __name__ == "__main__":
    app.debug = True
    app.run()
