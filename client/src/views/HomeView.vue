<script setup>
</script>

<style>
/* For mobile phones: */

h1{
  font-family: "Trirong", serif;
}

.spacer {
  height: 100vh;
  width: 100%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
}

.layer1{
  background-image: url('../assets/layered-waves-haikei (1).svg');
}

  .responsiveWidth{
    width: 95%;
    margin:auto;
  }

  .todoItem{
    padding-left: 20px;
    margin: 0;
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .circle{
    padding-right: 10px;
  }

  [class*="col-"] {
    width: 100%;
  }
 
  .round{
    border-radius: 10px
  }
  .inputField{
    border: none;
    width: 90%;
    margin-top: 10px;
    margin-bottom: 10px;
    padding: 5px;
    padding-top: 8px;
  }
  input:focus, input:focus{
    outline: none;
}


  .wrapper:hover{
    color:white;
    transition: 0.5s;
    transform: rotateZ(-90deg);
  }
  .wrapper{
    color: gray;
    transition: 0.9s;
    transform: rotateZ(45deg);
  }
 

  .secondaryBtn{
    text-decoration: none;
    cursor: pointer;
    color: gray;
  }
  .secondaryBtn:hover{
    color:darkcyan;
  }

  @media screen and (min-width: 576px) {
    /* For desktop: */
    .layer1{
      background-image: url('../assets/layered-waves-haikei.svg');
    }
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
  }

  @media screen and (min-width: 768px) {
    /* For desktop: */
    .round{border-radius: 10px;}
    .responsiveWidth{ width: 45%; margin:auto}
    .col-1 {width: 8.33%;}
    .col-2 {width: 16.66%;}
    .col-3 {width: 25%;}
    .col-4 {width: 33.33%;}
    .col-5 {width: 41.66%;}
    .col-6 {width: 50%;}
    .col-7 {width: 58.33%;}
    .col-8 {width: 66.66%;}
    .col-9 {width: 75%;}
    .col-10 {width: 83.33%;}
    .col-11 {width: 91.66%;}
    .col-12 {width: 100%;}
  }
</style>

<template>
  <div class="spacer layer1" style="width: 100%;top:0px">
    <div class="responsiveWidth  round text-white" >
      <h1 class="text-center pt-5" style="color: white;">ScheduleFree</h1>
      <form @submit.prevent=""  class="">
       
        <div class="mb-5 round py-3 text-center shadow-lg" style="background-transpatent;background-color: rgb(54, 48, 42);">
          <input
            autocomplete="off"
            type="text"
            class=" round inputField text-center"
            id="name"
            placeholder="Task Name"
            style=""
            v-model="addTaskForm.name">
            
            <input
            autocomplete="off"
            type="datetime-local"
            min="new Date()"
            class=" round inputField text-center"
            id="date"
            style=""
            v-model="addTaskForm.date">
  
            <label for="Timeframe" class="text-center">Minumum time:</label>
            <select v-model="addTaskForm.minTime" name="Timeframe" id="Timeframe" class="round inputField text-center">
              <option value="30">30 Minutes</option>
              <option value="60">1 Hour</option>
              <option value="180">3 Hours</option>
              <option value="300">5 Hours</option>
              <option value="420">7 Hours</option>
            </select>
  
            <label for="priority">Task Priority:</label>
            <select v-model="addTaskForm.priority" name="priority" id="priority" class="round inputField text-center">
              <option value="1">Urgent</option>
              <option value="2">Important</option>
              <option value="3">Medium</option>
              <option value="4">Low</option>
            </select>
  
            <button @click="handleAddSubmit" class="btn btn-primary inputField">
              Add Task
            </button>
        </div>
  
      </form>
      
    </div>
    
    <button @click="handleAddSubmit" style="z-index: 2; width: 15%; margin-left:42.5%" class="btn btn-primary ">
      Generate Schedule
    </button>  

  </div>
  
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      addTaskForm: {
        name: '',
        minTime: '',
        date: '',
        priority: '',
      },
      tasks: [],
    };
  },
  methods: {
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
        })
        .catch((error) => {

          console.log(error);
          this.getTasks();
        });
    },
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {

          console.error(error);
        });
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      const payload = {
        name: this.addTaskForm.name,
        min: this.addTaskForm.minTime,
        due: this.addTaskForm.date,
        priority: this.addTaskForm.priority,
        id: 1,
      };
      console.log(typeof(this.addTaskForm.date))
      this.addTask(payload);
      this.initForm();
    },
    initForm() {
      this.addTaskForm.name = '';
      this.addTaskForm.minTime = '';
      this.addTaskForm.date = '';
      this.addTaskForm.priority = '';
    },
  },
  created() {
    this.getTasks();
  },
};
</script>