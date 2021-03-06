import moves.moveTemplate

def FlyingTemplate(MoveTemplate):
    def __init__(self, name, moveType, pwr, acc, pp, targets, description):
        super().__init__(name, moveType, pwr, acc, pp, targets, description)

    def use(self, user, target):
        if user.type == "flying":
            stab = 1.5
        else:
            stab = 1

        if target.type == "grass" or target.type == "fighting" or target.type == "bug":
            eff = 2.0
        elif target.type == "electric" or target.type == "ice" or target.type == "rock":
            eff = .5
        else:
            eff = 1
        
        if self.targets > 1:
            modifier = .75 * stab * eff
        else:
            modifier = 1 * stab * eff
        damage = (((((2*user.lvl)/5 + 2)*self.pwr*(user.spAttack/target.spDef))/50)+2) * modifier
        target.changeHp(-damage);
