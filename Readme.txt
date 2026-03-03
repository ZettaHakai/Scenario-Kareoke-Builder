These Python files basically takes any string of CTR and PCT from Scenario.h 
and gives you a karaoke array based on your base file.
Text maker folder is used for generating your text array
You can then take this given array, and use it in window maker to autogenerate windows
Generated scenario windows will have a default wait value of 0x3

Notes about text maker

It does ignore spaces, but also ignores punctuation, you may need to adjust the yellow accourdingly
It does not, give you a "blank" Line first, you want to retain your input as your "start".
Make sure you change the ID on both top and bottom, and then run the py file.
This should dump text to scenario_arrays.c which you can then copy and use in window maker and your .c

notes about windows

 // Window setup
 STW,     0x801c77d8,          WTS, 0x64, //text speed. Sets to max. zoooooooom at 64 (100/100)
 STW, (s32)&D_801C7758_1C8358, WTS, 0x20, //x
 STW, (s32)&D_801C775C_1C835C, WTS, 0xAA, //y
 STW, (s32)&D_801C7768_1C8368, WTS, 0xB, //style 

The following numbers, ie 0000,0074, and 0004 can be changed, and are just what I use

static s16 scenario_text_0000[] = { CTR_BEGIN, CTR_ENDLINE }; - Start of text scenario past window setup
static s16 scenario_text_0074[] = { CTR_NEWWINDOW, CTR_ENDLINE }; - Start of window
static s16 scenario_text_0004[] = { PCT_SPACE, CTR_NEWLINE, CTR_ENDLINE }; - Endline/move down 1



You can chose your starting number for your scenario ID's at the top and bottom of text maker, 
insert your text at the bottom inside the Quote area, and it will give you karaoke array.


You then use this array in window maker, and it will give you your windows. 
Make sure you have declared the above variables at the top of your file as shown below


#include "scenario.h"
#include "common.h"
static s16 scenario_text_0000[] = { CTR_BEGIN, CTR_ENDLINE };  
static s16 scenario_text_0074[] = { CTR_NEWWINDOW, CTR_ENDLINE }; 
static s16 scenario_text_0004[] = { PCT_SPACE, CTR_NEWLINE, CTR_ENDLINE };
---------------------------------------------------------------------------
Useful for a niche, Scenario. haha. hahaha.
~zetta