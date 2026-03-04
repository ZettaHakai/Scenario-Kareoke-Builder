These Python files basically takes any string of CTR and PCT from Scenario.h 
and gives you a karaoke array based on your base file.
I personally run files in pycharm, edit .c with VS 
Text maker folder is used for generating your text array
You can then take this given array, and use it in window maker to autogenerate windows
Generated scenario windows will have a default wait value you set at the top

Notes about text maker

It does ignore spaces, but also ignores punctuation, you may need to adjust the yellow accordingly
It does not, give you a "blank" Line first, you want to retain your input as your "start".
Make sure you change the ID on the bottom, and then run the py file.
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


Notes about Ze timing thing

You put your original scenario window timing file (what you would use in original mod, example below), in windows.c

   // ======================================================
   // Akiramenaide
   // ======================================================

   TXT, (s32)&scenario_text_0074,
   TXT, (s32)&scenario_text_0004,
   TXT, (s32)&scenario_text_0202,

   STW, (s32)&D_801C7740_1C8340, WTS, 0xB4,
   ESR, (s32)&func_8003F460_40060,

   // ======================================================
   // Kuchibue fuki saa aruki-dasou yo
   // dump wait = 0xF0
   // ======================================================

   TXT, (s32)&scenario_text_0074,
   TXT, (s32)&scenario_text_0004,
   TXT, (s32)&scenario_text_0204,

   STW, (s32)&D_801C7740_1C8340, WTS, 0xD0,
   ESR, (s32)&func_8003F460_40060,

   // ====================================


You put your Created Karaoke window file, in Secnario_text.c (example below)

 
TXT, (s32)&scenario_text_0074, TXT, (s32)&scenario_text_0004, TXT, (s32)&scenario_text_1500, STW, (s32)&D_801C7740_1C8340, WTS, 0xD, ESR, (s32)&func_8003F460_40060,

this usually repeats for every letter of every word. 18 words can become 320 scenario files.

It will approximate the timings from the first file, and apply them to your default file. Really, only useful if you want to convert your original timings approximately, or manually adjust from a default speed. 

It dumps the text into  scenario_adjusted.c 
---------------------------------------------------------------------------
Useful for a niche, Scenario. haha. hahaha.
~zetta