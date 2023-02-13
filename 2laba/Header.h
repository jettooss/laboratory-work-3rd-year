using namespace std;
#include <numeric>
#include <cmath>
#include <iostream>
#include <iostream>
#include <vector>
#include <math.h>

#include <list>
class laba2 {

   public:
	   void  vectors(vector<int> vect)
	   {

		   sum = std::accumulate(vect.begin(), vect.end(),
			   decltype(vect)::value_type(0));
		   cout <<sum ;
		   cout << " ";

		  /* for (auto i : vect) {
			   cout << i << " ";

		   }*/ 
		   mean=fmod(sum, vect.size());
		   //mean= sum / vect.size();
		   cout<< endl;
           cout<<"среднее арифметическое " << mean << endl;
		   cout << "сумма:" << sum << endl;


		   cout << "значение вектора  : ";
		   for (vector<int>::iterator i = vect.begin(); i != vect.end(); ++i)
		   {
			   if (*i % 2 != 0)  
			   {
				   cout << (abs(*i)) / mean<<" ";
			   }

		   }
           

	   }
	   void lists(vector<int> vec)
	   {

		   list<int> dest(vec.begin(), vec.end());

		   /*for (const int& i : dest) {
			   std::cout << i <<" ";
		   }*/
		   cout << endl;
		   cout << "list  значения : ";
		   for (list<int>::iterator i = dest.begin(); i != dest.end(); ++i)
		   {
			   if (*i % 2 != 0)
			   {
				   cout << (abs(*i)) / mean<<" ";
			   }

		   }
	   }

   private:
	   int sum;
	   int  mean;
  


};