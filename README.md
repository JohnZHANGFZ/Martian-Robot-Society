# Martian-Robot-Society
Introduction
It is the year 3142. Robots have finally overtaken the world, and their society involves a very strict hierarchy where every robot knows their place in society. (Also, it should be noted that humans had obviously re-located to Mars by this time, so the planet which the robots have overtaken is Mars, not Earth.) Trees are a fundamental data structure used to model all sorts of hierarchical data. In this project, I will be modelling the organization of the Martian Robot Society using trees.

Every robot in the Martian Robot Society is considered a citizen of Mars. The nodes in our tree will each represent one citizen. Citizens all have subordinate-superior relationships, where one citizen may work under another. Additionally, some citizens are leaders of a specific district within the society. All citizens that work under a leader are considered part of that district.

Note that a district could be a geographical area, or just a domain of responsibility, like Finance.

Each node of the Martian Robot Society tree represents a citizen of this society. Each citizen will have its own set of characteristics:their citizen ID number, manufacturer (the name of which company manufactured this particular robot), model year, job, and their rating (kind of like a credit score; basically a measure of how good of a citizen they are, represented as an integer from 0 to 100).

Each citizen may have one superior and any number of subordinates.

There are 2 types of subordinate:

Direct subordinates: These are subordinates that work directly under another citizen. For example, Citizen ID: 2 is a direct subordinate of Citizen ID: 6.
Indirect subordinates: These are subordinates that do not work directly under another citizen. For example, being the subordinate of a subordinate. In our example above, Citizen ID: 7 is an indirect subordinate of Citizen ID: 6.

DistrictLeader class
DistrictLeader is a subclass of Citizen. While district leaders are fairly similar to a regular citizen, they also keep track of the district that they lead. All subordinates (both direct and indirect) are said to be part of (or "belong to") the district.

Society class
The Society class is responsible for keeping track of the head of the entire society (which is the root of the hierarchy), and providing operations that take the whole society into consideration. Most operations which involve accessing the citizens are done through the society class, such as adding a citizen to the society (when new robots are produced), removing one (when robots are deconstructed), or finding one with a specific citizen ID number.

The code is in three layers:
society_hierarchy.py: Defines classes that keep track of information about the Martian robot society.

society_ui.py: Defines a graphical user interface for interacting with information about the Martian robot society. Run this module to interact with the user interface.

client_code.py: A layer of code that is between the user interface and the "back end" defined in society_hierarchy.py. It uses the code in society_hierarchy.py to make the UI work.

citizens.csv: A sample file describing a robot society hierarchy.

a2_starter_tests.py: Some basic tests cases in order to test code.
