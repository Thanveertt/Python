money=575
phone_cost=240
tablet_cost=260
total_cost=phone_cost+tablet_cost
can_afford_both=money>=total_cost
can_afford_phone=money>=phone_cost
if can_afford_both:
    message="You have enough money for both"
elif can_afford_phone:
    message = "You can afford phone "
print(message)
raspberry_pi=25
pies=3*raspberry_pi
total_cost=total_cost+pies
if total_cost<=money:
    message="You have enough money for 3 raspberry pies as well"
else:
    message="You can't afford 3 raspberry pies"
print(message)
