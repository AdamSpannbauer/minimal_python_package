import my_pkg
import my_pkg.perimeter

# We can call area functions directly because they're imported in __init__.py
my_pkg.rect_area(10, 20)

# We have to refer to the perimeter 'submodule' because it's not referenced in __init__.py
my_pkg.perimeter.square_perimeter(10)
