=====================
Getting started
=====================

Clone the repository
********************
Now open the terminal and run this command 
::

    $ git clone https://github.com/kumarisneha/task_queue.git

    
Running the code:
*****************
Next run these commands on your terminal.
::

    $ cd task_queue/men_woman
    $ python r2.py
    $ python r3.py
    
Again open a new terminal at the project root and run:
::

    $ rq worker
    *** Listening for work on default
    Got count_words_at_url('http://nvie.com') from default
    Job result = 818
    *** Listening for work on default

For rq directory project:
::

    $rq worker
    
For men_women directory project
::

    $rq worker low
    $rq worker high




