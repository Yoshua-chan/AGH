% ITO - Lab 2
% Ex 1.
% Kacper Filipek 18.03.2022

clc; clear; close;
angles = linspace(0, 2 * pi, 12);
raw_data =  exp(i * angles) % creates 36 points with equal angle distribution on a complex plane
x = real(raw_data)
y = imag(raw_data)

plot(raw_data, ".","Color", "black", "MarkerSize", 10)
axis equal
hold on

data1 = atan(y ./ x);
data2 = atan2(y, x);
data3 = angle(raw_data);

plot(exp(i * data1), "o","Color", "blue",'markersize',8)
plot(exp(i * data2), "s","Color", "green",'markersize',10)
plot(exp(i * data3), "d","Color", "red",'markersize',12)


atan_max_error = max(abs(angles - data1))
atan2_max_error = max(abs(angles - data2))
angles_max_error = max(abs(angles - data3))