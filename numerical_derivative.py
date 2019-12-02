# 02.12.2019 Dasha
import datetime

print("Numerical derivative.\n" + str(datetime.datetime.now()) + "\n")
step = 0.5
num_points_equals_5 = False

#y_{-2}
y_m2 = 0.
#y_{-1}
y_m1 = 0.25
#y_{0}
y_0 = 75.
#y_{+1}
y_p1 = 1.
#y_{+2}
y_p2 = 4.

# 5 points
dev = 1/(12. * step) * (y_m2 - 8. * y_m1 + 8. * y_p1 - y_p2)
print("From 5 points: " + str(dev))

# 3 points
dev = 1/(2. * step) * (y_p1 - y_m1)
print("From 3 points: " + str(dev))
