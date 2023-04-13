//
#include <iostream> 
#include <random>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <vector>
#include <math.h>
#include <array>
#include <list>
#include <deque>
using namespace std;
#include <iostream>
#include <array>

   template<std::size_t Size>
   float  means(std::array<float, Size>& arr) {
		float summ=0, s;
		for (int i = 0; i < arr.size(); i++)
		{
			summ += arr[i];			
		}

		s = summ / arr.size();
		cout <<"s :" <<s;
		return s;

	}
   
	array<float, 30> func()

	{
		srand(time(0));
		std::array<float, 30> numbers; 

		for (int i = 0; i < numbers.size(); i++)
		{
		
			numbers[i] = rand() % 101 - 50;
		}

		return numbers; 
	}
	template<std::size_t Size>
	void f_vector(std::array<float, Size>& arr) {

	



		
		float s = means(arr);
		vector<float> vec(begin(arr),end(arr));

		cout << "Ответ vector :";
		for (const int& el : vec) {
			if (el % 2 != 0)
			{
				cout << abs(el) / s << " ";
			}
		}


	}
	template<std::size_t Size>
	void f_lists(std::array<float, Size>& arr) {
	
		float s= means(arr);
		list<float> dest(arr.begin(), arr.end());
	
		

		
		cout << "Ответ list :";
		for (const int& el : dest) {
			if (el % 2 != 0)
			{
				cout << abs(el) / s << " ";
			}
		}

	}

	template<std::size_t Size>
	void f_deque(std::array<float, Size>& arr) {
		for (int i = 0; i < Size; i++) {
			cout << arr[i] << "\t";
		}
		deque<float>  deq;
		float s = means(arr);
		move(
			begin(arr),
			end(arr),
			back_inserter(deq)
		);
		cout << endl;
		cout << "Ответ deque :";
	
		for (const int& el : deq) {
			if (el % 2 != 0)
			{
				cout << abs(el) / s << " ";
			}
			    }
	}


	template<std::size_t Size>
	void f_Array(std::array<float, Size>& arr) {

	
		float s = means(arr);
		cout << "Ответ Array :";
		for (const int& el : arr) {
			if (el % 2 != 0)
			{
				cout << abs(el) / s << " ";
			}
		}

		

	}



int main(){
	
	setlocale(LC_ALL, "Russian");
	srand(time(NULL));
	array<float, 30> arr ;

	arr = func(); 
	cout << endl;
	f_deque(arr);
	cout << endl;
	f_vector(arr);
	cout << endl;
	f_lists(arr);
	cout << endl;
	f_Array(arr);



}

