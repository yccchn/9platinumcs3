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
![Relationship Test Run](images/relationshipTestRun.png)

## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)

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
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: MissingYourEx
Description: This class represents a person who still misses their former partner and the different actions they do because they miss their ex.
## New Related Class
Class: MovingOnFromEx
Description: This class represents a person who finally decided to move on from their former partner, and the different actions they take to heal from the past.
## Association
Relationship: Moving from your ex includes missing your ex but choosing to move forward and heal.
Explanation: The process of moving on from your ex includes missing them but choosing not to get back together. 
## Multiplicity

Multiplicity: MovingOnFromEx ───────── 
Explanation: It is one to many because you can still move on from your ex and miss them at the same time. You can also move on and not miss them. These examples show that there are different situations a person can be in when they are in the process of moving on from their ex.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
The association between my two classes is that missing your ex is part of moving on.
### What multiplicity did you choose and why?
I chose the one to many multiplicity. This is because when you are moving on from your ex you can both miss and not miss them. It could also be that you do not miss the person in general, but rather the memories and momens you have shared with them. 
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
I stored the object reference instead of copying its data so that I can refer to it on future usage, making my work much more easier and organized.
### If your relationship uses many, why is a list appropriate?
If my relationship uses many, a list is appropriate as it can help me organize, store, and find the data more efficiently. 
