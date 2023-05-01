#In this project, we build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

weight = 2.59

# Ground shippping

if weight > 10:
  cost_ground = weight * 4.75 + 20
elif weight > 6:
  cost_ground = weight * 4.00 + 20
elif weight > 2:
  cost_ground = weight * 3.005 + 20
else:
  cost_ground = weight * 1.50 + 20
print("Ground Shipping: $",cost_ground)

#Premium Shipping 
cost_ground_premium  = 125
print("Ground Shipping Premium: $",cost_ground_premium)

#Drone SHipping

if weight > 10:
  cost_Drone = weight * 14.25 
elif weight > 6:
  cost_Drone = weight * 12.00 
elif weight > 2:
  cost_Drone = weight * 9.00
else:
  cost_Drone = weight * 4.50
print("Drone Shipping: $",cost_Drone)