//// laba4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
////
#include <string>
#include <iostream>
#include <stdexcept>
using namespace std;



class User_exceptions {
private:
    string message;
public:
    User_exceptions(int value, int num_option)
    {
        if (num_option == 1)
        {
            message = "Количество лет = " + to_string(value) + " должно быть больше 999";
        }
    }
    const string getMessage() const
    {
        return message;
    }
};


struct Date {
        int day = 0;
        int month = 0;
        int year = 0;
    };
class Time {


private:


   
    string message;
    const int SNLMonth[12] = { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 };
    const int SLMonth[12] = { 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335 };

    const int* SMonth[2] = { SNLMonth, SLMonth };

public:
  
    
   void Transformation_standard(const Date& date)
   {

       cout << date.month;
    if (date.year == 0 || date.month == 0 || date.day == 0)
    {
        throw invalid_argument("Ни одно значение не может быть равно 0!");
    }
 
    if (int(date.year) < 1  )
    {
        throw invalid_argument("год должен быть больше 0  !");
    }
    if ( 12  <= int(date.month) || 1 >= int(date.month))
    {
        throw invalid_argument("Чмсло месяца не может быть больше 12  и меньше  1 !");
    }
   }

   void Transformation_user(const Date& date)
   {
       if (date.year < 1000)
       {
           throw User_exceptions(date.year, 1);
       }
     
   }
    bool is_leap_year(int y)
    {
        cout << y << endl;;
        if (y % 400 == 0) return true;
        if (y % 100 == 0) return false;
        if (y % 4 == 0)   return true;
        return false;
    }

    int days_by_monthes(int m, int y) // m -  месяц , y - год
    {
       
        int days = 0;
        bool leap = is_leap_year(y);
        cout << leap << endl;;
        days += SMonth[leap][m - 1];
        //cout << days<< endl;;
        return days;
    }
    int leap_years(int year)
    {
      
        int years = year - 1;
        return (years / 4 - years / 100 + years / 400);
    }
    int calc_days(const Date& date)
    {
        int l_y = leap_years(date.year);
        int nl_y = date.year - 1 - l_y;
        return date.day + days_by_monthes(date.month, date.year) + l_y * 366 + nl_y * 365;
    }
};
  int main()
    {
        setlocale(LC_ALL, "Russian");
        Date begin{ 2,-1,999 };
        Date end{ 11,2,1002 };

      /*   Date begin{10,12,2020};
         Date end{11,12,2020};*/
        Time s;
       
            cout << "Функция с пользовательскими исключениями" << endl;
        try {

             
                    s.Transformation_user(end);
                    s.Transformation_user(begin);

             
          try
          {  

            cout << "Функция со стандартными исключениями" << endl;
            s.Transformation_standard(end);
            s.Transformation_standard(begin);
            int days = (s.calc_days(end) - s.calc_days(begin));
       
            cout << "Количество дней = " << days << endl;
          }
          catch (const invalid_argument& error)
          {
            cout << "Недействительный аргумент: " << error.what() << endl;
          }
                
        }
        catch (const User_exceptions& error) {
                    cout << "Недействительный аргумент: " << error.getMessage() << endl;
        }

        
    }



