import torch
from fastaudio.core.signal import AudioTensor

def create_sin_wave(seconds = 2, sr = 16000, freq = 400)
    "Creates a sin wave to be used for tests"
    max_samples = freq*seconds*2*pi
    rate = 2*pi*freq/sr
    samples = torch.arange(0, max_samples,, rate, dtype=torch.float)
    sin_wave = torch.sin(samples)
    return sin_wave, sr

def test_audio_tensor(seconds=2, sr =16000, channels=1):
    "Generates an Audio Tensor for testing that is based on a sine wave"
    sin_wave, sr = create_sin_wave(seconds=seconds, sr=sr)
    sin_wave = sin_wave.repeat(channels,1)
    return AudioTensor(sin_wave, sr)