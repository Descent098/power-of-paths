
# Schema limits
# <VEHICLE INDICATOR>-<RELATIVE LOATION INDICATOR>
# Vehicle indicator: [SC, AC, RC]<number> Shipping cargo, airplane cargo, road cargo
## The first part of the vehicle indicator tells you the vehicle type, then the number afterwards is the ID of the specific vehicle
# Relative Location Indicator (ship specific): Zone [A-Z]<number>-<package number> (26 zones) and then number for which container in that zone
## This changes based on the vehicle type, on a plane it would be different than a car (1 number for package number on each) etc.



# Lookup to find the order: b0bb789b-26a4-4d3a-b4b2-64639c92c8e7
# delimiter to represent the ship/region: SC224-D34-115 (SC224 for ship container [since planes/vans exist] and D is the zone on the ship)
# Cells for container in Zones: D34-115 (D34 is a cell representation of which container (zone D container 34, item 115))
