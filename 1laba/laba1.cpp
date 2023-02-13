//#include <iostream>
//
//#include <vector>
//#include <thread>
//#include <mutex>
//using namespace std;
////void* threadFunc(void* arg) {
////	int i = *static_cast<int*> (arg);
////	printf("I'm a thread number %d\n", i);
////	//cout << "I'm a thread" << i<< endl;
////}
//mutex mu;
//void threadF(int i) {
//	mu.lock();
//	cout << "I'm a thread " << i << endl;
//	mu.unlock();
//}
//int main()
//{
//	cout << "Hello World!" << endl;
//	const int N = 10;
//
//
//	thread threads[N];
//
//	for (auto i = 0; i < N; ++i) {
//		threads[i] = thread(threadF, i);
//	}
//	for (auto i = 0; i < N; ++i) {
//		threads[i].join();
//	}
//	return 0;
//}
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

mutex mtx;
static int counter = 0;
static const int MAX_COUNTER_VAL = 100;

void thread_proc(int tnum) 
{
    for (;;)
    {
        {
            lock_guard<mutex> lock(mtx);
            if (counter == MAX_COUNTER_VAL)
                break;
            int ctr_val = ++counter;
            cout << "Поток " << tnum << ": счетчик = " <<
                ctr_val << " id = " << this_thread::get_id() << endl;
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
}

int main() {
    setlocale(LC_ALL, "Russian");
    vector<thread> threads;
    for (int i = 0; i < 1001; i++) {
        thread thr(thread_proc, i);
        threads.emplace_back(move(thr));
    }

    for (auto& thr : threads) {
        thr.join();
    }


    return 0;
}
