class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def bite(self, other):
        """Deliver a dose of venom."""
        print(f'{other} has been bitten by {self}, two puncture wounds begin slowly dripping blood.')
	    print(f'{other} has been poisoned and desperately requires medical attention.')

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        print(f'{self} wraps itself tightly around {other}')

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""

    def __init__(self):
        """Create a new BoatConstrictor"""
        super().__init__()
        self.size = "enormous"
