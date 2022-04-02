
function odp = cardano(a)
    a = a / a(1); % znormalizuj współczynnik przy x^3
    p = (3 * a(3) - a(2)^2) / 9;
    q = a(2)^3 / 27 - (a(2) * a(3))/6 + a(4)/2;
    D = q^2 + p^3;



    if D >= 0
        u = nthroot(-q + sqrt(D), 3);
        v = nthroot(-q - sqrt(D), 3);

        y(1) = u + v;
        y(2) = (-1/2) * (u + v) + j * (sqrt(3)/2) * (u - v);
        y(3) = (-1/2) * (u + v) - j * (sqrt(3)/2) * (u - v);
    elseif D < 0
        phi = acos(-q/sqrt(-(p^3)));
        for k = 1:3
            y(k) = 2 * sqrt(-p) * cos( (phi + 2 * pi * (k - 1)) / 3);
        end
    end
    
    for k = 1:3
        odp(k) = y(k) - a(2) / 3;
    end
    odp = odp.';
end