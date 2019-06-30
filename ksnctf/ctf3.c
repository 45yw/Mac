#include <stdio.h>

int main(void)
{
    int p[] = {70, 152, 195, 284, 475, 612, 791, 896, 810,
                  850, 737, 1332, 1469, 1120, 1470, 832, 1785,
                  2196, 1520, 1480, 1449};
    for(int i = 0; i < (sizeof(p)/sizeof(int)); i++)
    {
        putchar(p[i] / (i + 1));
    }
    putchar('\n');
    return 0;
}
