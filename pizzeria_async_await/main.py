import asyncio
from random import randint

class Pizzeria:
    def __init__(self, name: str):
        self.name = name
        self.pizza_menu = {
            1: "Four Cheese Pizza",
            2: "Pepperoni Pizza",
            3: "Margherita Pizza",
            4: "Hawaiian Pizza",
            5: "Vegetarian Pizza"
        }

    async def make_pizza(self, order_id):
        cook_time = randint(2, 5)
        pizza_name = self.pizza_menu[randint(1, 5)]
        print(f'Pizzeria: {self.name} start cook pizza {pizza_name}! order_id: {order_id}')
        await asyncio.sleep(cook_time)
        print(f'Pizzeria: {self.name} finished cook pizza {pizza_name}! order_id: {order_id}')
        return pizza_name


async def main():
    pizzeria = Pizzeria('Pizzeria D&M')
    tasks = [pizzeria.make_pizza(pizza_num) for pizza_num in range(1, 11)]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
