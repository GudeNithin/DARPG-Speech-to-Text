# import speech_recognition as sr
# from pydub import AudioSegment
# from deep_translator import GoogleTranslator
# import os
# import sys

# uploads_folder = 'uploads'

# def convert_mp3_to_wav(mp3_file_path):
#   audio = AudioSegment.from_mp3(mp3_file_path)
#   wav_file_path = mp3_file_path.replace('.mp3', '.wav')
#   audio.export(wav_file_path, format="wav")
#   return wav_file_path

# def process_audio_segment(segment, recognizer):
#   audio_data = segment.raw_data
#   audio_segment = AudioSegment(audio_data,
#                                frame_rate=segment.frame_rate,
#                                sample_width=segment.sample_width,
#                                channels=segment.channels)

#   temp_wav_file = "temp_audio.wav"
#   audio_segment.export(temp_wav_file, format="wav")

#   with sr.AudioFile(temp_wav_file) as temp_source:
#     audio = recognizer.record(temp_source)

#   try:
#     text = recognizer.recognize_google(audio, language='hi-IN')
#     return text
#   except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio.")
#     return ""
#   except sr.RequestError as e:
#     print(
#         f"Could not request results from Google Speech Recognition service; {e}"
#     )
#     return ""
#   finally:
#     os.remove(temp_wav_file)

# def translate_to_english(text):
#   translated_text_en = GoogleTranslator(source='hi',
#                                         target='en').translate(text)
#   return translated_text_en

# def translate_to_hinglish(text):
#   translated_text_hi = GoogleTranslator(source='en',
#                                         target='hi').translate(text)
#   return translated_text_hi

# def hindi_audio_to_english_hinglish_text(audio_file_path):
#   recognizer = sr.Recognizer()

#   with sr.AudioFile(audio_file_path) as source:
#     recognizer.adjust_for_ambient_noise(source)

#     print("Converting audio to text...")

#     audio = AudioSegment.from_file(audio_file_path)
#     full_text_hindi = ""
#     segment_length = 18 * 1000

#     for start_time in range(0, len(audio), segment_length):
#       segment = audio[start_time:start_time + segment_length]
#       segment_text = process_audio_segment(segment, recognizer)
#       full_text_hindi += segment_text + " "

#     print("Hindi Text: ", full_text_hindi)

#     translated_text_en = translate_to_english(full_text_hindi)
#     translated_text_hi = translate_to_hinglish(full_text_hindi)

#     print("Translated Text in English: ", translated_text_en)
#     print("Translated Text in Hinglish: ", translated_text_hi)

# if __name__ == "__main__":
#   if len(sys.argv) != 2:
#     print("Usage: python translation.py <file_path>")
#     sys.exit(1)

#   mp3_file_path = "uploads/7002784528.mp3"
#   print("Processing file:", mp3_file_path)

#   # Convert MP3 to WAV and perform translation
#   wav_file_path = convert_mp3_to_wav(mp3_file_path)
#   hindi_audio_to_english_hinglish_text(wav_file_path)
# import speech_recognition as sr
# from pydub import AudioSegment
# from deep_translator import GoogleTranslator
# import os
# import sys

# uploads_folder = 'uploads'

# def convert_mp3_to_wav(mp3_file_path):
#   audio = AudioSegment.from_mp3(mp3_file_path)
#   wav_file_path = mp3_file_path.replace('.mp3', '.wav')
#   audio.export(wav_file_path, format="wav")
#   return wav_file_path

# def process_audio_segment(segment, recognizer):
#   audio_data = segment.raw_data
#   audio_segment = AudioSegment(audio_data,
#                                frame_rate=segment.frame_rate,
#                                sample_width=segment.sample_width,
#                                channels=segment.channels)

#   temp_wav_file = "temp_audio.wav"
#   audio_segment.export(temp_wav_file, format="wav")

#   with sr.AudioFile(temp_wav_file) as temp_source:
#     audio = recognizer.record(temp_source)

#   try:
#     text = recognizer.recognize_google(audio, language='hi-IN')
#     return text
#   except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio.")
#     return ""
#   except sr.RequestError as e:
#     print(
#         f"Could not request results from Google Speech Recognition service; {e}"
#     )
#     return ""
#   finally:
#     os.remove(temp_wav_file)

# def translate_to_english(text):
#   translated_text_en = GoogleTranslator(source='hi',
#                                         target='en').translate(text)
#   return translated_text_en

# def translate_to_hinglish(text):
#   translated_text_hi = GoogleTranslator(source='en',
#                                         target='hi').translate(text)
#   return translated_text_hi

# def hindi_audio_to_english_hinglish_text(audio_file_path):
#   recognizer = sr.Recognizer()

#   with sr.AudioFile(audio_file_path) as source:
#     recognizer.adjust_for_ambient_noise(source)

#     print("Converting audio to text...")

#     audio = AudioSegment.from_file(audio_file_path)
#     full_text_hindi = ""
#     segment_length = 18 * 1000

#     for start_time in range(0, len(audio), segment_length):
#       segment = audio[start_time:start_time + segment_length]
#       segment_text = process_audio_segment(segment, recognizer)
#       full_text_hindi += segment_text + " "

#     print("Hindi Text: ", full_text_hindi)

#     translated_text_en = translate_to_english(full_text_hindi)
#     translated_text_hi = translate_to_hinglish(full_text_hindi)

#     print("Translated Text in English: ", translated_text_en)
#     print("Translated Text in Hinglish: ", translated_text_hi)
#     return translated_text_en, translated_text_hi,full_text_hindi

# if _name_ == "_main_":
#   if len(sys.argv) != 2:
#     print("Usage: python translation.py <file_path>")
#     sys.exit(1)

#   mp3_file_path = sys.argv[1]
#   print("Processing file:", mp3_file_path)

#   # Convert MP3 to WAV and perform translation
#   wav_file_path = convert_mp3_to_wav(mp3_file_path)
#   hindi_audio_to_english_hinglish_text(wav_file_path)
import speech_recognition as sr
from pydub import AudioSegment
from deep_translator import GoogleTranslator
import os
import sys

uploads_folder = 'uploads'


def convert_mp3_to_wav(mp3_file_path):
  audio = AudioSegment.from_mp3(mp3_file_path)
  wav_file_path = mp3_file_path.replace('.mp3', '.wav')
  audio.export(wav_file_path, format="wav")
  return wav_file_path


def process_audio_segment(segment, recognizer):
  audio_data = segment.raw_data
  audio_segment = AudioSegment(audio_data,
                               frame_rate=segment.frame_rate,
                               sample_width=segment.sample_width,
                               channels=segment.channels)

  temp_wav_file = "temp_audio.wav"
  audio_segment.export(temp_wav_file, format="wav")

  with sr.AudioFile(temp_wav_file) as temp_source:
    audio = recognizer.record(temp_source)

  try:
    text = recognizer.recognize_google(audio, language='hi-IN')
    return text
  except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
    return ""
  except sr.RequestError as e:
    print(
        f"Could not request results from Google Speech Recognition service; {e}"
    )
    return ""
  finally:
    os.remove(temp_wav_file)


def translate_to_english(text):
  translated_text_en = GoogleTranslator(source='hi',
                                        target='en').translate(text)
  return translated_text_en


def translate_to_hinglish(text):
  translated_text_hi = GoogleTranslator(source='en',
                                        target='hi').translate(text)
  return translated_text_hi


def hindi_audio_to_english_hinglish_text(audio_file_path):
  recognizer = sr.Recognizer()

  with sr.AudioFile(audio_file_path) as source:
    recognizer.adjust_for_ambient_noise(source)

    print("Converting audio to text...")

    audio = AudioSegment.from_file(audio_file_path)
    full_text_hindi = ""
    segment_length = 18 * 1000

    for start_time in range(0, len(audio), segment_length):
      segment = audio[start_time:start_time + segment_length]
      segment_text = process_audio_segment(segment, recognizer)
      full_text_hindi += segment_text + " "

    print("Hindi Text: ", full_text_hindi)

    translated_text_en = translate_to_english(full_text_hindi)
    translated_text_hi = translate_to_hinglish(full_text_hindi)

    print("Translated Text in English: ", translated_text_en)
    print("Translated Text in Hinglish: ", translated_text_hi)

    # Write translated text to a file
    with open('translated_text.txt', 'w') as f:
      f.write(translated_text_en)


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python translation.py <file_path>")
    sys.exit(1)

  mp3_file_path = sys.argv[1]
  print("Processing file:", mp3_file_path)

  # Convert MP3 to WAV and perform translation
  wav_file_path = convert_mp3_to_wav(mp3_file_path)
  hindi_audio_to_english_hinglish_text(wav_file_path)
