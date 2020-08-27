# OpenCV implements two kind of Hough Line Transforms
# The Standard Hough Transform  (HoughLines method)
# The Probabilistic Hough Line Transform  (HoughLinesP method)


# Hough transformation Algorithm
# 1. Edge Detection eg. using the Canny edge detector
# 2. Mapping of edge points to the Hough Space and storage in an accumator.
# 3. Interpretation of the accumulators to yeids lines of infinite length The interpretation is done by threshold and other constraints
# 4. Conversion of infinite lines to finite