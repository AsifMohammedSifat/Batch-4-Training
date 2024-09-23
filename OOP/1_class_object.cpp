#include<bits/stdc++.h>
using namespace std;

// class A{
//     public:
//     int value;
//     //constructor
//     A(int value){
//         this->value = value;
//         cout<<"Constructor Called"<<endl;
//     }

//     //method
//     void display(){
//         cout<<"Hello\n";
//     }

//     //destructor
//     ~A(){
//         cout<<"Desonstructor Called"<<endl;
//     }
// };
                    
// int main(){
//     A obj(8);
//     obj.display();
//     // obj.value = 5;
//     cout<<obj.value<<endl;
            
              
//     return 0;
// }








class A{
public:
    A(){
        printf("I am Constructor\n");
    }

    void display(){
        cout<<"I am Display Method\n";
    }

    ~A(){
        cout<<"I am Destructor\n";
    }

};

int main(){
    A obj;
    obj.display();

}