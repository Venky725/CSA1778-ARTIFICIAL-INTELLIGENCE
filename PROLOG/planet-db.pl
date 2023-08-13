% Facts: Planets and their characteristics
planet(mercury, rocky, small, hot).
planet(venus, rocky, small, hot).
planet(earth, rocky, medium, temperate).
planet(mars, rocky, small, cold).
planet(jupiter, gas_giant, large, cold).
planet(saturn, gas_giant, large, cold).
planet(uranus, ice_giant, medium, very_cold).
planet(neptune, ice_giant, medium, very_cold).

% Rules: Querying planets based on characteristics
rocky_planet(Name) :-
    planet(Name, rocky, _, _).

gas_giant_planet(Name) :-
    planet(Name, gas_giant, _, _).

ice_giant_planet(Name) :-
    planet(Name, ice_giant, _, _).

small_planet(Name) :-
    planet(Name, _, small, _).

large_planet(Name) :-
    planet(Name, _, large, _).

cold_planet(Name) :-
    planet(Name, _, _, cold).

% Rules: Describing planets
description(Planet) :-
    planet(Planet, Type, Size, Temperature),
    write(Planet), write(' is a '), write(Size), write(' '), write(Type),
    write(' planet with a temperature of '), write(Temperature), write('.'), nl.
