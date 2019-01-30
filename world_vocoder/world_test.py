from scipy.io import wavfile #https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.io.wavfile.read.html
import pyworld as pw
import numpy as np
import soundfile as sf

WAV_FILE = './sample_voice.wav'

rate, data = wavfile.read(WAV_FILE)
data = data.astype(np.float)  # WORLDはfloat前提のコードになっているのでfloat型にしておく

# _f0, _time = pw.dio(data[:], fs,f0_floor=50.0, f0_ceil=600.0, channels_in_octave=2)    # 基本周波数の抽出
_f0, t = pw.dio(data, rate)  # 基本周波数の抽出
f0 = pw.stonemask(data, _f0, t, rate)  # 基本周波数の修正
sp = pw.cheaptrick(data, f0, t, rate)  # スペクトル包絡の抽出
ap = pw.d4c(data, f0, t, rate)  # 非周期性指標の抽出

# 得られた特徴量から音声を合成する
synthesized = pw.synthesize(f0, sp, ap, rate)
sf.write('./world_output.wav', synthesized, rate)