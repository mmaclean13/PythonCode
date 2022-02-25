#Enter package weight below
weight = 41.5

#Ground Shipping

if weight <= 2:
  ground_cost = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  ground_cost = weight * 3 + 20
elif weight > 6 and weight <= 10:
  ground_cost = weight * 4 + 20
if weight > 10:
  ground_cost = weight * 4.75 + 20
print ("Ground Shipping $ ",ground_cost)

#Ground Shipping Premium

premium_ground_cost = 125.00
print("Ground Shipping Premium $ ",premium_ground_cost)

#Drone Shipping

if weight <= 2:
  drone_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12
if weight > 10:
  drone_cost = weight * 14.25
print ("Drone Shipping $ ",drone_cost)
