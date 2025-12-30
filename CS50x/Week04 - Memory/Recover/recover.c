#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Aux variables
    int counter = 0;
    char filename[8];
    FILE *image = NULL;
    bool found = false;

    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover memory_card_name.raw\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // While there's still data left to read from the memory card
    while (fread(buffer, 512, 1, card) == 1)
    {
        // Checks if there is a JPEG file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // A JPEG file was found
            found = true;
        }
        if (found)
        {
            // If a JPEG file was found and is not the first one, means the file
            // is opened and must be closed
            if (counter != 0)
            {
                fclose(image);
            }

            // Create first JPEG from the data
            sprintf(filename, "%03i.jpg", counter);
            image = fopen(filename, "w");
            if (image == NULL)
            {
                return 3;
            }
            fwrite(buffer, 512, 1, image);
            // Found turns false to search another JPEG file
            found = false;
            counter++;
        }
        else if (counter != 0)
        {
            // Create other JPEGs
            fwrite(buffer, 512, 1, image);
        }
    }
    fclose(image);
    fclose(card);
    return 0;
}
