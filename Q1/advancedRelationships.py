class MissingYourEx:
    def __init__(self, last_contact, reason_for_missing):
        self.last_contact = last_contact
        self.__reason_for_missing = reason_for_missing

    def get_reason_for_missing(self):
        return self.__reason_for_missing

    def miss_ex(self):
        print("Missing the former partner.")

    def display_info(self):
        print(f"Last Contact: {self.last_contact}")
        print(f"Reason for Missing: {self.__reason_for_missing}")


class HealingAction:
    def __init__(self, action_name, description):
        self.action_name = action_name
        self.description = description

    def perform_action(self):
        print(f"Doing: {self.action_name}")
        print(self.description)


class MovingOnFromEx(MissingYourEx):
    def __init__(self, last_contact, reason_for_missing, progress):
        super().__init__(last_contact, reason_for_missing)
        self.progress = progress
        self.healing_actions = []

    def add_healing_action(self, action_name, description):
        action = HealingAction(action_name, description)
        self.healing_actions.append(action)

    def show_progress(self):
        print(f"Moving-on progress: {self.progress}")

    def display_healing_actions(self):
        print("Healing Actions:")
        for action in self.healing_actions:
            print(f"- {action.action_name}: {action.description}")


moving_on = MovingOnFromEx(
    "September 14, 2026",
    "Memories and shared experiences",
    "Making progress"
)

moving_on.add_healing_action(
    "Focus on school",
    "Spend time improving academically and reaching personal goals."
)

moving_on.add_healing_action(
    "Spend time with friends",
    "Stay connected with people who provide support."
)

moving_on.add_healing_action(
    "Accept the past",
    "Learn from the experience and continue moving forward."
)


print("--- TEST 1: INHERITANCE ---")
print("MovingOnFromEx is a type of MissingYourEx.")
print(f"Last Contact: {moving_on.last_contact}")
print(f"Reason for Missing: {moving_on.get_reason_for_missing()}")

print("\nCalling an inherited method:")
moving_on.miss_ex()


print("\n--- TEST 2: COMPOSITION ---")
moving_on.show_progress()

print("\nHealing actions connected to MovingOnFromEx:")
moving_on.display_healing_actions()


print("\n--- TEST 3: USING COMPOSED OBJECTS ---")

for action in moving_on.healing_actions:
    action.perform_action()