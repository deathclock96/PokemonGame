from moves.fire.fireTemplate import FireTemplate

class FlareBlitz(FireTemplate):
    def __init__(self, name="flare blitz", moveType="fire", pwr=120, acc=1, pp=15, targets=1, description="The user cloaks itself in fire and charges the target. This also damages the user quite a lot. This attack may leave the target with a burn."):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        super().use(user, target)
        


