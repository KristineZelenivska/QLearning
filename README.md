# QLearning

Task from udemy course "Artificial Intelligence A-Z 2024: Build 7 AI + LLM & ChatGPT"

A Q-Learning Implementation for Process Optimization
The problem to solve will be to optimize the flows inside the warehouse.
The warehouse belongs to an online retail company that sells products to a variety of customers. Inside this
warehouse, the products are stored in 12 different locations, labeled by the following letters from A to L.
[ A B C D
E F G H
I J K L]
As the orders are placed by the customers online, an Autonomous Warehouse Robot is moving around the
warehouse to collect the products for future deliveries. The 12 locations are all connected to a computer system, which is ranking in real time the priorities of
product collection for these 12 locations
Location G has priority 1, which means it is the top priority, as it contains a product that must be collected
and delivered immediately. Our Autonomous Warehouse Robot must move to location G by the shortest
route depending on where it is.
Our goal is to build an AI that will return that shortest route, wherever the
robot is. But then, locations K and L are in the Top 3 priorities. Hence we will want to implement
an option for our Autonomous Warehouse Robot to go by some intermediary locations before reaching its
final top priority location.
