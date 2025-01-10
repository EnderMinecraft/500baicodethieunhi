#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int countWords(const string& str) {
    istringstream iss(str);
    return distance(istream_iterator<string>(iss), istream_iterator<string>());
}

int main() {
    string strin, strin2;
    cout << "string1: ";
    getline(cin, strin);
    cout << "string2: ";
    getline(cin, strin2);

    int totalWords = countWords(strin) + countWords(strin2);
    cout << totalWords << endl;

    return 0;
}