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


@app.route('/', methods=['POST', 'GET'])
def home_page():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        voice_type = request.form['voice']

        #HB added for Julie, test latency
        print(request.form)
        if "use_corrections" in request.form:
            if request.form["use_corrections"] == "on":
                use_corrections = True
            else:
                use_corrections = False
        else:
            use_corrections = False
        if "use_cache" in request.form:
            if request.form["use_cache"] == "on":
                use_cache = True
            else:
                use_cache = False
        else:
            #HB this becomes the default..
            use_cache = False 
        if "audioformat" in request.form:
            audioformat = request.form["audioformat"]
        else:
            audioformat = "mp3" 

        
        with timer:
            if use_cache:
                mem = synthesise_cache(text,voice_type,use_corrections,audioformat)
            else:
                mem = synthesise_no_cache(text,voice_type,use_corrections,audioformat)
        print(f"TIME in synthesise: {timer.elapsed} -  correct: {use_corrections}, cache: {use_cache}, audioformat: {audioformat}, text: {text}", flush=True)
            
        return send_file(mem, mimetype="audio/mp3")
    return '''
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
             <label for="use_corrections">Use corrections:</label>
             <input type="checkbox" id="use_corrections" name="use_corrections"/>
             <label for="use_cache">Use cache:</label>
             <input type="checkbox" id="use_cache" name="use_cache" checked/>
 
            <p><input type=submit value=Submit>
        </form>
        '''


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
def synthesise_cache(text,voice_type,correct=True,audioformat="wav"):
    return synthesise(text,voice_type,correct,audioformat)


def synthesise_no_cache(text,voice_type,correct=True,audioformat="wav"):
    return synthesise(text,voice_type,correct,audioformat)

def synthesise(text,voice_type,correct=True,audioformat="wav"):
    _, sound_file = tts_corrector(text, voice_type, correct, audioformat)
    file = sound_file.json()
    sound = file["audioContent"]
    
    sound_ = base64.b64decode(sound)
    mem = io.BytesIO()
    mem.write(sound_)
    mem.seek(0)
    return mem

    

    



if __name__ == "__main__":
    app.debug = True
    app.run()
