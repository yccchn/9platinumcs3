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


class MovingOnFromEx:
    def __init__(self, process_name):
        self.process_name = process_name
        self.missing_exes = []

    def add_missing_ex(self, missing_ex):
        self.missing_exes.append(missing_ex)
        return f"{missing_ex.ex_name} was added to the moving-on process."

    def show_missing_exes(self):
        for missing_ex in self.missing_exes:
            print(f"Ex: {missing_ex.ex_name}")
            print(f"Ended: {missing_ex.ended_when}")
            print(f"Reason: {missing_ex.get_reason_for_missing()}")
            print(f"Last Contact: {missing_ex.last_contact}")
            print()


moving_on = MovingOnFromEx("Moving Forward")

person1 = MissingYourEx(
    "Xian",
    "June 2026",
    "I miss the memories we shared.",
    "September 2026"
)

person2 = MissingYourEx(
    "Chance",
    "January 2025",
    "I miss having someone who was not just a lover but also a best friend.",
    "September 2026"
)

person3 = MissingYourEx(
    "Alex",
    "March 2026",
    "I miss the friendship we had.",
    "August 2026"
)

print("--- BEFORE RELATIONSHIP ---")
print("Moving-on process:", moving_on.process_name)
print("Number of connected MissingYourEx objects:", len(moving_on.missing_exes))

print("\n--- FORMING RELATIONSHIP ---")
print(moving_on.add_missing_ex(person1))
print(moving_on.add_missing_ex(person2))
print(moving_on.add_missing_ex(person3))

print("\n--- AFTER RELATIONSHIP ---")
print("Moving-on process:", moving_on.process_name)
print("Number of connected MissingYourEx objects:", len(moving_on.missing_exes))

print("\n--- INFORMATION THROUGH RELATIONSHIP ---")
moving_on.show_missing_exes()