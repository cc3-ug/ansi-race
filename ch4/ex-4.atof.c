#include <ctype.h>
#include <stdio.h>



/*
  El capitulo 4 explica una funcion llamada atof
  Esta es similar al atoi, realiza la conversion ascii to float

  Debe manejar exponentes, como en los siguientes ejemplos
  123e4		equivale a 123*10^4		su resultado deberia ser	1230000
  123e-4	equivale a 123*10^-4	su resultado deberia ser	0.0123
  -123e-4	equivale a -123*10^-4	su resultado deberia ser	-0.0123
*/
double miatof(char s[]) {
    
}



/* No modifique este main */
int main(){
	float f = miatof("29"); printf("29.00 = %2.2f\n", f);
  float g = miatof("-3.4"); printf("-3.40 = %2.2f\n", g);
  float h = miatof("1e4"); printf("10000.00 = %2.2f\n", h);
  float i = miatof("3e-2"); printf("0.03 = %2.2f\n", i);
  float j = miatof("4.5e6"); printf("4500000.00 = %2.2f\n", j);
  float k = miatof("3333.3e-2"); printf("33.33 = %2.2f\n", k);
}