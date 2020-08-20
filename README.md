# simply-progress
A light and easy to use progress bar for python

# Example

from simply_progress.progress import Progress_Bar

myprogress = Progress_Bar(10)

myprogress.done_message = " is complete"
for i in range(10):
    myprogress.next_step()

