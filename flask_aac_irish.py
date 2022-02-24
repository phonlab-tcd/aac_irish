from flask import Flask, render_template
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['POST', 'GET'])
def home_page():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        voice_type = request.form['voice']
        from tts_corrector import tts_corrector
        _, sound_file = tts_corrector(text, voice_type)
        file = sound_file.json()
        sound = file["audioContent"]
        import base64
        sound_ = base64.b64decode(sound)
        import io
        mem = io.BytesIO()
        mem.write(sound_)
        mem.seek(0)
        from flask import send_file
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
            <p><input type=submit value=Submit>
        </form>
        '''


@app.route('/corrector', methods=['POST', 'GET'])
def corrector():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        from an_gramadoir import correct_errors_in_text
        corrected_text = correct_errors_in_text(text)
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
