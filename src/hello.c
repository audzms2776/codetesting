#include <stdio.h>

int main()
{
    char arr[26] = {0};
    char charMap[26][1] = {0};    

    scanf("%s", arr);

    for(int i=0; i<26; ++i)
    {
        char currChar = (arr[i] | 32) - 'a';
        
        if(charMap[currChar][0] == 1)
        {
            printf("FALSE");
            return 0;
            break;
        }
        else
        {
            charMap[currChar][0] = 1;
        }
    }

    char flag = 0;

    for(int i=0; i<25; i++)
    {
        if(charMap[i][0] != 1)
        {
            printf("FALSE");
            flag = 1;
            break;
        }
    }

    if(flag == 0)
    {
        printf("TRUE");
    }
}
