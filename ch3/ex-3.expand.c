#include <stdio.h>



/*
  El capitulo 3 explica una funcion llamada expand
  Esta nos sirve para expandir rangos de caracteres, por ejemplo
  a-d		  se convierte en   abcd
  4-8     se convierte en   45678
  x-z1-3  se convierte en   xyz123
  Implementela aqui
*/

/* Escriba aqui su funcion expand */
// s[] -> arreglo lo suficientemente grande para colocar su string expandido
// t[] -> arreglo de caracteres con la version compacta
void expand(char s[], char t[]){

}



/* No modifique este main */
int main(){
	char a[] = "a-z0-9";
	char b[] = "G-X";
	char c[] = "0-7";
	char s[100000];

	expand(s, a);
	printf("(%s)\n", s);
	expand(s, b);
	printf("(%s)\n", s);
	expand(s, c);
	printf("(%s)\n", s);
}