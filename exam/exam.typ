#import "@preview/grape-suite:3.1.0": exercise
#import exercise: project, task, subtask
#show selector(heading.where(level: 2)): set heading(numbering: none)
#show selector(heading.where(level: 3)): set heading(numbering: none)
#show selector(heading.where(level: 4)): set heading(numbering: none)
// #set thmbox.qed: "∎"

#show: project.with(
    title: "Exam",

    university: [University of Colorado, Denver],
    semester: [Fall 2026],
    seminar: [MATH 6388 - Statistical and Machine Learning],

    show-outline: true,

    author: "Brady Lamson",

    show-solutions: false,
    show-lines: false,
    type: "Homework Sheet"
)

#set math.mat(delim: "[")
#pagebreak()
#include "q1.typ"
#pagebreak()
#include "q2.typ"
#pagebreak()
#include "q3.typ"
#pagebreak()
#include "q4.typ"
#pagebreak()
#include "q5.typ"
