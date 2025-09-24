queries as below:
```
queries=['create alex','create alex','delete alex','create alex','create john']
```

result should be # ['alex1', 'alex2', 'alex1', 'john1']

Requirements:

```

write a python class with create() and delete() method. 
name should be sequential, ie alex1,alex2. when name is deleted, delete the one with smallest number first. ie alex1
when you create the same name again, it should start with the smallest number available again. ie alex1
capture all created names. 

```
