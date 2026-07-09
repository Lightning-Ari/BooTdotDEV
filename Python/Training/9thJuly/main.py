from typing import Any

class ListExercise:
    def __init__(self, name: str) -> None:
        self._list_name = name
        self.list: list[Any] = []

    def list_name(self) -> str :
        return self._list_name
    
    def show_list(self) -> None:
        for i in range(len(self.list)):
            print(self.list[i])

    def show_all_item(self) -> list[Any]:
        return self.list
    
    def add_item(self, item: Any) -> None:
        self.list.append(item)

    def check_element(self, position: int) -> Any:
        return self.list[position -1]
    
    def len_list(self) -> int:
        return len(self.list)
    
    def is_empty(self) -> str:
        if len(self.list) <=0 :
            result = "The list is empty"
            return result
        else :
            return "Not Empty"



new_list = ListExercise("new_list")

# Test adding items to verify the loop works

while True:
    print("To add Item to the list please select small a")
    print("Show list all item like array please select Cap R")
    print("Show item by item select cap A")
    print("check a element of the list select e")
    print("Show the length of list L")
    print("Quite the code select small q")

    # taking user input
    user_input = input()
    
    #Close the code with "q"
    if user_input == "q":
        print("Closing")
        break

    #To add item to the list

    if user_input == "a":
        item_input = input("Please enter the item: ")
        new_list.add_item(item_input)

    #To check all iteam array view

    if user_input == "R":
        print(new_list.show_all_item())
    
    #To check all item
    if user_input == "A":
        print()
        print()
        new_list.show_list()

    #To check element of the list
    if user_input == "e":
        item_input = int(input("Please enter the position of the element: "))
        result = new_list.check_element(item_input)
        print(f"Access {item_input} of the list: {result}")

    #To check the lingth
    if user_input == "L":
        result = new_list.len_list()
        print(f"Length of the list: {result}")

    print()
    print()
    print()


    






