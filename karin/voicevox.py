import json
import wave
import requests
from pathlib import Path

from karin.const import VOICEVOX_AUDIO_QUERY, VOICEVOX_SYNTHESIS, VOICEVOX_URI

class Voicevox:
    async def generate_wav(self, text: str, speaker: int, output: Path):
        audio_query = requests.post(
            VOICEVOX_URI+VOICEVOX_AUDIO_QUERY.format(text, speaker)
        )
        headers = {'Content-Type': 'application/json'}
        synthesis = requests.post(
            VOICEVOX_URI+VOICEVOX_SYNTHESIS.format(speaker),
            headers=headers,
            data=json.dumps(audio_query.json())
        )

        with wave.open(output, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(synthesis.content)

    