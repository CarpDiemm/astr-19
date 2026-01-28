class GoldenRetriever:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def describe_physical_characteristics(self):
        print(f"Arm Length: {self.arm_length}")
        print(f"Leg Length: {self.leg_length}")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has a Tail: {self.has_tail}")
        print(f"Is Furry: {self.is_furry}")

if __name__ == "__main__":
    retriever = GoldenRetriever(11.5, 11.5, 2, True, True)
    retriever.describe_physical_characteristics()