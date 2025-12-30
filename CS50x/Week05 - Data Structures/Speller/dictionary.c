// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Declare global variable for the number of words of a dictionary, for the size function
int words_quant = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Choose number of buckets in hash table
// Table will have 126 buckets
const unsigned int N = 126;

// Hash table

node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to obtain an hash value
    int table_index = hash(word);

    // Create a pointer called cursor
    node *cursor = table[table_index];

    // Access the linked list at the index above and compare the words
    cursor = table[table_index];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // It's not the most complete or well done function
    // but it fulfills the educational purposes, I guess
    // Time really reduces by a half

    // Table will have 126 buckets
    // Each vowel will link to 9 CHOSEN consonants
    // Each consonant will link to the 5 vowels
    // Each one of the remaining 11 consonants will have their own bucket
    // Vowels
    // A -> [0, 10]
    // E -> [11, 21]
    // I -> [22, 32]
    // O -> [33, 43]
    // U -> [44, 54]
    // Chosen Consonants
    // B -> [55, 60]
    // C -> [61, 66]
    // D -> [67, 72]
    // M -> [73, 78]
    // N -> [79, 84]
    // P -> [85, 90]
    // R -> [91, 96]
    // S -> [97, 102]
    // T -> [103, 108]
    // V -> [109, 114]
    // Remaining Consonants
    // F -> 115
    // G -> 116
    // H -> 117
    // J -> 118
    // K -> 119
    // L -> 120
    // Q -> 121
    // W -> 122
    // X -> 123
    // Y -> 124
    // Z -> 125

    // VOWELS

    // Letter A -> [0, 10]
    if (toupper(word[0]) == 'A')
    {
        switch (toupper(word[1]))
        {
            case 'B':
                return 1;
            case 'C':
                return 2;
            case 'D':
                return 3;
            case 'M':
                return 4;
            case 'N':
                return 5;
            case 'P':
                return 6;
            case 'R':
                return 7;
            case 'S':
                return 8;
            case 'T':
                return 9;
            case 'V':
                return 10;
            default:
                return 0;
        }
    }

    // Letter E -> [11, 21]
    if (toupper(word[0]) == 'E')
    {
        switch (toupper(word[1]))
        {
            case 'B':
                return 12;
            case 'C':
                return 13;
            case 'D':
                return 14;
            case 'M':
                return 15;
            case 'N':
                return 16;
            case 'P':
                return 17;
            case 'R':
                return 18;
            case 'S':
                return 19;
            case 'T':
                return 20;
            case 'V':
                return 21;
            default:
                return 11;
        }
    }

    // Letter I -> [22, 32]
    if (toupper(word[0]) == 'I')
    {
        switch (toupper(word[1]))
        {
            case 'B':
                return 23;
            case 'C':
                return 24;
            case 'D':
                return 25;
            case 'M':
                return 26;
            case 'N':
                return 27;
            case 'P':
                return 28;
            case 'R':
                return 29;
            case 'S':
                return 30;
            case 'T':
                return 31;
            case 'V':
                return 32;
            default:
                return 22;
        }
    }

    // Letter O -> [33, 43]
    if (toupper(word[0]) == 'O')
    {
        switch (toupper(word[1]))
        {
            case 'B':
                return 34;
            case 'C':
                return 35;
            case 'D':
                return 36;
            case 'M':
                return 37;
            case 'N':
                return 38;
            case 'P':
                return 39;
            case 'R':
                return 40;
            case 'S':
                return 41;
            case 'T':
                return 42;
            case 'V':
                return 43;
            default:
                return 33;
        }
    }

    // Letter U -> [44, 54]
    if (toupper(word[0]) == 'U')
    {
        switch (toupper(word[1]))
        {
            case 'B':
                return 45;
            case 'C':
                return 46;
            case 'D':
                return 47;
            case 'M':
                return 48;
            case 'N':
                return 49;
            case 'P':
                return 50;
            case 'R':
                return 51;
            case 'S':
                return 52;
            case 'T':
                return 53;
            case 'V':
                return 54;
            default:
                return 44;
        }
    }

    // CONSONANTS

    // Letter B -> [55, 60]
    if (toupper(word[0]) == 'B')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 56;
            case 'E':
                return 57;
            case 'I':
                return 58;
            case 'O':
                return 59;
            case 'U':
                return 60;
            default:
                return 55;
        }
    }

    // Letter C -> [61, 66]
    if (toupper(word[0]) == 'C')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 62;
            case 'E':
                return 63;
            case 'I':
                return 64;
            case 'O':
                return 65;
            case 'U':
                return 66;
            default:
                return 61;
        }
    }

    // Letter D -> [67, 72]
    if (toupper(word[0]) == 'D')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 68;
            case 'E':
                return 69;
            case 'I':
                return 70;
            case 'O':
                return 71;
            case 'U':
                return 72;
            default:
                return 67;
        }
    }

    // Letter M -> [73, 78]
    if (toupper(word[0]) == 'M')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 74;
            case 'E':
                return 75;
            case 'I':
                return 76;
            case 'O':
                return 77;
            case 'U':
                return 78;
            default:
                return 73;
        }
    }

    // Letter N -> [79, 84]
    if (toupper(word[0]) == 'N')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 80;
            case 'E':
                return 81;
            case 'I':
                return 82;
            case 'O':
                return 83;
            case 'U':
                return 84;
            default:
                return 79;
        }
    }

    // Letter P -> [85, 90]
    if (toupper(word[0]) == 'P')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 86;
            case 'E':
                return 87;
            case 'I':
                return 88;
            case 'O':
                return 89;
            case 'U':
                return 90;
            default:
                return 85;
        }
    }

    // Letter R -> [91, 96]
    if (toupper(word[0]) == 'R')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 92;
            case 'E':
                return 93;
            case 'I':
                return 94;
            case 'O':
                return 95;
            case 'U':
                return 96;
            default:
                return 91;
        }
    }

    // Letter S -> [97, 102]
    if (toupper(word[0]) == 'S')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 98;
            case 'E':
                return 99;
            case 'I':
                return 100;
            case 'O':
                return 101;
            case 'U':
                return 102;
            default:
                return 97;
        }
    }

    // Letter T -> [103, 108]
    if (toupper(word[0]) == 'T')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 104;
            case 'E':
                return 105;
            case 'I':
                return 106;
            case 'O':
                return 107;
            case 'U':
                return 108;
            default:
                return 103;
        }
    }

    // Letter V -> [109, 114]
    if (toupper(word[0]) == 'V')
    {
        switch (toupper(word[1]))
        {
            case 'A':
                return 110;
            case 'E':
                return 111;
            case 'I':
                return 112;
            case 'O':
                return 113;
            case 'U':
                return 114;
            default:
                return 109;
        }
    }

    // Letter F -> 115
    if (toupper(word[0]) == 'F')
    {
        return 115;
    }

    // Letter G -> 116
    if (toupper(word[0]) == 'G')
    {
        return 116;
    }

    // Letter H -> 117
    if (toupper(word[0]) == 'H')
    {
        return 117;
    }

    // Letter J -> 118
    if (toupper(word[0]) == 'J')
    {
        return 118;
    }

    // Letter K -> 119
    if (toupper(word[0]) == 'K')
    {
        return 119;
    }

    // Letter L -> 120
    if (toupper(word[0]) == 'L')
    {
        return 120;
    }

    // Letter Q -> 121
    if (toupper(word[0]) == 'Q')
    {
        return 121;
    }

    // Letter W -> 122
    if (toupper(word[0]) == 'W')
    {
        return 122;
    }

    // Letter X -> 123
    if (toupper(word[0]) == 'X')
    {
        return 123;
    }

    // Letter Y -> 124
    if (toupper(word[0]) == 'Y')
    {
        return 124;
    }

    // Letter Z -> 125
    if (toupper(word[0]) == 'Z')
    {
        return 125;
    }
    return 0;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the directory file
    FILE *ptrDict = fopen(dictionary, "r");
    if (ptrDict == NULL)
    {
        printf("Could not open dictionary!\n");
        return false;
    }

    char dict_word[LENGTH + 1];

    // Read each word in the file - Checks if the file has ended
    while (fscanf(ptrDict, "%s", dict_word) != EOF)
    {
        // Add each word to the hash table
        // Allocates memory to new node, and checks if it was correctly done
        node *ptrNew = malloc(sizeof(node));
        if (ptrNew == NULL)
        {
            printf("Memory failure!");
            return false;
        }

        // Copy the word to the New node
        strcpy(ptrNew->word, dict_word);

        // Hashing the word to obtain table index
        int table_index = hash(dict_word);

        // New pointer points to the one the table was already pointing
        ptrNew->next = table[table_index];

        // The table node point to the New node
        table[table_index] = ptrNew;

        // Increases a word once that is written, for the size function
        words_quant++;
    }

    // Close the dictionary file
    fclose(ptrDict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return words_quant;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Go through all the nodes in the hash list and free memory

    // Going through all the table indexes and connected lists
    for (int i = 0; i < N; i++)
    {
        // Iniciating the cursor
        node *cursor = table[i];

        // Iniciating temporary node
        node *temp = table[i];

        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(temp);
            temp = cursor;
        }
    }
    return true;
}
