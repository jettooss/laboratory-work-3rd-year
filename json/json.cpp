// json.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//
#include <fstream>
#include <iostream>
#include <string>
#include <nlohmann/json.hpp>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
struct flight
{
    string id;
    float time;
    string number;
    string from;
    string  direction;

};
class info
{
 public:
    string load(const flight& flight)
    {
      
        j["id"]= flight.id;
        j["time"] = flight.time;
        j["number"] = flight.number;
        j["from"] = flight.from;
        j["direction"] = flight.direction;
        string serializedString = j.dump();

       /* std::ifstream i("s1.json");
        nlohmann::json v;
        i >> v;
        cout << v["id"];*/

        //std::ifstream in("s3.json"); // окрываем файл для чтения
        //std::string line;
        //nlohmann::json v;
       /* if (in.is_open())
        {
            while (getline(in, line))
            {
                nlohmann::json j1 = nlohmann::json::parse(line);
                string serializedString = j1.dump();



                if ((flight.number) == serializedString )
                {
                    cout <<" Ошибка ";
                }
                else
                {

                


                }
               
                std::cout << j1["id"] << std::endl;
              
            }


        }*/
        //in.close();     // закрываем файл
        save(j);
        
        return serializedString;
    

    }
    void save(nlohmann::json s)
    {
      
        fstream o;
        o.open("s2.json",fstream::in | fstream::out | fstream::app);
        o  << s <<  "\n";
        o.close();
    }
    void print()
    {

        std::ifstream in("s2.json"); // окрываем файл для чтения
        std::string line;
        if (in.is_open())
       {
        while (getline(in, line))
        { 


            //cout << line;

            cout << line << endl;


        }


       }
        in.close();     
    }
  private:
    nlohmann::json j{};


};
int main()
{


    setlocale(LC_ALL, "Russian");
    //nlohmann::json j{};
    flight begin{"1",15.30,"121f","Moskva","khabarovsk"};
    flight end{"2" ,24,"121f","Moskva","khabarovsk" };
    info s;
    s.load(begin);
    s.load(end);
    s.print();
    std::cout << "Hello World!\n";
}

