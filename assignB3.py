print("_________MENU_________")
print("1.Insert new item in the list")
print("2.Count the occurance of an item in the list")
print("3.Sort the list")
print("4.Reverse the list")
print("5.Extend the list")
print("6 Remove specific item from the list")
print("7.Exit")

#create a list called cities
cities=["Delhi","Pune","Bengluru","Delhi","Chennai","Mumbai"]
print(cities)
while(True):
    choice=int(input("Enter your choice"))
    if choice==1:
        pos = int(input("enter the position to insert items into the list"))
        necity = input("enter the city name")
        cities.insert(pos.newcity)
        print("list after inserting new city is \n",cities)
    elif choice==2:
        print("No. of times delhi is present is ",cities.count('Delhi'))
    elif choice==3:
        cities.sort()
        print("list after sorting is \n",cities)
    elif choice==4:
        cities.reverse()
        print("list after reversing is \n",cities)
    elif choice==5:
        more_cities=["jaipur","Kholapur"]
        cities.extend(more.cities)
        print("list after adding more cities is \n",cities)
    elif choice==6:
        cityname=input("Enter the city name to remove")
        cities.remove(cityname)
        print("list after removing",cityname,"is \n",cities)
    elif choice==7:
        Exit()
    else:
        print("Invalid choice")
