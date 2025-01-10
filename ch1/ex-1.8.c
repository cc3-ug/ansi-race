#include <stdio.h>

// cuenta blanks=nb, tabs=nt, newlines=nl
int main(){ 
  long nb = 0;
  long nt = 0;
  long nl = 0;



  int charr;
  while ((charr = getchar()) != EOF)
  {
    if (charr == ' ')
    {
      ++nb;
    }
    else if (charr == '\t')
    {
      ++nt;
    }
    else if (charr == '\n')
    {
      ++nl;
    }
  }

printf("blanks: %ld tabs: %ld newlines: %ld\n ", nb, nt, nl);


return 0;


}
