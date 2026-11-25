#import "@preview/grape-suite:3.1.0": seminar-paper
#show figure.caption: set text(style: "italic")
#set outline(depth: 1)
#show bibliography: set heading(numbering: "1")
#show: seminar-paper.project.with(
    title: "Final Project Report",
    subtitle: "",

    university: [University of Colorado Denver],
    seminar: "MATH 6388 - Statistical & Machine Learning",
    docent: none,
    faculty: none,
    institute: none,
    submit-to: none,
    submit-by: none,
    semester: [Fall 2026],
    date-format: date => date.display("[month repr:long] [day], [year]"),

    author: "Brady Lamson",
    email: none,
    address: none,
    show-declaration-of-independent-work: false
)

// font sizes
#set text(size: 11pt)
#show heading.where(level: 1): set text(size: 14pt)
#show heading.where(level: 2): set text(size: 12pt)

// sections
#include "intro.typ"
#include "data.typ"
#include "methods.typ"
#include "design_and_preprocessing.typ"
#include "results.typ"
#include "investigation.typ"
#include "conclusion.typ"
#pagebreak()
#bibliography("references.bib")
#include "appendix.typ"