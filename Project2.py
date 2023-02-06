import math
print("This is a program which determine magnitude of force acting between the masses.")
###If you put 50 for the first mass, 100 for the second and 200 for the distance my answer should be 8.3407375×10−12####

###The formula of Gravity is G*x1*x2/r,2, G-represents the accerelation###
        ### of gravity,r- the distance and X1 and x2 the mass.###

print("The first number, which represents the accerelation is 6.67258 * 10^11.")
accerelation_of_gravity=float(6.67259 * pow(10,-11))
print("The second number, which represents the first mass.")
mass_1=float(input())
print("The second mass.")
mass_2=float(input())
print("and the distance.")
distance=float(input())


### The first step is to get the numbers###
### The second step is to put the numbers by their place in the formula###
### To calculate r(distance) you need to put (pow) which will square the distance just like in the formula, or multiply r*r###
### And the last step is store all of the information in variable called result###


gravitation_formula_force=(accerelation_of_gravity)*(mass_1*mass_2)/pow(distance,2)
print("The result is:)")
result=print(gravitation_formula_force)