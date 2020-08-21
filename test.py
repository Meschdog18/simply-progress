import time
from simply_progress.progress import Progress_Bar

myprogress = Progress_Bar(50, "Download")
myprogress.done_message = " is complete"
for i in range(50):
    time.sleep(1)
    myprogress.next_step()