#include <stdio.h>
int main (void)
{
  char str[1024] = {};
  FILE *fp;
  fp = fopen("ctf22.rtf", "r");
  if(fp == NULL){
    printf("miss\n");
    return -1;
  }
  while((fgets(str, 256, fp)) != NULL){
    printf("%s", str);
  }
  fclose(fp);
  return 0;
}
