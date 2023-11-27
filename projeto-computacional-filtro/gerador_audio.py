from scipy.io import wavfile
from scipy.fft import fft, ifft
from scipy.signal import convolve
from scipy.io.wavfile import write
import numpy as np

file_path = r'C:\Users\Marcos Portela\Documents\Desenv\repository\github\trabalho-miqueas\projeto-computacional-filtro\arquivos_trabalho\ImperialPlusCantina.wav'

# Carregar o arquivo .wav
try:
    sample_rate, signal = wavfile.read(file_path)

    W = 1800 # Largura do pulso em Hz
    T = 1 / W # Período do pulso

    print(f'Passagem para np.arange: {60 * sample_rate}')
    n = np.arange(0, 60 * sample_rate) # Considerando apenas os primeiros 60 segundos
    h = np.sinc(2 * W * (n / sample_rate - T / 2)) # Pulso retangular usando sinc function

    print(f'Largura do Pulso em Hz: {W} Hz')
    print(f'Período do Pulso: {T} Segundos')
    print(f'Comprimento do Sinal: {len(signal)}')
    print(f'Número de Canais: {signal.shape[0]}')
    print(f'Taxa de Amostragem em Hz: {sample_rate}')

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
    y_norm = y_conv / W
    y_norm_int16 = np.int16(y_norm.real / np.max(np.abs(y_norm.real)) * 32767)

    print(f'Convolução no domínio do Tempo: {y_conv}')
    print(f'Espectro de convolução no Domínio da Frequência: {np.abs(Y_conv)}')
    print(f'Multiplicação da Frequência no Domínio do Tempo: {y_freq}')
    print(f'Espectro de Multiplicação de Frequência no Domínio do Tempo: {np.abs(Y_freq)}')

    # Escrever o sinal processado em um arquivo .wav
    write(f'convolucionado_{W}.wav', sample_rate, np.int16(y_conv.real))

    # Escrever o sinal processado em um arquivo .wav
    write(f'filtrado_normalizado_{W}.wav', sample_rate, y_norm_int16)

except Exception as e:
    print(f"An error occurred: {e}")
