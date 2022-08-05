# aac_irish

This project combines ABAIR's Irish language voices with a trio of parsers (tts_corrector.py):
    1) An Gramadóir's grammar checker (an_gramadoir.py)
    2) ABAIR's genitive parser (genitive_parser.py)
    3) my own morphological parser based on AAC boards (morphological_parser.py)
    to create a self-correcting Irish language TTS API for use in AAC devices. 
This project also uses the voices developed at ABAIR (abair_voice.py).

Three pages are available from the flask server (flask_aac_irish.py):
1) Get voice of choice where the inputted text has been corrected. @ /
2) Get correction of text alone.    @ /corrector
3) Get hand-tuned parameterised hts voice. @ /voice


HB notes
synthesise_cache('Is maith liom ba mhaith liom', 'Ulster', False, 'mp3', True)
synthesise: skip_corrections: False
Is maith liom ba mhaith liom
Is fearr liom ba mhhaith liom
Is fearr liom ba mhhaith liom
Is fearr liom ba mhhaith liom
Original:       Is maith liom ba mhaith liom
Corrected:      Is fearr liom ba mhhaith liom
_________________________________________________synthesise_cache - 2.7s, 0.0min
TIME in synthesise: 2.7177788205444813 -  skip correction: False, skip cache: False, audioformat: mp3, cut silence: True, text: Is maith liom ba mhaith liom

Andy: "sí," works, "sí." doesn't - maybe add comma to single words? TEST 