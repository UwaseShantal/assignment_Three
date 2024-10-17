#1combine cities
cty1="Kampala"
cty2="Entebbe"

print(f"{cty1}{cty2}")

#2length string
string="Uganda Martyrs University"
print(len(string))

#3convert to uppercase
Str1="Kampala is the capital city of Uganda"
print(Str1.upper())

#4convert to lower case
str="The source of the Nile"
print(Str1.lower())

#5find substring
str_2="The Nile river is the longest river in the world"
sub="Nile"
print(str.find(sub))
if(str.find(sub)==-1):
    print("Not found")
else:
    print("Found")    

#6replace substring
str_3="The Nile river is the longest river in the world"
sub="Nile"
new="Victoria"
print(str_3.replace(sub,new,1))

#7length of string
word="Ugandan Matooke"
print(len(word))

#8dividing students into groups
total=45
qou=total//6
rem=total%6
print(f"The remaining students without a group will be {rem}")

#9 cost of buying maize
maize=2500
kilos=10
cost=maize*kilos
if cost>20000:
    print("The cost of buying maize will be more than UGX 20000")
else:
     print("The cost of buying maize will be less than UGX 20000")   

#10 Shop selling fruits
apples=1000
total_apples=apples*5
bananas=200
total_bananas=bananas*10
mangoes=1500
total_mangoes=mangoes*3
print(f"The total cost of the fruits is {total_apples+total_bananas+total_mangoes}")    