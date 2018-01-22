# ml-playground
A machine learning playground to test out some machinery and ideas.

ML is an empirical science meaning there are well established statistical and
numerical techniques but data being what it is, requires tremendous
experimentation to determine what works and what doesn't.

Whoever has the data and the means for experimentation (manpower and compute)
could potentially win big.

# So You Want to ML?

A flowchart to help guide you.

1. If you know everything about your data, then exit
2. If you can use analytical tools with standard formulas (MS Excel, etc), then
   exit
   (Note: There are LP solvers which can do 1 million variables)
3. If your data has too much variability, then exit
4. If you can use an existing model to solve your problem, then do so, exit.
4. If you do not have a lot of data (>100K or so), then exit
5. It is all about predictions - 2-value (binary) or N-value (multi-class). What
   kind of problem is yours?
6. Is your data structured (properly formatted?), if not, do so
7. Do you have labeled data or unlabeled data?
8. Take repeated small samples, and a simple model, and test for bias and
   variance. If high variance, then likely 3. above, so either try a different
   model, or exit
9. Knowing a little more about the data is helpful, in terms of picking the
   right features, and the right model. If not, repeat 8 till you do.
10. Now train and validate your model against your datatset and real world examples. 
   This will be pricey depending on the workload. Steps 1..9 were to save you time and money.
11. Hopefully, Step 10 was fruitful. But we are not done.
12. As we interact with the real world, we acquire more data, and some of 1..10
    must be constantly repeated.


# Toolkit
* Python
* Keras - growing on me for its simplicity and also uses Tensorflow as a backend
* scikit, numpy, etc
