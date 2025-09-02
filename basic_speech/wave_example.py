import wave 

obj = wave.open("file_example_WAV_1MG.wav", "rb")

print("No. of channel ", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate ", obj.getframerate())
print("Number of frames ", obj.getnframes())
print("parameters ",obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print("audio time ",t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/4)

obj.close()

obj_new = wave.open("file_exp_new.wav", "wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)

obj_new.writeframes(frames)
obj_new.close()