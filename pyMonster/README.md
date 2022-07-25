Damage Equation

Damage = ((((((2 x Level x Critical) / 5) + 2) x Power x A/D) / 50) + 2) x STAB x Type1 x Type2 x random

Level is attacker's level
Critical is 2 for critical hit and 1 otherwise
A is attack for attacker (either physical or special based on attack)
D is defense for defender (either physical or special base don attack)
Power is the power of the used move
STAB is Same Type Attack Bonus, 1.5 if move type matches type 1 or type 2 of attacker, 1 otherwise. 
Type 1 / Type 2 are for the type effectiveness of the used move based on target type: 0.5 for not effective, 1 normal, and 2 for super Effective. Type 2 is 1 if None type
random is a random integer from 217 to 255 divided by 255. (between .85 to 1)

Stats

Each monster should have HP, Attack, Defense, Special, SPeed, Evasion, Accuracy

Four Individual Values (IV) are stored: Attack, Defense, Speed, and Special. range from 0-15 in binary. HP is set with the final digit of the binary for those states in that order.

HP = ((((Base + DV) * 2 + (sqrt(STATEXP) / 4)) * Level) / 100) + Level + 10
OtherStat = ((((Base + DV) * 2 + (sqrt(STATEXP) / 4)) * Level) / 100) + 5

Data Structure
0x00 - index number - byte
0x01 - Base HP - byte
0x02 - Base Atk - byte
0x03 - Base Def - byte
0x04 - Base Speed - byte
0x05 - Base Spec - byte
0x06 - Type 1 - byte
0x07 - Type 2 - byte
0x08 - Catch Rate - byte
0x09 - Base Exp Yield - byte
0x0A - Dim of Front Sprite - byte
0x0B - Point to front sprite - word
0x0D - Point to back sprite - word
0x0F-0x12 - Attacks known at Lv 1 - 4 bytes
0x13 - Growth Rate - byte
0x14-0x1A - TM and HM Flags - 7 bytes
0x1B - Padding - byte

index     01 
Base HP   2D 
Base Atk  31 
Base Def  31 
Base Spd  2D 
Base Spc  41 
Type 1    16 
Type 2    03 
Ctch Rate 2D 
Base Exp  40 
Dim Sprt  55 
Pnt FntS  00 40
Pnt BckS  E5 40 
Attk 1    21 
Attk 2    2D 
Attk 3    00 
Attk 4    00 
Exp Rate  03 
TM/HM 1   A4 
TM/HM 2   03 
TM/HM 3   38 
TM/HM 4   C0 
TM/HM 5   03 
TM/HM 6   08 
TM/HM 7   06 
Padding   00  // BULBASAUR

TYPES
00 Normal 01 Fighting 02 Flying 03 Poison 04 Ground 05 Rock 06 Bird 07 Bug
08 Ghost 09-13 blank 14 Fire 15 Water 16 Grass 17 Electric 18 Psychic 19 Ice
1A Dragon

GROWTH RATE
00 Medium Fast   03 Medium Slow   04 Fast   05 Slow

CAPTURE METHOD
1. Master Ball = Caught
2. Generate random number, N
  Poke Ball: 0-255
  Great Ball: 0-200
  Otherwise: 0-150
3. Caught if asleep/frozen and N < 25 or paralyzed/burned/poisoned and N < 12
4. if N minus status threshold > catch rate, breaks free
5. generate random number M between 0-255
6. Calculate f:
  f = [(HPmax x 255 x 4) / (HPcurrent x Ball)] ... Ball = 8 (for Great ball) or 12 (all others)
7. If f >= M = CAUGHT else break free
--- Ball Shake --- 
  1. Calculate d:
    d = [(catchRate x 100) / Ball] ... Ball = 255 (pokeball), 200 (great ball), or 150 (all others)
  2. if d >= 256, shake 3 times then release
  3. else, calculate x
    x = [(d x f) / 255] + s ... where s is 10 if asleep/frozen, 5 if paralyzed/poisoned/burned else 0
  4. If:
    x < 10, miss
    x < 30, shake once
    x < 70, shake twice
    all others, shake thrice