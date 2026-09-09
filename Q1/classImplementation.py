class MissingYourEx:
    def __init__(self, ex_name, ended_when, reason_for_missing, last_contact):
        self.ex_name = ex_name
        self.ended_when = ended_when
        self.__reason_for_missing = reason_for_missing
        self.last_contact = last_contact

    def reach_out_on_holiday(self, holiday):
        self.last_contact = f"Contacted on {holiday}"
        return f"Reached out to {self.ex_name} on {holiday}."

    def message_late_at_night(self):
        self.last_contact = "Messaged late at night"
        return f"Sent a late-night message to {self.ex_name}."

    def call_on_birthday(self):
        self.last_contact = "Called on birthday"
        return f"Called {self.ex_name} on their birthday."

    def get_reason_for_missing(self):
        return self.__reason_for_missing


# Create two different objects
person1 = MissingYourEx(
    "Xian",
    "June 2026",
    "I miss the memories we shared.",
    "September 2026"
)

person2 = MissingYourEx(
    "Chance",
    "January 2025",
    "I miss having someone who was not just a lover but also a bestfriend",
    "September 2026"
)


# Show the initial state of both objects
print("--- BEFORE ---")

print("Object 1:")
print("Ex Name:", person1.ex_name)
print("Ended When:", person1.ended_when)
print("Last Contact:", person1.last_contact)
print("Reason for Missing:", person1.get_reason_for_missing())

print()

print("Object 2:")
print("Ex Name:", person2.ex_name)
print("Ended When:", person2.ended_when)
print("Last Contact:", person2.last_contact)
print("Reason for Missing:", person2.get_reason_for_missing())


# Perform an action on Object 1 only
print()
print("Performing action on Object 1...")
print(person1.reach_out_on_holiday("Christmas"))


# Show the updated state of both objects
print()
print("--- AFTER ---")

print("Object 1:")
print("Ex Name:", person1.ex_name)
print("Ended When:", person1.ended_when)
print("Last Contact:", person1.last_contact)
print("Reason for Missing:", person1.get_reason_for_missing())

print()

print("Object 2:")
print("Ex Name:", person2.ex_name)
print("Ended When:", person2.ended_when)
print("Last Contact:", person2.last_contact)
print("Reason for Missing:", person2.get_reason_for_missing())