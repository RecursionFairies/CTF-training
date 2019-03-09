#include <stdio.h>

int main(int argc, char const *argv[])
{
    int auth_code = 0;
    char username[16] = {0};

    printf("Enter your username: ");
    fflush(stdout);
    scanf("%20s", username); /* Ouch! */

    if (auth_code == 0x1337)
    {
        printf("Welcome back, admin!\n");
        /* ... */
    }
    else
    {
        printf("Welcome back, %s!\n", username);
    }
    return 0;
}
