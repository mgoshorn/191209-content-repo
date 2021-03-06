import tensorflow as tf

def init(model_dir, with_gpu = True):
    """One time initialization of the model and Tensorflow to be called
    as part of the server startup script."""
    if with_gpu:
        gpus = tf.config.experimental.list_physical_devices('GPU')
        if gpus:
            try:
                for gpu in gpus:
                    tf.config.experimental.set_memory_growth(gpu, True)
                    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            except RuntimeError as e:
                print(e)
    
    return tf.saved_model.load(model_dir)

def preprocess_img(img):
    """Image preprocessing function to prepare image for inference in the model"""
    img.set_shape((None, None, 1))
    img = tf.image.resize(img, [150, 150])
    
    img = tf.reshape(img, (-1, 150, 150, 1))

    # Casting to float32 - necessary as this is the input type of my models 
    # first layer
    img = tf.cast(img, dtype=tf.float32)
    
    # Normalize data and invert
    img = 1 - (img / 255)

    return img

def value_mapper(inference_result):
    np_arr = inference_result[0].numpy()

    # 19 values which represent what characters my model classifies
    chars = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    mapping = {}

    for (key, value) in zip(chars, np_arr):
        mapping[key] = value.item()

    return mapping


