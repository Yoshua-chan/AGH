% Miejsca zerowe funkcji kwadratowej
% Kacper Filipek 11/03/2022

% obliczanie miejsc zerowych

clc; clear; close;

wsp = rand(1, 3);

delta = wsp(2)^2 - 4 * wsp(1) * wsp(3);
if delta >= 0
    p = [0, 0];
    p(1) = (-wsp(2) - sqrt(delta))/(2*wsp(1));
    p(2) = (-wsp(2) + sqrt(delta))/(2*wsp(1));
elseif delta == 0
    p = (-1 * wsp(2)/(2*wsp(1)));
else
    p = NaN;
end

% współrzędne wierzchołka

w = [(-1 * wsp(2) / (2*wsp(1))), (-delta / (4 * wsp(1)))];

% wartość wielomianu

if delta >= 0
    x = linspace((p(1) - 1), (p(2) + 1), 100);
else
    x = -15:0.1:15;
end

y = wsp(1) * x.^2 + wsp(2)*x + wsp(3);

% wykres

plot(x, y, "LineWidth", 1.5);

hold on

plot(w(1), w(2), "Marker","*")
if delta >= 0
    plot(p(1), 0, "g", p(2), 0, "Marker",".","MarkerSize", 15, "Color", "r")
end
grid on