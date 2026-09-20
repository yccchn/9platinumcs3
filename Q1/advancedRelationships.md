# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description:
## Inheritance Relationship
Parent: MissingYourEX
Child: MovingOnFromEx
Explanation: MovingOnFromEx is a more specific type of MissingYourEx because moving on can still involve missing a former partner. The MovingOnFromEx class can reuse the common attributes and methods of MissingYourEx while adding information related to the process of moving forward.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Composition
Explanation: MovingOnFromEx has a strong HAS-A relationship with HealingAction. A HealingAction represents an action that is part of the moving-on process. In this system, the HealingAction objects are created and managed by MovingOnFromEx, so they belong to the MovingOnFromEx object.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
### 1. Why did you choose your inheritance relationship?
I chose MovingOnFromEx as the child class of MissingYourEx because moving on can still involve missing a former partner. MovingOnFromEx can reuse the common attributes and methods from MissingYourEx. It can also have additional features that are specifically related to moving forward.
### 2. How did inheritance reduce duplicate code?
Inheritance allowed MovingOnFromEx to reuse the attributes and methods already written in MissingYourEx. This means I did not have to write the same code again in the child class. It makes the program shorter and easier to maintain.
### 3. Why is your HAS-A relationship Composition or Aggregation?
The relationship between MovingOnFromEx and HealingAction is composition because the HealingAction objects are created and managed by MovingOnFromEx. The actions are treated as parts of the moving-on process in this system. If the MovingOnFromEx object is removed, its HealingAction objects are also removed from the system.
### 4. What is the difference between Association from Part III and the advanced relationship you implemented?
The association from Part III connected MovingOnFromEx with MissingYourEx objects using a one-to-many relationship. In this activity, inheritance makes MovingOnFromEx a specific type of MissingYourEx, while composition shows that MovingOnFromEx owns its HealingAction objects. These relationships describe different connections between the classes.
### 5. How does your design follow the DRY principle?
My design follows the DRY principle by allowing MovingOnFromEx to inherit the common attributes and methods of MissingYourEx. This prevents me from repeating the same code in both classes. The child class only needs to contain features that are specific to moving on.