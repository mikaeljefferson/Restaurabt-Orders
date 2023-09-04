from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 2
def test_dish():
    frist_dish = Dish("sanduiche presunto", 20.0)
    second_dish = Dish("macarrao de mae", 100.0)

    # testando nome
    assert frist_dish.name == "sanduiche presunto"
    assert second_dish.name == "macarrao de mae"

    # testando price
    assert frist_dish.price == 20.0
    assert second_dish.price == 100.0

#  testando Eq
    assert frist_dish.__eq__(frist_dish) is True
    assert frist_dish.__eq__(second_dish) is False

# testando hash
    assert hash(frist_dish) == hash("Dish('sanduiche presunto', R$20.00)")

# testando repr
    assert repr(frist_dish) == "Dish('sanduiche presunto', R$20.00)"

# testa add ingredient
    frist_dish.add_ingredient_dependency(Ingredient("ovo"), 5)
    frist_dish.add_ingredient_dependency(Ingredient("salmão"), 1)

    # testando restrições com ingreddientes added
    assert frist_dish.get_restrictions() == {
         Restriction.ANIMAL_MEAT,
         Restriction.SEAFOOD,
         Restriction.ANIMAL_DERIVED,
    }

    # testando receita
    assert frist_dish.get_ingredients() == {Ingredient("ovo"),
                                            Ingredient("salmão")}
    assert frist_dish.recipe == {Ingredient("ovo"): 5, Ingredient("salmão"): 1}

    # testando erros de tipagem de atributos
    with pytest.raises(ValueError) as error:
        Dish("ovo", -15)
    assert str(error.value) == "Dish price must be greater then zero."

    with pytest.raises(TypeError) as error:
        Dish("salmão", "200")
    assert str(error.value) == "Dish price must be float."
