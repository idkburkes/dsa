from code_challenges.animal_shelter.animal_shelter import Dog, Cat, AnimalShelter
import pytest

def test_enqueue_one_dog():
    dog = Dog('Dog 1')
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    actual = shelter.dogs[0].name
    expected = 'Dog 1'
    assert actual == expected

def test_enqueue_multiple_dogs():
    dogs = [Dog('Dog 1'), Dog('Dog 2'), Dog('Dog 3')]
    shelter = AnimalShelter()
    for dog in dogs:
        shelter.enqueue(dog)
    expected = ['Dog 1', 'Dog 2', 'Dog 3']
    actual = [shelter.dogs[0].name, shelter.dogs[1].name, shelter.dogs[2].name]
    assert actual == expected

def test_enqueue_one_cat():
    cat = Cat('Cat 1')
    shelter = AnimalShelter()
    shelter.enqueue(cat)
    expected = 'Cat 1'
    actual = shelter.cats[0].name
    assert actual == expected

def test_enqueue_multiple_cats():
    cats = [Cat('Cat 1'), Cat('Cat 2'), Cat('Cat 3')]
    shelter = AnimalShelter()
    for cat in cats:
        shelter.enqueue(cat)
    expected = ['Cat 1', 'Cat 2', 'Cat 3']
    actual = [shelter.cats[0].name, shelter.cats[1].name, shelter.cats[2].name]
    assert expected == actual

def test_enqueue_cats_and_dogs():
    shelter = AnimalShelter()
    shelter.enqueue(Cat('Cat1'))
    shelter.enqueue(Dog('Dog1'))
    shelter.enqueue(Cat('Cat2'))
    actual = [shelter.cats[0].name, shelter.dogs[0].name, shelter.cats[1].name]
    expected = ['Cat1', 'Dog1', 'Cat2']
    assert actual == expected

def test_dequeue_one_dog():
    shelter = AnimalShelter()
    shelter.enqueue(Dog('Dog1'))
    shelter.enqueue(Dog('Dog2'))
    actual = shelter.dequeue('dog').name
    expected = 'Dog1'
    assert actual == expected

def test_dequeue_multiple_dogs():
    shelter = AnimalShelter()
    shelter.dogs = [Dog('Dog1'), Dog('Dog2'), Dog('Dog3')]
    actual = []
    for _ in range(3):
        actual.append(shelter.dequeue('dog').name)
    expected = ['Dog1', 'Dog2', 'Dog3']
    assert actual == expected


def test_dequeue_one_cat():
    shelter = AnimalShelter()
    shelter.enqueue(Cat('Cat1'))
    shelter.enqueue(Cat('Cat2'))
    actual = shelter.dequeue('cat').name
    expected = 'Cat1'
    assert actual == expected

def test_dequeue_multiple_cats():
    shelter = AnimalShelter()
    shelter.cats = [Cat('Cat1'), Cat('Cat2'), Cat('Cat3')]
    actual = []
    for _ in range(3):
        actual.append(shelter.dequeue('cat').name)
    expected = ['Cat1', 'Cat2', 'Cat3']
    assert actual == expected

def test_dequeue_wrong_pref():
    shelter = AnimalShelter()
    shelter.enqueue(Dog('Dog'))
    actual = shelter.dequeue("Pig")
    expected = None
    assert actual == expected