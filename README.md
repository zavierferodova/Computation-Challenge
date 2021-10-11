# Computation-Challenge
This script used for testing computer processor bits word size RAM access usage.

**Warning !!** <br>
The calculation process from this script will filled much of your computer RAM memory like Processor RAM Access calculation theory.

## Example
If you pass value 32 that means x86 processor architecture to `architecture_processor_computation()` function, the RAM of computer will used more than 4 GB.

```python
# usememory.py

....

architecture_processor_computation(32)
```

The process will be like this :
- First script will count processor memory address length by passed argument.
- 2<sup>32</sup> = 4.294.967.296 bytes of memory address count.
- 1 byte of memory address are contains 8 bit of value. Then script will multiply value of 2<sup>32</sup> with 8.
- 2<sup>32</sup> &#x2715;	8 = 34.359.738.368 bits memory cell.
- After that script will power value of 2<sup>32</sup> &#x2715;	8 with 2, because 1 of bit are contains two value 1 and 0.
- (2<sup>32</sup> &#x2715;	8)<sup>2</sup> = _____ This calculation will filled every single cell of memory address with value.
- Cause of every single cell memory is filled by value, the computer memory will used for about 4 GB.
- Because this script is using Python that auto allocate memory size, the result of RAM usage will take more than 4 GB.
