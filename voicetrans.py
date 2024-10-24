import gradio as gr
import assemblyai as aai
from translate import Translator 
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs 
from pathlib import Path
import whisper

def voice_to_voice(audio_file):
    
    #trabscribe audio
    transcription_response = audio_transcription(audio_file)

    '''if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.text'''
    
    text = transcription_response['text']
    es_translation, tr_translation, ja_translation = text_translation(text) 

    es_audio_path = text_to_speech(es_translation)
    tr_audio_path = text_to_speech(tr_translation)
    ja_audio_path = text_to_speech(ja_translation)

    es_path = Path(es_audio_path)
    tr_path = Path(tr_audio_path)
    ja_path = Path(ja_audio_path) 

    return es_path, tr_path, ja_path

def audio_transcription(audio_file):

    '''aai.settings.api_key = "caf76a1e67a1455bacaca3f6556134d9"

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(audio_file)

    return transcription'''

    transcriber = whisper.load_model("base")
    transcription = transcriber.transcribe(audio_file)
    return transcription

def text_translation(text):
    
    translator_es = Translator(from_lang="en", to_lang="es")
    es_text = translator_es.translate(text)

    translator_tr = Translator(from_lang="en", to_lang="tr")
    tr_text = translator_tr.translate(text)

    translator_ja = Translator(from_lang="en", to_lang="ja")
    ja_text = translator_ja.translate(text)

    return es_text, tr_text, ja_text

def text_to_speech(text):
    client = ElevenLabs(
        api_key="sk_ef8de550764713fe8e9d4d36d66fd4b43e8c5f636324c428",
    )

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="Dt2jDzhoZC0pZw5bmy2S",    
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

audio_input = gr.Audio(
    sources=["microphone"],
    type="filepath"
)

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Spanish"),gr.Audio(label="Turkish"),gr.Audio(label="Japanese")]
)

if __name__ == "__main__":
    demo.launch()