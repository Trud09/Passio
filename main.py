import tensorflow as tf
import tensorflow.keras as keras

def create_model(image_size =[224, 224, 3]):
      input = keras.Input(image_size)
      x = keras.applications.MobileNetV2(input_shape=image_size, include_top=False)(input)
      vector = keras.layers.Flatten()(x)

      square = tf.math.square(vector)
      l2 = tf.math.reduce_sum(square, 1)
      output = tf.math.divide_no_nan(vector, l2)

      model = keras.Model(input, output)
  
      return model

if __name__ == "__main__":
	model = create_model()
	model.save('/model/MobileNetV2_l2.h5')
      