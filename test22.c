#include <stdio.h>
#include <ctype.h>

#define XPM_BLACK30 "##############################"
#define XPM_WHITE30 "______________________________"

int main()
{
    int i, j, k;
    char c;
    char line[32];

    FILE *fp;
    fp = fopen("take22.txt", "r");
    printf(
        //" /* XPM */\n"
        //"static char *take22_xpm[] = { \n"
        " \"%d %d 3 1\", \n",
        //" \".   c none\",\n"
        //" \"#   c black\",\n"
        //" \"_   c white\",\n",
        (31 * 30), ( 31 * 30)
     );

    for(i = 0; !feof(fp); i++){
      c = fgetc(fp);
      if(islower(c)){
         line[i] = '0';
       }
       if(isupper(c)){
         line[i] = '1';
       }
      if(c == '\n'){
        line[32] = '\0';
        i = -1;
        for(k = 0; k < 30; k++){
          printf("\"");
          for(j = 0; j < 31; j++){
            switch(line[j]){
              case '0':  printf(XPM_WHITE30); break;
              case '1':  printf(XPM_BLACK30); break;
            }
          }
          printf("\",\n");
        }
      }
    }
    printf("};");

    fclose(fp);
    return 0;
}
