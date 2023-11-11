import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pywt
matplotlib.use('Agg')
def generate_wavelet(xcg,fs,scales, wav):

    #t = np.array(range(len(ecg)-1))/fs            # Timestamps of the ecg samples
    coef, freqs = pywt.cwt(xcg, scales, wav, sampling_period= 1/fs)
    #freqs = freqs * fs
    #print (freqs)
    return coef, freqs


def generate_wavelet_images(sig, record_id, classification, fs, wav, scales, directory, index, resample=True, vmax_q = 99):
    i = index

    records = []
    y = classification
    r = record_id
    x = sig.flatten()
    #reflecting the signal to alleviate boundary effects
    x_padded = np.concatenate(( x[::-1], x, x[::-1]))
    data, f = generate_wavelet(x_padded, fs,scales, wav )
    data = data[:, len(x):len(x)*2]
    data=np.abs(data)
    vmax = np.percentile(data,vmax_q)
    vmin = np.abs(data).min()
    cmap = plt.get_cmap('jet', 128)
    #print (data.shape)
    #Padding to
    #
    print(data.shape)
    #print (data.shape)
    #plt.figure(figsize=(9,5))
    #print (data.shape)
    fig = matplotlib.pyplot.figure(figsize=(4, 3))
    ax = fig.add_subplot(111)
    t = np.arange(data.shape[1]) / fs  # Timestamps of the ECG samples
    if resample:
        data = data[:, ::5]
    plt.imshow(data, cmap=cmap, aspect ='auto', vmax=vmax, vmin=vmin, interpolation = 'None', origin = 'upper')

    #ax.set_yscale('log')
    ax.axis('off')
    fig.savefig(directory+'\\'+str(r)+'_'+str(i)+'.tiff', pad_inches=0, bbox_inches='tight', dpi=100 )
    #plt.close('all')
    matplotlib.pyplot.close(fig)
    #plt.ioff()

    image_dict = {'filename':str(r)+'_'+str(i)+'.tiff','label':y }
    print (str(r)+'_'+str(i)+'.tiff')

    return image_dict