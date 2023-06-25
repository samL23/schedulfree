<template>
    <div class="spacer layer1" style="z-index:-1;width: 100%; position:fixed; top:0px;">
    </div>
    <div class="weekly-schedule mt-3 px-3">
      <div class="header">
        <h2 class="text-white">Weekly Schedule</h2>
      </div>
      <div class="days">
        <div class="day" v-for="day in days" :key="day">
          <h3>{{ day }}</h3>
          <div class="events">
            <Event v-for="event in getEventsForDay(day)" :key="event.id" :event="event" />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import Event from '../components/Event.vue';
  
  export default {
    components: {
      Event,
    },
    data() {
      return {
        days: [24,25,26],
        events: [
          {  "id":1, "name":"finish report", "day": 24, "time":'10:00AM', "lenght":'style:"height:100px"'},
          { id: 2, day: 25, time: '2:00 PM', name: 'Meeting 2' },
          { id: 3, day: 30, time: '9:00 AM', name: 'Appointment 1' },
          { id: 4, day: 24, time: '4:00 PM', name: 'Appointment 2' },
          { id: 5, day: 26, time: '1:00 PM', name: 'Task 1' },
        ],
        blocks : []
      };
    },
    methods: {
      getEventsForDay(day) {
        return this.events.filter((event) => event.day === day);
      },
      getDays(){
        const date = new Date();
        let today= date.getDate(); 
        let days_list = []
        for (let i = 0; i < 7; i++) {
                days_list.push(today + i)
            }
        return days_list
      },
      getBlocks() {
      const path = 'http://localhost:5000/blocks';
      axios.get(path)
        .then((res) => {
          this.events = res.data.blocks;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    //   next method
  
    },
    created() {
        this.days = this.getDays();
        this.getBlocks();
        
     },
  };
  </script>
  
  <style scoped>

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
  
  .weekly-schedule {
    font-family: Arial, sans-serif;
  }
  
  .header {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .days {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 20px;
  }
  
  .day {
    background-color: rgba(248, 243, 243,0.7); 
    padding: 20px;
    border-radius: 4px;
  }
  
  h3 {
    margin-top: 0;
  }
  
  .events {
    margin-top: 10px;
  }

  @media screen and (min-width: 576px) {
    /* For desktop: */
    .layer1{
      background-image: url('../assets/layered-waves-haikei.svg');
    }
}
  </style>
  