
function res = ferrari(a)
    a = a/a(1) % normalise the polynomial
    k = [1, (-a(3)/2), ((a(2)*a(4)-4*a(5))/4), (4*a(3)*a(5)-a(2)^2 * a(5) - a(1)^2)/8 ]
    k_roots = cardano(k)
end