#!/usr/bin/python3



class Ordine:

	def __init__(self,purchase_list):
		self.id = purchase_list[0]
		self.costo = purchase_list[1]
		self.tempo = purchase_list[2]
		self.tempo_massimo = purchase_list[3]
		self.ricavo = purchase_list[4]

	def __str__(self):
		return ""+ str(self.id) + " " + str(self.costo) + " " + str(self.tempo) + " " + str(self.tempo_massimo) + " " + str(self.ricavo) 


class Ship:
	def __init__(self,id_):
		self.id = id_
		self.list_of_order = []
		self.time_enlapsed = 0

	def add_order(self,order):
		self.list_of_order.append(order)
		self.time_enlapsed += order.tempo






def maximizeProfit(number_of_ship,number_of_purchase,initial_budget,orders):

	#ordering based on the maximum time
	orders = sorted(orders, key=lambda x: (x.tempo_massimo, x.tempo_massimo - x.tempo))

	ships = [Ship(i) for i in range(0,number_of_ship) ]

	out_file = open("out.txt","w")
	for order in orders:
		min_ship = min(ships,key=lambda x: x.time_enlapsed)

		out_file.write("" + str(min_ship.id) + " " + str(order.id) + "\n")

		start_time = min_ship.time_enlapsed
		min_ship.add_order(order)

		initial_budget += order.ricavo
		initial_budget -= order.costo

		if min_ship.time_enlapsed > order.tempo_massimo:
			initial_budget -= ( min_ship.time_enlapsed - order.tempo_massimo)

		print(initial_budget)







if __name__ == "__main__":
	file = open("input","r")

	first_line = list(map(int,file.readline().rstrip().lstrip().split(" ")))

	number_of_ship = first_line[0]
	number_of_purchase = first_line[1]
	initial_budget = first_line[2]

	orders = []

	i = 0
	#read all the orders
	while i < number_of_purchase:
		actual_order_line = file.readline()
		
		order_line = list(map(int,actual_order_line.rstrip().lstrip().split(" ")))
		
		order = Ordine(order_line)
		orders.append(order)
		i += 1

	maximizeProfit(number_of_ship,number_of_purchase,initial_budget,orders)







		




