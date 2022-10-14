# Smart-Sensors

# Language: Python

# Description:

Last summer you installed a Smart Home system at your parents’ place, but this move cost you a lot of headache. One of the sensors malfunction which resulted in that the indoor temperature was all over the place. One day it could be hot like in a sauna indoors and the next day you would need to wear mittens. In the end you found, and replaced, the malfunctioning sensor but it took a long time to find out what the problem was.

This year when taking a course in embedded systems you remembered the ordeal from last summer and wanted to come up with a solution. The end goal is to make the Smart Home a little bit smarter, to have it report that one of its sensors is malfunctioning. In your prototype you have installed not one, but two, of each sensor (two sensors measuring the temperature in the kitchen instead of just one). The idea is to create a script that can check if the measurements from the two sensors deviate too much, if they do, there is most likely a problem with one of the sensors.

All the measurements from the primary sensors will be stored in one file and all the measurements from the secondary sensors (the validation sensors) will be stored in another file
 
What the script needs to do is to take the path to two of these measurement files as command line arguments and then figure out if the values from the two files deviate too much. Currently the threshold for what is too much is set to two degrees.


