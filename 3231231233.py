from pydub import AudioSegment 

audio = AudioSegment.from_file('audio.wav')
a=duration = audio.duration_seconds # 获取时长，单位为秒
print(a)