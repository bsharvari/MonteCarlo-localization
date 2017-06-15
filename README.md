# MonteCarlo-localization
Monte Carlo localization of a robot in a 2 dimensional cyclic world

The world is specified in terms of a two dimensional matrix, which consists of two colours, red and green. A pre-determinied motion of the robot is given, in the form of [0, 0] for no motion, [0, 1] for right, [0 , -1] for left, [1, 0] for down, and [-1, 0] for up. The measurements vector is the order in which the colours are observed during this motion.

The output p is the probable locations of the robot in the 2D world. The location with the highest probability is considered as the end position of the robot after the motion is executed.
