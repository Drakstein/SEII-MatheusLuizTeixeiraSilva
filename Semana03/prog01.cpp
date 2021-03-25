// Matheus Luiz Teixeira Silva 11311EMT025

/*1. Faça um programa que implemente uma struct ou classe para representar um 
número complexo e as funções que implementem as operações de: soma, subtração, 
multiplicação e divisão, além de permitir a conversão de representação na forma polar e retangular.
Requisitos: A biblioteca ou classe deverá ser implementada em dois arquivos separados 
(um para o cabeçalho *.h e outro para o código *.c/*.cpp), devendo ser chamada por meio de um include.
Motivação: Esse exercício visa revisar a criação e uso de funções próprias, além de tipos de dados próprios.
*/

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <bib.h>
#include <math.h>
#include <iomanip>
using namespace std;

int  real, img, den, opr;
float  artan, mod, ang, reald, imgd;
struct num
{
    int real, img;
};

int main() {
    struct num n1;
    struct num n2;
    struct num res;
    cout << "----------CALCULADORA----------\n";
    cout << "\nDIGITE A PARTE REAL DO PRIMEIRO NUMERO:\n";
    cin >> n1.real;
    cout << "\nDIGITE A PARTE IMAGINARIA DO PRIMEIRO NUMERO:\n";
    cin >> n1.img;
    cout << "\nDIGITE A PARTE REAL DO SEGUNDO NUMERO:\n";
    cin >> n2.real;
    cout << "\nDIGITE A PARTE IMAGINARIA DO SEGUNDO NUMERO:\n";
    cin >> n2.img;
    cout << "OS NUMEROS SAO:\n";
    cout << n1.real << " + " << n1.img << "i     ";
    mod = sqrt(pow(n1.real,2) + pow(n1.img,2));
        ang = atan((float)n1.img/(float)n1.real) * (180 /3.14159265);
        if(n1.real >= 0 && n1.img>=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << ang << "*\n";
            }
        if(n1.real <= 0 && n1.img >=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << (-ang+90) << "*\n";
            }
        if(n1.real <= 0 && n1.img <=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << (180+ang) << "*\n";
        }
        if(n1.real >= 0 && n1.img <=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << (360+ang) << "*\n";
        }   
    cout << n2.real << " + " << n2.img << "i     ";
    mod = sqrt(pow(n2.real,2) + pow(n2.img,2));
        ang = atan((float)n2.img/(float)n2.real) * (180 /3.14159265);
        if(n2.real >= 0 && n2.img>=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << ang << "*";
            }
        if(n2.real <= 0 && n2.img >=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << (-ang+90) << "*";
            }
        if(n2.real <= 0 && n2.img <=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << (180+ang) << "*";
        }
        if(n2.real >= 0 && n2.img <=0 ){
            cout << "SUA FORMA POLAR EH: " << mod << " | " << (360+ang) << "*";
        }   
    cout << "\nESCOLHA A OPERACAO:\n";
    cout << "SOMA[1]--SUBTRACAO[2]--MULTIPLICACAO[3]--DIVISAO[4]\n";
    cin >> opr;

     if (opr == 1)
    {
        real = funcsomaR(n1.real, n2.real);
        img = funcsomaI(n1.img, n2.img);
        cout << "O RESULTADO DA SOMA EH:\n" << real << " + " << img <<"i\n";
        mod = sqrt(pow(real,2) + pow(img,2));
        ang = atan((float)img/(float)real) * (180 /3.14159265);
        if(real >= 0 && img>=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << ang << "*\n";
            }
        if(real <= 0 && img >=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (-ang+90) << "*\n";
            }
        if(real <= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (180+ang) << "*\n";
        }
        if(real >= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (360+ang) << "*\n";
        }   
    }

     else if (opr == 2)
    {
        real = funcsubR(n1.real, n2.real);
        img = funcsubI(n1.img, n2.img);
        cout << "O RESULTADO DA SUBTRACAO EH:\n" << real << " + " << img <<"i\n";
        mod = sqrt(pow(real,2) + pow(img,2));
        ang = atan((float)img/(float)real) * (180 /3.14159265);
        if(real >= 0 && img>=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << ang << "*\n";
            }
        if(real <= 0 && img >=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (-ang+90) << "*\n";
            }
        if(real <= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (180+ang) << "*\n";
        }
        if(real >= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (360+ang) << "*\n";
        }   
    }

     else if (opr == 3)
    {
        real = {funcmultR(n1.real, n1.img, n2.real, n2.img)};
        img = {funcmultI(n1.real, n1.img, n2.real, n2.img)};
        cout << "O RESULTADO DA MULTIPLICACAO EH:\n" << real << " + " << img <<"i\n";
        mod = sqrt(pow(real,2) + pow(img,2));
        ang = atan((float)img/(float)real) * (180 /3.14159265);
        if(real >= 0 && img>=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << ang << "*\n";
            }
        if(real <= 0 && img >=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (-ang+90) << "*\n";
            }
        if(real <= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (180+ang) << "*\n";
        }
        if(real >= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (360+ang) << "*\n";
        }   
    }

    else if (opr == 4)
    {
        real = {funcdivR(n1.real, n1.img, n2.real, n2.img)};
        img = {funcdivI(n1.real, n1.img, n2.real, n2.img)};
        den = {funcdivDen(n2.real, n2.img)};
        cout << "O RESULTADO DA DIVISAO EH:\n" << real << "/" << den << " + " << img << "/" << den  <<"i\n";
        reald = (float)real/(float)den;
        imgd = (float)img/(float)den;
        mod = sqrt(pow(reald,2) + pow(imgd,2));
        ang = atan(imgd/reald) * (180 /3.14159265);
        if(real >= 0 && img>=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << ang << "*\n";
            }
        if(real <= 0 && img >=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (-ang+90) << "*\n";
            }
        if(real <= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (180+ang) << "*\n";
        }
        if(real >= 0 && img <=0 ){
            cout << "SUA FORMA POLAR EH:\n" << mod << " | " << (360+ang) << "*\n";
        }   
    }
    else{
        cout << "\nCOMANDO NAO RECONHECIDO\n";
        getchar(); getchar();
        return 0;
    }

    getchar(); getchar();
    return 0;
}
