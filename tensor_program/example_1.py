import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from sklearn.metrics import confusion_matrix
#tf.__version__
from tensorflow.examples.tutorials.mnist import input_data

#Download the mnist data
data = input_data.read_data_sets("data/mnist", one_hot=True)

#print the information of dataset
print("Size of:")
print("- Training set:\t\t{}".format(len(data.train.labels)))
print("- Test set:\t\t{}".format(len(data.test.labels)))
print("- Validation set:\t\t{}".format(len(data.validation.labels)))

#data.test.labels[0:5,:]
data.test.cls = np.array([label.argmax() for label in data.test.labels])
#data.test.cls[0:5]

#set the parameters
img_size = 28
img_size_flat = img_size * img_size
img_shape = (img_size, img_size)
num_classes = 10

def plot_images(images, cls_true, cls_pred=None):
  assert len(images) == len(cls_true) == 9
  #Create figure with 3*3 sub-plots
  fig, axes = plt.subplots(3, 3)
  fig.subplots_adjust(hspace=0.3, wspace=0.3)

  for i, ax in enumerate(axes.flat):
    #Plot image
    ax.imshow(images[i].reshape(img_shape), cmap='binary')
    #Show true and predicted classes
    if cls_pred is None:
      xlabel = "True: {0}".format(cls_true[i])
    else:
      xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])
    ax.set_xlabel(xlabel)

    #Remove ticks from the plot
    ax.set_xticks([])
    ax.set_yticks([])


#Get the first images from the test-set.
images = data.test.images[0:9]

#Get the true classes for those images
cls_true = data.test.cls[0:9]

'''
#test the exiting dataset
plot_images(images=images, cls_true=cls_true)
plt.show()
'''

x = tf.placeholder(tf.float32, [None, img_size_flat], name='X-input')
y_true = tf.placeholder(tf.float32, [None, num_classes], name='Y-input')
y_true_cls = tf.placeholder(tf.int64, [None])
weights = tf.Variable(tf.zeros([img_size_flat, num_classes]), name='Weight')
biases = tf.Variable(tf.zeros([num_classes]), name ='Bias')

'''
#Tensorboard histogram summary
tf.histogram_summary('Weight', weights)
tf.histogram_summary('Bias', biases)
#tf.summary.histogram('Weight', weights)
#tf.summary.histogram('Bias', biases)
'''

logits = tf.matmul(x, weights) + biases
y_pred = tf.nn.softmax(logits)
y_pred_cls = tf.argmax(y_pred, dimension=1)


with tf.name_scope('Cost'):
  cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_true)
  cost = tf.reduce_mean(cross_entropy)
with tf.name_scope('train'):
  optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(cost)
correct_prediction = tf.equal(y_pred_cls, y_true_cls)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#with tf.Session() as sess:
session = tf.Session()
session.run(tf.global_variables_initializer())
#write the graph to a file
writer = tf.summary.FileWriter('./graphs/linear_reg', session.graph)
batch_size = 100

#define the optimize function
def optimize(num_iterations):
  for i in range(num_iterations):
    x_batch, y_true_batch = data.train.next_batch(batch_size)
    feed_dict_train = {
            x: x_batch,
            y_true: y_true_batch}
    session.run(optimizer, feed_dict=feed_dict_train)

feed_dict_test = {x: data.test.images,
          y_true: data.test.labels,
          y_true_cls: data.test.cls}
def print_accuracy():
  #Use Tensorflow to compute the accuracy
  acc = session.run(accuracy, feed_dict=feed_dict_test)

  #Print the accuracy
  print("Accuracy on test-set: {0:.1%}".format(acc))

def print_confusion_matrix():
  #Get the true classifications for the test-set.
  cls_true = data.test.cls

  #Get the predicted classifications for the test-set.
  cls_pred = session.run(y_pred_cls, feed_dict = feed_dict_test)
  #GEt the confusion matrix using sklearn
  cm = confusion_matrix(y_true=cls_true, y_pred=cls_pred)

  #Print the confusion matrix as text
  print(cm)

  #Plot the confusion matrix as an image.
  plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)

  #Make various adjustments to the plot
  plt.tight_layout()
  plt.colorbar()
  tick_marks = np.arange(num_classes)
  plt.xticks(tick_marks, range(num_classes))
  plt.yticks(tick_marks, range(num_classes))
  plt.xlabel('Predicted')
  plt.ylabel('True')

def plot_example_errors():
  #Use TensorFlow to get a list of boolean values
  #whether each tes-image has been correctly classified
  #and a list for the predicted class of each image.
  correct, cls_pred = session.run([correct_prediction, y_pred_cls], feed_dict=feed_dict_test)

  #Negate the boolean array
  incorrect = (correct == False)

  #Get the images from the test-set that have been
  #incorrectly classified
  cls_pred = cls_pred[incorrect]

  #Plot the first 9 images
  plot_images(images=images[0:9], cls_true=cls_true[0:9], cls_pred=cls_pred[0:9])

def plot_weights():
   #Get the values for the weights from the TensorFlow variable
  w = session.run(weights)

  #Get the lowest and hightest values for the weights.
  #This is used to correct the colour intensity across
  #the images so they can be compared with each other.
  w_min = np.min(w)
  w_max = np.max(w)

  #Create figure with 3*4 sub-plots.
  #where the last 2 sub-plots are unused
  fig, axes = plt.subplots(3, 4)
  fig.subplots_adjust(hspace=0.3, wspace=0.3)

  for i, ax in enumerate(axes.flat):
    #Only use the weights for the first 10 sub-plots.
    if i<10:
      #Get the weights for the i'th digit and reshape it.
      #Note that w.shape == (img_size_flat, 10) 
      image = w[:, i].reshape(img_shape)

      #Set the label for the sub-plot.
      ax.set_xlabel("Weights: {0}".format(i))

      #Plot the image.
      ax.imshow(image, vmin=w_min, vmax=w_max, cmap='seismic')
    #Remove ticks from each sub-plot.
    ax.set_xticks([])
    ax.set_yticks([])

print_accuracy()
plot_example_errors()
#plt.show()

optimize(num_iterations=1)
print_accuracy()
plot_example_errors()
plot_weights()
#plt.show()

optimize(num_iterations=9)
#plt.show()
print_accuracy()
plot_example_errors()
plot_weights()
#plt.show()

optimize(num_iterations=990)
print_accuracy()
plot_example_errors()
plot_weights()
print_confusion_matrix()
#plt.show()

writer.close() 
session.close()

#tensorboard --logdir=./graphs/linear_reg --port=6006
