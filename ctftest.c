#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln(char *input){
  char buf[16];
  int secret = 0;
  strcpy(buf, input);

  if (secret == 0xc0deface){
    puts("flag is ...");
  }
  else{
    printf("The secret is %x\n", secret);
  }
}

int main(int argc, char **argv){
  if (argc > 1)
    vuln(argv[1]);
  return 0;
}
