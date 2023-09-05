# This file defines the classes used in the shipping system
from __future__ import annotations
import string
from datetime import datetime
from typing import Dict, List, ClassVar
from dataclasses import dataclass, field

MAX_CONTAINERS_PER_ZONE = 35 # Number of containers per zone on a ship

@dataclass
class Package:
    tracking_number:str
    internal_location_identifier: str

@dataclass
class Order:
    tracking_number:str
    packages:List[Package]
    ETA: datetime # The number of hours left estimated to deliver an order
    orders:ClassVar[Dict[str, Order]] = dict() # list of all Orders that have been instantiated
    
    def __post_init__(self):
        Order.orders[self.tracking_number] = self
    
    @property
    def ETA(self): # Updates the order ETA to match the ship eta when accessing it
        ship_identifier = self.packages[0].internal_location_identifier.split("-")[0]
        ship_number = int(ship_identifier.replace("SC", ""))
        
        for ship in Ship.ships:
            if ship_number == ship.vid:
                if not self._ETA == ship.ETA:
                    self._ETA = ship.ETA
        return self._ETA
    
    @ETA.setter
    def ETA(self, value):
        self._ETA = value

@dataclass
class VehicleType: # A base class other vehicle types can inherit from
    vid: int # The ID of the specific vehicle
    indicator: str # Will be set for each type (i.e. SC for ship, AC for airplane)
    orders: Dict[str, Order] = field(default_factory=lambda: dict()) # A dictionary with all the orders on a vehicle
    
    
@dataclass
class Container:
    container_id:int
    items: List[Package] = field(default_factory=lambda: [])

@dataclass
class Ship(VehicleType):
    ETA: datetime = datetime(datetime.now().year, datetime.now().month, datetime.now().day + 3) # The number of hours left estimated to deliver an order (default 3 days)
    ships:ClassVar[List[Ship]] = [] # list of all ships that have been instantiated
    indicator:str = "SC"
    zones: Dict[str, List[Container]] = field(default_factory=lambda: {letter: [Container(index) for index in range(1, MAX_CONTAINERS_PER_ZONE+1)] for letter in string.ascii_uppercase})

    def __post_init__(self):
        Ship.ships.append(self) # Add new ship to Ship.ships
