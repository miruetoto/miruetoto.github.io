def checkgpu():
    ## 5. Check GPU
    from keras import backend as K
    print('GPU check 4 Keras: '+ str(K.tensorflow_backend._get_available_gpus()))
    import torch
    print('GPU check 4 Pytorch: '+ str(torch.cuda.get_device_name(0)))