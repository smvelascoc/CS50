    # Traffic project
    #### Video Demo:  <https://youtu.be/KvLU3usW_38>
    #### Description:

    The training process started with the minimum requirements: A first convolution layer with 100 filters applied, followed by the flatten layer and the output layer. As a first approach, it gave an acceptable accuracy about 0.915. Then a pooling layer added after the convolution layer with a 2 by 2 matrix showed better results with an accuracy of 0.9267. At this point, some overfitting is shown, considering that the accuracy obtained during the training process was significantly higher than the test accuracy. Then, dropout layer was added. Different dropout parameter was tested. 1% and 5% gave almost the same result. 5% is retained to give the result more aleatorily to the process.

    Finally, testing about adding more layer than the basic ones was tested.  Adding two and three layers with convolution and pooling layer gave a better accuracy. A fourth layer did not give any considerable improvement in the training result. Then, only three layers of convolution and pooling was retained. Filters size in the convolution layer are set to 100, where a good compromise about accuracy and training time. An additional intermediate flatten layer was tested, however the result was really worst. So, this option is not retained.

    Finally, the model is composed by three layers of convolution and pooling. Pooling matrix size is smaller in each next layer to avoid losing to much information in the pooling process. The six layers are followed by a flatten layer, a dropout layer and the output layer.
