#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

// Common variables
int i, letterCounter, wordCounter, sentenceCounter;

// Function Prototipes
int get_letters(int lenght, string txt);
int get_words(int lenght, string txt);
int get_sentences(int lenght, string txt);

int main(void)
{
    // Get a text
    string text = get_string("Text: ");
    // Get the text lenght (number of characters) to pass to functions
    int lenght = strlen(text);

    // Count the number of letters, words and sentences
    // Letters
    int nLetters = get_letters(lenght, text);
    // Words
    int nWords = get_words(lenght, text);
    // Sentences
    int nSentences = get_sentences(lenght, text);

    // Coleman-Liau Index
    float L = (nLetters * 100.00) / nWords;
    float S = (nSentences * 100.00) / nWords;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // Outputs
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", round(index));
    }
}

int get_letters(int lenght, string txt)
{
    for (i = 0; i < lenght; i++)
    {
        if (txt[i] >= 'A' && txt[i] <= 'z')
        {
            letterCounter++;
        }
    }
    return letterCounter;
}

int get_words(int lenght, string txt)
{
    for (i = 0; i < lenght; i++)
    {
        if (txt[i] == ' ')
        {
            wordCounter++;
        }
    }
    return wordCounter + 1;
}

int get_sentences(int lenght, string txt)
{
    for (i = 0; i < lenght; i++)
    {
        if (txt[i] == '.' || txt[i] == '?' || txt[i] == '!')
        {
            sentenceCounter++;
        }
    }
    return sentenceCounter;
}
