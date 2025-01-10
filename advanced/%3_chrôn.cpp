#include <iostream>
#include <chrono>
using namespace std;
//hoàn thành việc xây dựng hàm output(), không xây dựng thêm bất kỳ hàm nào khác.
void output(string name,int namsinh,string gioitinh){
    int tuoi = 2024 - namsinh;
    if (gioitinh == "Nam") {
        cout << "Xin chao anh " << name << " " << tuoi << " tuoi";
    } else if (gioitinh == "Nu") {
        cout << "Xin chao chi " << name << " " << tuoi << " tuoi";
    } else {
        cout << "Xin chao ban " << name << " " << tuoi << " tuoi";
    }
    
}

int main() {
    auto start_time = std::chrono::high_resolution_clock::now();
    output("Huy", 1999, "Nam");
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    std::cout << "--- " << elapsed.count() << " seconds ---" << std::endl;
    return 0;
}