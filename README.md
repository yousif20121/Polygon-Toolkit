# Polygon Toolkit Documentation

Welcome to the Polygon Toolkit documentation. This toolkit provides classes for working with different types of polygons and shapes. It includes various classes for polygons, triangles, and quadrilaterals.

## Polygon Toolkit Welcome Menu

### Welcome menu for the Polygon Toolkit.

Function: `welcome_menu()`

Display the welcome menu for the Polygon Toolkit.

#### Options:

1. Polygon (with identical sides)
2. Triangle
3. Quadrilateral
4. Quit

## Shape Actions Menu

### Menu for actions related to shapes.

Function: `actions_menu()`

Display the menu for actions related to shapes.

#### Options:

1. Calculate Perimeter
2. Calculate Area
3. Draw

## Polygon Classes

### Base Class: `Polygon`

```python
class Polygon:
    """
    Base class for polygons.
    """
    # Initialization, perimeter, area, and drawing methods are defined here.
```

### Subclass: `Pentagon`

```python
class Pentagon(Polygon):
    """
    Subclass of Polygon representing a Pentagon.
    """
    # Initialization, perimeter, area, and drawing methods for pentagons are defined here.
```

### Subclass: `Hexagon`

```python
class Hexagon(Polygon):
    """
    Subclass of Polygon representing a Hexagon.
    """
    # Initialization, perimeter, area, and drawing methods for hexagons are defined here.
```

### Subclass: `Octagon`

```python
class Octagon(Polygon):
    """
    Subclass of Polygon representing an Octagon.
    """
    # Initialization, perimeter, area, and drawing methods for octagons are defined here.
```

## Triangle Classes

### Subclass: `Triangle`

```python
class Triangle(Polygon):
    """
    Subclass of Polygon representing a Triangle.
    """
    # Initialization, perimeter, area, and drawing methods for triangles are defined here.
```

### Subclass: `IsoTriangle`

```python
class IsoTriangle(Triangle):
    """
    Subclass of Triangle representing an Isosceles Triangle.
    """
    # Initialization, perimeter, and drawing methods for isosceles triangles are defined here.
```

### Subclass: `EquiTriangle`

```python
class EquiTriangle(Triangle):
    """
    Subclass of Triangle representing an Equilateral Triangle.
    """
    # Initialization, perimeter, area, and drawing methods for equilateral triangles are defined here.
```

## Quadrilateral Classes

### Subclass: `Quadrilateral`

```python
class Quadrilateral(Polygon):
    """
    Subclass of Polygon representing a Quadrilateral.
    """
    # Initialization, perimeter, area, and drawing methods for quadrilaterals are defined here.
```

### Subclass: `Square`

```python
class Square(Quadrilateral):
    """
    Subclass of Quadrilateral representing a Square.
    """
    # Initialization, perimeter, area, and drawing methods for squares are defined here.
```

### Subclass: `Rectangle`

```python
class Rectangle(Quadrilateral):
    """
    Subclass of Quadrilateral representing a Rectangle.
    """
    # Initialization, perimeter, area, and drawing methods for rectangles are defined here.
```

This documentation provides an overview of the Polygon Toolkit and its classes. You can use the functions and methods mentioned in the respective sections to work with different shapes and polygons. You find more details in the file codes themselves.