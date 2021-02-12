#include <stdlib.h>
#include <stdio.h>

int  valor_inicial = 10;
int  valor_intermediario = 5;

void  calcula(int* valores){
    int  taxa = 3;
    valores [0] = valor_inicial + valor_intermediario * taxa;
    valores [1] = valores [0] * 3;
}

int  main(){
    int* valores = (int*) malloc (3 * sizeof(int));
    calcula(valores);
    valores [2] = valor_inicial + valor_intermediario;
    printf("[%i %i %i]", valores[0], valores[1], valores[2]);
}
