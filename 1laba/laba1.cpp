#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

mutex mtx;
static int counter = 0;
int c = 1;
static const int MAX_COUNTER_VAL = 10;

void thread_proc(int tnum) 
{
    for (;;)
    {
        {
            lock_guard<mutex> lock(mtx);
            if (counter == MAX_COUNTER_VAL)
                break;
            int ctr_val = ++counter;
            c += c;
            cout << "Поток " << tnum << ": счетчик = " <<
                ctr_val << " id = " << this_thread::get_id() << endl;
            
            cout <<c << endl;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}
void  fun2(char ch){
    lock_guard<mutex> lock(mtx);
for (int i = 0; i < 5; ++i)
{
    for (int i = 0; i < 10; ++i)
    {
        cout << ch;
    }
    cout << endl;
 }
cout << " id = :" << this_thread::get_id()<< endl;
};
void fun3(int i)
{
    lock_guard<mutex> lock(mtx);
    c = i + 3423 * 43;
    cout << c <<" id = :" << this_thread::get_id() << endl;

}
void fun4(int i)
{
    lock_guard<mutex> lock(mtx);
    c = i + 3423 / 100+c-1000;
    cout << c << " id = :" << this_thread::get_id() << endl;

}
void fun5(int i)
{
    vector<int> threads;
    lock_guard<mutex> lock(mtx);
    c = i + 3423 / 100 + c - 1000;
    threads.push_back(c);
    cout << c << " id = :" << this_thread::get_id() << endl;

    for (int n : threads)
        cout << n << "\t";
    cout<< endl;

}
int main() {
    setlocale(LC_ALL, "Russian");
   

    thread thr1(fun2, 'd');

    thread thr3(fun2, 'a');
    thread thr5(fun2, '0');
    thread thr4(fun3, c);
    thread thr6(fun4, c);
    thread thr7(fun4, c);
    thread thr(thread_proc, 8);
    thread thr8(fun5, c);
    thread thr9(fun5, c);
    thr.join();
    thr1.join();
    thr3.join();
    thr4.join();
    thr5.join();
    thr6.join();
    thr7.join();
    thr8.join();
    thr9.join();


    return 0;
}


