from scipy.io import wavfile
from scipy.fft import fft, ifft
from scipy.signal import convolve
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt

file_path = r'C:\Users\Marcos Portela\Documents\Desenv\repository\github\trabalho-miqueas\projeto-computacional-filtro\arquivos_trabalho\ImperialPlusCantina.wav'

# Carregar o arquivo .wav
try:
    sample_rate, signal = wavfile.read(file_path)

    # Create subplots
    fig, axs = plt.subplots(7, 1, figsize=(10, 12))

    # Plotar o gráfico do sinal 𝑥[𝑛]
    axs[0].plot(signal)
    axs[0].set_title('Sinal x[n]')
    axs[0].set_xlabel('Amostras')
    axs[0].set_ylabel('Amplitude')

    X = fft(signal)

    # Plotar o gráfico do espectro (magnitude) de 𝑥 [ 𝑛 ]
    axs[1].plot(np.abs(X))
    axs[1].set_title('Espectro de x[n]')
    axs[1].set_xlabel('Frequência (Hz)')
    axs[1].set_ylabel('Magnitude')

    # Gerar resposta ao impulso ℎ[𝑛]
    W = 1200  # Largura do pulso em Hz
    T = 1 / W  # Período do pulso
    
    print(f'Largura do pulso: {W}')
    print(f'Período do Pulso: {W}')
    print(f'Tamanho do Signal: {len(signal)}')
    print(f'number of channels: {signal.shape[0]}')
    #print(f'Lengh Signal Audio: {signal.shape[0] / sample_rate}')
    print(f'Sample Rate: {sample_rate}')

    n = np.arange(0, 60 * sample_rate)  # Considerando apenas os primeiros 0.01 segundos
    h = np.sinc(2 * W * (n / sample_rate - T / 2))  # Pulso retangular usando sinc function

    print(f'Tamanho n: {len(n)}')
    print(f'Tamanho de h: {len(h)}')

    # Plotar o gráfico da resposta ao impulso ℎ[𝑛]
    axs[2].plot(h)
    axs[2].set_title('Resposta ao impulso h[n]')
    axs[2].set_xlabel('Amostras')
    axs[2].set_ylabel('Amplitude')

    # Calcular a resposta do filtro 𝑦[𝑛] usando o método da convolução no tempo
    y_conv = convolve(signal, h, mode='same')

    # Calcular a Transformada de Fourier de 𝑦[𝑛] (método da convolução)
    Y_conv = fft(y_conv)

    # Trim or zero-pad the h array to match the length of the signal array
    #h_trimmed = np.pad(h[:len(signal)], (0, len(signal) - len(h)), mode='constant')

    # Calcular a resposta do filtro 𝑦[𝑛] usando o método da multiplicação na frequência
    y_freq = signal * h
    Y_freq = fft(y_freq)

    # Comparar os resultados
    axs[3].plot(y_conv)
    axs[3].set_title('Saída de y[n] (Convolução no tempo)')

    axs[4].plot(np.abs(Y_conv))
    axs[4].set_title('Espectro de y[n] (Convolução no tempo)')

    axs[5].plot(y_freq)
    axs[5].set_title('Saída de y[n] (Multiplicação na frequência)')

    axs[6].plot(np.abs(Y_freq))
    axs[6].set_title('Espectro de y[n] (Multiplicação na frequência)')

    # Calcular a Transformada Inversa de Fourier da resposta do método da multiplicação na frequência
    y_ifft_freq = ifft(Y_freq)

    # Adicionar um novo subplot para y_ifft
    axs[6].plot(y_ifft_freq.real)
    axs[6].set_title('Saída de y[n] (Multiplicação na frequência + IFT)')

    # Adjust layout to prevent clipping of titles
    plt.tight_layout()

    plt.show()

    # Ajustar a escala para valores inteiros de 16 bits (PCM)
    #y_ifft_int = np.int16(y_ifft_freq.real)
    #y_ifft_scaled = y_ifft_freq.real / np.max(np.abs(y_ifft_freq.real))
    y_ifft_int16 = np.int16(y_ifft_freq.real / np.max(np.abs(y_ifft_freq.real)) * 32767)

    #y_ifft_int = np.int32(y_ifft_scaled * 2147483647)  # Scale to the range of 16-bit integers
 

    # Calcular a resposta do filtro 𝑦[𝑛] usando o método da convolução no tempo
    y_conv = convolve(signal, h, mode='same')

    # Escrever o sinal processado em um arquivo .wav
    write('y_conv.wav', sample_rate, np.int16(y_conv.real))

    # Escrever o sinal processado em um arquivo .wav
    write('y_filtered.wav', sample_rate, y_ifft_int16)

except Exception as e:
    print(f"An error occurred: {e}")