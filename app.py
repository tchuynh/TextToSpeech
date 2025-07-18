from flask import Flask, request, send_file, jsonify, render_template
from flask_cors import CORS
from TTS.api import TTS
import tempfile, os

app = Flask(__name__)
CORS(app)  # allow all origins

# Load model once at startup for performance
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
@app.route("/")
def index():
    # Serves your HTML!
    return render_template("index.html")


@app.route('/api/tts', methods=['POST'])
def tts_api():
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Generate temp file
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmpf:
        tmp_path = tmpf.name

    # Generate TTS to file
    tts.tts_to_file(text=text, file_path=tmp_path)

    # Return file as response
    response = send_file(tmp_path, mimetype='audio/wav', as_attachment=False)
    # Cleanup file after sending
    @response.call_on_close
    def cleanup():
        os.remove(tmp_path)
    return response

if __name__ == "__main__":
    app.run()
