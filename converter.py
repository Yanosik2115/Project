from pydub import AudioSegment


def convertToWav(input_file) -> str:
    if not input_file.endswith(".mp3"):
        raise "File format must be mp3"

    output_file = f"./SongsWav/{input_file[:-4]}.wav"
    input = f"./Songs/{input_file}"
    sound = AudioSegment.from_mp3(input)
    sound.export(output_file, format="wav")
