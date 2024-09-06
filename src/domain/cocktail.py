from dataclasses import dataclass


@dataclass
class CocktailIngredient:
    name: str
    quantity: str

@dataclass
class Cocktail:
    preparation: str
    garnish: str
    glassware: str
    name: str
    category: str
    ingredients: list[CocktailIngredient]
    page: int
    ice_type: str = None
    observation: str = None

