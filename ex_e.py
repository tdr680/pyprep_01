
# TODO 1 Calculating the Factors of an Integer
#        When a nonzero integer, a, divides another integer, b, leaving a remainder 0, a is said to be a factor of b
#        As an example, 2 is a factor of all even integers hence e.g. is_factor(2, 8) should return True


# TODO 2 Using is_factor function write another function print_factors(n) which prints for n = 20
#      2 is a factor of 20
#      4 is a factor of 20
#      5 is a factor of 20
#      10 is a factor of 20


# TODO 3 Write function leap_year(year) which returns boolean according to following rules:
#        if (year is not divisible by 4) then (it is a common year)
#        else if (year is not divisible by 100) then (it is a leap year)
#        else if (year is not divisible by 400) then (it is a common year)
#        else (it is a leap year)


# TODO 4 Using previous function prints the leap years years between 2000 and 2050


# TODO 5 Following dictionary uses as a key upper case character and as the value morse code.
#        Write function to_morse(str) having as a parameter arbitrary string containing characters and returns
#        morse code of the argument. E.g. to_morse("Hello world") returns: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

MORSE = {'A': '.-',     'B': '-...',   'C': '-.-.',
         'D': '-..',    'E': '.',      'F': '..-.',
         'G': '--.',    'H': '....',   'I': '..',
         'J': '.---',   'K': '-.-',    'L': '.-..',
         'M': '--',     'N': '-.',     'O': '---',
         'P': '.--.',   'Q': '--.-',   'R': '.-.',
         'S': '...',    'T': '-',      'U': '..-',
         'V': '...-',   'W': '.--',    'X': '-..-',
         'Y': '-.--',   'Z': '--..',   ' ': '/'
         }


# TODO 6 Extend MORSE dictionary to include numbers and try to_morse("Anno 2070")
#   1    .----
#   2    ..---
#   3    ...--
#   4    ....-
#   5    .....
#   6    -....
#   7    --...
#   8    ---..
#   9    ----.
#   0    -----


# TODO 7 Write class Character having three attributes: name, race, faction and create objects:
#        player_1 = Character("Gringo", "Dwarf", "Alliance")
#        player_2 = Character("Balath", "Orc", "Horde")


# TODO 8 Implement __str__ for Character class that print player_1 outputs:
#        Player  Gringo
#        Race    Dwarf
#        Faction Alliance


# TODO 9 Modify constructor to initiate one more attribute: talent - dictionary that describes charater's staticstic.
#        player_1 = Character("Gringo", "Dwarf", "Alliance",
#                            {"strength" : 3, "dexterity" : 8, "intelligence" : 10, "health" : 10})
#        player_2 = Character("Balath", "Orc", "Horde",
#                            {"strength": 10, "dexterity": 5, "intelligence": 3, "health": 10})


# TODO 10 Improve __str__ for Character class that print player_1 outputs its statistic too:
#        Player  Gringo
#        Race    Dwarf
#        Faction Alliance
#        S/D/I/H 3/8/10/10

