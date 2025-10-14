#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float pixel_average;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculating the average ammount of blue, green and red for each pixel, and assigning
            // it to all of them
            pixel_average =
                round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0);
            image[i][j].rgbtBlue = pixel_average;
            image[i][j].rgbtGreen = pixel_average;
            image[i][j].rgbtRed = pixel_average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            temp[i][j] = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp[i][j];
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Average Variables
    int blue_pixel_average, green_pixel_average, red_pixel_average;

    // Creating a copy of the original image
    RGBTRIPLE image_copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image_copy[i][j] = image[i][j];
        }
    }

    // Generating new image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Top Line
            if (i == 0)
            {
                // Top Left Corner
                if (j == 0)
                {
                    blue_pixel_average =
                        round((image_copy[0][0].rgbtBlue + image_copy[0][1].rgbtBlue +
                               image_copy[1][0].rgbtBlue + image_copy[1][1].rgbtBlue) /
                              4.0);
                    green_pixel_average =
                        round((image_copy[0][0].rgbtGreen + image_copy[0][1].rgbtGreen +
                               image_copy[1][0].rgbtGreen + image_copy[1][1].rgbtGreen) /
                              4.0);
                    red_pixel_average =
                        round((image_copy[0][0].rgbtRed + image_copy[0][1].rgbtRed +
                               image_copy[1][0].rgbtRed + image_copy[1][1].rgbtRed) /
                              4.0);
                } // Top Left Corner

                // Top Right Corner
                else if (j == width - 1)
                {
                    blue_pixel_average = round(
                        (image_copy[0][width - 1].rgbtBlue + image_copy[0][width - 2].rgbtBlue +
                         image_copy[1][width - 1].rgbtBlue + image_copy[1][width - 2].rgbtBlue) /
                        4.0);
                    green_pixel_average = round(
                        (image_copy[0][width - 1].rgbtGreen + image_copy[0][width - 2].rgbtGreen +
                         image_copy[1][width - 1].rgbtGreen + image_copy[1][width - 2].rgbtGreen) /
                        4.0);
                    red_pixel_average = round(
                        (image_copy[0][width - 1].rgbtRed + image_copy[0][width - 2].rgbtRed +
                         image_copy[1][width - 1].rgbtRed + image_copy[1][width - 2].rgbtRed) /
                        4.0);
                } // Top Right Corner

                // Top Line
                else
                {
                    blue_pixel_average =
                        round((image_copy[0][j].rgbtBlue + image_copy[0][j - 1].rgbtBlue +
                               image_copy[0][j + 1].rgbtBlue + image_copy[1][j - 1].rgbtBlue +
                               image_copy[1][j].rgbtBlue + image_copy[1][j + 1].rgbtBlue) /
                              6.0);
                    green_pixel_average =
                        round((image_copy[0][j].rgbtGreen + image_copy[0][j - 1].rgbtGreen +
                               image_copy[0][j + 1].rgbtGreen + image_copy[1][j - 1].rgbtGreen +
                               image_copy[1][j].rgbtGreen + image_copy[1][j + 1].rgbtGreen) /
                              6.0);
                    red_pixel_average =
                        round((image_copy[0][j].rgbtRed + image_copy[0][j - 1].rgbtRed +
                               image_copy[0][j + 1].rgbtRed + image_copy[1][j - 1].rgbtRed +
                               image_copy[1][j].rgbtRed + image_copy[1][j + 1].rgbtRed) /
                              6.0);
                } // Top Line

                image[i][j].rgbtBlue = blue_pixel_average;
                image[i][j].rgbtGreen = green_pixel_average;
                image[i][j].rgbtRed = red_pixel_average;
            } // if (i == 0) -> Top Line

            // Middle Lines
            else if (i != 0 && i != (height - 1))
            {
                // Left Line
                if (j == 0)
                {
                    blue_pixel_average =
                        round((image_copy[i][0].rgbtBlue + image_copy[i - 1][0].rgbtBlue +
                               image_copy[i + 1][0].rgbtBlue + image_copy[i + 1][1].rgbtBlue +
                               image_copy[i][1].rgbtBlue + image_copy[i - 1][1].rgbtBlue) /
                              6.0);
                    green_pixel_average =
                        round((image_copy[i][0].rgbtGreen + image_copy[i - 1][0].rgbtGreen +
                               image_copy[i + 1][0].rgbtGreen + image_copy[i + 1][1].rgbtGreen +
                               image_copy[i][1].rgbtGreen + image_copy[i - 1][1].rgbtGreen) /
                              6.0);
                    red_pixel_average =
                        round((image_copy[i][0].rgbtRed + image_copy[i - 1][0].rgbtRed +
                               image_copy[i + 1][0].rgbtRed + image_copy[i + 1][1].rgbtRed +
                               image_copy[i][1].rgbtRed + image_copy[i - 1][1].rgbtRed) /
                              6.0);

                } // Left Line

                // Right Line
                else if (j == (width - 1))
                {
                    blue_pixel_average = round((image_copy[i][width - 1].rgbtBlue +
                                                image_copy[i][width - 2].rgbtBlue +
                                                image_copy[i + 1][width - 1].rgbtBlue +
                                                image_copy[i + 1][width - 2].rgbtBlue +
                                                image_copy[i - 1][width - 1].rgbtBlue +
                                                image_copy[i - 1][width - 2].rgbtBlue) /
                                               6.0);
                    green_pixel_average = round((image_copy[i][width - 1].rgbtGreen +
                                                 image_copy[i][width - 2].rgbtGreen +
                                                 image_copy[i + 1][width - 1].rgbtGreen +
                                                 image_copy[i + 1][width - 2].rgbtGreen +
                                                 image_copy[i - 1][width - 1].rgbtGreen +
                                                 image_copy[i - 1][width - 2].rgbtGreen) /
                                                6.0);
                    red_pixel_average =
                        round((image_copy[i][width - 1].rgbtRed + image_copy[i][width - 2].rgbtRed +
                               image_copy[i + 1][width - 1].rgbtRed +
                               image_copy[i + 1][width - 2].rgbtRed +
                               image_copy[i - 1][width - 1].rgbtRed +
                               image_copy[i - 1][width - 2].rgbtRed) /
                              6.0);
                } // Right Line

                // Middle Lines
                else
                {
                    blue_pixel_average =
                        round((image_copy[i][j].rgbtBlue + image_copy[i - 1][j - 1].rgbtBlue +
                               image_copy[i - 1][j].rgbtBlue + image_copy[i - 1][j + 1].rgbtBlue +
                               image_copy[i][j - 1].rgbtBlue + image_copy[i][j + 1].rgbtBlue +
                               image_copy[i + 1][j - 1].rgbtBlue + image_copy[i + 1][j].rgbtBlue +
                               image_copy[i + 1][j + 1].rgbtBlue) /
                              9.0);
                    green_pixel_average =
                        round((image_copy[i][j].rgbtGreen + image_copy[i - 1][j - 1].rgbtGreen +
                               image_copy[i - 1][j].rgbtGreen + image_copy[i - 1][j + 1].rgbtGreen +
                               image_copy[i][j - 1].rgbtGreen + image_copy[i][j + 1].rgbtGreen +
                               image_copy[i + 1][j - 1].rgbtGreen + image_copy[i + 1][j].rgbtGreen +
                               image_copy[i + 1][j + 1].rgbtGreen) /
                              9.0);
                    red_pixel_average =
                        round((image_copy[i][j].rgbtRed + image_copy[i - 1][j - 1].rgbtRed +
                               image_copy[i - 1][j].rgbtRed + image_copy[i - 1][j + 1].rgbtRed +
                               image_copy[i][j - 1].rgbtRed + image_copy[i][j + 1].rgbtRed +
                               image_copy[i + 1][j - 1].rgbtRed + image_copy[i + 1][j].rgbtRed +
                               image_copy[i + 1][j + 1].rgbtRed) /
                              9.0);
                } // Middle Lines
                image[i][j].rgbtBlue = blue_pixel_average;
                image[i][j].rgbtGreen = green_pixel_average;
                image[i][j].rgbtRed = red_pixel_average;
            } // if (i != 0 && i < height) -> Middle Lines

            // Bottom Line
            else if (i == (height - 1))
            {
                // Bottom Left Corner
                if (j == 0)
                {
                    blue_pixel_average = round(
                        (image_copy[height - 1][0].rgbtBlue + image_copy[height - 1][1].rgbtBlue +
                         image_copy[height - 2][0].rgbtBlue + image_copy[height - 2][1].rgbtBlue) /
                        4.0);
                    green_pixel_average = round((image_copy[height - 1][0].rgbtGreen +
                                                 image_copy[height - 1][1].rgbtGreen +
                                                 image_copy[height - 2][0].rgbtGreen +
                                                 image_copy[height - 2][1].rgbtGreen) /
                                                4.0);
                    red_pixel_average = round(
                        (image_copy[height - 1][0].rgbtRed + image_copy[height - 1][1].rgbtRed +
                         image_copy[height - 2][0].rgbtRed + image_copy[height - 2][1].rgbtRed) /
                        4.0);
                } // Bottom Left Corner

                // Bottom Right Corner
                else if (j == (width - 1))
                {
                    blue_pixel_average = round((image_copy[height - 1][width - 1].rgbtBlue +
                                                image_copy[height - 1][width - 2].rgbtBlue +
                                                image_copy[height - 2][width - 1].rgbtBlue +
                                                image_copy[height - 2][width - 2].rgbtBlue) /
                                               4.0);
                    green_pixel_average = round((image_copy[height - 1][width - 1].rgbtGreen +
                                                 image_copy[height - 1][width - 2].rgbtGreen +
                                                 image_copy[height - 2][width - 1].rgbtGreen +
                                                 image_copy[height - 2][width - 2].rgbtGreen) /
                                                4.0);
                    red_pixel_average = round((image_copy[height - 1][width - 1].rgbtRed +
                                               image_copy[height - 1][width - 2].rgbtRed +
                                               image_copy[height - 2][width - 1].rgbtRed +
                                               image_copy[height - 2][width - 2].rgbtRed) /
                                              4.0);
                } // Bottom Right Corner

                // Bottom Line
                else
                {
                    blue_pixel_average = round((image_copy[height - 1][j].rgbtBlue +
                                                image_copy[height - 1][j - 1].rgbtBlue +
                                                image_copy[height - 1][j + 1].rgbtBlue +
                                                image_copy[height - 2][j - 1].rgbtBlue +
                                                image_copy[height - 2][j].rgbtBlue +
                                                image_copy[height - 2][j + 1].rgbtBlue) /
                                               6.0);
                    green_pixel_average = round((image_copy[height - 1][j].rgbtGreen +
                                                 image_copy[height - 1][j - 1].rgbtGreen +
                                                 image_copy[height - 1][j + 1].rgbtGreen +
                                                 image_copy[height - 2][j - 1].rgbtGreen +
                                                 image_copy[height - 2][j].rgbtGreen +
                                                 image_copy[height - 2][j + 1].rgbtGreen) /
                                                6.0);
                    red_pixel_average = round(
                        (image_copy[height - 1][j].rgbtRed + image_copy[height - 1][j - 1].rgbtRed +
                         image_copy[height - 1][j + 1].rgbtRed +
                         image_copy[height - 2][j - 1].rgbtRed + image_copy[height - 2][j].rgbtRed +
                         image_copy[height - 2][j + 1].rgbtRed) /
                        6.0);
                } // Bottom Line
                image[i][j].rgbtBlue = blue_pixel_average;
                image[i][j].rgbtGreen = green_pixel_average;
                image[i][j].rgbtRed = red_pixel_average;
            } // i == (height - 1) -> Bottom Line
        } // for j
    } // for i
    return;
} // void

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Average Variables
    int blue_pixel_average_x, green_pixel_average_x, red_pixel_average_x;
    int blue_pixel_average_y, green_pixel_average_y, red_pixel_average_y;
    int blue_module, green_module, red_module;

    // Matrixes
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    // Creating a copy of the original image
    RGBTRIPLE image_copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image_copy[i][j] = image[i][j];
        }
    }

    // Generating new image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Top Line
            if (i == 0)
            {
                // Top Left Corner
                if (j == 0)
                {
                    blue_pixel_average_x = image_copy[0][0].rgbtBlue * Gx[1][1] +
                                           image_copy[0][1].rgbtBlue * Gx[1][2] +
                                           image_copy[1][0].rgbtBlue * Gx[2][1] +
                                           image_copy[1][1].rgbtBlue * Gx[2][2];
                    blue_pixel_average_y = image_copy[0][0].rgbtBlue * Gy[1][1] +
                                           image_copy[0][1].rgbtBlue * Gy[1][2] +
                                           image_copy[1][0].rgbtBlue * Gy[2][1] +
                                           image_copy[1][1].rgbtBlue * Gy[2][2];

                    green_pixel_average_x = image_copy[0][0].rgbtGreen * Gx[1][1] +
                                            image_copy[0][1].rgbtGreen * Gx[1][2] +
                                            image_copy[1][0].rgbtGreen * Gx[2][1] +
                                            image_copy[1][1].rgbtGreen * Gx[2][2];
                    green_pixel_average_y = image_copy[0][0].rgbtGreen * Gy[1][1] +
                                            image_copy[0][1].rgbtGreen * Gy[1][2] +
                                            image_copy[1][0].rgbtGreen * Gy[2][1] +
                                            image_copy[1][1].rgbtGreen * Gy[2][2];

                    red_pixel_average_x =
                        image_copy[0][0].rgbtRed * Gx[1][1] + image_copy[0][1].rgbtRed * Gx[1][2] +
                        image_copy[1][0].rgbtRed * Gx[2][1] + image_copy[1][1].rgbtRed * Gx[2][2];
                    red_pixel_average_y =
                        image_copy[0][0].rgbtRed * Gy[1][1] + image_copy[0][1].rgbtRed * Gy[1][2] +
                        image_copy[1][0].rgbtRed * Gy[2][1] + image_copy[1][1].rgbtRed * Gy[2][2];
                } // Top Left Corner

                // Top Right Corner
                else if (j == width - 1)
                {
                    blue_pixel_average_x = image_copy[0][width - 1].rgbtBlue * Gx[1][1] +
                                           image_copy[0][width - 2].rgbtBlue * Gx[1][0] +
                                           image_copy[1][width - 1].rgbtBlue * Gx[2][1] +
                                           image_copy[1][width - 2].rgbtBlue * Gx[2][0];
                    blue_pixel_average_y = image_copy[0][width - 1].rgbtBlue * Gy[1][1] +
                                           image_copy[0][width - 2].rgbtBlue * Gy[1][0] +
                                           image_copy[1][width - 1].rgbtBlue * Gy[2][1] +
                                           image_copy[1][width - 2].rgbtBlue * Gy[2][0];

                    green_pixel_average_x = image_copy[0][width - 1].rgbtGreen * Gx[1][1] +
                                            image_copy[0][width - 2].rgbtGreen * Gx[1][0] +
                                            image_copy[1][width - 1].rgbtGreen * Gx[2][1] +
                                            image_copy[1][width - 2].rgbtGreen * Gx[2][0];
                    green_pixel_average_y = image_copy[0][width - 1].rgbtGreen * Gy[1][1] +
                                            image_copy[0][width - 2].rgbtGreen * Gy[1][0] +
                                            image_copy[1][width - 1].rgbtGreen * Gy[2][1] +
                                            image_copy[1][width - 2].rgbtGreen * Gy[2][0];

                    red_pixel_average_x = image_copy[0][width - 1].rgbtRed * Gx[1][1] +
                                          image_copy[0][width - 2].rgbtRed * Gx[1][0] +
                                          image_copy[1][width - 1].rgbtRed * Gx[2][1] +
                                          image_copy[1][width - 2].rgbtRed * Gx[2][0];
                    red_pixel_average_y = image_copy[0][width - 1].rgbtRed * Gy[1][1] +
                                          image_copy[0][width - 2].rgbtRed * Gy[1][0] +
                                          image_copy[1][width - 1].rgbtRed * Gy[2][1] +
                                          image_copy[1][width - 2].rgbtRed * Gy[2][0];
                } // Top Right Corner

                // Top Line
                else
                {
                    blue_pixel_average_x = image_copy[0][j].rgbtBlue * Gx[1][1] +
                                           image_copy[0][j - 1].rgbtBlue * Gx[1][0] +
                                           image_copy[0][j + 1].rgbtBlue * Gx[1][2] +
                                           image_copy[1][j].rgbtBlue * Gx[2][1] +
                                           image_copy[1][j - 1].rgbtBlue * Gx[2][0] +
                                           image_copy[1][j + 1].rgbtBlue * Gx[2][2];

                    blue_pixel_average_y = image_copy[0][j].rgbtBlue * Gy[1][1] +
                                           image_copy[0][j - 1].rgbtBlue * Gy[1][0] +
                                           image_copy[0][j + 1].rgbtBlue * Gy[1][2] +
                                           image_copy[1][j].rgbtBlue * Gy[2][1] +
                                           image_copy[1][j - 1].rgbtBlue * Gy[2][0] +
                                           image_copy[1][j + 1].rgbtBlue * Gy[2][2];

                    green_pixel_average_x = image_copy[0][j].rgbtGreen * Gx[1][1] +
                                            image_copy[0][j - 1].rgbtGreen * Gx[1][0] +
                                            image_copy[0][j + 1].rgbtGreen * Gx[1][2] +
                                            image_copy[1][j].rgbtGreen * Gx[2][1] +
                                            image_copy[1][j - 1].rgbtGreen * Gx[2][0] +
                                            image_copy[1][j + 1].rgbtGreen * Gx[2][2];

                    green_pixel_average_y = image_copy[0][j].rgbtGreen * Gy[1][1] +
                                            image_copy[0][j - 1].rgbtGreen * Gy[1][0] +
                                            image_copy[0][j + 1].rgbtGreen * Gy[1][2] +
                                            image_copy[1][j].rgbtGreen * Gy[2][1] +
                                            image_copy[1][j - 1].rgbtGreen * Gy[2][0] +
                                            image_copy[1][j + 1].rgbtGreen * Gy[2][2];

                    red_pixel_average_x = image_copy[0][j].rgbtRed * Gx[1][1] +
                                          image_copy[0][j - 1].rgbtRed * Gx[1][0] +
                                          image_copy[0][j + 1].rgbtRed * Gx[1][2] +
                                          image_copy[1][j].rgbtRed * Gx[2][1] +
                                          image_copy[1][j - 1].rgbtRed * Gx[2][0] +
                                          image_copy[1][j + 1].rgbtRed * Gx[2][2];

                    red_pixel_average_y = image_copy[0][j].rgbtRed * Gy[1][1] +
                                          image_copy[0][j - 1].rgbtRed * Gy[1][0] +
                                          image_copy[0][j + 1].rgbtRed * Gy[1][2] +
                                          image_copy[1][j].rgbtRed * Gy[2][1] +
                                          image_copy[1][j - 1].rgbtRed * Gy[2][0] +
                                          image_copy[1][j + 1].rgbtRed * Gy[2][2];
                } // Top Line
                blue_module =
                    round(sqrt((pow(blue_pixel_average_x, 2) + pow(blue_pixel_average_y, 2))));
                green_module =
                    round(sqrt((pow(green_pixel_average_x, 2) + pow(green_pixel_average_y, 2))));
                red_module =
                    round(sqrt((pow(red_pixel_average_x, 2) + pow(red_pixel_average_y, 2))));

                if (blue_module > 255)
                {
                    image[i][j].rgbtBlue = 255;
                }
                else
                {
                    image[i][j].rgbtBlue = blue_module;
                }
                if (green_module > 255)
                {
                    image[i][j].rgbtGreen = 255;
                }
                else
                {
                    image[i][j].rgbtGreen = green_module;
                }
                if (red_module > 255)
                {
                    image[i][j].rgbtRed = 255;
                }
                else
                {
                    image[i][j].rgbtRed = red_module;
                }
            } // if (i = 0) -> Top Line

            // Middle Lines
            else if (i != 0 && i != (height - 1))
            {
                // Left Line
                if (j == 0)
                {
                    blue_pixel_average_x = image_copy[i][0].rgbtBlue * Gx[1][1] +
                                           image_copy[i - 1][0].rgbtBlue * Gx[0][1] +
                                           image_copy[i + 1][0].rgbtBlue * Gx[2][1] +
                                           image_copy[i + 1][1].rgbtBlue * Gx[2][2] +
                                           image_copy[i][1].rgbtBlue * Gx[1][2] +
                                           image_copy[i - 1][1].rgbtBlue * Gx[0][2];
                    blue_pixel_average_y = image_copy[i][0].rgbtBlue * Gy[1][1] +
                                           image_copy[i - 1][0].rgbtBlue * Gy[0][1] +
                                           image_copy[i + 1][0].rgbtBlue * Gy[2][1] +
                                           image_copy[i + 1][1].rgbtBlue * Gy[2][2] +
                                           image_copy[i][1].rgbtBlue * Gy[1][2] +
                                           image_copy[i - 1][1].rgbtBlue * Gy[0][2];

                    green_pixel_average_x = image_copy[i][0].rgbtGreen * Gx[1][1] +
                                            image_copy[i - 1][0].rgbtGreen * Gx[0][1] +
                                            image_copy[i + 1][0].rgbtGreen * Gx[2][1] +
                                            image_copy[i + 1][1].rgbtGreen * Gx[2][2] +
                                            image_copy[i][1].rgbtGreen * Gx[1][2] +
                                            image_copy[i - 1][1].rgbtGreen * Gx[0][2];
                    green_pixel_average_y = image_copy[i][0].rgbtGreen * Gy[1][1] +
                                            image_copy[i - 1][0].rgbtGreen * Gy[0][1] +
                                            image_copy[i + 1][0].rgbtGreen * Gy[2][1] +
                                            image_copy[i + 1][1].rgbtGreen * Gy[2][2] +
                                            image_copy[i][1].rgbtGreen * Gy[1][2] +
                                            image_copy[i - 1][1].rgbtGreen * Gy[0][2];

                    red_pixel_average_x = image_copy[i][0].rgbtRed * Gx[1][1] +
                                          image_copy[i - 1][0].rgbtRed * Gx[0][1] +
                                          image_copy[i + 1][0].rgbtRed * Gx[2][1] +
                                          image_copy[i + 1][1].rgbtRed * Gx[2][2] +
                                          image_copy[i][1].rgbtRed * Gx[1][2] +
                                          image_copy[i - 1][1].rgbtRed * Gx[0][2];
                    red_pixel_average_y = image_copy[i][0].rgbtRed * Gy[1][1] +
                                          image_copy[i - 1][0].rgbtRed * Gy[0][1] +
                                          image_copy[i + 1][0].rgbtRed * Gy[2][1] +
                                          image_copy[i + 1][1].rgbtRed * Gy[2][2] +
                                          image_copy[i][1].rgbtRed * Gy[1][2] +
                                          image_copy[i - 1][1].rgbtRed * Gy[0][2];
                } // Left Line

                // Right Line
                else if (j == (width - 1))
                {
                    blue_pixel_average_x = image_copy[i][width - 1].rgbtBlue * Gx[1][1] +
                                           image_copy[i][width - 2].rgbtBlue * Gx[1][0] +
                                           image_copy[i + 1][width - 1].rgbtBlue * Gx[0][1] +
                                           image_copy[i + 1][width - 2].rgbtBlue * Gx[0][0] +
                                           image_copy[i - 1][width - 1].rgbtBlue * Gx[2][1] +
                                           image_copy[i - 1][width - 2].rgbtBlue * Gx[2][0];
                    blue_pixel_average_y = image_copy[i][width - 1].rgbtBlue * Gy[1][1] +
                                           image_copy[i][width - 2].rgbtBlue * Gy[1][0] +
                                           image_copy[i + 1][width - 1].rgbtBlue * Gy[0][1] +
                                           image_copy[i + 1][width - 2].rgbtBlue * Gy[0][0] +
                                           image_copy[i - 1][width - 1].rgbtBlue * Gy[2][1] +
                                           image_copy[i - 1][width - 2].rgbtBlue * Gy[2][0];

                    green_pixel_average_x = image_copy[i][width - 1].rgbtGreen * Gx[1][1] +
                                            image_copy[i][width - 2].rgbtGreen * Gx[1][0] +
                                            image_copy[i + 1][width - 1].rgbtGreen * Gx[0][1] +
                                            image_copy[i + 1][width - 2].rgbtGreen * Gx[0][0] +
                                            image_copy[i - 1][width - 1].rgbtGreen * Gx[2][1] +
                                            image_copy[i - 1][width - 2].rgbtGreen * Gx[2][0];
                    green_pixel_average_y = image_copy[i][width - 1].rgbtGreen * Gy[1][1] +
                                            image_copy[i][width - 2].rgbtGreen * Gy[1][0] +
                                            image_copy[i + 1][width - 1].rgbtGreen * Gy[0][1] +
                                            image_copy[i + 1][width - 2].rgbtGreen * Gy[0][0] +
                                            image_copy[i - 1][width - 1].rgbtGreen * Gy[2][1] +
                                            image_copy[i - 1][width - 2].rgbtGreen * Gy[2][0];

                    red_pixel_average_x = image_copy[i][width - 1].rgbtRed * Gx[1][1] +
                                          image_copy[i][width - 2].rgbtRed * Gx[1][0] +
                                          image_copy[i + 1][width - 1].rgbtRed * Gx[0][1] +
                                          image_copy[i + 1][width - 2].rgbtRed * Gx[0][0] +
                                          image_copy[i - 1][width - 1].rgbtRed * Gx[2][1] +
                                          image_copy[i - 1][width - 2].rgbtRed * Gx[2][0];
                    red_pixel_average_y = image_copy[i][width - 1].rgbtRed * Gy[1][1] +
                                          image_copy[i][width - 2].rgbtRed * Gy[1][0] +
                                          image_copy[i + 1][width - 1].rgbtRed * Gy[0][1] +
                                          image_copy[i + 1][width - 2].rgbtRed * Gy[0][0] +
                                          image_copy[i - 1][width - 1].rgbtRed * Gy[2][1] +
                                          image_copy[i - 1][width - 2].rgbtRed * Gy[2][0];
                } // Right Line

                // Middle Lines
                else
                {
                    blue_pixel_average_x = image_copy[i][j].rgbtBlue * Gx[1][1] +
                                           image_copy[i - 1][j - 1].rgbtBlue * Gx[0][0] +
                                           image_copy[i - 1][j].rgbtBlue * Gx[0][1] +
                                           image_copy[i - 1][j + 1].rgbtBlue * Gx[0][2] +
                                           image_copy[i][j - 1].rgbtBlue * Gx[1][0] +
                                           image_copy[i][j + 1].rgbtBlue * Gx[1][2] +
                                           image_copy[i + 1][j - 1].rgbtBlue * Gx[2][0] +
                                           image_copy[i + 1][j].rgbtBlue * Gx[2][1] +
                                           image_copy[i + 1][j + 1].rgbtBlue * Gx[2][2];
                    blue_pixel_average_y = image_copy[i][j].rgbtBlue * Gy[1][1] +
                                           image_copy[i - 1][j - 1].rgbtBlue * Gy[0][0] +
                                           image_copy[i - 1][j].rgbtBlue * Gy[0][1] +
                                           image_copy[i - 1][j + 1].rgbtBlue * Gy[0][2] +
                                           image_copy[i][j - 1].rgbtBlue * Gy[1][0] +
                                           image_copy[i][j + 1].rgbtBlue * Gy[1][2] +
                                           image_copy[i + 1][j - 1].rgbtBlue * Gy[2][0] +
                                           image_copy[i + 1][j].rgbtBlue * Gy[2][1] +
                                           image_copy[i + 1][j + 1].rgbtBlue * Gy[2][2];

                    green_pixel_average_x = image_copy[i][j].rgbtGreen * Gx[1][1] +
                                            image_copy[i - 1][j - 1].rgbtGreen * Gx[0][0] +
                                            image_copy[i - 1][j].rgbtGreen * Gx[0][1] +
                                            image_copy[i - 1][j + 1].rgbtGreen * Gx[0][2] +
                                            image_copy[i][j - 1].rgbtGreen * Gx[1][0] +
                                            image_copy[i][j + 1].rgbtGreen * Gx[1][2] +
                                            image_copy[i + 1][j - 1].rgbtGreen * Gx[2][0] +
                                            image_copy[i + 1][j].rgbtGreen * Gx[2][1] +
                                            image_copy[i + 1][j + 1].rgbtGreen * Gx[2][2];
                    green_pixel_average_y = image_copy[i][j].rgbtGreen * Gy[1][1] +
                                            image_copy[i - 1][j - 1].rgbtGreen * Gy[0][0] +
                                            image_copy[i - 1][j].rgbtGreen * Gy[0][1] +
                                            image_copy[i - 1][j + 1].rgbtGreen * Gy[0][2] +
                                            image_copy[i][j - 1].rgbtGreen * Gy[1][0] +
                                            image_copy[i][j + 1].rgbtGreen * Gy[1][2] +
                                            image_copy[i + 1][j - 1].rgbtGreen * Gy[2][0] +
                                            image_copy[i + 1][j].rgbtGreen * Gy[2][1] +
                                            image_copy[i + 1][j + 1].rgbtGreen * Gy[2][2];

                    red_pixel_average_x = image_copy[i][j].rgbtRed * Gx[1][1] +
                                          image_copy[i - 1][j - 1].rgbtRed * Gx[0][0] +
                                          image_copy[i - 1][j].rgbtRed * Gx[0][1] +
                                          image_copy[i - 1][j + 1].rgbtRed * Gx[0][2] +
                                          image_copy[i][j - 1].rgbtRed * Gx[1][0] +
                                          image_copy[i][j + 1].rgbtRed * Gx[1][2] +
                                          image_copy[i + 1][j - 1].rgbtRed * Gx[2][0] +
                                          image_copy[i + 1][j].rgbtRed * Gx[2][1] +
                                          image_copy[i + 1][j + 1].rgbtRed * Gx[2][2];
                    red_pixel_average_y = image_copy[i][j].rgbtRed * Gy[1][1] +
                                          image_copy[i - 1][j - 1].rgbtRed * Gy[0][0] +
                                          image_copy[i - 1][j].rgbtRed * Gy[0][1] +
                                          image_copy[i - 1][j + 1].rgbtRed * Gy[0][2] +
                                          image_copy[i][j - 1].rgbtRed * Gy[1][0] +
                                          image_copy[i][j + 1].rgbtRed * Gy[1][2] +
                                          image_copy[i + 1][j - 1].rgbtRed * Gy[2][0] +
                                          image_copy[i + 1][j].rgbtRed * Gy[2][1] +
                                          image_copy[i + 1][j + 1].rgbtRed * Gy[2][2];

                } // Middle Lines
                blue_module =
                    round(sqrt((pow(blue_pixel_average_x, 2) + pow(blue_pixel_average_y, 2))));
                green_module =
                    round(sqrt((pow(green_pixel_average_x, 2) + pow(green_pixel_average_y, 2))));
                red_module =
                    round(sqrt((pow(red_pixel_average_x, 2) + pow(red_pixel_average_y, 2))));

                if (blue_module > 255)
                {
                    image[i][j].rgbtBlue = 255;
                }
                else
                {
                    image[i][j].rgbtBlue = blue_module;
                }
                if (green_module > 255)
                {
                    image[i][j].rgbtGreen = 255;
                }
                else
                {
                    image[i][j].rgbtGreen = green_module;
                }
                if (red_module > 255)
                {
                    image[i][j].rgbtRed = 255;
                }
                else
                {
                    image[i][j].rgbtRed = red_module;
                }
            } // if (i != 0 && i < height) -> Middle Lines

            // Bottom Line
            else if (i == (height - 1))
            {
                // Bottom Left Corner
                if (j == 0)
                {
                    blue_pixel_average_x = image_copy[height - 1][0].rgbtBlue * Gx[1][1] +
                                           image_copy[height - 1][1].rgbtBlue * Gx[1][2] +
                                           image_copy[height - 2][0].rgbtBlue * Gx[0][1] +
                                           image_copy[height - 2][1].rgbtBlue * Gx[0][2];
                    blue_pixel_average_y = image_copy[height - 1][0].rgbtBlue * Gy[1][1] +
                                           image_copy[height - 1][1].rgbtBlue * Gy[1][2] +
                                           image_copy[height - 2][0].rgbtBlue * Gy[0][1] +
                                           image_copy[height - 2][1].rgbtBlue * Gy[0][2];

                    green_pixel_average_x = image_copy[height - 1][0].rgbtGreen * Gx[1][1] +
                                            image_copy[height - 1][1].rgbtGreen * Gx[1][2] +
                                            image_copy[height - 2][0].rgbtGreen * Gx[0][1] +
                                            image_copy[height - 2][1].rgbtGreen * Gx[0][2];
                    green_pixel_average_y = image_copy[height - 1][0].rgbtGreen * Gy[1][1] +
                                            image_copy[height - 1][1].rgbtGreen * Gy[1][2] +
                                            image_copy[height - 2][0].rgbtGreen * Gy[0][1] +
                                            image_copy[height - 2][1].rgbtGreen * Gy[0][2];

                    red_pixel_average_x = image_copy[height - 1][0].rgbtRed * Gx[1][1] +
                                          image_copy[height - 1][1].rgbtRed * Gx[1][2] +
                                          image_copy[height - 2][0].rgbtRed * Gx[0][1] +
                                          image_copy[height - 2][1].rgbtRed * Gx[0][2];
                    red_pixel_average_y = image_copy[height - 1][0].rgbtRed * Gy[1][1] +
                                          image_copy[height - 1][1].rgbtRed * Gy[1][2] +
                                          image_copy[height - 2][0].rgbtRed * Gy[0][1] +
                                          image_copy[height - 2][1].rgbtRed * Gy[0][2];
                } // Bottom Left Corner

                // Bottom Right Corner
                else if (j == (width - 1))
                {
                    blue_pixel_average_x = image_copy[height - 1][width - 1].rgbtBlue * Gx[1][1] +
                                           image_copy[height - 1][width - 2].rgbtBlue * Gx[1][0] +
                                           image_copy[height - 2][width - 1].rgbtBlue * Gx[0][1] +
                                           image_copy[height - 2][width - 2].rgbtBlue * Gx[0][0];
                    blue_pixel_average_y = image_copy[height - 1][width - 1].rgbtBlue * Gy[1][1] +
                                           image_copy[height - 1][width - 2].rgbtBlue * Gy[1][0] +
                                           image_copy[height - 2][width - 1].rgbtBlue * Gy[0][1] +
                                           image_copy[height - 2][width - 2].rgbtBlue * Gy[0][0];

                    green_pixel_average_x = image_copy[height - 1][width - 1].rgbtGreen * Gx[1][1] +
                                            image_copy[height - 1][width - 2].rgbtGreen * Gx[1][0] +
                                            image_copy[height - 2][width - 1].rgbtGreen * Gx[0][1] +
                                            image_copy[height - 2][width - 2].rgbtGreen * Gx[0][0];
                    green_pixel_average_y = image_copy[height - 1][width - 1].rgbtGreen * Gy[1][1] +
                                            image_copy[height - 1][width - 2].rgbtGreen * Gy[1][0] +
                                            image_copy[height - 2][width - 1].rgbtGreen * Gy[0][1] +
                                            image_copy[height - 2][width - 2].rgbtGreen * Gy[0][0];

                    red_pixel_average_x = image_copy[height - 1][width - 1].rgbtRed * Gx[1][1] +
                                          image_copy[height - 1][width - 2].rgbtRed * Gx[1][0] +
                                          image_copy[height - 2][width - 1].rgbtRed * Gx[0][1] +
                                          image_copy[height - 2][width - 2].rgbtRed * Gx[0][0];
                    red_pixel_average_y = image_copy[height - 1][width - 1].rgbtRed * Gy[1][1] +
                                          image_copy[height - 1][width - 2].rgbtRed * Gy[1][0] +
                                          image_copy[height - 2][width - 1].rgbtRed * Gy[0][1] +
                                          image_copy[height - 2][width - 2].rgbtRed * Gy[0][0];
                } // Bottom Right Corner

                // Bottom Line
                else
                {
                    blue_pixel_average_x = image_copy[height - 1][j].rgbtBlue * Gx[1][1] +
                                           image_copy[height - 1][j - 1].rgbtBlue * Gx[1][0] +
                                           image_copy[height - 1][j + 1].rgbtBlue * Gx[1][2] +
                                           image_copy[height - 2][j - 1].rgbtBlue * Gx[0][0] +
                                           image_copy[height - 2][j].rgbtBlue * Gx[0][1] +
                                           image_copy[height - 2][j + 1].rgbtBlue * Gx[0][2];
                    blue_pixel_average_y = image_copy[height - 1][j].rgbtBlue * Gy[1][1] +
                                           image_copy[height - 1][j - 1].rgbtBlue * Gy[1][0] +
                                           image_copy[height - 1][j + 1].rgbtBlue * Gy[1][2] +
                                           image_copy[height - 2][j - 1].rgbtBlue * Gy[0][0] +
                                           image_copy[height - 2][j].rgbtBlue * Gy[0][1] +
                                           image_copy[height - 2][j + 1].rgbtBlue * Gy[0][2];

                    green_pixel_average_x = image_copy[height - 1][j].rgbtGreen * Gx[1][1] +
                                            image_copy[height - 1][j - 1].rgbtGreen * Gx[1][0] +
                                            image_copy[height - 1][j + 1].rgbtGreen * Gx[1][2] +
                                            image_copy[height - 2][j - 1].rgbtGreen * Gx[0][0] +
                                            image_copy[height - 2][j].rgbtGreen * Gx[0][1] +
                                            image_copy[height - 2][j + 1].rgbtGreen * Gx[0][2];
                    green_pixel_average_y = image_copy[height - 1][j].rgbtGreen * Gy[1][1] +
                                            image_copy[height - 1][j - 1].rgbtGreen * Gy[1][0] +
                                            image_copy[height - 1][j + 1].rgbtGreen * Gy[1][2] +
                                            image_copy[height - 2][j - 1].rgbtGreen * Gy[0][0] +
                                            image_copy[height - 2][j].rgbtGreen * Gy[0][1] +
                                            image_copy[height - 2][j + 1].rgbtGreen * Gy[0][2];

                    red_pixel_average_x = image_copy[height - 1][j].rgbtRed * Gx[1][1] +
                                          image_copy[height - 1][j - 1].rgbtRed * Gx[1][0] +
                                          image_copy[height - 1][j + 1].rgbtRed * Gx[1][2] +
                                          image_copy[height - 2][j - 1].rgbtRed * Gx[0][0] +
                                          image_copy[height - 2][j].rgbtRed * Gx[0][1] +
                                          image_copy[height - 2][j + 1].rgbtRed * Gx[0][2];
                    red_pixel_average_y = image_copy[height - 1][j].rgbtRed * Gy[1][1] +
                                          image_copy[height - 1][j - 1].rgbtRed * Gy[1][0] +
                                          image_copy[height - 1][j + 1].rgbtRed * Gy[1][2] +
                                          image_copy[height - 2][j - 1].rgbtRed * Gy[0][0] +
                                          image_copy[height - 2][j].rgbtRed * Gy[0][1] +
                                          image_copy[height - 2][j + 1].rgbtRed * Gy[0][2];
                } // Bottom Line
                blue_module =
                    round(sqrt((pow(blue_pixel_average_x, 2) + pow(blue_pixel_average_y, 2))));
                green_module =
                    round(sqrt((pow(green_pixel_average_x, 2) + pow(green_pixel_average_y, 2))));
                red_module =
                    round(sqrt((pow(red_pixel_average_x, 2) + pow(red_pixel_average_y, 2))));

                if (blue_module > 255)
                {
                    image[i][j].rgbtBlue = 255;
                }
                else
                {
                    image[i][j].rgbtBlue = blue_module;
                }
                if (green_module > 255)
                {
                    image[i][j].rgbtGreen = 255;
                }
                else
                {
                    image[i][j].rgbtGreen = green_module;
                }
                if (red_module > 255)
                {
                    image[i][j].rgbtRed = 255;
                }
                else
                {
                    image[i][j].rgbtRed = red_module;
                }
            } // i == (height - 1) -> Bottom Line

        } // for j
    } // for i
    return;
} // void
