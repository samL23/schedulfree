<script setup>
</script>

<style>
/* For mobile phones: */

h1{
  font-family: "Trirong", serif;
}

.center{
  margin: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
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
    padding-top: 10px;
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
       
        <div class="mb-5 round py-3 text-center shadow" style="background-transpatent;background-color: #072944">
          <input
            autocomplete="off"
            type="text"
            class="my-3 round inputField text-center"
            id="name"
            placeholder="Task Name"
            style=""
            v-model="addTaskForm.name">
            
            <input
            placeholder="Due date"
            onfocus="(this.type='datetime-local')"
            name="date"
            autocomplete="off"
            
            min="new Date()"
            class="my-3 round inputField text-center"
            id="date"
            style=""
            v-model="addTaskForm.date">
  
            <select v-model="addTaskForm.minTime" name="Timeframe" id="Timeframe" class="round my-3 inputField text-center">
              <option value="" disabled selected>Select task length</option>
              <option value="30">30 Minutes</option>
              <option value="60">1 Hour</option>
              <option value="180">3 Hours</option>
              <option value="300">5 Hours</option>
              <option value="420">7 Hours</option>
              <option value="600">10 Hours</option>
              <option value="900">15 hours</option>
            </select>
  
  
            <button @click="handleAddSubmit" class="btn btn-primary inputField my-3 shadow-sm">
              Add Task
            </button>
        </div>
  
      </form>
      
    </div>
    
    <div style="height:50px; position:relative" >
      <button onclick="window.location.href='http://localhost:5173/week';" class="center btn btn-primary shadow-lg">
        Generate Schedule
      </button>  
    </div>
    
    

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
      if (this.addTaskForm.name !='' && this.addTaskForm.minTime !='' && this.addTaskForm.date !=''){
        const payload = {
        name: this.addTaskForm.name,
        min: this.addTaskForm.minTime,
        due: this.addTaskForm.date,
      };
      this.addTask(payload);
      this.initForm();
      }
      
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