from datetime import datetime
import time
import bisect

stringDate = "2023-06-23T13:13"
def string_to_date(stringDate):
    year = int(stringDate.split('-')[0])
    month = int(stringDate.split('-')[1])
    day = int(stringDate.split('-')[2].split('T')[0])
    hour = int(stringDate.split('-')[2].split('T')[1].split(':')[0])
    minute = int(stringDate.split('-')[2].split('T')[1].split(':')[1])
    newTime = datetime(year,month,day,hour,minute)
    unix_timestamp = datetime.timestamp(newTime)*1000
    return unix_timestamp


# databse for now:
TASKS = [
            {"task_id":1,
             "task_name":"finish french report",
             "due":1687664460000.0,
             "priority":2,
             "min_time":420
             }, 
             {"task_id":2,
             "task_name":"wash dishes",
             "due":1687714920000.0,
             "priority":2,
             "min_time": 120
             },
        ]
{
    "task_id": {"task_name": 743894728904
                "due": u893274587029
                }
}
def task_sort(LONG_TASK_TIME = 120): ### currently in minutes 
    short_tasks = []
    long_tasks = []
    long_task_dict = {}
    # make dictionary for long_task_dict bc otherwise we have to search for the task in list 
    for task in TASKS: 
        #TODO: sort algo for times
        key_function = lambda x: x["due"]
        
        if task["min_time"] > LONG_TASK_TIME: 
            insertion_index = bisect.bisect_left(long_tasks, task["min_time"], key = key_function)
            long_tasks.insert(insertion_index, task)
            # Now make dict for long tasks
            long_task_dict[task["task_id"]] = {}
            
            for item in task:
                if item == "task_id": 
                    continue
                else: 
                   long_task_dict[item] = task[item]
        else: 
            insertion_index = bisect.bisect_left(short_tasks, task["min_time"], key = key_function)
            short_tasks.insert(insertion_index, task)
        
        
    return(long_tasks, short_tasks)


print("long list:")
print(task_sort()[0])


print("\nshort list:")
print(task_sort()[1])
