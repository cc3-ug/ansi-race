#include <stdio.h>
#include <string.h>



/*
  El capitulo 3 explica una funcion llamada itoa
  Esta es el opuesto a la funcion atoi del capitula anterior
  Es decir, esta realiza la conversion integer to ascii
*/

/* Escriba aqui su funcion itoa */
// Asuma que el arreglo s tiene suficiente espacio para colocar su respuesta
void miitoa(int n, char s[]){

}



/* No modifique este main */
int main () {
  char s[1000];
  s[6] = 8;
	miitoa(345090, s);
  printf("345090 = %s\n", s);
  s[6] = 8;
  miitoa(-10002, s);
	printf("-10002 = %s\n", s);
}