import tensorflow as tf 
a = tf.constant([3, -0.5, 2, 7])
b = tf.constant([2.5, 0.0, 2, 8])
c = tf.metrics.mean_squared_error(a,b)
sess = tf.InteractiveSession()
sess.run(tf.local_variables_initializer())
sess.run(tf.global_variables_initializer())
print(sess.run(c))
