#include <stdio.h>

#define MAX_WORD_LENGTH 15

// i, j -> variables temporales para los ciclos
// nCharsPerWord[MAX_WORD_LENGTH] -> arreglo para guardar las frecuencias de cada longitud de palabra
int main(){
  // No modifique estas variables e inicializacion
  int i, j;
  int nCharsPerWord[MAX_WORD_LENGTH];
  for (int i = 0; i < MAX_WORD_LENGTH; i++) {
    nCharsPerWord[i] = 0;
  }



  /* Escriba su codigo aqui abajo */


  /* Escriba su codigo aqui arriba */



  // No modifique estos print
  for(i=1; i<MAX_WORD_LENGTH;++i) {
    printf("%2d|", i);
    for (j=0; j<nCharsPerWord[i]; printf("*"), ++j);
    printf("\n");
  }

  /* 
    El ciclo viene listo para imprimir un histograma que se vera mas o menos asi:
    1|****
    2|**
    3|******
    4|*
  */

  return 0;
}