# How to Write a Question

Much of the syntax here was inspired by the `shell` language.

## Variables

| Syntax       |               Explanation                |    Example |
| ------------ | :--------------------------------------: | ---------: |
| `var`        |            Define a variable             | `var1 = 2` |
| `$var`       |      Call the value of the variable      | `$var + 1` |
| `rand(a, b)` | Generates a random integer between `a` (inclusive) and `b` (exclusive) |            |



## Question Format

- Define your variables at the beginning
- For multi-word variables, use underscores
  - They will be replaced with spaces
- Avoid equals signs in the question body

Example:

```shell
tablespoons_per_serving=rand(1,4)*10
substance="cream_cheese"
density=rand(15,20)/10
servings=rand(2,8)*1000
"A recipe calls for exactly $tablespoons_per_serving tablespoons of $substance per 10 servings. Assume there are exactly 16 tablespoons of $substance in a cup and that the density of "+$substance +" is about $density pounds per cup.How many pounds of chili pepper do you need to feed one serving to each of $servings people?\n\n\ Express your answer in 'hyper-scientific' notation to three significant digits. \n\n"
```

Turns into:

```
A recipe calls for exactly 20 tablespoons of chili powder per 10 servings.  Assume there are exactly 16 tablespoons of chili powder in a cup and that the density of chili powder is about 0.177 pounds per cup.

How many pounds of chili pepper do you need to feed one serving to each of 4000 people?

Express your answer in 'hyper-scientific' notation to three significant digits.
```

