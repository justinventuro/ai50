Requirements:
https://cs50.harvard.edu/ai/2020/projects/5/traffic/

_Test 1:_ (same as handwriting)     
tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
        ),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(128, activation="relu"),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]   
**loss: 3.4830 - accuracy: 0.0559**                                           

_Test 2:_ (double the convulation and pool)     
tf.keras.layers.Conv2D(
    32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
tf.keras.layers.Conv2D(
    32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
),
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(128, activation="relu"),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
])  
**loss: 0.0852 - accuracy: 0.9661**

_Test 3:_ (same as above, dropout rate 0.4)     
**0.9080 accuracy**

_Test 4_ (same as above, dropout rate 0.2)     
 **loss: 0.5421 - accuracy: 0.9300**
 
 _Test 5_ (2 hidden layers (128 neurons) with 0.5 dropout)

tf.keras.layers.Dense(128, activation="relu"),
tf.keras.layers.Dropout(0.5),   
tf.keras.layers.Dense(128, activation="relu"),
tf.keras.layers.Dropout(0.5),   
**loss: 0.7144 - accuracy: 0.7814**

_Test 6_ (double conv and pool with 64 and 32 filters respectively)     
tf.keras.layers.Conv2D(
64, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
),  
tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),     
tf.keras.layers.Conv2D(
    32, (3, 3), activation="relu", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)
),      
**loss: 0.2385 - accuracy: 0.9346**

_Test 6_ (double conv and pool with 64 and 32 filters respectively, 2 layers 256 neurons and 128 neurons)       
loss: 0.2728 - accuracy: 0.9108

_Test 7_ (double the convulation and pool, single layer 256 neurons)    
**loss: 0.1506 - accuracy: 0.9650**

_Test 8_ (double the convulation and pool, single layer 256 neurons, 0.5 test size)     
**loss: 0.1587 - accuracy: 0.9152**

_Test 9_ (double the convulation and pool, single layer 256 neurons, 0.3 test size)     
**loss: 0.2321 - accuracy: 0.9364**

Therefore test 7 had the best accuracy with a %96.5. Just to be sure I averaged 3 tests resulting in 
(%96.5, %97.22, %96.53).
The process I used was to chance one parameter at a time, in multiple directions, and see how it impacted the accuracy.
The first parameter I changed was doubling the convolution and pool cycle, this increased the accuracy from %5 to
%96, a dramatic increase. After this I decided to try lowering the dropout rate to see if the model could fit the data
better. This decreased accuracy.
Next I tried increasing the amount of filters on the first convolution, this only slightly decreased accuracy.
After this I tried adding an extra hidden layer, this actually decreased accuracy dramatically to %78. Finally I tried modifying the
test size up and down from 0.4. These both slightly decreased accuracy.                                                                         
The conclusion is that adding an extra cycle of convultion had the most dramatic increase, and by doubling the neurons in the only hidden
layer helped slightly. Overallmy results were pretty random and I know I need to learn more about which parameters 
are best to solve which problems.
