#import "@preview/grape-suite:4.0.0": exercise
#import exercise: project, task, subtask
#show selector(heading.where(level: 1)): set heading(numbering: none)
#show selector(heading.where(level: 2)): set heading(numbering: none)
#show selector(heading.where(level: 3)): set heading(numbering: none)
#show selector(heading.where(level: 4)): set heading(numbering: none)
#set par(
    leading:1.0em,
    spacing:2em
)

#show: project.with(
    title: "Project Proposal",

    university: [University of Colorado, Denver],
    semester: [Fall 2026],
    seminar: [MATH 6388 - Statistical and Machine Learning],

    show-outline: false,

    author: "Brady Lamson",

    show-solutions: false,
    show-lines: false,
    type: "Homework Sheet"
)

#include "regression.typ"

#include "classification.typ"