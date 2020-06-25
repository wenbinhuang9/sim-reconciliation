# Reconciliation System Design

## Goal 

A simple reconciliation system for small data. The big data is an another design, which we should use big data infrastructure. This is another topic. 

## How 

The linux utilities , sed, awk and diff, provides tools for simple reconsiliation implementation.

We will define small parts of operations, and then we can combine thoes opertions to our reconciliation system. 

## Formal Operation definiton 

### Head rename 

Each our orginal data is a structure data with fields name, we should be able to rename the head name. 

We call this operation rename. 

### Filter columns and rows 

We need to delete the unnecessary columns and select the necessary columns for further reconciliation. 

We call this operation filterCol.

### Diff 

The diff is used to compare the two structured text with the same filed name and field type. It will output the difference of the two structured files. 

We call this operation being diff 

### Field Transformer

Sometimes we need to change  a specific data into a fixed format, so we need to define a field transformer.

We can define standard field transformer and also allows self-defined field transformer. 

The defintion of standard field transformer depends on the requirements and your system data format. 

### Merge 

we can merge two structured texts into one texts. 

## Topological pipeline

After defining thoes operations , we need to define the how the basic operations are organized to develop the reconciliation. 

I use the idea from the linux pipeline. The ouptut of previous operations can be used for the next operations. 

But the idea is also a little different from the linux pipeline. Our pipeline is topological because it allows more than two operations executed simultaneously, and the ouput of each operation will be used as the parameters of the operatoin behind. 

## An example 
Data fram A.csv as following 

orderId,amount
a113231,100
a123231,209
a213131,300

Data from B.csv as following 

tradeId,amt
a113231,1.00
a123231,2.09
a213131,3.00

We can create implement by such a pipeline . 
rename(amtTransform(B.csv))
diff(A.csv,)











