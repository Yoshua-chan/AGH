#include <iostream>
#include <cstdio>
#include <memory>
#include <cmath>

struct Result{
    double mean;
    double deviation;
};

struct Result deviation(std::shared_ptr<double[]> ptr, size_t size) {
    struct Result result; 
    double total{}, mean{}, sigma{}, sum{};
    for(size_t i = 0; i < size; i++) {
        total += ptr[i];
    }
    mean = total/size;

    for(size_t i = 0; i < size; i++)
        sum += pow((ptr[i] - mean), 2);

    sigma = sqrt(sum/size);

    result.deviation = sigma;
    result.mean = mean;
    return result;
}

int main() {
    srand(time(NULL));

    size_t size;
    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> size;

    std::shared_ptr<double[]> tab = std::make_shared<double[]>(size);

    for(size_t i = 0; i < size; i++) {
        tab[i] = (rand() * 1.0) / (RAND_MAX / 2) - 1.0;
    }

    Result result = deviation(tab, size);

    std::cout << "sigma: " << result.deviation << std::endl;
    std::cout << "mean: " << result.mean << std::endl;
}