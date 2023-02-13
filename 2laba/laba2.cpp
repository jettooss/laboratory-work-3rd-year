// laba2.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
#include <random>
#include <algorithm>



#include "Header.h"
int main()
{
    std::cout << "Hello World!\n";
    setlocale(LC_ALL, "Russian");
    laba2 s;
    random_device rnd_device;
   
    mt19937 mersenne_engine{ rnd_device() };  
    uniform_int_distribution<int> dist{ -50, 50 };

    auto gen = [&dist, &mersenne_engine]() {
        return dist(mersenne_engine);
    };
    vector<int> vec(30);
    generate(begin(vec), end(vec), gen);
    cout << "изначальные значения :" ;
    for (auto i : vec) {
        cout << i << " ";

    }
    s.vectors(vec);
    s.lists(vec);
}

