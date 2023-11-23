from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt
import scipy.fft as spfft
import numpy as np

# Ler o arquivo .wav e obter o sinal x[n]
a = read("ImperialPlusCantina.wav")
x = np.array(a[1], dtype=float)

# Limitar o processamento para alguns segundos iniciais (opcional)
duration = 0.02
samples_to_keep = int(duration * a[0])
x = x[:samples_to_keep]

# Plotar o gráfico do sinal x[n]
plt.plot(x)
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.title('Sinal x[n]')
plt.show()

# Calcular a Transformada de Fourier de x[n]
X = spfft.fft(x)

# Plotar o gráfico do espectro (magnitude) de x[n]
frequencies = spfft.fftfreq(len(x), 1 / a[0])
plt.plot(frequencies, np.abs(X))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.title('Espectro de x[n]')
plt.show()

# Função para criar a resposta ao impulso h[n]
def rectangular_pulse(W, sample_rate):
    length = int(W * sample_rate)
    h = np.ones(length)
    return h

# Definir a largura do pulso retangular
W = 2000 # Largura em Hz

# Criar a resposta ao impulso h[n]
h = rectangular_pulse(W, a[0])

# Plotar o gráfico da resposta ao impulso h[n]
plt.plot(h)
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.title('Resposta ao Impulso h[n]')
plt.show()

# Calcular a Transformada de Fourier de h[n]
H = spfft.fft(h)

# Plotar o gráfico do espectro (magnitude) de h[n]
frequencies_h = spfft.fftfreq(len(h), 1 / a[0])
plt.plot(frequencies_h, np.abs(H))
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude')
plt.title('Espectro de h[n]')
plt.show()

# Calcular a resposta do filtro y[n] para o sinal de áudio x[n] usando a convolução no tempo
y_conv = np.convolve(x, h, mode='same')

# Calcular a Transformada de Fourier de y_conv
Y_conv = spfft.fft(y_conv)

X_padded = np.zeros(len(H), dtype=complex)
X_padded[:len(X)] = X
X = X_padded

# Comparar a resposta usando convolução no tempo com a resposta usando multiplicação na frequência
Y_freq = X * H

# Calcular a Transformada Inversa de Fourier da resposta usando multiplicação na frequência
y_freq = spfft.ifft(Y_freq)

# Plotar o gráfico comparando as respostas
plt.plot(y_conv, label='Convolução no Tempo')
plt.plot(np.real(y_freq), label='Multiplicação na Frequência')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.title('Resposta do Filtro y[n]')
plt.legend()
plt.show()

# Escrever o sinal filtrado y_conv em um arquivo .wav
write("filtered_audio_conv.wav", a[0], np.array(y_conv, dtype=np.int16))

# Escrever o sinal filtrado y_freq em um
write("filtered_audio_freq.wav" , a[0], np.array(np.real(y_freq), dtype=np.int16))