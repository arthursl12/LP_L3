#include <string>
#include <iostream>

template  <class T> 
class  auto_ptr {
private: 
    T* ptr;
public:
    explicit  auto_ptr(T* p = 0) : ptr(p) { }
    ~auto_ptr () { std::cout << "Destructor" << std::endl; delete  ptr; }
    T& operator *() { return *ptr; }
    T* operator ->() { return  ptr; }
};

void  foo0() {
    auto_ptr <std::string > p(new  std:: string("I did  one P.O.F!\n"));
    std::cout  << *p;
}

void  foo1() {
    try {
        auto_ptr <std::string > p(new  std:: string("Oi!\n"));
        throw  20;
    } catch (int e) { 
        std::cout  << "Oops: " << e << "\n"; 
    }
}

void  foo2() {
    try {
        std:: string* p = new std:: string("Oi!\n");
        throw  20;
        delete p;
    } catch (int e) { 
        std::cout  << "Oops: " << e << "\n"; 
    }
}

int main(){
    // auto_ptr<int> p1(new int(6));
    // foo0();
    // foo1();
    foo2();
    return 0;
}