#include <stdio.h>

int main()
{
    char arr[26] = {0};
    char charMap[26][1] = {0};    
    char charCnt = 0;

    scanf("%s", arr);

    for(int i=0; i<26; ++i)
    {
        char currChar = (arr[i] | 32) - 'a';
        
        if(charMap[currChar][0] == 1)
        {
            printf("FALSE");
            break;
        }
        else
        {
            charMap[currChar][0] = 1;
            ++charCnt;
        }
    }

    if(charCnt == 26)
    {
        printf("TRUE");
    }
}
