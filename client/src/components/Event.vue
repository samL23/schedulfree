<template>
    <div class="event" v-bind:id="`${event.id}`">
      <div class="event-time">{{ event.time }} - {{ event.end }} </div>
      <div class="event-name">{{ event.name }}</div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      event: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .event {
    background-color: #3b306b;
    color: #fff;
    padding: 5px;
    margin-top: 5px;
    border-radius: 4px;
  }
  
  .event-time {
    font-weight: bold;
  }
  
  .event-name {
    margin-top: 5px;
  }
  </style>
  