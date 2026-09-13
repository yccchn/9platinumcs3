# Class Relationships: Association and Multiplicity

## Previous Work
[Part I - Classes and Objects](classObjectUML.md)

[Part II - Class Attributes and Methods](classAttributesMethods.md)

## Existing Class
Class: MissingYourEx
Description: This class represents a person who still misses their former partner and the different actions they do because they miss their ex.

## New Related Class
Class: MovingOnFromEx
Description: This class represents the process of moving on from a former partner and the different situations connected to that process.

## Association
Relationship: MovingOnFromEx HAS-A MissingYourEx.
Explanation: A MovingOnFromEx object can contain and manage MissingYourEx objects. It keeps track of different situations where someone still misses their former partner while moving forward.

## Multiplicity
Multiplicity: MovingOnFromEx 1 ───────── 0..* MissingYourEx
Explanation: It is one-to-many because one MovingOnFromEx object can contain zero or more MissingYourEx objects. A person can have different situations where they miss their former partner while they are trying to move on.

## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)

## Python Implementation
[View Python Source](classRelationships.py)

## Test Run
![Relationship Test Run](images/relationshipTestRun.png) ![alt text](image-3.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png) ![alt text](image-2.png)

## Analysis

### What is the association between your two classes?
The association between my two classes is that MovingOnFromEx has and manages MissingYourEx objects. The MovingOnFromEx class keeps track of different situations where someone still misses their former partner.
### What multiplicity did you choose and why?
I chose one-to-many multiplicity because one MovingOnFromEx object can have zero or more MissingYourEx objects. This represents how a person can experience different situations where they miss their former partner while trying to move forward.
### How did you implement the relationship in Python?
I implemented the relationship by creating a list called missing_exes inside the MovingOnFromEx class. I used the add_missing_ex() method to add MissingYourEx objects to the list. This allows one MovingOnFromEx object to manage multiple related objects.
### Why did you store an object reference instead of copying its data?
I stored an object reference instead of copying its data so that the relationship connects the actual objects. This also prevents duplicate data and allows the MovingOnFromEx object to access the information of each MissingYourEx object.
### If your relationship uses many, why is a list appropriate?
A list is appropriate because one MovingOnFromEx object can be connected to many MissingYourEx objects. The list stores the actual object references, allowing each related object to be accessed through the relationship.