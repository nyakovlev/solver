Note: this project is not functional yet; the goal is shown below:

Simple Algebraic Problem Solving
---
Let's assume you have an environment with three variables:
<pre>
x, y, z
</pre>
This environment is constrained as so:
<pre>
x + y + z = 18
x + y = z + 4
x + z = y + 6
</pre>
The system of equations can be modeled like so:
[](https://github.com/nyakovlev/solver/blob/master/basic_solve.svg)

- A Param is key-value pair in a user environment.
  - Every environment is defined by a single dictionary; it stores
  every piece of information needed to define a functional system.
  - Params have no inherent value; they are set by Constraints.
  - Since params have no inherent value, they can be defined
  implicitly through interrelated artifacts, like Computed params
  and Constraints.
- a Constraint is a defined range of values that a parameter can
equal.
  - constraints are, for the most part, **user defined**. 
  Savvy UIs
  can help present and edit complex systems of constraints for
  positive user experience.
- a Computed param is the sum, product, collection, or other
calculated aggregate of one or more other params. 
  - aggregation functions are orderless (commutative property)
  - Linked params may or may not be paired with a conversion 
(-1, 1/x, int(x, 2) <--> "{0:b}".format(x), etc.) before being
aggregated.
  - Computed params live in the same namespace as normal params
  and can be treated like them, too.
- A Conversion is a 1-to-1 translation of a single value.
  - A conversion must translate **to** AND **from** another form.
  - The Solver utilizes conversions to simplify and
  solve algebraic systems. 

This model provides a generic way to define and solve systems
of computed constraints. The Solver takes user-defined constraints
and moves up and down layers of conversions and computed params
in order to define a system as completely as possible.

The would also be able to detect constraint conflicts, where no
solution exists for a system of params.

---
There are many other applications for such a solving tool.
The following features are planned:
- circuit design
- mechanical design (feature constraints, 
functional mechanisms, etc.)
- PCB layout
- Verilog/VHDL design
- Classic programming design (for debug and vizualization)

A core feature of this project is to integrate different design
environments. For instance, in a system with a circuit, a PCB,
and a chip running RTL, design constraints in Verilog might 
involve an EMI-sensitive signal, which would need appropriate
P/N signal circuitry and PCB trace positioning to transmit
successfully. 

With a common solver across each design environment,
These dependencies can be automatically resolved. Constraints
defined in circuit design could modify RTL and PCB layout as
needed in order to make a functional product.

In the long term, this would allow engineers to build entire
systems in only a few steps; rather than meticulously define and
test every part of a system, systems could be defined by generic
overarching constraints, and detailed specifications would only
be needed for specificity, not functionality.

---
License: CC BY 4.0

*(free for anybody to modify and use, even commercially)*
