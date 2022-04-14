% ITO - Lab 2
% Ex 1.
% Kacper Filipek 18.03.2022

clc; clear; close;

format long

angles = 0:0.1:10000;

sine_data = cos(angles) + i * sin(angles);
exp_data = exp(i * angles);

real_sine = real(sine_data);
real_exp = real(exp_data);

im_sine = imag(sine_data);
im_exp = imag(exp_data);

hold on
plot(angles, real_sine, "Color", "red");
plot(angles, real_exp, "Color", "blue");
axis equal

plot(angles, im_sine, "Color", "green");
plot(angles, im_exp, "Color", "#FFA500");

format long

real_errors = real_sine - real_exp
im_errors = im_sine - im_exp

max(real_errors)
max(im_errors)