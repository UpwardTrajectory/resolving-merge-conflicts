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
        pass

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass
