#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    int countMain = 0;
    int countAux = 0;
    int sumOthers = 0;
    int sumLeftovers = 0;

    // Prompt user for credit card number
    long number = get_long("Number: ");

    // Getting the "other digits" of the number
    for (long i = 1; i < number; i *= 10)
    {
        // Only counting the requested "other digits"
        if (countMain % 2 != 0)
        {
            // Multiplying those numbers by 2
            int digit = ((number / i) % 10) * 2;
            // Breaking the digits bigger than 9 to sum them with each other
            if (digit > 9)
            {
                digit = (digit / 10) % 10 + digit % 10;
            }
            // Summing those digits
            sumOthers += digit;
        }
        // Counts the digits of the given number
        countMain++;
    }

    // Geting first digit
    long quoefFirstDigit = pow(10, countMain - 1);
    int firstDigit = (number / quoefFirstDigit) % 10;
    // Getting second digit
    long quoefSecondDigit = pow(10, countMain - 2);
    int secondDigit = (number / quoefSecondDigit) % 10;

    // Geting the leftover digits
    for (long i = 1; i < number; i *= 10)
    {
        // Here we have the even indentations, contrarily to the other ones, witch was counting the
        // odd iterations
        if (countAux % 2 == 0)
        {
            int digit = (number / i) % 10;
            // Summing the digits
            sumLeftovers += digit;
        }
        countAux++;
    }
    // For the number to be valid, this total sum has to be a 10 potency
    int module = (sumLeftovers + sumOthers) % 10;

    // Conditions to verify if the cards are valid and, if so, from witch company

    // VISA -> Has to have 13 or 16 digits, the first digit must be 4, module has to be 0
    if ((countMain == 13 || countMain == 16) && firstDigit == 4 && module == 0)
    {
        printf("VISA\n");
    }

    // American Express -> Has to have 15 digits, first two digits must be 34 or 37, module has to
    // be 0
    else if (countMain == 15 && firstDigit == 3 && (secondDigit == 4 || secondDigit == 7) &&
             module == 0)
    {
        printf("AMEX\n");
    }

    // Master Card -> Has to have 16 digits, the first two digits must be 51, 52, 53, 54 or 55,
    // module has to be 0
    else if (countMain == 16 && firstDigit == 5 &&
             (secondDigit == 1 || secondDigit == 2 || secondDigit == 3 || secondDigit == 4 ||
              secondDigit == 5) &&
             module == 0)
    {
        printf("MASTERCARD\n");
    }

    else
    {
        printf("INVALID\n");
    }
}
