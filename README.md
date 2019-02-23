# Poetry
Outputs a random poem from a predefined directory. 

## Usage
```python3 poems.py```

outputs a random poem.

```python3 poems.py "Edgar Allan Poe"```
outputs a random poem by Edgar Allan Poe if it exists.

```python3 poems.py Ozymandias``` 
Outputs the poem titled Ozymandias, if it exists.

```python3 poems.py --update```
or
```python3 poems.py -u``` 
Updates the database.

To add a new poem, simply add a new text file into Poetry/poems with the title as 
the first line, and the author as the second line. You should also make sure the file ends with a newline. Then run ```python3 poems.py -u```.


Aaron Hadley  
aahadley1@gmail.com