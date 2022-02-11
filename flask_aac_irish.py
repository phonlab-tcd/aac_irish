from flask import Flask
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home_page():
    from flask import request
    if request.method == 'POST':
        text = request.form['text']
        voice_type = request.form['voice']
        from tts_corrector import tts_corrector
        _, sound_file = tts_corrector(text, voice_type)
        import io
        mem = io.BytesIO()
        mem.write(sound_file.content)
        mem.seek(0)
        from flask import send_file
        return send_file(mem, mimetype="audio/mp3")
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
        import io
        mem = io.BytesIO()
        mem.write(sound_file.content)
        mem.seek(0)
        from flask import send_file
        return send_file(mem, mimetype="audio/mp3")
    return '''
        <form method="post">
            <p><input type=text name=text>
             <label for="voice">Choose a voice:</label>
             <select id="voice" name="voice">
             <option value="irish_1">Ulster</option>
             <option value="irish_3">Connacht 1</option>
             <option value="irish_5">Connacht 2</option>
             <option value="irish_7">Munster</option>
             </select> 
             <br>
            <label for="alpha">All-pass constant (between 0.2 and 0.6):</label>
             <br>
            <input type="range" id="alpha" name="alpha" value="0.4" min="0.2" max="0.6" step=0.01 oninput="this.nextElementSibling.value = this.value">
            Value:
            <output></output>
            <br><br>
            <label for="filter">Filter (between -20 and 20):</label>
             <br>
            <input type="range" id="filter" name="filter" value="0" min="-20" max="20" step=0.1 oninput="this.nextElementSibling.value = this.value">
            Value:
            <output></output>
            <br><br>
            <p><input type=submit value=Submit>
        </form>
        '''
