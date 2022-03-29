#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

std::string string_reverse(const std::string& str) {
    std::string new_str = str;
    std::reverse(new_str.begin(), new_str.end());
    return new_str;
}

int main() {
    std::ifstream in_file;
    std::ofstream out_file;

    in_file.open("input.txt");
    
    std::string buffer{};

    if(in_file.is_open()) {
        std::getline(in_file, buffer);
    }
    in_file.close();
    buffer = string_reverse(buffer);
    out_file.open("output.txt");
    if(out_file.is_open()) {
        out_file << buffer;
    }
    out_file.close();
}