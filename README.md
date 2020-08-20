# Simply-Progress
### A light and easy to use progress bar for python

# Installation

### python3 -m pip install simply-progress

# Example

### Code
```
from simply_progress.progress import Progress_Bar

myprogress = Progress_Bar(10, "File download")

myprogress.done_message = " is complete"
for i in range(10):
    myprogress.next_step()
```
### Output

```
File download |=---------|
File download |==--------|
File download |===-------|
File download |====------|
File download |=====-----|
File download |======----|
File download |=======---|
File download |========--|
File download |=========-|
File download |==========|
File download is complete
```
