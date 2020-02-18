Using the py file to perform LOOCV function

Run the scripts in py file, then using the command below:
>>> LOORegression(textfile_path)

for example:
>>>LOORegression("D:/3. LOOCV/1. data/32DAP.txt")

The data and structure of 32DAP.txt:
    89 291 316 448 375 489
    308 802 719 1009 1118 1461

This text file contains two rows and the data in a row are separate with space.
    Row 1: the number of rapeseed seedlings in 6 training sample plots
    Row 2: the number of rapeseed canopy leaves in 6 training  sample plots

then get the results on 32DAP as below:

    TRAIN: [1 2 3 4 5] TEST: [0]
    [ 802.  719. 1009. 1118. 1461.] [308.]
    [291. 316. 448. 375. 489.] [89.]
    37.783688964678795
    ['0.25x+128.696', 0.749, 0.058, 0.083, 205.592, 116.592]

    TRAIN: [0 2 3 4 5] TEST: [1]
    [ 308.  719. 1009. 1118. 1461.] [802.]
    [ 89. 316. 448. 375. 489.] [291.]
    49.167536928722654
    ['0.339x+30.881', 0.877, 0.019, 0.073, 302.431, 11.431]

    TRAIN: [0 1 3 4 5] TEST: [2]
    [ 308.  802. 1009. 1118. 1461.] [719.]
    [ 89. 291. 448. 375. 489.] [316.]
    44.17635548041983
    ['0.353x+6.334', 0.903, 0.013, 0.067, 260.437, 55.563]

    TRAIN: [0 1 2 4 5] TEST: [3]
    [ 308.  802.  719. 1118. 1461.] [1009.]
    [ 89. 291. 316. 375. 489.] [448.]
    31.334082025733533
    ['0.327x+23.687', 0.943, 0.006, 0.047, 353.664, 94.336]

    TRAIN: [0 1 2 3 5] TEST: [4]
    [ 308.  802.  719. 1009. 1461.] [1118.]
    [ 89. 291. 316. 448. 489.] [375.]
    46.473362218100384
    ['0.352x+23.938', 0.891, 0.016, 0.071, 417.49, 42.49]

    TRAIN: [0 1 2 3 4] TEST: [5]
    [ 308.  802.  719. 1009. 1118.] [1461.]
    [ 89. 291. 316. 448. 375.] [489.]
    42.9985934269351
    ['0.401x-13.14', 0.872, 0.02, 0.089, 572.109, 83.109]

Interpretation:
    Each block represents each interation.
    Row 1: the indices of data plots used for training and testing during the interation.
    Row 2: the number of manual-counted rapeseed leaf of the corresponding plots.
    Row 3: the number of manual-counted rapeseed seedlings of the corresponding plots.
    Row 4: RMSE based on the traning data.
    Row 5: The results of the interation including Formula, R-squared, P-value, slope_std_error, and predicted_Y_test, MAE_test. 

Finally, the output was saved, and runned the function for the next DAP text file. 
	