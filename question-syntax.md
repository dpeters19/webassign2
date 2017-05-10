# How to Write a Question

Much of the syntax here was inspired by the `shell` language.

## Special Syntax

| Syntax       |               Explanation                |  Example |
| ------------ | :--------------------------------------: | -------: |
| `var`        |            Define a variable             | `var1=2` |
| `$var`       |      Call the value of the variable      | `$var+1` |
| `rand(a, b)` | Generates a random integer between `a` (inclusive) and `b` (exclusive) |          |



## Question Format	

#### Defining Variables:

- Define one variable per line


- Underscores are replaced with spaces

#### Notes

- Separate the defined variables from the question with `QUESTION`



## Example:

```shell
tablespoons_per_serving=rand(1,4)*10
substance="cream_cheese"
density=rand(15,20)/10
servings=rand(2,8)*1000
QUESTION
A recipe calls for exactly $tablespoons_per_serving tablespoons of $substance per 10 servings.
Assume there are exactly 16 tablespoons of $substance in a cup and that the density of $substance is about $density pounds per cup. 
How many pounds of chili pepper do you need to feed one serving to each of $servings people?"
```

Turns into:

```
A recipe calls for exactly 20 tablespoons of chili powder per 10 servings.
Assume there are exactly 16 tablespoons of chili powder in a cup and that the density of chili powder is about 0.177 pounds per cup.
How many pounds of chili pepper do you need to feed one serving to each of 4000 people?
```

