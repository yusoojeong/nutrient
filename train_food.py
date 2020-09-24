import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import utils
from tensorflow.keras import layers
from tensorflow.keras import datasets
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

import numpy as np
import matplotlib.pyplot as plt


############################데이터탐색############################

# tensorflow keras 내에 있는 dataset cifar10을 불러온다.
cifar_mnist = datasets.cifar10

# cifar10의 데이터셋을 로드해서 train, test(validation)로 나눈다
(train_images, train_labels),(test_images, test_labels) = cifar_mnist.load_data()

# 미리 정해진 사물들을 알기쉽게 텍스트로
class_names=[
    'Airplane',
    'Car',
    'Birs',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Ship',
    'Truck'
]
#print("classname : "+class_names[1])
#print(type(train_labels))

# 창 크기를 가로 10, 세로 10으로 정함
plt.figure(figsize=(10,10))
for i in range(25):
    # subplot은 여러 그래프를 한 번에 띄우기 위함. 줄이 길수록 subplots가 편함
    plt.subplot(5,5,i+1)
    # matplotlib에서 그림을 그릴 때, tick을 몇 개나, 또 어떤 label로 표현할지를 조절하고 싶을때 plt.xticks()를 사용합니다.
    plt.xticks([])
    plt.yticks([])
    # cmap = color map 설정
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()

batch_size = 64     # 
num_classes = 10    # ?
epochs = 50         # 반복 횟수

# .astype: 타입을 바꾸는 함수를 통해 float 실수화. -> 255로 나누기
train_images = train_images.astype('float32')
train_images = train_images / 255

test_images = test_images.astype('float32')
test_images = test_images / 255

train_labels = utils.to_categorical(train_labels, num_classes)
test_labels = utils.to_categorical(test_labels, num_classes)


print(len(train_labels)) # 50000
print(len(test_labels)) # 10000

############################모델구성############################
model = keras.Sequential([
    Conv2D(32,kernel_size=(3,3),padding='same', input_shape=train_images.shape[1:],
    activation=tf.nn.relu),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),

    Conv2D(64,kernel_size=(3,3),padding='same', activation=tf.nn.relu),
    MaxPooling2D(pool_size=(2,2)),
    Dropout(0.25),

    Flatten(),
    Dense(64,activation=tf.nn.relu),
    Dropout(0.25),
    Dense(num_classes, activation=tf.nn.softmax)
])

model.summary()

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

#print(len(train_images)) # 50000 
#print(len(test_images)) # 50000
#print(len(train_labels)) # 50000
#print(len(test_labels)) # 10000
# 왜?


############################모델훈련############################
# 과대적합을 막기위해 설정
early_stopping = EarlyStopping(monitor='val_loss', patience=35)

history = model.fit(
    train_images, train_labels,
    epochs=epochs,
    validation_data=(test_images, test_labels),
    shuffle=True,
    callbacks=[early_stopping]
)


############################평가############################
loss, acc = model.evaluate(test_images,test_labels)
print("\nloss: {}, Acc: {}".format(loss,acc))



def plt_show_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)


def plt_show_acc(history):
    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc=0)


plt_show_loss(history)
plt.show()

#plt_show_acc(history)
#plt.show()



############################예측############################
predictions = model.predict(test_images)

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == np.argmax(true_label):
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],100*np.max(predictions_array),class_names[np.argmax(true_label)]),color=color)

def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i] #
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0,1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[np.argmax(true_label)].set_color('blue')

num_rows=5
num_cols=3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
    plt.subplot(num_rows, 2*num_cols, 2*i+2)
    plot_value_array(i, predictions, test_labels) #
plt.show()