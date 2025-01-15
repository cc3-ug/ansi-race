#include <stdio.h>



/*
  El capitulo 4 explica una funcion llamada strindex
  Esta recibe un string s que contiene la cadena completa, y un string t que contiene un texto a buscar
  Implementela aqui
*/
int strindex(char s[], char t[]){

}



/* No modifique este main */
int main(){
	char str[] = "Anita lava la tina";
  char lava[] = "lava";
  char tina[] = "tina";
  char jabon[] = "jabon";
  int x = strindex(str, lava); printf("lava, pos 6 = %d\n", x);
  int y = strindex(str, tina); printf("tina, pos 14 = %d\n", y);
  int z = strindex(str, jabon); printf("jabon, pos -1 = %d\n", z);
}
