from uuid import uuid4
from typing import List
from random import randint
from datetime import datetime

from classes import Package, Order, Ship

def generate_random_order() -> Order:
    """Generates a completely random order

    Returns
    -------
    Order
        The randomly generated Order
    """
    tracking_number = str(uuid4())
    ship_number = randint(1, 250)
    zone_number = randint(1, 35)
    zone_letter = chr(randint(65, 65+25)) # Letter from A-Z
    item_number = randint(1, 120)
    days_to_delivery = randint(0,10)
    
    return Order(tracking_number, 
        packages =[ 
            Package(tracking_number, f"SC{ship_number}-{zone_letter}{zone_number}-{item_number+index}") 
            for index in range(randint(1, 10))
        ],
        ETA = datetime(datetime.now().year, datetime.now().month, datetime.now().day + days_to_delivery) # in 0-10 days
    )


def generate_order(item_starting_number:int = 0, number_of_items:int=10, zone_letter:str = "A", zone_number: int = 1, ship_number:int = 1):
    tracking_number = str(uuid4())
    days_to_delivery = randint(0,10)
    
    return Order(tracking_number, 
        packages =[ 
            Package(tracking_number, f"SC{ship_number}-{zone_letter}{zone_number}-{item_starting_number+index}") 
            for index in range(number_of_items)
        ],
        ETA = datetime(datetime.now().year, datetime.now().month, datetime.now().day + days_to_delivery) # in 0-10 days
    )        
        
def generate_ship(vid:int) -> Ship:
    """Creates a full Ship with random contents

    Parameters
    ----------
    vid : int
        The ID of the ship

    Notes
    -----
    - A full ship is 26 Zones ("A"-"Z") with 35 containers (1-35) per zone and 120 items per container, so 109,200 items per ship

    Returns
    -------
    Ship
        The full Ship
    """
    s = Ship(vid)
    for zone_letter in s.zones:
        for container in s.zones[zone_letter]:
            item_number = 0
            for _ in range(12): # 120 total items
                o = generate_order(item_number, zone_letter=zone_letter, zone_number=container.container_id, ship_number=vid)
                container.items += o.packages
                item_number += 10                
    return s

def find_package(internal_identifier:str) -> List[Package]:
    
    # Parse internal_identifier into values
    print(f"Searching for item with identifier: {internal_identifier}")
    ship_id = int(internal_identifier.split("-")[0].replace("SC",""))
    zone_letter = internal_identifier.split("-")[1][0]
    zone_number = int(internal_identifier.split("-")[1][1:])
    item_number = int(internal_identifier.split("-")[2])
    print(f"Looking for item in\n\tShip: {ship_id}\n\tZone: {zone_letter}\n\tContainer: {zone_number}\n\tItem: {item_number}")
    # Find objects based on values
    package_ship = Ship.ships[ship_id-1]
    package_container = package_ship.zones[zone_letter][zone_number-1]
    
    # Return item
    return package_container.items[item_number]

def get_order_by_tracking_number(tracking_number:str) -> Order:
    return Order.orders[tracking_number]

def get_eta_by_tracking_number(tracking_number:str) -> datetime:
    return get_order_by_tracking_number(tracking_number).ETA

def get_internal_identifiers_by_tracking_number(tracking_number:str) ->List[str]:
    return [item.internal_location_identifier for item in get_order_by_tracking_number(tracking_number).packages]

def get_ship_by_tracking_number(tracking_number:str) -> Ship:
    package = get_order_by_tracking_number(tracking_number).packages[0]
    ship_id = int(package.internal_location_identifier.split("-")[0].replace("SC",""))
    return Ship.ships[ship_id-1]

