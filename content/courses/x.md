---
title: "Mathematics for Macroeconomics" 
date: 2013-10-01
url: /x/
aliases:
    - /c3/
    - /t3.html
    - /uploads/7/0/2/0/70200055/t3a.pdf
    - /uploads/7/0/2/0/70200055/t3b.pdf
    - /uploads/7/0/2/0/70200055/t3c.pdf
    - /uploads/7/0/2/0/70200055/t3d.pdf
    - /uploads/7/0/2/0/70200055/t3f.pdf 
    - /tags/benveniste-scheinkman-equation/
    - /tags/dynamic-programming/
author: "Pascal Michaillat"
description: "This graduate course covers basic mathematical methods for macroeconomics: dynamic programming, optimal control, and differential equations." 
summary: "This graduate course covers basic mathematical methods for macroeconomics: dynamic programming, optimal control, and differential equations. The methods are used to study dynamical macroeconomic systems in discrete time and continuous time." 
cover:
    image: "/x.png"
    alt: "Phase diagram depicting a saddle path"
editPost:
    URL: "https://github.com/pmichaillat/math-for-macro"
    Text: "Source files"
showToc: true
disableAnchoredHeadings: false

---

## Introduction

This course covers basic mathematical methods to study dynamical systems in discrete time and in continuous time. Dynamical systems are systems that involve more than one time-period; they are prevalent in macroeconomics. We first discuss dynamic programming, which is a method to solve dynamic optimization problems in discrete time. We then turn to optimal control, which is a method to solve dynamic optimization problems in continuous time. Finally, we show how to solve differential equations, which are used to describe continuous-time dynamical systems.

---

## Dynamic programming

This section covers dynamic programming, which is a method to solve dynamic optimization problems in discrete time. It introduces key concepts of dynamic programming in a simple, deterministic consumption-saving problem: value function, policy function, Bellman equation, and Benveniste-Scheinkman equation. Then randomness is introduced into the consumption-saving problem, and the stochastic problem is solved with dynamic programming. As a further application, a Real Business-Cycle model is solved with dynamic programming. Finally, we discuss how to solve general problems with dynamic programming.

This section also shows that optimizing via dynamic programming yields the same results as optimizing via the Lagrangian approach. There is a certain obsession with dynamic programming in macroeconomics, but sometimes you will find that it is easier and more intuitive to use the Lagrangian method.

+ [Lecture notes](/x1.pdf)
+ [Problem set](/x4.pdf)
+ Reference: [Acemoglu (2008, chapter 6)](https://press.princeton.edu/books/hardcover/9780691132921/introduction-to-modern-economic-growth)

---

## Optimal control

This section studies optimal control, which is a method to solve dynamic optimization problems in continuous time. We start by formulating the consumption-saving problem in continuous time. The continuous-time problem is solved first with a present-value Hamiltonian, then with a current-value Hamiltonian. (Both approaches are equivalent.) Then we discuss the optimality conditions for general optimization problems solved by optimal control. We also establish the connection between these optimality conditions and the optimality conditions obtained via dynamic programming. To conclude, we derive and discuss the Hamilton-Jacobi-Bellman (HJB) equation.

+ [Lecture notes](/x2.pdf)
+ [Problem set](/x5.pdf)
+ Reference: [Acemoglu (2008, chapter 7)](https://press.princeton.edu/books/hardcover/9780691132921/introduction-to-modern-economic-growth)

---

## Differential equations

This third section introduces differential equations, which are used to describe continuous-time dynamical systems. We first solve linear first-order differential equations. We then move to linear systems of first-order differential equations. Next, we show how to derive the properties of a linear system of first-order differential equations by drawing its phase diagram. Finally, we turn to nonlinear systems of first-order differential equations—which are common in macroeconomics. Although such systems cannot be solved explicitly, we characterize their properties by constructing their phase diagrams.

+ [Lecture notes](/x3.pdf)
+ [Problem set](/x6.pdf)
+ Reference: [Hirsch, Smale, Devaney (2013, chapters 1–6)](https://www.sciencedirect.com/book/9780123820105/differential-equations-dynamical-systems-and-an-introduction-to-chaos)

---

## Conclusion

To conclude, a little more practice and an application. The problem set below brings together all the material from the course. And the paper below applies the course's techniques to analyze the New Keynesian model in normal times and at the zero lower bound. 

Outside of growth theory, optimal control and differential equations are not used very much. Yet they are powerful tools to obtain theoretical results not only in long-run macroeconomics but also in short-run macroeconomics. For instance, as the paper shows, you can use them to analyze the New Keynesian model. It is easy to set up the model in continuous time, solve the household's problem with optimal control, and study the model's properties in normal times and at the zero lower bound using phase diagrams. The analysis is short and simple, and it offers many insights that are difficult to obtain in discrete time. For instance, with the phase diagrams, it is easy to understand the origins of the anomalies of the New Keynesian model at the zero lower—both the collapse of output and inflation and the implausibly large effects of government spending and forward guidance.

+ [Cumulative problem set](/x7.pdf)
+ Application to the New Keynesian model: 
    + [Analysis of the model by phase diagrams](/11.pdf)
    + [Derivation of the differential equations by optimal control](/11a.pdf)