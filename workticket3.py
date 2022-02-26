#Declare variables
st1 = "Animals"
st2 = "Badger"
st3 = "Honey Bee"
st4 = "Honey Badger"

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

sting1 = "Becomes"
sting2 = "becomes"
sting3 = "BEAR"
sting4 = " bEautiful"

#Replace whitespace
nospaces1 = string1.replace(" ", "")
nospaces2 = string2.replace(" ", "")
nospaces3 = string3.replace(" ", "")

#starts with method
w = sting1.startswith("be")
x = sting2.startswith("be")
y = sting3.startswith("be")
z = sting4.startswith("be")

#print outputs
print(st1.lower())
print(st2.lower())
print(st3.lower())
print(st4.lower())

print(st1.upper())
print(st2.upper())
print(st3.upper())
print(st4.upper())

print(nospaces1);
print(nospaces2);
print(nospaces3);

print(w);
print(x);
print(y);
print(z);
