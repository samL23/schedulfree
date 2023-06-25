from flask import Flask, jsonify, request
from flask_cors import CORS

from datetime import datetime, timezone
import time
from datetime import date
import datetime
import bisect
import heapq
import uuid


# databse for now:
TASKS = [
            # {"task_id":1,
            #  "task_name":"finish french report",
            #  "due":1687714920080.0,
            #  "priority":2,
            #  "min_time":120
            #  }, 
        ]

BLOCKS = [
            {
                "id":1,
                "name":"finish report",
                "day": 24,
                "time":'10:00AM',
                "end": '11:00AM',
             }, 
]


def string_to_date(stringDate):
    year = int(stringDate.split('-')[0])
    month = int(stringDate.split('-')[1])
    day = int(stringDate.split('-')[2].split('T')[0])
    hour = int(stringDate.split('-')[2].split('T')[1].split(':')[0])
    minute = int(stringDate.split('-')[2].split('T')[1].split(':')[1])
    newTime = datetime(year,month,day,hour,minute)
    unix_timestamp = datetime.timestamp(newTime)*1000
    return(unix_timestamp)



# TODO: get task from UI
def get_task():
    return

def task_sort( LONG_TASK_TIME = 120): ### currently in minutes 
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
    newTime = datetime.datetime(year,month,day,hour,minute)
    unix_timestamp = datetime.datetime.timestamp(newTime)*1000
    return(unix_timestamp)



def append_block(task_name, day, time, end):
    print(task_name,day,time,end)
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


def heap_maker(task_list):
     # initialze heap #go trhough list and calculate the compare value
    # print(task_list)
    temp_heap = []
    for task in task_list:
        task_id = task['task_id']
        time_till_due = task['due']/1000
        lenght = task['min_time']
        cv =  time_till_due/lenght
        heapq.heappush(temp_heap, (cv,task_id))
    return temp_heap

def long_task_dict_maker(task_list):
     #initialize the dict of the long tasks, using the id as a key
    temp_dict = {}
    for task in task_list:
        task_id = task['task_id']
        task_name = task['task_name']
        time_till_due = task['due']
        lenght = task['min_time']
        priority = task['priority']
        temp_dict[task_id] = {
            "task_name": task_name,
            "due" : time_till_due,
            "min_time": lenght,
            "priority": priority
        }
    return temp_dict


def create_blocks():
    #reset blocks
    BLOCKS.clear()

    #sort tasks into long and short list
    long_tasks, short_tasks = task_sort()

    heap = heap_maker(long_tasks)
    long_dict = long_task_dict_maker(long_tasks)
    

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
    max_block_time = 3*60*60*1000
    #lunch_break = 12pm

   
    # loop for 7 days
    for i in range(8):
        current_insert_time = datetime.datetime.now(timezone.utc)
        current_insert_time = current_insert_time.replace(hour=8,minute=0,second=0,microsecond=0)
        current_insert_time += datetime.timedelta(days=i)

        stop_time = current_insert_time.replace(hour=21,minute=0)
        end_of_day = current_insert_time + datetime.timedelta(days=1)
        time_since_break = 0

        current_insert_time = datetime.datetime.timestamp(current_insert_time)*1000
        end_of_day = datetime.datetime.timestamp(end_of_day)*1000
        stop_time = datetime.datetime.timestamp(stop_time)*1000
        
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

            time_since_break += 60*1000*lenght_in_min # update time since user had a break
            current_insert_time = end_time  #update the current insert time to after added block
            end_time = convert_unix_to_string(end_time)

            append_block(t_name, day, start_time, end_time)
            short_tasks.pop(0)  #remove the short task now that it was added as a block

            #checking if user needs a break now
            if time_since_break > 0.8 * max_block_time:
                time_since_break = 0
                current_insert_time += 60*60*1000 #add one hour break
            
            #check base condition
            condition = False
            for task in short_tasks:
                if task['due'] < end_of_day:
                    condition = True
        

        #now finish the day with tasks from long task list. repeat till work day is done
        while current_insert_time < (stop_time-60*90*1000):
            #get top of heap
            if len(heap) > 0:
                t = heapq.heappop(heap)
                #get infro from task taken from heap
                print("check 1")
                try:
                    temp_task = long_dict[t[1]]
                    task_id = t[1]
                    task_name = temp_task['task_name']
                    due = temp_task['due']
                    min_time = temp_task['min_time']
                    start_time = convert_unix_to_string(current_insert_time)
                    

                    if min_time > 120:
                        print("in check 1")
                        #take block out
                        min_time -= 90
                        end_time = convert_unix_to_string(current_insert_time + 60*90*1000)
                        time_since_break += 60*90*1000
                        current_insert_time += 60*90*1000 #update current insertion time to block end time
                        #calculate new cv value and insert back to heap
                        time_till_due = task['due']/1000
                        new_cv =  time_till_due/min_time
                        heapq.heappush(heap, (new_cv, task_id))
                        #replace min_time in the task dictionary
                        long_dict[task_id]['min_time'] = min_time

                    else:
                        #finish the task
                        task_name = "finishing " + task_name
                        end_time = convert_unix_to_string(current_insert_time + 60*min_time*1000)
                        time_since_break += 60*min_time*1000
                        current_insert_time += 60*min_time*1000 #update current insertion time to block end time
                        #dont put task back in heap since it is complete
                        print(task_name, day, start_time,end_time)
                    
                    append_block(task_name, day, start_time,end_time)
                    #checking if user needs a break now
                    if time_since_break > 0.8 * max_block_time:
                        time_since_break = 0
                        current_insert_time += 60*60*1000 #add one hour break
                    
                    
                except:
                    print("except")
                    break
            else:
                break
            #add block to schedule, remove the time used in block from the task time
            #recalculate the compare value since min time of task was lowered
            #insert this back to the heap
        day += 1








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


#----------start api ----------------------

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


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
            "task_id": uuid.uuid4().hex,
             "task_name": post_data.get('name'),
             "due": string_to_date(post_data.get('due')),
             "priority": post_data.get('priority'),
             "min_time": int(post_data.get('min'))
        })
        response_object['message'] = 'Task added!'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)

#get block
@app.route('/blocks', methods=['GET'])
def all_blocks():
    create_blocks()
    return jsonify({
        'status': 'success',
        'blocks': BLOCKS
    })

if __name__ == '__main__':
    app.run()

#--------------------end of api----------------------------------