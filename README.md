# strings68 an experimental compiler language

program.txt:

# comment
string 1;
string 2;

1 = "@@@ SOFIA IS GEWELDIG";
2 = test;
2 = 1;
print 2;

if (1 == 2)
    print "1 == 2";
endif

loop
    shiftl 2;
    print 2;
    if (2 == "DIG")
        break;
    endif
endloop


output:

[reinold@fedora stringsan]$ ./strings68 -fprogram.txt
@@@ SOFIA IS GEWELDIG
"1 == 2"
@@ SOFIA IS GEWELDIG
@ SOFIA IS GEWELDIG
 SOFIA IS GEWELDIG
SOFIA IS GEWELDIG
OFIA IS GEWELDIG
FIA IS GEWELDIG
IA IS GEWELDIG
A IS GEWELDIG
 IS GEWELDIG
IS GEWELDIG
S GEWELDIG
 GEWELDIG
GEWELDIG
EWELDIG
WELDIG
ELDIG
LDIG
DIG
[reinold@fedora stringsan]$ 
