% Dietary recommendations based on diseases
% disease(Name, RecommendedFoods)
disease(high_blood_pressure, [fruits, vegetables, whole_grains, lean_protein, low_sodium]).
disease(diabetes, [whole_grains, lean_protein, non-starchy_vegetables, healthy_fats, low_added_sugar]).
disease(celiac_disease, [gluten_free_grains, lean_protein, fruits, vegetables, dairy_alternatives]).

% Rules for recommending diet based on disease
recommend_diet(Person, Disease) :-
    disease(Disease, RecommendedFoods),
    write('For '), write(Person), write(' with '), write(Disease),
    write(', it is recommended to include: '), write(RecommendedFoods), nl.

% Example usage
:- recommend_diet(john, high_blood_pressure).
:- recommend_diet(susan, diabetes).
