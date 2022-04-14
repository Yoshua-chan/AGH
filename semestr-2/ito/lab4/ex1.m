% wygeneruj wielomiany Legendre'a na przedziale [-1, 1]
% zwróć współczynniki wielomianu

clear; clc; close;

legendre_pol(3);

for i = 1:50 
    plot(linspace(-1, 1, 1000), legendre_pol(i));
    hold on;
    pause(0.05);
end
