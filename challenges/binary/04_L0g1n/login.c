#include <stdio.h>
#include <stdlib.h>

int login()
{
    char password[48] = {0};
    printf("(password starts at address: %p)\n", password);

    printf("Please enter the admin password: ");
    fflush(stdout);

    gets(password);
    return 0; /* TODO implement proper authorization */
}

void admin_menu()
{
    printf("Welcome back, admin!\n");
    /* ... */
    exit(0);
}

int main(int argc, char const *argv[])
{
    int authorized = login();
    if (authorized)
    {
        admin_menu();
    }
    else
    {
        printf("Not authorized!\n");
    }
    return 0;
}
