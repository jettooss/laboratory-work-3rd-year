#include "Header.h"


Vegetable::Vegetable(string name, int calories, double vitamins) {
    this->name = name;
    this->calories = calories;
    this->vitamins = vitamins;
}

Vegetable::~Vegetable() {}

string Vegetable::getName() {
    return name;
}

int Vegetable::getCalories() {
    return calories;
}

double Vegetable::getVitamins() {
    return vitamins;
}

string Vegetable::toString() {
    return name + " - " + std::to_string(calories) + " калории";
}

bool Vegetable::equals(const Vegetable& other) const {
    return name == other.name && calories == other.calories && vitamins == other.vitamins;
}

LeafyVegetable::LeafyVegetable(string name, int calories, double vitamins, string texture) : Vegetable(name, calories, vitamins) {
    this->texture = texture;
}

LeafyVegetable::~LeafyVegetable() {}

string LeafyVegetable::getTexture() {
    return texture;
}

string LeafyVegetable::toString() {
    return name + " - " + std::to_string(calories) + " калории, " + texture + " текстура";
}

bool LeafyVegetable::equals(const LeafyVegetable& other) const {
    return Vegetable::equals(other) && texture == other.texture;
}

RootVegetable::RootVegetable(string name, int calories, double vitamins, bool isEdibleRaw) : Vegetable(name, calories, vitamins) {
    this->isEdibleRaw = isEdibleRaw;
}

RootVegetable::~RootVegetable() {}

bool RootVegetable::getIsEdibleRaw() {
    return isEdibleRaw;
}

string RootVegetable::toString() {
    return name + " - " + std::to_string(calories) + " калории, " + (isEdibleRaw ? "съедобный сырой" : "не съедобен в сыром виде");
}

bool RootVegetable::equals(const RootVegetable& other) const {
    return Vegetable::equals(other) && isEdibleRaw == other.isEdibleRaw;
}

Salad::Salad() {}

Salad::~Salad() {
    for (Vegetable* vegetable : vegetables) { delete vegetable; }
}

void Salad::addVegetable(Vegetable* vegetable) { vegetables.push_back(vegetable); }

void Salad::removeVegetable(int index) { if (index >= 0 && index < vegetables.size()) { Vegetable* vegetable = vegetables[index]; vegetables.erase(vegetables.begin() + index); delete vegetable; } }

int Salad::getCalories() { int totalCalories = 0; for (Vegetable* vegetable : vegetables) { totalCalories += vegetable->getCalories(); } return totalCalories; }

vector<Vegetable*> Salad::getVegetables() { return vegetables; }

void Salad::sortVegetablesByName() { 
    sort(vegetables.begin(), vegetables.end(), [](Vegetable* a, Vegetable* b) 
        { return a->getName() < b->getName(); 
        }); 
}

void Salad::sortVegetablesByCalories() { sort(vegetables.begin(), vegetables.end(), [](Vegetable* a, Vegetable* b) { return a->getCalories() < b->getCalories(); }); }


vector<Vegetable*> Salad::findVegetablesInRange(int minCalories, int maxCalories) { 
    vector<Vegetable*> foundVegetables;
    for (Vegetable* vegetable : vegetables) {
        int calories = vegetable->getCalories(); 
        if (calories >= minCalories && calories <= maxCalories) {
            foundVegetables.push_back(vegetable); 
        } 
    }
    return foundVegetables; 
}



void showMenu() {
    cout << "1. Показать салат" << endl;
    cout << "2. Добавить листовой овощ" << endl;
    cout << "3. Добавить корнеплод" << endl;
    cout << "4. Удалить овощ из салата" << endl;
    cout << "5. Создать тестовые овощи" << endl;
    cout << "6.  Найти овощи по заданному диапазону калорийности " << endl;

}
int main() {
    setlocale(LC_ALL, "Russian");
    int userInput = 0;
    Salad salad;
    do {
        showMenu();
        cout << "Выберите действие: ";
        cin >> userInput;
        switch (userInput) {
        case 1:
            cout << "Общее количество калорий: " << salad.getCalories() << endl;
            for (Vegetable* vegetable : salad.getVegetables()) {
                cout << vegetable->toString() << endl;
            }
            /* for (Vegetable* vegetable : salad.getVegetables()) {
                 cout << vegetable->toString() << endl;
             }
             cout << endl << endl;*/
            break;
        case 2: {
            cout << "Введите название, калории, витамины и текстуру для Листового овоща:" << endl;
            string name, texture;
            int calories;
            double vitamins;
            cin >> name >> calories >> vitamins >> texture;
            LeafyVegetable* leafy = new LeafyVegetable(name, calories, vitamins, texture);
            salad.addVegetable(leafy);
            cout << "Листовой овощ добавлен в салат" << endl;
            break;
        }
        case 3: {
            cout << "Введите название, калории, витамины и информацию о съедобности Корнеплода (введите 1 для съедобности, 0 для несъедобности):" << endl;
            string name;
            int calories;
            double vitamins;
            bool isEdibleRaw;
            cin >> name >> calories >> vitamins >> isEdibleRaw;
            RootVegetable* root = new RootVegetable(name, calories, vitamins, isEdibleRaw);
            salad.addVegetable(root);
            cout << "Корнеплод добавлен в салат" << endl;
            break;
        }
        case 4: {
            cout << endl << endl;
            cout << "Введите номер индекса : " << endl;
            // Удаляем один овощ из салата и выводим обновленную информацию:
            int index;
            cin >> index;
            if (index >= 0 && index < salad.getVegetables().size()) {
                salad.removeVegetable(index);
                cout << "Новое общее количество калорий: " << salad.getCalories() << endl;
            }
            else {
                cout << "Некорректный индекс" << endl;
            }
            break;
        }
        case 5: {
            cout << endl << endl;
            LeafyVegetable* lettuce = new LeafyVegetable("Салат", 20, 5.0, "хрустящая");
            LeafyVegetable* spinach = new LeafyVegetable("Шпинат", 30, 10.0, "мягкая");
            RootVegetable* carrot = new RootVegetable("Морковь", 25, 8.0, true);
            RootVegetable* beetroot = new RootVegetable("Свекла", 35, 12.0, false);
            salad.addVegetable(lettuce);
            salad.addVegetable(spinach);
            salad.addVegetable(carrot);
            salad.addVegetable(beetroot);
            cout << "Тестовые овощи добавлены в салат" << endl;
            break; }
        case 6:{
            cout << "Введите диапазон калорийности в формате  min max";
            int minCal, maxCal;
            cin >> minCal >> maxCal;
            vector<Vegetable*> foundVegetables = salad.findVegetablesInRange(minCal, maxCal);
            cout << "Найденные овощи:" << endl;
            for (Vegetable* vegetable : foundVegetables) {
                cout << vegetable->toString() << endl;
            }
            break;}

        default:
            cout << endl << endl;
            userInput = 0;
        };
    } while (userInput);
    return 0;
}
