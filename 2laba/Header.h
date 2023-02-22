using namespace std;
#include <numeric>
#include <cmath>
#include <iostream>
#include <vector>
#include <math.h>
#include <array>
#include <deque>
#include <list>
class laba2 {
#include <deque>
   public:
	   void  vectors(vector<int> vect)
	   {

		   sum = std::accumulate(vect.begin(), vect.end(),
			   decltype(vect)::value_type(0));
		   cout<< endl;

	
		   mean=fmod(sum, vect.size());
		   if (mean == 0)
		   {
			   throw invalid_argument("�� 0 ������ ������ !");
		   }
		
           cout<<"������� �������������� " << mean << endl;
		   cout << "�����:" << sum << endl;


		   cout << "����� vector : ";
		   for (vector<int>::iterator i = vect.begin(); i != vect.end(); i++)
		   {   
			   if (*i % 2 != 0)  
			   {
				
				   cout << abs(*i) / mean<<" ";
			   }
		   }
           

	   }
	   void lists(vector<int> vec)
	   {

		   list<int> dest(vec.begin(), vec.end());
		   cout << endl;
		   cout << "����� list :" ;
		   for (list<int>::iterator i = dest.begin(); i != dest.end(); ++i)
		   {
			   if (*i % 2 != 0)
			   {
				   cout << (abs(*i)) / mean<<" ";
			   }
		   }
	
	   }


       void deque(deque<int> d)
	    {   
		   cout << endl;
		   cout << "����� deque :";
		   for (int& el : d)
		   {
			   if (el % 2 != 0)
			   {
				   cout << abs(el) / mean << " ";
			   }

		   }
		
	   }
	   void Array( )
	   {   
		   srand((unsigned)time(NULL));

		   array<float, 30> numbers;      
		   cout << endl;
		   
		   for (int i = 0; i < numbers.size(); i++)
		   {
			   numbers[i] = rand() % 101 - 50;
		   }
		   float sum1, mean1;
		   sum1 = accumulate(numbers.begin(), numbers.end(),
			   decltype(numbers)::value_type(0));
		   mean1 = fmod(sum, numbers.size());
		   if (mean == 0)
		   {
			   throw invalid_argument("�� 0 ������ ������ !");

		   }
		   cout << "������� �������������� " << mean1 << endl;
		   cout << "�����:" << sum1 << endl;
           cout << "�������� array : ";
           for (auto i : numbers) {
		     cout << i << " ";
	       }
		   cout << endl;
		   cout << "����� Array: "  ;
		   for (int i = 0; i < numbers.size(); i++)
		   {   
			   if (i % 2 != 0)
			   {
				   cout << (abs(numbers[i])) / mean1 <<" ";
			   }

		   }

	   }
	  

   private:
	   int sum;
	   int  mean;



};
