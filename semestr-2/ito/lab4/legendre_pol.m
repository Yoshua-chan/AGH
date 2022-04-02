% funkcja generująca wielomiany legendre'a

function result = legendre_pol(N)
    resolution = 1000;
    arg = linspace(-1, 1, resolution);
    if N == 0
        result = ones(1, resolution);
    elseif N == 1
        result = arg;
    else
        result = (2 * N + 1)/(N+1) .* arg .* legendre_pol(N-1) - N/(N+1) .* legendre_pol(N-2);
    end

end