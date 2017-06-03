#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
  FILE *fp1 = fopen("ctf36.txt", "r");
  FILE *fp2 = fopen("ctf36result.txt", "w");
  char string[10000];
  while(fgets(string, 10000, fp1)){
     fprintf(fp2, "%s\n", strstr("string", "2563"));
  }
  fclose(fp1);
  fclose(fp2);
  return 0;
}
