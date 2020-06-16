import itertools
import threading
import time
import sys
import random

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r' + c +" Loading...")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r RetroTube')

t = threading.Thread(target=animate)
t.start()

random_number = random.randint(4, 20)

#long process here
time.sleep(random_number)
done = True

time.sleep(1)
print("Trending Today:")
print()