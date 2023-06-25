from datetime import datetime, timezone
import time
import bisect
from datetime import date
import datetime

stringDate = "2023-06-23T13:13"


# databse for now:
TASKS = [
            {"task_id":1,
             "task_name":"finish french report",
             "due":1687714920080.0,
             "priority":2,
             "min_time":100
             }, 
             {"task_id":2,
             "task_name":"wash dishes",
             "due":1687627886000.0,
             "priority":2,
             "min_time": 100
             },
        ]

BLOCKS = [
           
]


def task_sort(LONG_TASK_TIME = 120): ### currently in minutes 
    short_tasks = []
    long_tasks = []
    long_task_dict = {}
    # make dictionary for long_task_dict bc otherwise we have to search for the task in list 
    for task in TASKS: 
        #TODO: sort algo for times
        key_function = lambda x: x["due"]
        
        if task["min_time"] > LONG_TASK_TIME: 
            insertion_index = bisect.bisect_left(long_tasks, task["due"], key = key_function)
            long_tasks.insert(insertion_index, task)
            # Now make dict for long tasks
            long_task_dict[task["task_id"]] = {}
            
            for item in task:
                if item == "task_id": 
                    continue
                else: 
                   long_task_dict[item] = task[item]
        else: 
            insertion_index = bisect.bisect_left(short_tasks, task["due"], key = key_function)
            short_tasks.insert(insertion_index, task)
        
    return(long_tasks, short_tasks)



def string_to_date(stringDate):
    year = int(stringDate.split('-')[0])
    month = int(stringDate.split('-')[1])
    day = int(stringDate.split('-')[2].split('T')[0])
    hour = int(stringDate.split('-')[2].split('T')[1].split(':')[0])
    minute = int(stringDate.split('-')[2].split('T')[1].split(':')[1])
    newTime = datetime(year,month,day,hour,minute)
    unix_timestamp = datetime.timestamp(newTime)*1000
    return(unix_timestamp)



def append_block(task_name, day, time, end):
    new_dict = {
        "id":1,
        "name": task_name,
        "day": day,
        "time": time,
        "end": end,
    }
    BLOCKS.append(new_dict)

def convert_unix_to_string(unix_timestamp):
    #   string_time = datetime.datetime.utcfromtimestamp(unix_timestamp/1000).strftime('%Y-%m-%d %H:%M')
    string_time = datetime.datetime.utcfromtimestamp(unix_timestamp/1000).strftime('%H:%M')
    return string_time


def create_blocks():
    #sort tasks into long and short list
    long_tasks, short_tasks = task_sort()
    # start day is today
    day = datetime.datetime.now(timezone.utc).day
    current_insert_time = datetime.datetime.now(timezone.utc)
    end_of_day = current_insert_time + datetime.timedelta(days=1)


    current_insert_time = current_insert_time.replace(hour=8,minute=0,second=0,microsecond=0)
    print(current_insert_time)
    current_insert_time = datetime.datetime.timestamp(current_insert_time)*1000
    print(current_insert_time)
    end_of_day = datetime.datetime.timestamp(end_of_day)*1000
    time_since_break = 0
    max_block_time = 60*1000 *3
    #lunch_break = 12pm

   
    # loop for 7 days

    #check if there is a short task due today
    condition = False
    for task in short_tasks:
        if task['due'] < end_of_day:
            condition = True
            
    while condition:
        # get the small task that will be due today and complete it, repeat till they are done. then move to large task for rest of day
        current_task = short_tasks[0]
        t_name = current_task["task_name"]
        start_time = convert_unix_to_string(current_insert_time)
        lenght_in_min = current_task["min_time"]
        end_time = current_insert_time + 60*1000*lenght_in_min

        time_since_break += end_time - current_insert_time # update time since user had a break
        current_insert_time = end_time  #update the current insert time to after added block
        end_time = convert_unix_to_string(end_time)

        append_block(t_name, day, start_time, end_time)
        short_tasks.pop(0)  #remove the short task now that it was added as a block

        #checking if user needs a break now
        if time_since_break > 0.8 * max_block_time:
            time_since_break = 0
            current_insert_time += 60*1000 #add one a

        #check base condition
        condition = False
        for task in short_tasks:
            if task['due'] < end_of_day:
                condition = True



    # while condition:
    #     print
    #check if short task today
    #insert
    # while loop till done
    #next big tasks: use tree

create_blocks()
print(BLOCKS)
