#include <cs50.h>
#include <stdio.h>

int get_int_one_eight(void);

int main(void)
{
    int col;
    int row;
    int spaces;
    int h = get_int_one_eight();

    for (col = 1; col <= h; col++)
    {
        for (spaces = col; spaces < h; spaces++)
        {
            printf(" ");
        }
        for (row = 0; row < col; row++)
        {
            printf("#");
        }
        printf("  ");
        for (row = 0; row < col; row++)
        {
            printf("#");
        }
        printf("\n");
    }
}

int get_int_one_eight(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    return height;
}
