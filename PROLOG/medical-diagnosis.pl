% Symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(rash).
symptom(sore_throat).

% Diseases and their symptoms
disease(cold, [cough, headache]).
disease(flu, [fever, cough, headache, sore_throat]).
disease(measles, [fever, rash, cough]).
disease(allergies, [cough, rash]).

% Predicate to diagnose diseases based on symptoms
diagnose(Disease) :-
    findall(Symptom, symptom(Symptom), Symptoms),
    disease(Disease, DiseaseSymptoms),
    sublist(DiseaseSymptoms, Symptoms).

% Predicate to check if a list is a sublist of another list
sublist([], _).
sublist([X|Xs], [X|Ys]) :- sublist(Xs, Ys).
sublist([X|Xs], [_|Ys]) :- sublist([X|Xs], Ys).
