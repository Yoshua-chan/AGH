% ex 1
% ITO
% Kacper Filipek 25.03.2022

clear; clc; close;

w1 = [1, 0, 0, 0]
w2 = [2, -8, 2, 12]
w3 = [4, -12, 32, -40]
w4 = [2, -16, -34, -20]

polynomials = [w1; w2; w3; w4];
for i = 1:4
    results_c = sort(cardano(polynomials(i, :)))
    results_r = sort(roots(polynomials(i, :)))
    % error(i) = abs(results_r(i,:) - results_c(i,:))
end

