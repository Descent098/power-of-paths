from datetime import datetime

from utility_functions import *
from classes import Ship, Package, Order

# Schema limits
# <VEHICLE INDICATOR>-<RELATIVE LOATION INDICATOR>
# Vehicle indicator: [SC, AC, RC]<number> Shipping cargo, airplane cargo, road cargo
## The first part of the vehicle indicator tells you the vehicle type, then the number afterwards is the ID of the specific vehicle
# Relative Location Indicator (ship specific): Zone [A-Z]<number>-<package number> (26 zones) and then number for which container in that zone
## This changes based on the vehicle type, on a plane it would be different than a car (1 number for package number on each) etc.


# Lookup to find the order: b0bb789b-26a4-4d3a-b4b2-64639c92c8e7
# delimiter to represent the ship/region: SC224-D34-115 (SC224 for ship container [since planes/vans exist] and D is the zone on the ship)
# Cells for container in Zones: D34-115 (D34 is a cell representation of which container (zone D container 34, item 115))

if __name__ == "__main__":
    print("Creating ships")
    for index in range(250):
        print(f"Creating ship {index}/250")
        generate_ship(index + 1)

    from pprint import pprint

    # Add in example order
    orders = {
    "b0bb789b-26a4-4d3a-b4b2-64639c92c8e7": Order("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7", 
        packages =[
            Package("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7", "SC224-D34-114"),
            Package("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7", "SC224-D34-115"),
        ],
        ETA = datetime(datetime.now().year, datetime.now().month, datetime.now().day + 3) # in 3 days
    ),
    }

    Ship.ships[223].zones["D"][33].items[114] = orders["b0bb789b-26a4-4d3a-b4b2-64639c92c8e7"].packages[0]
    Ship.ships[223].zones["D"][33].items[115] = orders["b0bb789b-26a4-4d3a-b4b2-64639c92c8e7"].packages[1]

    print(f'{orders["b0bb789b-26a4-4d3a-b4b2-64639c92c8e7"].packages[0]=}')
    print(f'{orders["b0bb789b-26a4-4d3a-b4b2-64639c92c8e7"].packages[1]=}')
    print(f'{find_package("SC224-D34-114")=}')
    print(f'{find_package("SC224-D34-115")=}')
    
    print(find_package("SC224-D34-114") == orders["b0bb789b-26a4-4d3a-b4b2-64639c92c8e7"].packages[0])
    print(find_package("SC224-D34-115") == orders["b0bb789b-26a4-4d3a-b4b2-64639c92c8e7"].packages[1])
    
    print(f'{get_order_by_tracking_number("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7")=}')
    print(f'{get_eta_by_tracking_number("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7")=}')
    print(f'{get_internal_identifiers_by_tracking_number("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7")=}')
    # print(f'{get_ship_by_tracking_number("b0bb789b-26a4-4d3a-b4b2-64639c92c8e7")=}')
    
    # Print example ship container
    # pprint(Ship.ships[224].zones["D"][33])