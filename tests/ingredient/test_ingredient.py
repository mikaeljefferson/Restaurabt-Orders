from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    frist_ingredient = Ingredient("presunto")
    second_ingredient = Ingredient("macarrao")

# testa o name e igual ao passado
    assert frist_ingredient.name == "presunto"

# Testa as restrições
    assert frist_ingredient.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    # Testa (__eq__)
    assert frist_ingredient.__eq__(frist_ingredient) is True

    assert frist_ingredient.__eq__(second_ingredient) is False

# testa método mágico __hash__ funcione como esperado.
    assert frist_ingredient.__hash__() == hash(frist_ingredient.name)

    assert frist_ingredient.__hash__() != hash(second_ingredient.name)

# testa o método mágico __repr__ funcione como esperado;
    assert frist_ingredient.__repr__() == "Ingredient('presunto')"
