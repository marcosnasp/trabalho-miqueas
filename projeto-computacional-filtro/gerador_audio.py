from scipy.io import wavfile
from scipy.fft import fft, ifft
from scipy.signal import convolve
from scipy.io.wavfile import write
import numpy as np

file_path = r'C:\Users\Marcos Portela\Documents\Desenv\repository\github\trabalho-miqueas\projeto-computacional-filtro\arquivos_trabalho\ImperialPlusCantina.wav'

# Carregar o arquivo .wav
try:
    sample_rate, signal = wavfile.read(file_path)

    W = 1200  # Largura do pulso em Hz
    T = 1 / W  # Período do pulso

    n = np.arange(0, 60 * sample_rate)  # Considerando apenas os primeiros 60 segundos
    h = np.sinc(2 * W * (n / sample_rate - T / 2))  # Pulso retangular usando sinc function

    print(f'Width of the pulse: {W}')
    print(f'Period of the pulse: {T}')
    print(f'Length of Signal: {len(signal)}')
    print(f'Number of channels: {signal.shape[0]}')
    print(f'Sample Rate: {sample_rate}')

    # Calcular a resposta do filtro 𝑦[𝑛] usando o método da convolução no tempo
    y_conv = convolve(signal, h, mode='same')

    # Calcular a Transformada de Fourier de 𝑦[𝑛] (método da convolução)
    Y_conv = fft(y_conv)

    # Calcular a resposta do filtro 𝑦[𝑛] usando o método da multiplicação na frequência
    y_freq = signal * h
    Y_freq = fft(y_freq)

    # Calcular a Transformada Inversa de Fourier da resposta do método da multiplicação na frequência
    y_ifft_freq = ifft(Y_freq)

    # Ajustar a escala para valores inteiros de 16 bits (PCM)
    y_ifft_int16 = np.int16(y_ifft_freq.real / np.max(np.abs(y_ifft_freq.real)) * 32767)

    print(f'Time-domain Convolution: {y_conv}')
    print(f'Frequency-domain Convolution Spectrum: {np.abs(Y_conv)}')
    print(f'Time-domain Frequency Multiplication: {y_freq}')
    print(f'Frequency-domain Frequency Multiplication Spectrum: {np.abs(Y_freq)}')

    # Calcular a resposta do filtro 𝑦[𝑛] usando o método da convolução no tempo
    y_conv = convolve(signal, h, mode='same')

    # Escrever o sinal processado em um arquivo .wav
    write('y_conv.wav', sample_rate, np.int16(y_conv.real))

    # Escrever o sinal processado em um arquivo .wav
    write('y_filtered.wav', sample_rate, y_ifft_int16)

except Exception as e:
    print(f"An error occurred: {e}")
