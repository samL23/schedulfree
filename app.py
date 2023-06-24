from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import time
from datetime import date
import bisect
import heapq



def string_to_date(stringDate):
    year = int(stringDate.split('-')[0])
    month = int(stringDate.split('-')[1])
    day = int(stringDate.split('-')[2].split('T')[0])
    hour = int(stringDate.split('-')[2].split('T')[1].split(':')[0])
    minute = int(stringDate.split('-')[2].split('T')[1].split(':')[1])
    newTime = datetime(year,month,day,hour,minute)
    unix_timestamp = datetime.timestamp(newTime)*1000
    return(unix_timestamp)

#----------start api ----------------------

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# databse for now:
TASKS = [
            {"task_id":1,
             "task_name":"finish french report",
             "due":1687664460000.0,
             "priority":2,
             "min_time":"5hours"
             }, 
             {"task_id":2,
             "task_name":"wash dishes",
             "due":1687714920000.0,
             "priority":2,
             "min_time":"5hours"
             }
        ]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status':'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TASKS.append({
            "task_id": post_data.get('id'),
             "task_name": post_data.get('name'),
             "due": string_to_date(post_data.get('due')),
             "priority": post_data.get('priority'),
             "min_time": post_data.get('min')
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()

#--------------------end of api----------------------------------





# TODO: get task from UI
def get_task():
    return

def task_sort(LONG_TASK_TIME = 120): ### currently in minutes 
    short_tasks = []
    long_tasks = []
    long_tasks_dict = {}
    # make dictionary for long_tasks_dict bc otherwise we have to search for the task in list

    for task in TASKS: 
        #TODO: sort algo for times
        key_function = lambda x: x["due"]
        
        if task["min_time"] > LONG_TASK_TIME: 
            insertion_index = bisect.bisect_left(long_tasks, task["min_time"], key = key_function)
            long_tasks.insert(insertion_index, task)

            # Now make dict for long tasks
            long_tasks_dict[task["task_id"]] = {}
            
            for item in task:
                if item == "task_id": 
                    continue
                else: 
                   long_tasks_dict[item] = task[item]
        else: 
            insertion_index = bisect.bisect_left(short_tasks, task["min_time"], key = key_function)
            short_tasks.insert(insertion_index, task)
        
        print(long_tasks)
        print(short_tasks)

    return(long_tasks, short_tasks, long_tasks_dict)

def getHeap(tasks_dict, tasks): 
    minHeap = []
    for item in tasks: 
        #sort tasks from highest to lowest priority
        heapq.heappush((tasks_dict["due"] - int(time.time())) / ["min_time"], tasks_dict["task_id"])
    return minHeap
# front end will send
# list of dict : [{task_id:id,task_name:name,due:date,user_priority:lvl, min_time:time},
#                 {task_id:id, task_name:name,due:date,priprity:lvl,  min_time:time}
# ]
# have minimum time it will take in total
# we have to decide how to divide this task into block to work on througout the week
#
#fit in for user breaks - time slots
# algo to sort 
# enough time?
# algo priority levels relative to due date and time required 
# finish earlier rather than later for higher user priority
# Maximum work blocks

