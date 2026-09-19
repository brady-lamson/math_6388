#import "@preview/grape-suite:3.1.0": exercise
#import exercise: project, task, subtask
#show selector(heading.where(level: 2)): set heading(numbering: none)
#show selector(heading.where(level: 3)): set heading(numbering: none)
#show selector(heading.where(level: 4)): set heading(numbering: none)
// #set thmbox.qed: "∎"

#show: project.with(
    title: "Homework 3",

    university: [University of Colorado, Denver],
    semester: [Fall 2026],
    seminar: [MATH 6388 - Statistical and Machine Learning],

    show-outline: false,

    author: "Brady Lamson",

    show-solutions: false,
    show-lines: false,
    type: "Homework Sheet"
)

= Problem 2.1

Why does the following identity hold? 

#let w = $bold(w)$
#let A = $bold(A)$
#let wmat = $mat(w_1; w_2, delim:"[")$
#let wmat_trans = $mat(w_1, w_2, delim:"[")$
#let xmat = $mat(x_1; x_2, delim:"[")$
#let Amat = $mat(a,b;c,d, delim:"[")$
#let Amat_trans = $mat(a,c;b,d, delim:"[")$
#let delta1 = $frac(delta, delta w_1)$
#let delta2 = $frac(delta, delta w_2)$
#let identity_left = $nabla_#w (#w^T #A #w)$
#let identity_right = $(#A + #A^T)#w$
#set align(center)

$#identity_left  = #identity_right$

#align(left)[For the 2D case, let]

$#A = #Amat, #w = #wmat$

#align(left)[Expanding the quadratic form gives]

#let quadratic_expansion = $w_1^2a + w_1w_2c + w_1w_2b + w_2^2d$

$
  #w^T #A #w &= #wmat_trans #Amat #wmat \
  &= mat(w_1 a + w_2 c, w_1 b + w_2 d, delim:"[") #wmat \
  &= (w_1 a + w_2 c)w_1 + (w_1 b + w_2 d)w_2 \
   &= #quadratic_expansion
$


#align(left)[Therefore,]

#let identity_answer = $mat(2w_1a + w_2(b+c); w_1(b+c) + 2w_2d, delim:"[")$

$
  #identity_left &= mat(#delta1 #quadratic_expansion;; #delta2 #quadratic_expansion, delim:"[") \
  &= mat(2w_1a + w_2c + w_2b; w_1c + w_1b + 2w_2d, delim:"[") \
  &= #identity_answer
$

#align(left)[Notice that]

$
  #A + #A^T &= #Amat + #Amat_trans \
  &= mat(2a, b+c; b+c, 2d, delim:"[")
$

#align(left)[So, ]

$
  (#A + #A^T)#w &= mat(2a, b+c; b+c, 2d, delim:"[") #wmat \
  &= #identity_answer
$

#align(left)[Therefore,]

$#identity_left = #identity_right$

#align(left)[Showing that the identity holds.]