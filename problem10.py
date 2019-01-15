import tensorflow as tf
class MultiplicationLayer(tf.keras.layers.Layer):
  def __init__(self, num_outputs):
    super(MultiplicationLayer, self).__init__()
    self.num_outputs = num_outputs
    
  def build(self, input_shape):
    self.kernel = self.add_variable("kernel", 
                                    shape=[int(input_shape[-1]), 
                                           self.num_outputs])
    
  def call(self, input):
    return tf.matmul(input, 255)
  
layer = MultiplicationLayer(10)
print(layer(tf.zeros([10, 5])))
print(layer.variables)
