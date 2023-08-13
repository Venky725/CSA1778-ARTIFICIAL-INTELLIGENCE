% Facts: Students, Teachers, Subjects
student(john).
student(susan).
student(alex).

teacher(mr_smith).
teacher(ms_jones).

subject(math).
subject(science).
subject(history).

% Relationships: Teaching and Enrolled
teaches(mr_smith, math).
teaches(ms_jones, science).

enrolled(john, math).
enrolled(john, science).
enrolled(susan, history).
enrolled(alex, science).

% Rules: Who teaches what subject
teaches_subject(Teacher, Subject) :-
    teacher(Teacher),
    teaches(Teacher, Subject).

% Rules: What subjects a student is enrolled in
enrolled_in_subject(Student, Subject) :-
    student(Student),
    enrolled(Student, Subject).
