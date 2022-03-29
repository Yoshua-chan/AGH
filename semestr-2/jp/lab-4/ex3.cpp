#include <iostream>
#include <string>
#include <algorithm>

size_t get_x_len(const std::string& str) {
    size_t index = str.find('X');
    int xsize{0};

    if(index == std::string::npos)
        return 0;

    while(index < str.size()) {
        if(str[index] == 'X') {
            index++;
            xsize++;
        } else
            break;
    }
    return xsize;
}

int main() {
    std::string messege = "Congratulations Mrs. <name>, you and Mr. <name> are the lucky recipients of a trip for two to XXXXXX. Your trip to XXX is already scheduled ";
    while(messege.find("<name>") != std::string::npos) {
        messege.replace(messege.find("<name>"), 6, "Smith");
    }
    while(get_x_len(messege)) {
        messege.replace(messege.find("X"), get_x_len(messege), "Siberia");
    }
    messege.replace(messege.find("lucky"), 5, "unlucky");
    messege += "in December";

    std::cout << messege;

}