import numpy as np
import matplotlib.pyplot as plt

with open('data.txt', 'r') as f:
    adc_data = np.array([int(line.strip()) for line in f.readlines()])

with open('settings.txt', 'r') as f:
    settings = [float(line.strip()) for line in f.readlines()]
    voltage_step = settings[0]
    time_step = settings[1]

voltage = adc_data * voltage_step
time = np.arange(len(adc_data)) * time_step

max_voltage = np.max(voltage)
charge_time = time[np.argmax(voltage >= 0.99 * max_voltage)]
discharge_time = time[-1] - charge_time

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(time, voltage,
        color='blue',
        linewidth=1.5,
        marker='o',
        markersize=4,
        markevery=20,
        label='V(t)')

ax.set_xlim([0, np.max(time)])
ax.set_ylim([0, 1.1 * np.max(voltage)])

ax.set_xlabel('Время, с', fontsize=12)
ax.set_ylabel('Напряжение, В', fontsize=12)

ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке',
             fontsize=14, pad=20, loc='center', wrap=True)

ax.grid(which='major', linestyle='-', linewidth=0.5, color='gray')
ax.grid(which='minor', linestyle=':', linewidth=0.5, color='lightgray')
ax.minorticks_on()

text_x = 0.7 * np.max(time)
text_y = 0.7 * np.max(voltage)
ax.text(text_x, text_y,
        f'Время заряда = {charge_time:.2f} с\nВремя разряда = {discharge_time:.2f} с',
        fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

ax.legend(fontsize=12)
plt.savefig('rc_plot.svg', format='svg')
plt.show()