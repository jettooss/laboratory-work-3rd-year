
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;

class Vegetable {
protected:
    string name;
    int calories;
    double vitamins;

public:
    Vegetable(string name, int calories, double vitamins);
    virtual ~Vegetable();

    string getName();
    int getCalories();
    double getVitamins();

    virtual string toString();
    virtual bool equals(const Vegetable& other) const;
};

class LeafyVegetable : public Vegetable {
protected:
    string texture;

public:
    LeafyVegetable(string name, int calories, double vitamins, string texture);
    virtual ~LeafyVegetable();

    string getTexture();

    virtual string toString();
    virtual bool equals(const LeafyVegetable& other) const;
};

class RootVegetable : public Vegetable {
protected:
    bool isEdibleRaw;

public:
    RootVegetable(string name, int calories, double vitamins, bool isEdibleRaw);
    virtual ~RootVegetable();

    bool getIsEdibleRaw();

    virtual string toString();
    virtual bool equals(const RootVegetable& other) const;
};

class Salad {
private:
    vector<Vegetable*> vegetables;

public:
    Salad();
    ~Salad();

    void addVegetable(Vegetable* vegetable);
    void removeVegetable(int index);
    int getCalories();
    vector<Vegetable*> getVegetables();
    void sortVegetablesByName();
    void sortVegetablesByCalories();
    vector<Vegetable*> findVegetablesInRange(int minCalories, int maxCalories);

};